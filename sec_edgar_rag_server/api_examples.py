"""
Example usage of the SEC Edgar Agentic RAG FastAPI server.
"""
import requests
import json
from datetime import datetime

# Base URL for the API
BASE_URL = "http://localhost:8000"


def example_single_query():
    """Example of a single query."""
    url = f"{BASE_URL}/query"
    
    payload = {
        "query": "What are the main business risks mentioned in the filing?",
        "company_ticker": "AAPL",
        "filing_type": "10-K",
        "company_name": "Apple Inc.",
        "verbose": False
    }
    
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response:")
    print(json.dumps(response.json(), indent=2))


def example_batch_query():
    """Example of batch queries."""
    url = f"{BASE_URL}/batch"
    
    payload = {
        "queries": [
            "What are the main business risks?",
            "What is the revenue breakdown by segment?",
            "What are the key financial metrics?"
        ],
        "company_ticker": "AAPL",
        "filing_type": "10-K",
        "company_name": "Apple Inc.",
        "verbose": False
    }
    
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response:")
    print(json.dumps(response.json(), indent=2))


def example_streaming_query():
    """Example of streaming query with verbose output."""
    url = f"{BASE_URL}/query/stream"
    
    payload = {
        "query": "What are the main business risks mentioned in the filing?",
        "company_ticker": "AAPL",
        "filing_type": "10-K",
        "company_name": "Apple Inc.",
        "verbose": True  # Ignored, always streams
    }
    
    print("Streaming query response:")
    print("-" * 80)
    
    response = requests.post(url, json=payload, stream=True)
    
    if response.status_code == 200:
        result_data = None
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    data_str = line_str[6:]  # Remove 'data: ' prefix
                    try:
                        data = json.loads(data_str)
                        if data.get('type') == 'progress':
                            # Print progress messages
                            print(data.get('message', ''), end='', flush=True)
                        elif data.get('type') == 'result':
                            # Store final result
                            result_data = data
                        elif data.get('type') == 'error':
                            print(f"\nError: {data.get('message')}")
                    except json.JSONDecodeError:
                        pass
        
        print("\n" + "-" * 80)
        if result_data:
            print("\nFinal Result:")
            print(f"Answer: {result_data.get('answer', '')[:200]}...")
            print(f"Correctness Score: {result_data.get('correctness', {}).get('correctness_score', 0):.2f}")
    else:
        print(f"Request failed with status {response.status_code}")
        print(response.text)


def example_export():
    """Example of exporting results."""
    # First, get a query result
    query_url = f"{BASE_URL}/query"
    query_payload = {
        "query": "What are the main business risks?",
        "company_ticker": "AAPL",
        "filing_type": "10-K",
        "verbose": False
    }
    
    query_response = requests.post(query_url, json=query_payload)
    result = query_response.json()
    
    # Then export it
    export_url = f"{BASE_URL}/export"
    export_payload = {
        "result": result,
        "format": "json"  # or "txt"
    }
    
    export_response = requests.post(export_url, json=export_payload)
    
    if export_response.status_code == 200:
        # Save the file
        content_disposition = export_response.headers.get('content-disposition', '')
        if 'filename=' in content_disposition:
            # Extract filename and strip quotes
            filename = content_disposition.split('filename=')[1].strip().strip('"').strip("'")
        else:
            # Fallback filename if header is missing
            filename = f"sec_edgar_rag_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'wb') as f:
            f.write(export_response.content)
        print(f"File saved as {filename}")
    else:
        print("Export failed:", export_response.text)


if __name__ == "__main__":
    print("=== Single Query Example ===")
    example_single_query()
    
    print("\n=== Batch Query Example ===")
    example_batch_query()
    
    print("\n=== Streaming Query Example ===")
    example_streaming_query()
    
    print("\n=== Export Example ===")
    example_export()

