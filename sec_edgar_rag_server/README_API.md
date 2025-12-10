# SEC Edgar Agentic RAG FastAPI Server

FastAPI server implementation of the Agentic RAG system for querying SEC Edgar documents.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or on Windows:
```bash
set OPENAI_API_KEY=your-api-key-here
```

3. Run the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### 1. Single Query (`POST /query`)

Perform a single Agentic RAG query on SEC Edgar documents.

**Request Body:**
```json
{
  "query": "What are the main business risks mentioned in the filing?",
  "company_ticker": "AAPL",
  "filing_type": "10-K",
  "company_name": "Apple Inc.",
  "verbose": false
}
```

### 1a. Streaming Query (`POST /query/stream`)

Perform a query with real-time streaming of verbose progress updates (Server-Sent Events).

**Request Body:** (Same as `/query`)

**Response:** Server-Sent Events stream with:
- `type: "progress"` - Progress messages during processing
- `type: "result"` - Final result JSON
- `type: "error"` - Error messages if any

**Example using Python:**
```python
import requests
import json

url = "http://localhost:8000/query/stream"
payload = {
    "query": "What are the main business risks?",
    "company_ticker": "AAPL",
    "filing_type": "10-K"
}

response = requests.post(url, json=payload, stream=True)

for line in response.iter_lines():
    if line:
        line_str = line.decode('utf-8')
        if line_str.startswith('data: '):
            data = json.loads(line_str[6:])
            if data.get('type') == 'progress':
                print(data.get('message'), end='', flush=True)
            elif data.get('type') == 'result':
                print("\n\nFinal Result:", json.dumps(data, indent=2))
```

**Example using curl:**
```bash
curl -N -X POST "http://localhost:8000/query/stream" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the main business risks?",
    "company_ticker": "AAPL",
    "filing_type": "10-K"
  }'
```

**Response:**
```json
{
  "question": "What are the main business risks mentioned in the filing?",
  "company_ticker": "AAPL",
  "company_name": "Apple Inc.",
  "filing_type": "10-K",
  "answer": "...",
  "citations": [1, 2],
  "sources": [...],
  "correctness": {...},
  "plan": {...},
  "retrieved_documents": 10,
  "verified_documents": 9,
  "relevant_documents": 8,
  "metadata": {...},
  "processing_summary": {...}
}
```

### 2. Batch Query (`POST /batch`)

Process multiple queries in batch.

**Request Body:**
```json
{
  "queries": [
    "What are the main business risks?",
    "What is the revenue breakdown by segment?",
    "What are the key financial metrics?"
  ],
  "company_ticker": "AAPL",
  "filing_type": "10-K",
  "company_name": "Apple Inc.",
  "verbose": false
}
```

**Response:**
```json
{
  "results": [...],
  "total_queries": 3,
  "successful_queries": 3,
  "failed_queries": 0,
  "processing_time": 45.2
}
```

### 3. Export Results (`POST /export`)

Export query results to a file (JSON or TXT format).

**Request Body:**
```json
{
  "result": {...},  // Query result from /query or /batch
  "format": "json"  // or "txt"
}
```

**Response:** File download

### 4. Health Check (`GET /health`)

Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00"
}
```

## Usage Examples

### Using curl

```bash
# Single query
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the main business risks?",
    "company_ticker": "AAPL",
    "filing_type": "10-K",
    "verbose": false
  }'

# Batch query
curl -X POST "http://localhost:8000/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "queries": ["Question 1", "Question 2"],
    "company_ticker": "AAPL",
    "filing_type": "10-K"
  }'
```

### Using Python requests

See `api_examples.py` for complete examples.

```python
import requests

response = requests.post(
    "http://localhost:8000/query",
    json={
        "query": "What are the main business risks?",
        "company_ticker": "AAPL",
        "filing_type": "10-K",
        "verbose": False
    }
)

result = response.json()
print(result["answer"])
```

## Architecture

The server uses:
- **FastAPI** for the web framework
- **Pydantic** for request/response validation
- **AgenticRAGOrchestrator** from `agents.py` for processing
- **Caching** of orchestrators to avoid reinitialization

## Notes

- The server caches orchestrators per company/filing combination for efficiency
- Verbose mode controls whether detailed processing steps are included
- Export supports both JSON and TXT formats
- All endpoints return structured JSON responses with proper error handling

