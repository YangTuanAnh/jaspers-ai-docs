# Multi-Source Market Intelligence RAG System Architecture

**Version:** 1.0  
**Date:** December 10, 2024  
**Status:** Design Document  
**Owner:** Engineering Team

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [System Overview](#system-overview)
3. [High-Level Architecture](#high-level-architecture)
4. [Data Sources & Ingestion](#data-sources--ingestion)
5. [Data Model & Storage](#data-model--storage)
6. [RAG Pipeline Architecture](#rag-pipeline-architecture)
7. [Asset Coverage & On-Demand Processing](#asset-coverage--on-demand-processing)
8. [Component Details](#component-details)
9. [Data Flow Diagrams](#data-flow-diagrams)
10. [Scalability & Performance](#scalability--performance)
11. [Security & Compliance](#security--compliance)

---

## 1. Executive Summary

This document describes the architecture for a unified, multi-source market intelligence RAG system that consolidates SEC EDGAR filings, real-time news, and social signals for both equity and cryptocurrency assets. The system extends the existing agentic RAG framework to support heterogeneous data sources with intelligent ranking, time-weighting, and cross-source synthesis.

### Key Design Principles

- **Unified Insight Layer**: Single query interface across all data sources per asset
- **Source-Agnostic Retrieval**: Consistent embedding and retrieval regardless of source type
- **Time-Weighted Relevance**: Recent information prioritized while maintaining historical context
- **Scalable Ingestion**: Background pipelines for continuous data updates
- **Graceful Degradation**: Partial results when data is incomplete or unavailable

---

## 2. System Overview

### 2.1 Core Capabilities

1. **Multi-Source Data Integration**
   - SEC EDGAR filings (10-K, 10-Q, 8-K, etc.)
   - Real-time news feeds (Yahoo Finance, financial news APIs)
   - Social signals (Twitter/X for stocks and crypto)
   - Crypto-specific sources (Binance News, crypto-native feeds)

2. **Unified Asset Intelligence**
   - Single insight layer per asset (ticker or token)
   - Cross-source correlation and synthesis
   - Temporal context preservation

3. **Intelligent Retrieval**
   - Source-aware chunking strategies
   - Time-weighted similarity search
   - Multi-source ranking and fusion

4. **Dynamic Asset Management**
   - Preloaded top 200 stock tickers
   - On-demand ticker ingestion
   - Background indexing pipelines

---

## 3. High-Level Architecture

### 3.1 System Architecture Diagram (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CLIENT LAYER                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                    │
│  │  Web UI      │  │  API Gateway │  │  Mobile App  │                    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                    │
└─────────┼──────────────────┼──────────────────┼────────────────────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
┌────────────────────────────┼────────────────────────────────────────────────┐
│                    APPLICATION LAYER                                        │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                    Query Orchestrator                                │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │  │
│  │  │   Planner    │  │   Router     │  │   Aggregator │             │  │
│  │  │   Agent      │  │   Agent      │  │   Agent      │             │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘             │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │              Multi-Source RAG Pipeline                                │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │  │
│  │  │   Retrieval  │  │ Verification │  │   Synthesis   │             │  │
│  │  │   Agents     │  │   Agent      │  │   Agent      │             │  │
│  │  │  (per source)│  │              │  │              │             │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘             │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
┌─────────┼──────────────────┼──────────────────┼────────────────────────────┐
│         │                  │                  │                             │
│  ┌──────▼──────┐  ┌───────▼──────┐  ┌───────▼──────┐                      │
│  │   Equity    │  │    Crypto    │  │   Unified    │                      │
│  │   Pipeline  │  │   Pipeline   │  │   Vector DB  │                      │
│  └──────┬──────┘  └───────┬──────┘  └───────┬──────┘                      │
│         │                  │                  │                             │
│  ┌──────▼──────────────────▼──────────────────▼──────┐                    │
│  │         Multi-Source Vector Store                   │                    │
│  │  ┌──────────────┐  ┌──────────────┐              │                    │
│  │  │   ChromaDB    │  │   Metadata   │              │                    │
│  │  │  Collections  │  │   Index      │              │                    │
│  │  └──────────────┘  └──────────────┘              │                    │
│  └────────────────────────────────────────────────────┘                    │
└──────────────────────────────────────────────────────────────────────────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
┌─────────┼──────────────────┼──────────────────┼────────────────────────────┐
│         │                  │                  │                             │
│  ┌──────▼──────┐  ┌───────▼──────┐  ┌───────▼──────┐                      │
│  │   Ingestion │  │   Ingestion  │  │   Ingestion  │                      │
│  │   Service   │  │   Service    │  │   Service    │                      │
│  │  (EDGAR)    │  │  (News)      │  │  (Social)    │                      │
│  └──────┬──────┘  └───────┬──────┘  └───────┬──────┘                      │
│         │                  │                  │                             │
│  ┌──────▼──────────────────▼──────────────────▼──────┐                    │
│  │         Data Source Layer                           │                    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │                    │
│  │  │  SEC     │  │  Yahoo   │  │ Twitter/ │        │                    │
│  │  │  EDGAR   │  │  Finance │  │    X     │        │                    │
│  │  └──────────┘  └──────────┘  └──────────┘        │                    │
│  │  ┌──────────┐  ┌──────────┐                       │                    │
│  │  │ Binance  │  │  Crypto  │                       │                    │
│  │  │  News    │  │   APIs   │                       │                    │
│  │  └──────────┘  └──────────┘                       │                    │
│  └────────────────────────────────────────────────────┘                    │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Component Layers

1. **Client Layer**: Web UI, API Gateway, Mobile Applications
2. **Application Layer**: Query orchestration, multi-agent RAG pipeline
3. **Data Processing Layer**: Equity/Crypto pipelines, vector storage
4. **Ingestion Layer**: Background services for each data source
5. **Source Layer**: External APIs and data providers

---

## 4. Data Sources & Ingestion

### 4.1 Equity Data Sources

#### 4.1.1 SEC EDGAR Filings
- **Source**: SEC EDGAR API / edgartools library
- **Filing Types**: 10-K (annual), 10-Q (quarterly), 8-K (current events), DEF 14A (proxy)
- **Update Frequency**: 
  - Quarterly reports: Within 45 days of quarter end
  - Annual reports: Within 60 days of fiscal year end
  - Current reports: Real-time (as filed)
- **Ingestion Strategy**: 
  - Initial bulk load for top 200 tickers
  - Scheduled checks for new filings (daily)
  - On-demand fetch for new tickers

#### 4.1.2 News Sources (Equity)
- **Yahoo Finance News**
  - Update Frequency: Real-time (polling every 5-15 minutes)
  - Coverage: Company-specific news, earnings, analyst reports
- **Twitter/X**
  - Update Frequency: Near-real-time (streaming API)
  - Coverage: Social sentiment, breaking news, analyst commentary
  - Filtering: Company mentions, hashtags, verified accounts
- **Financial News APIs**
  - Options: Alpha Vantage, NewsAPI, Financial Modeling Prep
  - Update Frequency: Real-time to hourly
  - Coverage: Professional financial news, market analysis

### 4.2 Crypto Data Sources

#### 4.2.1 News Sources (Crypto)
- **Binance News**
  - Update Frequency: Real-time (API polling every 5 minutes)
  - Coverage: Exchange announcements, market updates, token listings
- **Twitter/X (Crypto)**
  - Update Frequency: Near-real-time (streaming API)
  - Coverage: Project updates, community sentiment, influencer analysis
  - Filtering: Token symbols, project handles, crypto hashtags
- **Crypto-Native News Feeds**
  - Options: CoinDesk, CoinTelegraph, The Block
  - Update Frequency: Real-time to hourly
  - Coverage: Industry news, regulatory updates, technical analysis

### 4.3 Ingestion Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Ingestion Orchestrator                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │   Scheduler  │  │   Queue      │  │   Monitor    │        │
│  │   Service    │  │   Manager    │  │   Service    │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
          │                  │                  │
    ┌─────┴─────┐      ┌─────┴─────┐      ┌─────┴─────┐
    │           │      │           │      │           │
┌───▼───┐  ┌───▼───┐ ┌─▼───┐  ┌───▼───┐ ┌─▼───┐  ┌───▼───┐
│EDGAR │  │ News  │ │Social│  │Crypto │ │Bin. │  │Other  │
│Ingest│  │Ingest │ │Ingest│  │News   │ │News │  │Source │
│Worker│  │Worker │ │Worker│  │Worker │ │Worker│  │Worker │
└───┬───┘  └───┬───┘ └───┬───┘  └───┬───┘ └───┬───┘  └───┬───┘
    │          │         │         │         │          │
    └──────────┼─────────┼─────────┼─────────┼──────────┘
               │         │         │         │
    ┌──────────▼─────────▼─────────▼─────────▼──────────┐
    │         Unified Processing Pipeline                │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
    │  │  Chunk   │  │  Embed   │  │  Index   │       │
    │  │  Service │  │  Service │  │  Service │       │
    │  └──────────┘  └──────────┘  └──────────┘       │
    └───────────────────────────────────────────────────┘
               │
    ┌──────────▼──────────┐
    │   Vector Store      │
    │   (ChromaDB)        │
    └─────────────────────┘
```

### 4.4 Ingestion Workflow

1. **Scheduled Ingestion** (Top 200 Tickers)
   - Daily: Check for new EDGAR filings
   - Every 15 minutes: Poll news APIs
   - Real-time: Stream social media (Twitter/X)
   - Hourly: Update metadata and refresh stale data

2. **On-Demand Ingestion** (New Tickers)
   - User request triggers ingestion pipeline
   - Priority queue for user-requested assets
   - Background processing with status updates
   - Partial results available during warm-up

3. **Data Processing Pipeline**
   - **Normalization**: Convert all sources to unified schema
   - **Deduplication**: Remove duplicate content across sources
   - **Chunking**: Source-specific chunking strategies
   - **Embedding**: Generate embeddings using unified model
   - **Indexing**: Store in vector DB with rich metadata

---

## 5. Data Model & Storage

### 5.1 Unified Data Schema

```python
{
    "asset_id": "AAPL",  # Ticker or token symbol
    "asset_type": "equity" | "crypto",
    "source": "edgar" | "yahoo_finance" | "twitter" | "binance_news" | "crypto_news",
    "content": "Full text content",
    "chunk_id": "unique_chunk_identifier",
    "metadata": {
        "title": "Document/article title",
        "url": "Source URL",
        "published_at": "ISO 8601 timestamp",
        "author": "Author or source name",
        "filing_type": "10-K" | "10-Q" | "8-K" | null,  # For EDGAR
        "section": "ITEM 1A - Risk Factors",  # For EDGAR
        "sentiment": "positive" | "negative" | "neutral",  # For social/news
        "engagement_metrics": {  # For social
            "likes": 0,
            "retweets": 0,
            "replies": 0
        },
        "relevance_score": 0.0-1.0,  # Computed relevance
        "time_weight": 0.0-1.0,  # Time-based weight
        "source_credibility": 0.0-1.0  # Source reliability score
    },
    "embedding": [float],  # Vector embedding
    "created_at": "ISO 8601 timestamp",
    "updated_at": "ISO 8601 timestamp"
}
```

### 5.2 Vector Store Architecture

#### 5.2.1 Collection Strategy

**Option 1: Single Unified Collection**
- All assets and sources in one collection
- Filter by metadata fields
- Pros: Simple queries, cross-source retrieval
- Cons: Large collection size, potential performance issues

**Option 2: Per-Asset Collections**
- One collection per asset (ticker/token)
- All sources for that asset in same collection
- Pros: Fast per-asset queries, isolated updates
- Cons: More collections to manage

**Option 3: Hybrid Approach (Recommended)**
- Per-asset collections for primary queries
- Unified metadata index for cross-asset search
- Pros: Best of both worlds
- Cons: More complex architecture

**Recommended: Option 3 (Hybrid)**

```
┌─────────────────────────────────────────────────────────┐
│              ChromaDB Architecture                       │
│                                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │         Per-Asset Collections                      │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │  │
│  │  │ AAPL     │  │ MSFT     │  │ BTC      │       │  │
│  │  │ (all     │  │ (all     │  │ (all     │       │  │
│  │  │ sources) │  │ sources) │  │ sources) │       │  │
│  │  └──────────┘  └──────────┘  └──────────┘       │  │
│  └───────────────────────────────────────────────────┘  │
│                                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │         Metadata Index (PostgreSQL/Redis)         │  │
│  │  - Asset coverage tracking                         │  │
│  │  - Source availability per asset                   │  │
│  │  - Last update timestamps                          │  │
│  │  - Ingestion status                                │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### 5.3 Metadata Index Schema

```sql
CREATE TABLE asset_coverage (
    asset_id VARCHAR(10) PRIMARY KEY,
    asset_type VARCHAR(10) NOT NULL,  -- 'equity' or 'crypto'
    status VARCHAR(20) NOT NULL,  -- 'preloaded', 'warmup', 'ready', 'partial'
    sources_available TEXT[],  -- Array of available sources
    last_edgar_update TIMESTAMP,
    last_news_update TIMESTAMP,
    last_social_update TIMESTAMP,
    total_chunks INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ingestion_jobs (
    job_id UUID PRIMARY KEY,
    asset_id VARCHAR(10) NOT NULL,
    source_type VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,  -- 'pending', 'processing', 'completed', 'failed'
    chunks_processed INTEGER DEFAULT 0,
    error_message TEXT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 6. RAG Pipeline Architecture

### 6.1 Extended Agentic RAG Pipeline

```
User Query
    ↓
┌─────────────────────────────────────┐
│      Query Router Agent             │
│  - Detect asset type (equity/crypto)│
│  - Identify asset symbol            │
│  - Check asset availability          │
│  - Route to appropriate pipeline    │
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┐
    │                     │
┌───▼────┐          ┌─────▼────┐
│Equity │          │  Crypto  │
│Pipeline│          │ Pipeline │
└───┬────┘          └─────┬────┘
    │                     │
    └──────────┬──────────┘
               │
┌──────────────▼──────────────────────┐
│      Planner Agent                  │
│  - Decompose into sub-questions     │
│  - Identify required sources         │
│  - Generate retrieval plan           │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Multi-Source Retrieval Agents      │
│  ┌──────────┐  ┌──────────┐        │
│  │ EDGAR    │  │  News    │        │
│  │ Retriever│  │ Retriever│        │
│  └──────────┘  └──────────┘        │
│  ┌──────────┐  ┌──────────┐        │
│  │ Social   │  │  Crypto  │        │
│  │ Retriever│  │ Retriever│        │
│  └──────────┘  └──────────┘        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Cross-Source Ranking & Fusion      │
│  - Time-weighted scoring             │
│  - Source credibility weighting      │
│  - Relevance fusion                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Verification Agent              │
│  - Relevance verification            │
│  - Cross-source consistency check    │
│  - Fact verification                 │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Synthesis Agent                 │
│  - Multi-source synthesis            │
│  - Temporal context integration      │
│  - Citation generation                │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Final Verification                 │
│  - Answer correctness                │
│  - Source support validation         │
└──────────────┬──────────────────────┘
               │
         Final Answer
```

### 6.2 Source-Specific Retrieval Strategies

#### 6.2.1 EDGAR Filing Retrieval
- **Chunking**: Section-based (ITEM 1A, MD&A, Financial Statements)
- **Embedding**: Full section content
- **Retrieval**: Semantic search within filing sections
- **Ranking**: Filing recency + section relevance

#### 6.2.2 News Article Retrieval
- **Chunking**: Paragraph-based with overlap
- **Embedding**: Article title + content
- **Retrieval**: Semantic search + keyword matching
- **Ranking**: Time decay + source credibility + engagement

#### 6.2.3 Social Media Retrieval
- **Chunking**: Per-post (tweets are already small)
- **Embedding**: Post content + context (thread, replies)
- **Retrieval**: Semantic + keyword + author verification
- **Ranking**: Time decay + engagement + author credibility

### 6.3 Time-Weighted Ranking

```python
def calculate_time_weight(timestamp: datetime, current_time: datetime) -> float:
    """
    Calculate time-based weight for ranking.
    Recent content gets higher weight.
    """
    age_hours = (current_time - timestamp).total_seconds() / 3600
    
    # Exponential decay
    if age_hours < 1:
        return 1.0
    elif age_hours < 24:
        return 0.9 * math.exp(-age_hours / 24)
    elif age_hours < 168:  # 1 week
        return 0.7 * math.exp(-(age_hours - 24) / 144)
    elif age_hours < 720:  # 1 month
        return 0.5 * math.exp(-(age_hours - 168) / 552)
    else:
        return 0.3 * math.exp(-(age_hours - 720) / 2160)  # 3 months

def calculate_final_score(
    similarity_score: float,
    time_weight: float,
    source_credibility: float,
    relevance_score: float
) -> float:
    """
    Combine multiple factors into final retrieval score.
    """
    return (
        0.4 * similarity_score +
        0.3 * time_weight +
        0.2 * source_credibility +
        0.1 * relevance_score
    )
```

### 6.4 Cross-Source Fusion

**Reciprocal Rank Fusion (RRF)**
```python
def reciprocal_rank_fusion(results_by_source: Dict[str, List[Document]]) -> List[Document]:
    """
    Combine results from multiple sources using RRF.
    """
    k = 60  # RRF constant
    doc_scores = {}
    
    for source, docs in results_by_source.items():
        for rank, doc in enumerate(docs, 1):
            doc_id = doc.metadata.get('chunk_id')
            if doc_id not in doc_scores:
                doc_scores[doc_id] = {'doc': doc, 'score': 0.0}
            doc_scores[doc_id]['score'] += 1.0 / (k + rank)
    
    # Sort by combined score
    sorted_docs = sorted(
        doc_scores.values(),
        key=lambda x: x['score'],
        reverse=True
    )
    
    return [item['doc'] for item in sorted_docs]
```

---

## 7. Asset Coverage & On-Demand Processing

### 7.1 Preloaded Assets (Top 200 Stocks)

**Selection Criteria:**
- Market capitalization (S&P 500 top constituents)
- Trading volume
- User portfolio holdings (if available)
- Popular search queries

**Initial Load Process:**
1. Bulk download EDGAR filings for all 200 tickers
2. Historical news ingestion (last 90 days)
3. Social media ingestion (last 30 days)
4. Parallel processing with progress tracking
5. Status: "ready" when all sources indexed

### 7.2 On-Demand Asset Ingestion

**Workflow:**
```
User Request → Asset Check → Status Response
                    │
                    ├─→ "ready": Immediate query
                    ├─→ "warmup": Queue job + return partial results
                    └─→ "not_found": Queue job + return "ingestion_started"
```

**Ingestion Pipeline:**
1. **Immediate Response**
   - Return status: "warmup" or "ingestion_started"
   - Provide estimated completion time
   - Enable partial query capability

2. **Background Processing**
   - Priority queue: User-requested > Scheduled
   - Parallel source ingestion
   - Incremental indexing (results available as ready)

3. **Status Updates**
   - WebSocket/SSE for real-time updates
   - Progress percentage per source
   - Estimated time remaining

4. **Partial Results**
   - Query with available sources only
   - Clear indication of missing sources
   - Graceful degradation in synthesis

### 7.3 Asset Status Management

```python
class AssetStatus:
    READY = "ready"  # All sources indexed, ready for queries
    WARMUP = "warmup"  # Ingestion in progress, partial results available
    PARTIAL = "partial"  # Some sources available, others missing
    NOT_FOUND = "not_found"  # Asset not yet ingested
    FAILED = "failed"  # Ingestion failed, retry needed

def get_asset_status(asset_id: str) -> Dict:
    """
    Get current status and available sources for an asset.
    """
    coverage = get_asset_coverage(asset_id)
    
    if not coverage:
        return {
            "status": AssetStatus.NOT_FOUND,
            "available_sources": [],
            "message": f"Asset {asset_id} not yet indexed. Starting ingestion..."
        }
    
    sources = coverage.sources_available
    expected_sources = get_expected_sources(coverage.asset_type)
    missing_sources = set(expected_sources) - set(sources)
    
    if not missing_sources:
        return {
            "status": AssetStatus.READY,
            "available_sources": sources,
            "message": "Asset fully indexed and ready"
        }
    elif sources:
        return {
            "status": AssetStatus.PARTIAL,
            "available_sources": sources,
            "missing_sources": list(missing_sources),
            "message": f"Partial data available. Missing: {missing_sources}"
        }
    else:
        return {
            "status": AssetStatus.WARMUP,
            "available_sources": [],
            "message": "Ingestion in progress..."
        }
```

---

## 8. Component Details

### 8.1 Query Orchestrator

**Responsibilities:**
- Parse user queries
- Identify asset type and symbol
- Check asset availability
- Route to appropriate pipeline
- Aggregate multi-source results
- Format final response

**Key Methods:**
```python
class QueryOrchestrator:
    def route_query(self, query: str) -> QueryPlan
    def check_asset_availability(self, asset_id: str) -> AssetStatus
    def execute_query(self, query_plan: QueryPlan) -> QueryResult
    def aggregate_results(self, results_by_source: Dict) -> AggregatedResult
```

### 8.2 Multi-Source Retrieval Agents

**Base Retrieval Agent Interface:**
```python
class BaseRetrievalAgent:
    def retrieve(
        self,
        query: str,
        asset_id: str,
        k: int = 5,
        time_range: Optional[TimeRange] = None
    ) -> List[Document]
    
    def retrieve_with_scores(
        self,
        query: str,
        asset_id: str,
        k: int = 5
    ) -> List[DocumentWithScore]
```

**Source-Specific Implementations:**
- `EDGARRetrievalAgent`: SEC filing retrieval
- `NewsRetrievalAgent`: News article retrieval
- `SocialRetrievalAgent`: Social media retrieval
- `CryptoNewsRetrievalAgent`: Crypto-specific news

### 8.3 Ingestion Services

**EDGAR Ingestion Service:**
```python
class EDGARIngestionService:
    def ingest_ticker(self, ticker: str, filing_types: List[str])
    def check_new_filings(self, ticker: str) -> List[Filing]
    def process_filing(self, filing: Filing) -> List[Chunk]
```

**News Ingestion Service:**
```python
class NewsIngestionService:
    def ingest_asset_news(self, asset_id: str, asset_type: str)
    def poll_news_api(self, asset_id: str, since: datetime)
    def process_article(self, article: Article) -> List[Chunk]
```

**Social Ingestion Service:**
```python
class SocialIngestionService:
    def stream_mentions(self, asset_id: str, asset_type: str)
    def ingest_historical(self, asset_id: str, days: int)
    def process_post(self, post: Post) -> Chunk
```

### 8.4 Chunking Service

**Source-Aware Chunking:**
```python
class ChunkingService:
    def chunk_edgar_filing(self, filing: Filing) -> List[Chunk]
    def chunk_news_article(self, article: Article) -> List[Chunk]
    def chunk_social_post(self, post: Post) -> Chunk  # Usually single chunk
    def chunk_crypto_news(self, article: Article) -> List[Chunk]
```

**Chunking Strategies:**
- **EDGAR**: Section-based (preserve document structure)
- **News**: Paragraph-based with overlap (preserve context)
- **Social**: Per-post (already small units)
- **Crypto News**: Similar to news articles

---

## 9. Data Flow Diagrams

### 9.1 Query Flow

```
User Query: "What are the risks for AAPL?"
    ↓
Query Router
    ├─→ Extract: asset_id="AAPL", asset_type="equity"
    ├─→ Check Status: READY
    └─→ Route to Equity Pipeline
        ↓
Planner Agent
    ├─→ Sub-question 1: "What risks are mentioned in AAPL's 10-K?"
    ├─→ Sub-question 2: "What recent news mentions AAPL risks?"
    └─→ Sub-question 3: "What do analysts say about AAPL risks?"
        ↓
Multi-Source Retrieval
    ├─→ EDGAR Agent: Retrieve from AAPL collection (k=5)
    ├─→ News Agent: Retrieve from AAPL collection (k=5)
    └─→ Social Agent: Retrieve from AAPL collection (k=5)
        ↓
Cross-Source Fusion
    ├─→ Combine results (RRF)
    ├─→ Apply time weights
    └─→ Rank by final score
        ↓
Verification Agent
    ├─→ Relevance check
    └─→ Filter low-relevance docs
        ↓
Synthesis Agent
    ├─→ Generate answer with citations
    └─→ Include source attribution
        ↓
Final Answer with Sources
```

### 9.2 Ingestion Flow (On-Demand)

```
User Request: Query for "XYZ" (not in top 200)
    ↓
Query Router
    ├─→ Check Status: NOT_FOUND
    └─→ Trigger Ingestion Job
        ↓
Ingestion Orchestrator
    ├─→ Create job record (status: "processing")
    ├─→ Queue EDGAR ingestion
    ├─→ Queue News ingestion
    └─→ Queue Social ingestion
        ↓
Parallel Processing
    ├─→ EDGAR Worker: Download filings → Chunk → Embed → Index
    ├─→ News Worker: Fetch articles → Chunk → Embed → Index
    └─→ Social Worker: Fetch posts → Embed → Index
        ↓
Incremental Updates
    ├─→ Update asset_coverage table
    ├─→ Mark sources as available
    └─→ Update job status
        ↓
Status Updates (WebSocket)
    ├─→ "EDGAR: 50% complete"
    ├─→ "News: 30% complete"
    └─→ "Social: 20% complete"
        ↓
Completion
    ├─→ Status: READY
    └─→ Notify user: "Asset ready for queries"
```

---

## 10. Future Enhancements

1. **Real-Time Streaming**: WebSocket-based real-time updates
2. **Advanced Analytics**: Trend analysis, sentiment tracking
3. **Multi-Asset Queries**: Compare multiple assets
4. **Custom Sources**: User-defined data sources
5. **ML-Based Ranking**: Learn optimal ranking from user feedback
6. **Graph Database**: Relationship modeling between assets and sources

---

**End of Architecture Document**

