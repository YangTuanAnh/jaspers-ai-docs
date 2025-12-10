"""
Agent classes for Agentic RAG system.
Extracted from the notebook for use in FastAPI server.
"""
from typing import List, Dict, Any, Optional
from datetime import datetime
import json
import re

# Load environment variables first
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import sec2md
from edgar import Company, set_identity

# Initialize LLM and embeddings
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings()


class PlannerAgent:
    """Decomposes complex questions into sub-questions for better retrieval."""

    def __init__(self, llm):
        self.llm = llm
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are a planning agent that decomposes complex questions about SEC Edgar filings into
            smaller, more focused sub-questions. Each sub-question should be:
            1. Specific and answerable
            2. Focused on a single aspect of the original question
            3. Suitable for document retrieval

            Return a JSON list of sub-questions."""),
            ("human", "Original question: {question}\n\nDecompose this into sub-questions. Return only a JSON array of strings.")
        ])

    def decompose(self, question: str) -> List[str]:
        """Decompose a question into sub-questions."""
        chain = self.prompt_template | self.llm
        response = chain.invoke({"question": question})

        try:
            # Extract JSON from response
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()

            sub_questions = json.loads(content)
            if isinstance(sub_questions, list):
                return sub_questions
            else:
                return [question]  # Fallback to original question
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            # Fallback: return original question
            print(f"Error parsing sub-questions: {e}")
            return [question]

    def plan(self, question: str) -> Dict[str, Any]:
        """Create a plan with sub-questions."""
        sub_questions = self.decompose(question)
        return {
            "original_question": question,
            "sub_questions": sub_questions,
            "num_sub_questions": len(sub_questions)
        }


class SECEdgarRetrievalAgent:
    """Retrieves and processes SEC Edgar documents."""

    def __init__(self, llm, embeddings, company_ticker: str, filing_type: str = "10-K"):
        self.llm = llm
        self.embeddings = embeddings
        self.company_ticker = company_ticker.upper()
        self.filing_type = filing_type
        self.vectorstore = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        self.loaded_documents: List[Document] = []  # Store loaded documents
        set_identity("social@testopia.io")

    def download_filings(self, num_filings: int = 1):
        """Download SEC Edgar filings for the company."""
        print(f"Downloading {self.filing_type} filings for {self.company_ticker}...")
        try:
            company = Company(self.company_ticker)
            filing = company.get_filings(form=self.filing_type).latest()

            print(f"Downloaded {self.filing_type} filings for {self.company_ticker}")

            return filing
        except Exception as e:
            print(f"Error downloading filings: {e}")
            # Do not return mock documents here, let process_documents handle the fallback

    def _create_mock_documents(self) -> List[Document]:
        """Create mock documents for demonstration if download fails or no files found."""
        return [
            Document(
                page_content=f"Mock {self.filing_type} filing content for {self.company_ticker}. "
                           f"This is a placeholder document. In production, this would contain "
                           f"the actual SEC Edgar filing content.",
                metadata={"source": f"{self.company_ticker}_{self.filing_type}_mock.pdf",
                         "ticker": self.company_ticker,
                         "filing_type": self.filing_type}
            )
        ]

    def process_documents(self, documents: Optional[List[Document]] = None) -> Chroma:
        """Process documents and create vector store."""
        if documents is None:
            # Attempt to load from downloaded files if available
            if not self.loaded_documents:  # Only load if not already loaded
                filing = self.download_filings()

                if filing:
                    try:
                        md = sec2md.convert_to_markdown(filing.html(), return_pages=True)
                        sections = sec2md.extract_sections(md, filing_type=self.filing_type)

                        self.loaded_documents = [
                            Document(
                                page_content=sec.markdown(),
                                metadata={
                                    "source": f"{sec.item} - {sec.item_title} - pages{str(sec.page_range)}",
                                    "ticker": self.company_ticker,
                                    "filing_type": self.filing_type,
                                }
                            )
                            for sec in sections
                        ]
                    except Exception as e:
                        print(f"Error processing filing: {e}")
                        self.loaded_documents = []
            documents = self.loaded_documents

            # Fallback to mock documents if download/processing failed
            if not documents:
                documents = self._create_mock_documents()

        # Split documents
        texts = self.text_splitter.split_documents(documents)

        # Create vector store
        self.vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=self.embeddings,
            collection_name=f"{self.company_ticker}_{self.filing_type}"
        )

        return self.vectorstore

    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        """Retrieve relevant documents for a query."""
        if self.vectorstore is None:
            print("Vectorstore not initialized. Processing documents first.")
            self.process_documents()

        # No filter needed - collection is already scoped to company_ticker and filing_type
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})
        docs = retriever.invoke(query)

        return docs

    def retrieve_with_scores(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve documents with relevance scores."""
        if self.vectorstore is None:
            print("Vectorstore not initialized. Processing documents first.")
            self.process_documents()

        # Use similarity search with scores
        docs_with_scores = self.vectorstore.similarity_search_with_score(query, k=k)

        results = []
        for doc, score in docs_with_scores:
            results.append({
                "document": doc,
                "score": score,
                "content": doc.page_content,
                "metadata": doc.metadata
            })

        return results


class VerificationAgent:
    """Self-RAG style verification agent that checks relevance and correctness."""

    def __init__(self, llm):
        self.llm = llm
        self.relevance_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a verification agent that evaluates the relevance of retrieved documents
            to a given question. Rate each document on a scale of 0.0 to 1.0 where:
            - 1.0 = Highly relevant and directly answers the question
            - 0.5 = Somewhat relevant but may not fully answer
            - 0.0 = Not relevant

            Return a JSON object with relevance scores for each document."""),
            ("human", """Question: {question}

            Document: {document_content}

            Rate the relevance of this document to the question. Return only a JSON object with:
            {{
                "relevance_score": <float 0.0-1.0>,
                "reasoning": "<brief explanation>",
                "is_relevant": <boolean>
            }}""")
        ])

        self.correctness_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a verification agent that checks if an answer is correct and well-supported
            by the provided documents. Evaluate:
            1. Factual correctness
            2. Completeness
            3. Support from documents

            Return a JSON object with your evaluation."""),
            ("human", """Question: {question}

            Answer: {answer}

            Supporting Documents:
            {documents}

            Evaluate the correctness and support. Return only a JSON object with:
            {{
                "correctness_score": <float 0.0-1.0>,
                "is_supported": <boolean>,
                "missing_information": [<list of missing info>],
                "reasoning": "<brief explanation>"
            }}""")
        ])

    def verify_relevance(self, question: str, documents: List[Document]) -> List[Dict[str, Any]]:
        """Verify relevance of documents to the question."""
        verified_docs = []

        for doc in documents:
            chain = self.relevance_prompt | self.llm
            response = chain.invoke({
                "question": question,
                "document_content": doc.page_content[:2000]  # Limit content length
            })

            try:
                content = response.content.strip()
                if content.startswith("```json"):
                    content = content[7:]
                if content.startswith("```"):
                    content = content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                content = content.strip()

                verification = json.loads(content)
                verification["document"] = doc
                verified_docs.append(verification)
            except (json.JSONDecodeError, ValueError, KeyError):
                # Fallback: assume relevant
                verified_docs.append({
                    "document": doc,
                    "relevance_score": 0.5,
                    "reasoning": "Could not parse verification",
                    "is_relevant": True
                })

        # Sort by relevance score
        verified_docs.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
        return verified_docs

    def verify_correctness(self, question: str, answer: str, documents: List[Document]) -> Dict[str, Any]:
        """Verify correctness and support of an answer."""
        docs_text = "\n\n".join([
            f"Document {i+1}:\n{doc.page_content[:500]}"
            for i, doc in enumerate(documents)
        ])

        chain = self.correctness_prompt | self.llm
        response = chain.invoke({
            "question": question,
            "answer": answer,
            "documents": docs_text
        })

        try:
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()

            return json.loads(content)
        except (json.JSONDecodeError, ValueError, KeyError):
            return {
                "correctness_score": 0.5,
                "is_supported": True,
                "missing_information": [],
                "reasoning": "Could not parse verification"
            }


class SynthesisAgent:
    """Synthesizes answers from verified documents with proper citations."""

    def __init__(self, llm):
        self.llm = llm
        self.synthesis_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a synthesis agent that creates comprehensive answers from multiple
            verified documents. Your answers must:
            1. Be accurate and well-supported
            2. Include citations in the format [Document N] where N is the document number
            3. Synthesize information from multiple sources when relevant
            4. Clearly indicate when information is not available in the documents

            Format your response with:
            - A clear, direct answer
            - Supporting details with citations
            - A list of sources at the end"""),
            ("human", """Question: {question}

            Verified Documents:
            {documents}

            Create a comprehensive answer with citations.""")
        ])

    def synthesize(self, question: str, verified_documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Synthesize answer from verified documents."""
        # Filter to only relevant documents
        relevant_docs = [
            v for v in verified_documents
            if v.get("is_relevant", True) and v.get("relevance_score", 0) > 0.3
        ]

        if not relevant_docs:
            return {
                "answer": "I could not find relevant information in the documents to answer this question.",
                "citations": [],
                "sources": []
            }

        # Format documents for prompt
        docs_text = ""
        sources = []
        for i, v in enumerate(relevant_docs, 1):
            doc = v["document"]
            docs_text += f"\n\n[Document {i}]\n"
            docs_text += f"Content: {doc.page_content[:1500]}\n"
            docs_text += f"Relevance Score: {v.get('relevance_score', 0):.2f}\n"

            source_info = {
                "document_id": i,
                "metadata": doc.metadata,
                "relevance_score": v.get("relevance_score", 0),
                "reasoning": v.get("reasoning", "")
            }
            sources.append(source_info)

        # Generate answer
        chain = self.synthesis_prompt | self.llm
        response = chain.invoke({
            "question": question,
            "documents": docs_text
        })

        answer = response.content

        # Extract citations from answer
        citations = self._extract_citations(answer)

        return {
            "answer": answer,
            "citations": citations,
            "sources": sources,
            "num_sources": len(citations)
        }

    def _extract_citations(self, text: str) -> List[int]:
        """Extract document citations from text."""
        citations = re.findall(r'\[Document (\d+)\]', text)
        return [int(c) for c in citations]


class AgenticRAGOrchestrator:
    """Orchestrates the complete Agentic RAG workflow."""

    def __init__(self, company_ticker: str, filing_type: str = "10-K"):
        self.company_ticker = company_ticker
        self.filing_type = filing_type

        # Initialize all agents
        self.planner = PlannerAgent(llm)
        self.retrieval_agent = SECEdgarRetrievalAgent(llm, embeddings, company_ticker, filing_type)
        self.verification_agent = VerificationAgent(llm)
        self.synthesis_agent = SynthesisAgent(llm)

        # Initialize retrieval agent's vector store
        self.retrieval_agent.process_documents()

    def query(self, question: str, verbose: bool = False, stream_callback=None) -> Dict[str, Any]:
        """Execute the complete Agentic RAG pipeline.
        
        Args:
            question: The question to answer
            verbose: Whether to output verbose progress
            stream_callback: Optional callback function(message: str) for streaming messages
        """
        def log(message: str):
            """Helper to log messages if verbose or callback is provided."""
            if verbose:
                print(message)
            if stream_callback:
                stream_callback(message)
        
        # Step 1: Planning - Decompose question
        log(f"🔍 Processing question: {question}\n")
        log("📋 Step 1: Planning - Decomposing question...")
        plan = self.planner.plan(question)
        sub_questions = plan["sub_questions"]
        log(f"   Generated {len(sub_questions)} sub-question(s)\n")

        # Step 2: Retrieval - Get documents for each sub-question
        log("🔎 Step 2: Retrieval - Fetching relevant documents...")
        all_retrieved_docs = []
        for i, sq in enumerate(sub_questions, 1):
            log(f"   Sub-question {i}: {sq}")
            docs = self.retrieval_agent.retrieve(sq, k=5)
            all_retrieved_docs.extend(docs)
            log(f"      Retrieved {len(docs)} document(s)")

        # Remove duplicates based on content
        seen = set()
        unique_docs = []
        for doc in all_retrieved_docs:
            content_hash = hash(doc.page_content[:100])
            if content_hash not in seen:
                seen.add(content_hash)
                unique_docs.append(doc)

        log(f"   Total unique documents: {len(unique_docs)}\n")

        # Step 3: Verification - Verify relevance
        log("✅ Step 3: Verification - Verifying document relevance...")
        verified_docs = self.verification_agent.verify_relevance(question, unique_docs)
        relevant_docs = [v for v in verified_docs if v.get("is_relevant", True) and v.get("relevance_score", 0) > 0.3]
        log(f"   Verified {len(verified_docs)} document(s)")
        log(f"   {len(relevant_docs)} document(s) passed relevance threshold\n")

        # Step 4: Synthesis - Generate answer with citations
        log("📝 Step 4: Synthesis - Generating answer with citations...")
        result = self.synthesis_agent.synthesize(question, verified_docs)

        # Step 5: Final verification - Check answer correctness
        log("🔍 Step 5: Final Verification - Checking answer correctness...")
        correctness = self.verification_agent.verify_correctness(
            question,
            result["answer"],
            [v["document"] for v in relevant_docs]
        )
        result["correctness"] = correctness
        log(f"   Correctness Score: {correctness.get('correctness_score', 0):.2f}")
        log(f"   Is Supported: {correctness.get('is_supported', False)}\n")

        # Compile final result
        final_result = {
            "question": question,
            "plan": plan,
            "retrieved_documents": len(unique_docs),
            "verified_documents": len(verified_docs),
            "relevant_documents": len(relevant_docs),
            "answer": result["answer"],
            "citations": result["citations"],
            "sources": result["sources"],
            "correctness": correctness,
            "metadata": {
                "company_ticker": self.company_ticker,
                "filing_type": self.filing_type,
                "timestamp": datetime.now().isoformat()
            }
        }

        return final_result

