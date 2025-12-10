"""
FastAPI server for Agentic RAG orchestration of SEC Edgar documents.
"""
import os
import json
import tempfile
from typing import List, Optional
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()  # Load environment variables BEFORE importing agents

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field
import asyncio

from agents import AgenticRAGOrchestrator

# Initialize FastAPI app
app = FastAPI(
    title="SEC Edgar Agentic RAG API",
    description="Multi-agent RAG system for querying SEC Edgar documents",
    version="1.0.0"
)

# Set OpenAI API key from environment
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable must be set")


# Pydantic Models
class QueryRequest(BaseModel):
    """Request model for single query."""
    query: str = Field(..., description="The question to ask about the SEC filing")
    company_ticker: str = Field(..., description="Company ticker symbol (e.g., AAPL, MSFT)")
    filing_type: str = Field(default="10-K", description="Type of SEC filing (e.g., 10-K, 10-Q, 8-K)")
    company_name: Optional[str] = Field(None, description="Company name (optional, for reference)")
    verbose: bool = Field(default=False, description="Whether to include verbose processing details")


class BatchQueryRequest(BaseModel):
    """Request model for batch queries."""
    queries: List[str] = Field(..., description="List of questions to ask")
    company_ticker: str = Field(..., description="Company ticker symbol (e.g., AAPL, MSFT)")
    filing_type: str = Field(default="10-K", description="Type of SEC filing (e.g., 10-K, 10-Q, 8-K)")
    company_name: Optional[str] = Field(None, description="Company name (optional, for reference)")
    verbose: bool = Field(default=False, description="Whether to include verbose processing details")


class ExportRequest(BaseModel):
    """Request model for exporting results."""
    result: dict = Field(..., description="The query result to export")
    format: str = Field(default="json", description="Export format: json or txt")


# Response Models
class QueryResponse(BaseModel):
    """Response model for query endpoint."""
    question: str
    company_ticker: str
    company_name: Optional[str]
    filing_type: str
    answer: str
    citations: List[int]
    sources: List[dict]
    correctness: dict
    plan: dict
    retrieved_documents: int
    verified_documents: int
    relevant_documents: int
    metadata: dict
    processing_summary: dict


class BatchQueryResponse(BaseModel):
    """Response model for batch query endpoint."""
    results: List[QueryResponse]
    total_queries: int
    successful_queries: int
    failed_queries: int
    processing_time: Optional[float]


# Cache for orchestrators (to avoid reinitializing for same company/filing)
_orchestrator_cache: dict = {}


def get_orchestrator(company_ticker: str, filing_type: str) -> AgenticRAGOrchestrator:
    """Get or create orchestrator for company/filing combination."""
    cache_key = f"{company_ticker}_{filing_type}"
    if cache_key not in _orchestrator_cache:
        _orchestrator_cache[cache_key] = AgenticRAGOrchestrator(
            company_ticker=company_ticker,
            filing_type=filing_type
        )
    return _orchestrator_cache[cache_key]


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "SEC Edgar Agentic RAG API",
        "version": "1.0.0",
        "description": "Multi-agent RAG system for querying SEC Edgar documents",
        "endpoints": {
            "/query": "POST - Single query endpoint",
            "/batch": "POST - Batch query endpoint",
            "/export": "POST - Export results to file",
            "/health": "GET - Health check"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/query", response_model=QueryResponse)
async def query_sec_edgar(request: QueryRequest):
    """
    Perform Agentic RAG query on SEC Edgar documents.
    
    - **query**: The question to ask
    - **company_ticker**: Company ticker symbol (e.g., AAPL, MSFT)
    - **filing_type**: Type of SEC filing (default: 10-K)
    - **company_name**: Optional company name
    - **verbose**: Whether to include verbose processing details (non-streaming)
    """
    try:
        # Get orchestrator
        orchestrator = get_orchestrator(request.company_ticker, request.filing_type)
        
        # Execute query
        result = orchestrator.query(request.query, verbose=request.verbose)
        
        # Format response
        response = QueryResponse(
            question=result["question"],
            company_ticker=result["metadata"]["company_ticker"],
            company_name=request.company_name,
            filing_type=result["metadata"]["filing_type"],
            answer=result["answer"],
            citations=result["citations"],
            sources=result["sources"],
            correctness=result["correctness"],
            plan=result["plan"],
            retrieved_documents=result["retrieved_documents"],
            verified_documents=result["verified_documents"],
            relevant_documents=result["relevant_documents"],
            metadata=result["metadata"],
            processing_summary={
                "sub_questions_generated": result["plan"]["num_sub_questions"],
                "retrieved_documents": result["retrieved_documents"],
                "verified_documents": result["verified_documents"],
                "relevant_documents": result["relevant_documents"],
                "correctness_score": result["correctness"].get("correctness_score", 0),
                "is_supported": result["correctness"].get("is_supported", False)
            }
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.post("/query/stream")
async def query_sec_edgar_stream(request: QueryRequest):
    """
    Perform Agentic RAG query with streaming verbose output (Server-Sent Events).
    
    - **query**: The question to ask
    - **company_ticker**: Company ticker symbol (e.g., AAPL, MSFT)
    - **filing_type**: Type of SEC filing (default: 10-K)
    - **company_name**: Optional company name
    - **verbose**: Ignored (always streams verbose output)
    
    Returns a streaming response with:
    - Progress updates during processing
    - Final result as JSON at the end
    """
    async def generate_stream():
        """Generator function for SSE streaming."""
        try:
            # Get orchestrator
            orchestrator = get_orchestrator(request.company_ticker, request.filing_type)
            
            # Collect messages for callback
            messages = []
            
            def stream_callback(message: str):
                """Callback to collect streaming messages."""
                messages.append(message)
            
            # Execute query with streaming callback
            result = orchestrator.query(request.query, verbose=True, stream_callback=stream_callback)
            
            # Stream all collected messages
            for msg in messages:
                yield f"data: {json.dumps({'type': 'progress', 'message': msg})}\n\n"
                await asyncio.sleep(0.01)  # Small delay for smooth streaming
            
            # Send final result
            response_data = {
                "type": "result",
                "question": result["question"],
                "company_ticker": result["metadata"]["company_ticker"],
                "company_name": request.company_name,
                "filing_type": result["metadata"]["filing_type"],
                "answer": result["answer"],
                "citations": result["citations"],
                "sources": result["sources"],
                "correctness": result["correctness"],
                "plan": result["plan"],
                "retrieved_documents": result["retrieved_documents"],
                "verified_documents": result["verified_documents"],
                "relevant_documents": result["relevant_documents"],
                "metadata": result["metadata"],
                "processing_summary": {
                    "sub_questions_generated": result["plan"]["num_sub_questions"],
                    "retrieved_documents": result["retrieved_documents"],
                    "verified_documents": result["verified_documents"],
                    "relevant_documents": result["relevant_documents"],
                    "correctness_score": result["correctness"].get("correctness_score", 0),
                    "is_supported": result["correctness"].get("is_supported", False)
                }
            }
            yield f"data: {json.dumps(response_data)}\n\n"
            
        except Exception as e:
            error_data = {"type": "error", "message": str(e)}
            yield f"data: {json.dumps(error_data)}\n\n"
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable buffering for nginx
        }
    )


@app.post("/batch", response_model=BatchQueryResponse)
async def batch_query_sec_edgar(request: BatchQueryRequest):
    """
    Perform batch Agentic RAG queries on SEC Edgar documents.
    
    - **queries**: List of questions to ask
    - **company_ticker**: Company ticker symbol
    - **filing_type**: Type of SEC filing (default: 10-K)
    - **company_name**: Optional company name
    - **verbose**: Whether to include verbose processing details
    """
    import time
    start_time = time.time()
    
    try:
        # Get orchestrator
        orchestrator = get_orchestrator(request.company_ticker, request.filing_type)
        
        results = []
        successful = 0
        failed = 0
        
        for query in request.queries:
            try:
                result = orchestrator.query(query, verbose=request.verbose)
                
                response = QueryResponse(
                    question=result["question"],
                    company_ticker=result["metadata"]["company_ticker"],
                    company_name=request.company_name,
                    filing_type=result["metadata"]["filing_type"],
                    answer=result["answer"],
                    citations=result["citations"],
                    sources=result["sources"],
                    correctness=result["correctness"],
                    plan=result["plan"],
                    retrieved_documents=result["retrieved_documents"],
                    verified_documents=result["verified_documents"],
                    relevant_documents=result["relevant_documents"],
                    metadata=result["metadata"],
                    processing_summary={
                        "sub_questions_generated": result["plan"]["num_sub_questions"],
                        "retrieved_documents": result["retrieved_documents"],
                        "verified_documents": result["verified_documents"],
                        "relevant_documents": result["relevant_documents"],
                        "correctness_score": result["correctness"].get("correctness_score", 0),
                        "is_supported": result["correctness"].get("is_supported", False)
                    }
                )
                results.append(response)
                successful += 1
            except Exception as e:
                failed += 1
                # Add error result
                error_response = QueryResponse(
                    question=query,
                    company_ticker=request.company_ticker,
                    company_name=request.company_name,
                    filing_type=request.filing_type,
                    answer=f"Error processing query: {str(e)}",
                    citations=[],
                    sources=[],
                    correctness={"correctness_score": 0.0, "is_supported": False, "error": str(e)},
                    plan={"original_question": query, "sub_questions": [], "num_sub_questions": 0},
                    retrieved_documents=0,
                    verified_documents=0,
                    relevant_documents=0,
                    metadata={
                        "company_ticker": request.company_ticker,
                        "filing_type": request.filing_type,
                        "timestamp": datetime.now().isoformat()
                    },
                    processing_summary={"error": str(e)}
                )
                results.append(error_response)
        
        processing_time = time.time() - start_time
        
        return BatchQueryResponse(
            results=results,
            total_queries=len(request.queries),
            successful_queries=successful,
            failed_queries=failed,
            processing_time=processing_time
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing batch queries: {str(e)}")


@app.post("/export")
async def export_results(request: ExportRequest):
    """
    Export query results to a file.
    
    - **result**: The query result dictionary to export
    - **format**: Export format - "json" or "txt" (default: json)
    """
    try:
        # Clean result for export (remove non-serializable objects)
        exportable_result = request.result.copy()
        
        # Handle sources if present
        if "sources" in exportable_result:
            for source in exportable_result["sources"]:
                if "document" in source:
                    source["document_content"] = source["document"].page_content[:500] if hasattr(source["document"], "page_content") else str(source["document"])
                    source["document_metadata"] = source["document"].metadata if hasattr(source["document"], "metadata") else {}
                    del source["document"]
        
        if request.format.lower() == "json":
            # Export as JSON
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
                json.dump(exportable_result, f, indent=2, default=str)
                temp_path = f.name
            
            return FileResponse(
                temp_path,
                media_type="application/json",
                filename=f"sec_edgar_rag_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
        
        elif request.format.lower() == "txt":
            # Export as formatted text
            output = []
            output.append("=" * 80)
            output.append("AGENTIC RAG RESPONSE")
            output.append("=" * 80)
            output.append(f"\nQuestion: {exportable_result.get('question', 'N/A')}")
            output.append(f"\nCompany: {exportable_result.get('metadata', {}).get('company_ticker', 'N/A')}")
            output.append(f"Filing Type: {exportable_result.get('metadata', {}).get('filing_type', 'N/A')}")
            output.append("\nProcessing Summary:")
            plan = exportable_result.get('plan', {})
            output.append(f"  - Sub-questions generated: {plan.get('num_sub_questions', 0)}")
            output.append(f"  - Documents retrieved: {exportable_result.get('retrieved_documents', 0)}")
            output.append(f"  - Documents verified: {exportable_result.get('verified_documents', 0)}")
            output.append(f"  - Relevant documents: {exportable_result.get('relevant_documents', 0)}")
            correctness = exportable_result.get('correctness', {})
            output.append(f"  - Correctness score: {correctness.get('correctness_score', 0):.2f}")
            output.append("\n" + "-" * 80)
            output.append("ANSWER:")
            output.append("-" * 80)
            output.append(exportable_result.get('answer', 'N/A'))
            output.append("\n" + "-" * 80)
            output.append("SOURCES:")
            output.append("-" * 80)
            for i, source in enumerate(exportable_result.get('sources', []), 1):
                output.append(f"\nSource {i}:")
                output.append(f"  Relevance Score: {source.get('relevance_score', 0):.2f}")
                output.append(f"  Metadata: {source.get('metadata', {})}")
            output.append("\n" + "=" * 80)
            
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
                f.write("\n".join(output))
                temp_path = f.name
            
            return FileResponse(
                temp_path,
                media_type="text/plain",
                filename=f"sec_edgar_rag_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )
        
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported format: {request.format}. Use 'json' or 'txt'")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting results: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

