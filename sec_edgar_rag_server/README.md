# Agentic RAG Orchestration for SEC Edgar

A comprehensive multi-agent RAG (Retrieval-Augmented Generation) system for querying SEC Edgar documents with intelligent question decomposition, retrieval, verification, and synthesis.

## Features

### 🤖 Multi-Agent Architecture

1. **Planner Agent**: Decomposes complex questions into focused sub-questions for better retrieval
2. **Retrieval Agents**: Fetches and processes SEC Edgar documents using vector embeddings
3. **Verification Agent**: Self-RAG style verification that checks:
   - Document relevance to the question
   - Answer correctness and support from documents
4. **Synthesis Agent**: Combines verified information into comprehensive answers with proper citations

### 🔄 Complete Workflow

The system follows a 5-step orchestrated pipeline:
1. **Planning**: Question decomposition
2. **Retrieval**: Document fetching for each sub-question
3. **Verification**: Relevance scoring and filtering
4. **Synthesis**: Answer generation with citations
5. **Final Verification**: Correctness and support checking

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key in the notebook:
```python
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
```

3. Open and run the notebook: `sec_edgar_agentic_rag.ipynb`

## Usage

### Basic Query

```python
from sec_edgar_agentic_rag import query_sec_edgar

result = query_sec_edgar(
    "What are the main business risks mentioned in the filing?",
    company_ticker="AAPL",
    filing_type="10-K",
    verbose=True
)
```

### Using the Orchestrator Directly

```python
orchestrator = AgenticRAGOrchestrator(company_ticker="AAPL", filing_type="10-K")
result = orchestrator.query("What are the financial performance metrics?", verbose=True)
print(orchestrator.format_response(result))
```

### Batch Processing

```python
questions = [
    "What are the main business risks?",
    "What is the revenue breakdown by segment?",
    "What are the key financial metrics?"
]
results = batch_query(questions, company_ticker="AAPL")
```

## Architecture

```
User Question
    ↓
[Planner Agent] → Sub-questions
    ↓
[Retrieval Agents] → Documents for each sub-question
    ↓
[Verification Agent] → Relevance scores & filtering
    ↓
[Synthesis Agent] → Answer with citations
    ↓
[Verification Agent] → Correctness check
    ↓
Final Answer with Sources
```

## Key Components

- **Vector Store**: ChromaDB for efficient document retrieval
- **Embeddings**: OpenAI embeddings for semantic search
- **LLM**: GPT-4 for planning, verification, and synthesis
- **SEC Edgar Downloader**: Automatic filing retrieval

## Output Format

The system returns structured results including:
- Original question and decomposed sub-questions
- Retrieved and verified document counts
- Comprehensive answer with citations
- Source metadata and relevance scores
- Correctness verification scores

## Requirements

- Python 3.8+
- OpenAI API key
- See `requirements.txt` for full dependency list

## Notes

- The notebook includes mock documents for demonstration. In production, actual SEC Edgar filings will be downloaded and processed.
- Adjust chunk sizes and retrieval parameters based on your document size and requirements.
- The verification threshold (0.3) can be adjusted for stricter/looser filtering.


