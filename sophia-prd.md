# Product Requirements Document (PRD)
# SOPHIA — Your Intelligent Market Mind

**Version:** 1.0  
**Date:** November 27, 2025  
**Status:** MVP Development  
**Owner:** Engineering Team

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Product Overview](#2-product-overview)
3. [User Personas & Stories](#3-user-personas--stories)
4. [Technical Architecture](#4-technical-architecture)
5. [Data Scraping Layer](#5-data-scraping-layer)
6. [Database Schema](#6-database-schema)
7. [Data Transfer Objects (DTOs)](#7-data-transfer-objects-dtos)
8. [API Specifications](#8-api-specifications)
9. [API Testing (api.http)](#9-api-testing-apihttp)
10. [Security & Compliance](#10-security--compliance)
11. [Implementation Plan](#11-implementation-plan)
12. [Success Metrics](#12-success-metrics)

---

## 1. Executive Summary

### 1.1 Vision

**SOPHIA — Your Intelligent Market Mind** is a unified investment intelligence platform that aggregates portfolios across stock brokerages and cryptocurrency exchanges, continuously scrapes real-time market data, and provides AI-powered insights through natural language conversations.

### 1.2 Core Value Propositions

| Value | Description |
|-------|-------------|
| **Unified Portfolio** | Single view across stocks, ETFs, and crypto from multiple sources |
| **Real-Time Intelligence** | Continuous data scraping for prices, news, filings, and on-chain metrics |
| **AI-Powered Insights** | Natural language Q&A with cited sources and contextual analysis |
| **Multi-Asset Support** | First-class support for both traditional securities and cryptocurrencies |
| **Actionable Alerts** | Smart notifications based on price movements, news, and sentiment |

### 1.3 Target Market

- Retail investors managing portfolios across multiple platforms
- Crypto traders seeking unified portfolio tracking
- Active traders wanting AI-assisted research
- Long-term investors tracking performance across asset classes

---

## 2. Product Overview

### 2.1 Core Features

#### Feature 1: Multi-Platform Portfolio Aggregation
- **Stock Brokerages:** Alpaca, Interactive Brokers
- **Crypto Exchanges:** Coinbase, Binance, Kraken
- **Crypto Wallets:** Read-only via public blockchain addresses (ETH, BTC, SOL)
- Automatic synchronization every 5 minutes
- Manual sync on-demand

#### Feature 2: Real-Time Data Scraping Engine
- Stock quotes and metrics (Yahoo Finance, Finnhub, Polygon.io)
- Crypto prices and metrics (CoinGecko, CoinMarketCap, Binance API)
- News aggregation (Finnhub, CryptoPanic, NewsAPI)
- SEC EDGAR filings (10-K, 10-Q, 8-K)
- Social sentiment (Reddit, Twitter/X mentions)
- On-chain analytics (Etherscan, Blockchain.com APIs)

#### Feature 3: AI Chat Assistant (Sophia)
- Portfolio analysis and Q&A
- Stock and crypto research
- News summarization
- Comparative analysis
- All responses include cited sources

#### Feature 4: Watchlists & Alerts
- Custom watchlists (mixed stocks + crypto)
- Price threshold alerts
- News mention alerts
- Volume spike alerts
- Portfolio change notifications

#### Feature 5: Analytics Dashboard
- Total portfolio value and P&L
- Asset allocation visualization
- Historical performance charts
- Sector/category breakdown
- Risk metrics

---

## 3. User Personas & Stories

### 3.1 User Personas

#### Persona 1: The Diversified Investor
**Name:** Marcus Chen  
**Age:** 34  
**Occupation:** Software Engineer  
**Portfolio:** $150K across Alpaca (stocks), Coinbase (crypto), MetaMask (DeFi)

**Goals:**
- See total net worth across all platforms in one place
- Track performance without logging into 5 different apps
- Get AI summaries of relevant news for his holdings

**Pain Points:**
- Spreadsheet tracking is tedious and error-prone
- Misses important news because it's scattered across platforms
- Doesn't have time to research every holding manually

**Quote:** "I just want to know how my money is doing without spending an hour checking different apps."

---

#### Persona 2: The Crypto-Native Trader
**Name:** Zara Okonkwo  
**Age:** 27  
**Occupation:** Freelance Designer  
**Portfolio:** $40K in crypto across Binance, Kraken, and multiple wallets

**Goals:**
- Track wallet balances without manually checking each chain
- Get alerts on whale movements and market sentiment
- Research new tokens before investing

**Pain Points:**
- Hard to track DeFi positions across protocols
- News moves fast; needs real-time sentiment analysis
- Wants on-chain insights but APIs are complex

**Quote:** "The market moves 24/7 and I can't keep up manually. I need something watching for me."

---

#### Persona 3: The Research-Focused Investor
**Name:** David Park  
**Age:** 52  
**Occupation:** Financial Consultant  
**Portfolio:** $500K primarily in stocks via Interactive Brokers

**Goals:**
- Deep research into SEC filings before earnings
- Compare companies within same sector
- Generate reports for personal analysis

**Pain Points:**
- SEC EDGAR is hard to navigate
- Wants AI to summarize 100+ page 10-K filings
- Needs citations to verify AI claims

**Quote:** "I trust my own analysis, but I need help gathering and organizing the data faster."

---

#### Persona 4: The Passive Observer
**Name:** Emily Rodriguez  
**Age:** 29  
**Occupation:** Marketing Manager  
**Portfolio:** $25K in index funds and some Bitcoin

**Goals:**
- Monthly check-ins on portfolio performance
- Simple alerts if something major happens
- Understand market movements without jargon

**Pain Points:**
- Financial apps are overwhelming
- Doesn't know what questions to ask
- Wants plain-English explanations

**Quote:** "I don't want to become a day trader. Just tell me if I should be worried."

---

### 3.2 User Stories

#### Epic 1: User Authentication & Onboarding

| ID | Story | Priority | Acceptance Criteria |
|----|-------|----------|---------------------|
| AUTH-01 | As a new user, I want to register with email/password so I can create an account | P0 | Email validated, password meets requirements, account created |
| AUTH-02 | As a user, I want to log in securely so I can access my portfolio | P0 | JWT issued, session established, redirect to dashboard |
| AUTH-03 | As a user, I want to reset my password if I forget it | P1 | Reset email sent, link expires in 1 hour, password updated |
| AUTH-04 | As a user, I want to enable 2FA for extra security | P2 | TOTP setup, backup codes generated, login requires 2FA |
| AUTH-05 | As a user, I want to update my profile information | P1 | Name, timezone, currency preference saved |

#### Epic 2: Brokerage & Exchange Connections

| ID | Story | Priority | Acceptance Criteria |
|----|-------|----------|---------------------|
| CONN-01 | As a user, I want to connect my Alpaca account via OAuth | P0 | OAuth flow completes, tokens stored encrypted, positions synced |
| CONN-02 | As a user, I want to connect my Coinbase account via OAuth | P0 | OAuth flow completes, balances synced within 1 minute |
| CONN-03 | As a user, I want to add a crypto wallet by public address | P0 | Address validated, balances fetched from blockchain |
| CONN-04 | As a user, I want to see connection status for all accounts | P1 | Health indicator shown, last sync time displayed |
| CONN-05 | As a user, I want to disconnect an account and remove its data | P0 | Tokens deleted, holdings removed, confirmation shown |
| CONN-06 | As a user, I want to manually trigger a portfolio sync | P1 | Sync initiated, progress shown, completion confirmed |

#### Epic 3: Portfolio Management

| ID | Story | Priority | Acceptance Criteria |
|----|-------|----------|---------------------|
| PORT-01 | As a user, I want to see my total portfolio value | P0 | Sum of all holdings displayed in preferred currency |
| PORT-02 | As a user, I want to see all my holdings in one table | P0 | Holdings listed with symbol, quantity, price, value, P&L |
| PORT-03 | As a user, I want to see my asset allocation breakdown | P0 | Pie chart showing stocks vs crypto vs cash |
| PORT-04 | As a user, I want to track daily P&L changes | P1 | Today's gain/loss shown with percentage |
| PORT-05 | As a user, I want to view historical portfolio performance | P1 | Line chart with selectable time ranges (1D, 1W, 1M, 1Y) |
| PORT-06 | As a user, I want to see holdings grouped by source | P1 | Expandable sections per brokerage/exchange |

#### Epic 4: Market Data & Research

| ID | Story | Priority | Acceptance Criteria |
|----|-------|----------|---------------------|
| DATA-01 | As a user, I want to see real-time quotes for any stock | P0 | Price, change, volume displayed with <1 min delay |
| DATA-02 | As a user, I want to see real-time prices for any crypto | P0 | Price in USD, 24h change, market cap shown |
| DATA-03 | As a user, I want to read recent news for a ticker | P1 | Latest 10 articles shown with source and timestamp |
| DATA-04 | As a user, I want to view SEC filings for a stock | P1 | List of 10-K, 10-Q, 8-K filings with links |
| DATA-05 | As a user, I want to see company/token information | P1 | Description, sector, metrics displayed |
| DATA-06 | As a user, I want to see on-chain metrics for crypto | P2 | Active addresses, transaction volume shown |

#### Epic 5: AI Chat Assistant

| ID | Story | Priority | Acceptance Criteria |
|----|-------|----------|---------------------|
| CHAT-01 | As a user, I want to ask questions about my portfolio | P0 | AI responds with accurate portfolio data |
| CHAT-02 | As a user, I want AI responses to include sources | P0 | Every claim has a citation with link |
| CHAT-03 | As a user, I want to research stocks via chat | P0 | AI fetches and analyzes stock data |
| CHAT-04 | As a user, I want to research crypto via chat | P0 | AI fetches and analyzes crypto data |
| CHAT-05 | As a user, I want to see my chat history | P1 | Previous sessions listed, messages loadable |
| CHAT-06 | As a user, I want AI to summarize SEC filings | P1 | Key points extracted with section citations |

#### Epic 6: Watchlists & Alerts

| ID | Story | Priority | Acceptance Criteria |
|----|-------|----------|---------------------|
| WATCH-01 | As a user, I want to create custom watchlists | P1 | Watchlist created with name, tickers added |
| WATCH-02 | As a user, I want to set price alerts | P1 | Alert triggers when price crosses threshold |
| WATCH-03 | As a user, I want to receive notifications for alerts | P2 | Push/email notification sent within 1 minute |
| WATCH-04 | As a user, I want to see all my active alerts | P1 | List of alerts with status and trigger conditions |

---

## 4. Technical Architecture

### 4.1 System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT LAYER                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   Web App       │  │   Mobile App    │  │   API Clients   │             │
│  │   (Next.js)     │  │   (Future)      │  │   (REST/WS)     │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
└───────────┼─────────────────────┼─────────────────────┼─────────────────────┘
            │                     │                     │
            └─────────────────────┼─────────────────────┘
                                  │ HTTPS / WSS
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              API GATEWAY                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Rate Limiting │ Authentication │ Request Validation │ CORS         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BACKEND API (NestJS)                              │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                         APPLICATION MODULES                          │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐        │  │
│  │  │  Auth   │ │ Users   │ │Portfolio│ │  Chat   │ │ Alerts  │        │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘        │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐        │  │
│  │  │Brokerage│ │Exchange │ │ Wallet  │ │Watchlist│ │Analytics│        │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘        │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                         SERVICE LAYER                                │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐       │  │
│  │  │ Portfolio       │  │ Market Data     │  │ AI/RAG          │       │  │
│  │  │ Aggregation     │  │ Service         │  │ Pipeline        │       │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘       │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
         ▼                         ▼                         ▼
┌─────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│   PostgreSQL    │    │       Redis         │    │   Message Queue     │
│   (Primary DB)  │    │   (Cache + PubSub)  │    │   (Bull/BullMQ)     │
│                 │    │                     │    │                     │
│ • Users         │    │ • Quote Cache       │    │ • Sync Jobs         │
│ • Connections   │    │ • Session Store     │    │ • Scraping Jobs     │
│ • Holdings      │    │ • Rate Limit        │    │ • Alert Jobs        │
│ • Chat History  │    │ • Real-time PubSub  │    │ • AI Processing     │
│ • Audit Logs    │    │                     │    │                     │
└─────────────────┘    └─────────────────────┘    └─────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DATA SCRAPING LAYER                                │
│                                                                             │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                      SCRAPER ORCHESTRATOR                          │    │
│  │  • Job Scheduling (Cron) • Rate Limit Management • Retry Logic     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │   Stock     │ │   Crypto    │ │    News     │ │   Filing    │          │
│  │  Scraper    │ │  Scraper    │ │  Scraper    │ │  Scraper    │          │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘          │
│         │               │               │               │                  │
│         ▼               ▼               ▼               ▼                  │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                     EXTERNAL API ADAPTERS                           │  │
│  │  Yahoo │ Finnhub │ Polygon │ CoinGecko │ Binance │ EDGAR │ NewsAPI  │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EXTERNAL SERVICES                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  BROKERAGES        │  EXCHANGES         │  AI                       │   │
│  │  • Alpaca          │  • Coinbase        │  • Anthropic Claude       │   │
│  │  • Interactive     │  • Binance         │                           │   │
│  │    Brokers         │  • Kraken          │                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  MARKET DATA       │  BLOCKCHAIN        │  NEWS/FILINGS             │   │
│  │  • Yahoo Finance   │  • Etherscan       │  • SEC EDGAR              │   │
│  │  • Finnhub         │  • Blockchain.com  │  • Finnhub News           │   │
│  │  • CoinGecko       │  • Solscan         │  • CryptoPanic            │   │
│  │  • CoinMarketCap   │                    │  • NewsAPI                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Technology Stack

#### Backend Core
| Component | Technology | Purpose |
|-----------|------------|---------|
| Framework | NestJS (TypeScript) | Modular, scalable API framework |
| Runtime | Node.js 20+ | JavaScript runtime |
| Database | PostgreSQL 16 | Primary data store |
| ORM | TypeORM | Database abstraction |
| Cache | Redis 7 | Caching, sessions, pub/sub |
| Queue | BullMQ | Background job processing |
| Validation | class-validator | Request validation |
| Documentation | Swagger/OpenAPI | API documentation |

#### External Integrations
| Category | Services | Purpose |
|----------|----------|---------|
| Stock Data | Yahoo Finance, Finnhub, Polygon.io | Quotes, metrics, history |
| Crypto Data | CoinGecko, CoinMarketCap, Binance | Prices, market data |
| Brokerages | Alpaca, Interactive Brokers | Stock portfolio sync |
| Exchanges | Coinbase, Binance, Kraken | Crypto portfolio sync |
| Blockchain | Etherscan, Blockchain.com, Solscan | Wallet balance lookup |
| News | Finnhub, CryptoPanic, NewsAPI | Market news |
| Filings | SEC EDGAR | Company filings |
| AI | Anthropic Claude | Chat assistant |

### 4.3 Module Structure

```
/backend/src/
├── main.ts                          # Application entry point
├── app.module.ts                    # Root module
│
├── common/                          # Shared utilities
│   ├── decorators/                  # Custom decorators
│   ├── filters/                     # Exception filters
│   ├── guards/                      # Auth guards
│   ├── interceptors/                # Logging, transform
│   ├── pipes/                       # Validation pipes
│   └── utils/                       # Helper functions
│
├── config/                          # Configuration
│   ├── database.config.ts
│   ├── redis.config.ts
│   ├── jwt.config.ts
│   └── external-apis.config.ts
│
├── modules/
│   ├── auth/                        # Authentication
│   │   ├── auth.module.ts
│   │   ├── auth.controller.ts
│   │   ├── auth.service.ts
│   │   ├── strategies/
│   │   │   ├── jwt.strategy.ts
│   │   │   └── local.strategy.ts
│   │   └── dto/
│   │       ├── register.dto.ts
│   │       ├── login.dto.ts
│   │       └── tokens.dto.ts
│   │
│   ├── users/                       # User management
│   │   ├── users.module.ts
│   │   ├── users.controller.ts
│   │   ├── users.service.ts
│   │   ├── entities/
│   │   │   └── user.entity.ts
│   │   └── dto/
│   │       ├── create-user.dto.ts
│   │       └── update-user.dto.ts
│   │
│   ├── connections/                 # Brokerage/Exchange connections
│   │   ├── connections.module.ts
│   │   ├── connections.controller.ts
│   │   ├── connections.service.ts
│   │   ├── providers/
│   │   │   ├── alpaca.provider.ts
│   │   │   ├── coinbase.provider.ts
│   │   │   ├── binance.provider.ts
│   │   │   └── wallet.provider.ts
│   │   ├── entities/
│   │   │   └── connection.entity.ts
│   │   └── dto/
│   │
│   ├── portfolio/                   # Portfolio aggregation
│   │   ├── portfolio.module.ts
│   │   ├── portfolio.controller.ts
│   │   ├── portfolio.service.ts
│   │   ├── entities/
│   │   │   ├── holding.entity.ts
│   │   │   └── snapshot.entity.ts
│   │   └── dto/
│   │
│   ├── market-data/                 # Market data service
│   │   ├── market-data.module.ts
│   │   ├── market-data.controller.ts
│   │   ├── market-data.service.ts
│   │   ├── scrapers/
│   │   │   ├── stock.scraper.ts
│   │   │   ├── crypto.scraper.ts
│   │   │   ├── news.scraper.ts
│   │   │   └── edgar.scraper.ts
│   │   ├── providers/
│   │   │   ├── yahoo-finance.provider.ts
│   │   │   ├── finnhub.provider.ts
│   │   │   ├── coingecko.provider.ts
│   │   │   └── edgar.provider.ts
│   │   ├── entities/
│   │   │   ├── stock-quote.entity.ts
│   │   │   ├── crypto-quote.entity.ts
│   │   │   ├── news-article.entity.ts
│   │   │   └── filing.entity.ts
│   │   └── dto/
│   │
│   ├── chat/                        # AI Chat
│   │   ├── chat.module.ts
│   │   ├── chat.controller.ts
│   │   ├── chat.service.ts
│   │   ├── ai/
│   │   │   ├── claude.service.ts
│   │   │   ├── rag.service.ts
│   │   │   └── tools/
│   │   │       ├── portfolio.tool.ts
│   │   │       ├── stock-quote.tool.ts
│   │   │       ├── crypto-quote.tool.ts
│   │   │       ├── news.tool.ts
│   │   │       └── filing.tool.ts
│   │   ├── entities/
│   │   │   ├── chat-session.entity.ts
│   │   │   └── chat-message.entity.ts
│   │   └── dto/
│   │
│   ├── watchlists/                  # Watchlists & Alerts
│   │   ├── watchlists.module.ts
│   │   ├── watchlists.controller.ts
│   │   ├── alerts.controller.ts
│   │   ├── watchlists.service.ts
│   │   ├── alerts.service.ts
│   │   ├── entities/
│   │   │   ├── watchlist.entity.ts
│   │   │   └── alert.entity.ts
│   │   └── dto/
│   │
│   └── analytics/                   # Usage & audit
│       ├── analytics.module.ts
│       ├── analytics.service.ts
│       └── entities/
│           └── audit-log.entity.ts
│
├── jobs/                            # Background jobs
│   ├── jobs.module.ts
│   ├── processors/
│   │   ├── sync.processor.ts
│   │   ├── scraper.processor.ts
│   │   └── alert.processor.ts
│   └── schedulers/
│       ├── portfolio-sync.scheduler.ts
│       └── market-data.scheduler.ts
│
└── database/
    ├── migrations/
    └── seeds/
```

---

## 5. Data Scraping Layer

### 5.1 Scraping Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SCRAPER ORCHESTRATOR                                │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        SCHEDULER (Cron Jobs)                        │   │
│  │                                                                     │   │
│  │  • Stock Quotes: Every 1 min (market hours) / 15 min (after hours) │   │
│  │  • Crypto Quotes: Every 1 min (24/7)                               │   │
│  │  • News: Every 5 min                                                │   │
│  │  • SEC Filings: Every 1 hour                                       │   │
│  │  • Portfolio Sync: Every 5 min                                     │   │
│  │  • On-Chain Data: Every 5 min                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         JOB QUEUE (BullMQ)                          │   │
│  │                                                                     │   │
│  │  Queues:                                                           │   │
│  │  • stock-quotes    (priority: high,   concurrency: 5)              │   │
│  │  • crypto-quotes   (priority: high,   concurrency: 5)              │   │
│  │  • news-scraper    (priority: medium, concurrency: 3)              │   │
│  │  • edgar-scraper   (priority: low,    concurrency: 2)              │   │
│  │  • portfolio-sync  (priority: high,   concurrency: 10)             │   │
│  │  • blockchain-sync (priority: medium, concurrency: 5)              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       RATE LIMITER (per provider)                   │   │
│  │                                                                     │   │
│  │  Provider          │ Limit              │ Window                   │   │
│  │  ─────────────────────────────────────────────────────────────     │   │
│  │  Yahoo Finance     │ 100 requests       │ per minute               │   │
│  │  Finnhub           │ 60 requests        │ per minute               │   │
│  │  CoinGecko         │ 50 requests        │ per minute               │   │
│  │  Binance           │ 1200 requests      │ per minute               │   │
│  │  SEC EDGAR         │ 10 requests        │ per second               │   │
│  │  Etherscan         │ 5 requests         │ per second               │   │
│  │  Anthropic         │ 60 requests        │ per minute               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            SCRAPER WORKERS                                  │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │                      STOCK QUOTE SCRAPER                          │     │
│  │                                                                   │     │
│  │  Input: List of stock symbols from user holdings + watchlists    │     │
│  │                                                                   │     │
│  │  Flow:                                                           │     │
│  │  1. Collect unique symbols from all users                        │     │
│  │  2. Batch symbols (max 10 per request)                           │     │
│  │  3. Primary: Yahoo Finance → Fallback: Finnhub                   │     │
│  │  4. Parse response → StockQuote entity                           │     │
│  │  5. Upsert to stock_quotes_cache table                           │     │
│  │  6. Publish to Redis channel: stock:quotes:{symbol}              │     │
│  │                                                                   │     │
│  │  Output: StockQuote { symbol, price, change, changePercent,      │     │
│  │          volume, marketCap, peRatio, high, low, timestamp }      │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │                      CRYPTO QUOTE SCRAPER                         │     │
│  │                                                                   │     │
│  │  Input: List of crypto symbols from holdings + watchlists        │     │
│  │                                                                   │     │
│  │  Flow:                                                           │     │
│  │  1. Collect unique crypto IDs (coingecko IDs)                    │     │
│  │  2. Batch IDs (max 100 per request on CoinGecko)                 │     │
│  │  3. Primary: CoinGecko → Fallback: Binance API                   │     │
│  │  4. Parse response → CryptoQuote entity                          │     │
│  │  5. Upsert to crypto_quotes_cache table                          │     │
│  │  6. Publish to Redis channel: crypto:quotes:{symbol}             │     │
│  │                                                                   │     │
│  │  Output: CryptoQuote { symbol, name, price, change24h,           │     │
│  │          marketCap, volume24h, circulatingSupply, timestamp }    │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │                        NEWS SCRAPER                               │     │
│  │                                                                   │     │
│  │  Input: Symbols from holdings + watchlists + trending            │     │
│  │                                                                   │     │
│  │  Flow:                                                           │     │
│  │  1. For stocks: Finnhub news API by symbol                       │     │
│  │  2. For crypto: CryptoPanic API by currencies                    │     │
│  │  3. General market: Finnhub general news                         │     │
│  │  4. Deduplicate by URL                                           │     │
│  │  5. Store in news_articles table                                 │     │
│  │  6. Link to symbols via news_article_symbols junction            │     │
│  │                                                                   │     │
│  │  Output: NewsArticle { title, summary, url, source, publishedAt, │     │
│  │          sentiment, symbols[] }                                  │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │                       EDGAR SCRAPER                               │     │
│  │                                                                   │     │
│  │  Input: Stock symbols from holdings + watchlists                 │     │
│  │                                                                   │     │
│  │  Flow:                                                           │     │
│  │  1. Map symbol → CIK using SEC ticker lookup                     │     │
│  │  2. Query EDGAR API for recent filings                           │     │
│  │  3. Filter by form type (10-K, 10-Q, 8-K)                        │     │
│  │  4. Check if already cached (by accession number)                │     │
│  │  5. If new: fetch filing document, extract key sections          │     │
│  │  6. Store in sec_filings table                                   │     │
│  │                                                                   │     │
│  │  Output: SecFiling { cik, symbol, formType, filingDate,          │     │
│  │          accessionNumber, documentUrl, extractedSections }       │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │                     BLOCKCHAIN SCRAPER                            │     │
│  │                                                                   │     │
│  │  Input: Wallet addresses from user connections                   │     │
│  │                                                                   │     │
│  │  Flow:                                                           │     │
│  │  1. Group addresses by chain (ETH, BTC, SOL)                     │     │
│  │  2. ETH: Etherscan API for balances + token balances             │     │
│  │  3. BTC: Blockchain.com API for balance                          │     │
│  │  4. SOL: Solscan API for balance + token accounts                │     │
│  │  5. Update holdings for wallet connections                       │     │
│  │                                                                   │     │
│  │  Output: WalletBalance { address, chain, nativeBalance,          │     │
│  │          tokens[{ symbol, balance, contractAddress }] }          │     │
│  └───────────────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         DATA FLOW: Quote Update                          │
│                                                                          │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌───────┐ │
│  │Scheduler│───▶│  Queue  │───▶│ Worker  │───▶│ Provider│───▶│  API  │ │
│  │ (Cron)  │    │(BullMQ) │    │         │    │ Adapter │    │(Yahoo)│ │
│  └─────────┘    └─────────┘    └────┬────┘    └─────────┘    └───────┘ │
│                                     │                                    │
│                                     ▼                                    │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                              │
│  │ Clients │◀───│  Redis  │◀───│  Cache  │                              │
│  │(WebSocket)   │ (PubSub)│    │  Layer  │                              │
│  └─────────┘    └─────────┘    └────┬────┘                              │
│                                     │                                    │
│                                     ▼                                    │
│                               ┌─────────┐                                │
│                               │PostgreSQL│                               │
│                               │ (Store)  │                               │
│                               └─────────┘                                │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.3 Scraper Configuration

```typescript
// Scraper configuration schema (for reference, not implementation)

interface ScraperConfig {
  stock: {
    providers: ['yahoo-finance', 'finnhub', 'polygon'];
    primaryProvider: 'yahoo-finance';
    schedule: {
      marketHours: '*/1 * * * *';    // Every 1 minute
      afterHours: '*/15 * * * *';    // Every 15 minutes
    };
    batchSize: 10;
    cacheTtl: 60;                    // seconds
  };
  
  crypto: {
    providers: ['coingecko', 'binance', 'coinmarketcap'];
    primaryProvider: 'coingecko';
    schedule: '*/1 * * * *';         // Every 1 minute (24/7)
    batchSize: 100;
    cacheTtl: 60;
  };
  
  news: {
    providers: ['finnhub', 'cryptopanic', 'newsapi'];
    schedule: '*/5 * * * *';         // Every 5 minutes
    maxArticlesPerSymbol: 20;
    cacheTtl: 300;
  };
  
  filings: {
    providers: ['sec-edgar'];
    schedule: '0 * * * *';           // Every hour
    formTypes: ['10-K', '10-Q', '8-K'];
    lookbackDays: 30;
  };
  
  blockchain: {
    chains: {
      ethereum: { provider: 'etherscan', schedule: '*/5 * * * *' };
      bitcoin: { provider: 'blockchain.com', schedule: '*/5 * * * *' };
      solana: { provider: 'solscan', schedule: '*/5 * * * *' };
    };
  };
}
```

### 5.4 Error Handling & Retry Strategy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ERROR HANDLING STRATEGY                             │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        RETRY CONFIGURATION                          │   │
│  │                                                                     │   │
│  │  Attempt 1: Immediate                                              │   │
│  │  Attempt 2: Wait 5 seconds                                         │   │
│  │  Attempt 3: Wait 30 seconds                                        │   │
│  │  Attempt 4: Wait 2 minutes                                         │   │
│  │  Attempt 5: Wait 10 minutes (final)                                │   │
│  │                                                                     │   │
│  │  After 5 failures:                                                 │   │
│  │  • Move to dead-letter queue                                       │   │
│  │  • Log error with full context                                     │   │
│  │  • Alert via monitoring (optional)                                 │   │
│  │  • Serve stale cache if available                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      FALLBACK HIERARCHY                             │   │
│  │                                                                     │   │
│  │  Stock Quotes:   Yahoo Finance → Finnhub → Polygon → Stale Cache   │   │
│  │  Crypto Quotes:  CoinGecko → Binance → CMC → Stale Cache           │   │
│  │  News:           Finnhub → CryptoPanic → NewsAPI → Empty           │   │
│  │  Filings:        SEC EDGAR → Stale Cache                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      ERROR CLASSIFICATION                           │   │
│  │                                                                     │   │
│  │  RETRYABLE:                                                        │   │
│  │  • 429 Too Many Requests (wait + retry)                            │   │
│  │  • 500, 502, 503, 504 Server Errors                                │   │
│  │  • ECONNRESET, ETIMEDOUT network errors                            │   │
│  │                                                                     │   │
│  │  NON-RETRYABLE:                                                    │   │
│  │  • 401 Unauthorized (invalid API key)                              │   │
│  │  • 403 Forbidden (rate limited permanently)                        │   │
│  │  • 404 Not Found (invalid symbol)                                  │   │
│  │  • 400 Bad Request (malformed request)                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Database Schema

### 6.1 Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ENTITY RELATIONSHIP DIAGRAM                           │
│                                                                             │
│  ┌──────────────┐       ┌──────────────────┐       ┌──────────────────┐    │
│  │    users     │       │   connections    │       │    holdings      │    │
│  ├──────────────┤       ├──────────────────┤       ├──────────────────┤    │
│  │ id (PK)      │──┐    │ id (PK)          │──┐    │ id (PK)          │    │
│  │ email        │  │    │ user_id (FK)     │  │    │ user_id (FK)     │    │
│  │ password_hash│  └───▶│ provider_type    │  │    │ connection_id(FK)│    │
│  │ first_name   │       │ provider_id      │  └───▶│ asset_type       │    │
│  │ last_name    │       │ access_token_enc │       │ symbol           │    │
│  │ currency     │       │ refresh_token_enc│       │ name             │    │
│  │ timezone     │       │ wallet_address   │       │ quantity         │    │
│  │ created_at   │       │ chain            │       │ avg_cost         │    │
│  │ updated_at   │       │ is_active        │       │ current_price    │    │
│  └──────────────┘       │ last_sync_at     │       │ market_value     │    │
│         │               │ sync_status      │       │ created_at       │    │
│         │               │ created_at       │       │ updated_at       │    │
│         │               └──────────────────┘       └──────────────────┘    │
│         │                                                                   │
│         │               ┌──────────────────┐       ┌──────────────────┐    │
│         │               │  chat_sessions   │       │  chat_messages   │    │
│         │               ├──────────────────┤       ├──────────────────┤    │
│         │               │ id (PK)          │──┐    │ id (PK)          │    │
│         └──────────────▶│ user_id (FK)     │  │    │ session_id (FK)  │    │
│                         │ title            │  └───▶│ role             │    │
│                         │ is_archived      │       │ content          │    │
│                         │ created_at       │       │ citations (JSON) │    │
│                         │ updated_at       │       │ tool_calls(JSON) │    │
│                         └──────────────────┘       │ tokens_used      │    │
│                                                    │ created_at       │    │
│         │               ┌──────────────────┐       └──────────────────┘    │
│         │               │   watchlists     │                               │
│         │               ├──────────────────┤       ┌──────────────────┐    │
│         │               │ id (PK)          │──┐    │ watchlist_items  │    │
│         └──────────────▶│ user_id (FK)     │  │    ├──────────────────┤    │
│                         │ name             │  │    │ id (PK)          │    │
│                         │ description      │  └───▶│ watchlist_id(FK) │    │
│                         │ created_at       │       │ asset_type       │    │
│                         │ updated_at       │       │ symbol           │    │
│                         └──────────────────┘       │ added_at         │    │
│                                                    └──────────────────┘    │
│         │               ┌──────────────────┐                               │
│         │               │     alerts       │                               │
│         │               ├──────────────────┤                               │
│         └──────────────▶│ id (PK)          │                               │
│                         │ user_id (FK)     │                               │
│                         │ asset_type       │                               │
│                         │ symbol           │                               │
│                         │ alert_type       │                               │
│                         │ condition        │                               │
│                         │ threshold        │                               │
│                         │ is_active        │                               │
│                         │ triggered_at     │                               │
│                         │ created_at       │                               │
│                         └──────────────────┘                               │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                         CACHE TABLES                                 │  │
│  │                                                                      │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │  │
│  │  │ stock_quotes    │  │ crypto_quotes   │  │ news_articles   │      │  │
│  │  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤      │  │
│  │  │ symbol (PK)     │  │ symbol (PK)     │  │ id (PK)         │      │  │
│  │  │ price           │  │ coingecko_id    │  │ title           │      │  │
│  │  │ change          │  │ name            │  │ summary         │      │  │
│  │  │ change_percent  │  │ price           │  │ url (UNIQUE)    │      │  │
│  │  │ volume          │  │ change_24h      │  │ source          │      │  │
│  │  │ market_cap      │  │ change_percent  │  │ sentiment       │      │  │
│  │  │ pe_ratio        │  │ market_cap      │  │ published_at    │      │  │
│  │  │ day_high        │  │ volume_24h      │  │ fetched_at      │      │  │
│  │  │ day_low         │  │ circulating_sup │  └─────────────────┘      │  │
│  │  │ year_high       │  │ total_supply    │                           │  │
│  │  │ year_low        │  │ ath             │  ┌─────────────────┐      │  │
│  │  │ data_source     │  │ ath_date        │  │ sec_filings     │      │  │
│  │  │ fetched_at      │  │ data_source     │  ├─────────────────┤      │  │
│  │  └─────────────────┘  │ fetched_at      │  │ id (PK)         │      │  │
│  │                       └─────────────────┘  │ cik             │      │  │
│  │                                            │ symbol          │      │  │
│  │  ┌─────────────────┐                       │ form_type       │      │  │
│  │  │ company_profiles│                       │ filing_date     │      │  │
│  │  ├─────────────────┤                       │ accession_num   │      │  │
│  │  │ symbol (PK)     │                       │ document_url    │      │  │
│  │  │ name            │                       │ primary_doc     │      │  │
│  │  │ description     │                       │ extracted_text  │      │  │
│  │  │ sector          │                       │ fetched_at      │      │  │
│  │  │ industry        │                       └─────────────────┘      │  │
│  │  │ market_cap      │                                                │  │
│  │  │ employees       │                                                │  │
│  │  │ website         │                                                │  │
│  │  │ fetched_at      │                                                │  │
│  │  └─────────────────┘                                                │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Detailed Table Schemas

#### 6.2.1 Users Table

```sql
-- Table: users
-- Purpose: Store user accounts and authentication data

CREATE TABLE users (
    -- Primary Key
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Authentication
    email               VARCHAR(255) NOT NULL UNIQUE,
    password_hash       VARCHAR(255) NOT NULL,
    email_verified      BOOLEAN DEFAULT FALSE,
    email_verified_at   TIMESTAMP WITH TIME ZONE,
    
    -- Profile
    first_name          VARCHAR(100),
    last_name           VARCHAR(100),
    avatar_url          VARCHAR(500),
    
    -- Preferences
    preferred_currency  VARCHAR(3) DEFAULT 'USD',      -- ISO 4217 currency code
    timezone            VARCHAR(50) DEFAULT 'UTC',     -- IANA timezone
    locale              VARCHAR(10) DEFAULT 'en-US',
    
    -- Security
    two_factor_enabled  BOOLEAN DEFAULT FALSE,
    two_factor_secret   VARCHAR(255),                  -- Encrypted TOTP secret
    failed_login_count  INTEGER DEFAULT 0,
    locked_until        TIMESTAMP WITH TIME ZONE,
    last_login_at       TIMESTAMP WITH TIME ZONE,
    last_login_ip       INET,
    
    -- Status
    is_active           BOOLEAN DEFAULT TRUE,
    deleted_at          TIMESTAMP WITH TIME ZONE,      -- Soft delete
    
    -- Timestamps
    created_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
```

**Field Mapping:**

| Database Field | Request DTO | Response DTO | Notes |
|---------------|-------------|--------------|-------|
| id | - | user.id | Auto-generated |
| email | email (required) | user.email | Validated format |
| password_hash | password (required) | - | Never exposed |
| first_name | firstName (optional) | user.firstName | |
| last_name | lastName (optional) | user.lastName | |
| preferred_currency | currency (optional) | user.currency | Default: USD |
| timezone | timezone (optional) | user.timezone | Default: UTC |
| created_at | - | user.createdAt | Auto-generated |

---

#### 6.2.2 Connections Table

```sql
-- Table: connections
-- Purpose: Store brokerage, exchange, and wallet connections

CREATE TABLE connections (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Provider Identification
    provider_type           VARCHAR(20) NOT NULL,       -- 'brokerage', 'exchange', 'wallet'
    provider_id             VARCHAR(50) NOT NULL,       -- 'alpaca', 'coinbase', 'ethereum', etc.
    
    -- Account Info (for OAuth providers)
    external_account_id     VARCHAR(255),               -- Provider's account ID
    account_name            VARCHAR(255),               -- Display name
    
    -- OAuth Tokens (encrypted)
    access_token_encrypted  TEXT,
    refresh_token_encrypted TEXT,
    token_expires_at        TIMESTAMP WITH TIME ZONE,
    token_scope             VARCHAR(500),               -- OAuth scopes granted
    
    -- Wallet-specific (for blockchain wallets)
    wallet_address          VARCHAR(255),               -- Public address
    chain                   VARCHAR(20),                -- 'ethereum', 'bitcoin', 'solana'
    
    -- Sync Status
    is_active               BOOLEAN DEFAULT TRUE,
    sync_status             VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'syncing', 'success', 'error'
    sync_error_message      TEXT,
    last_sync_at            TIMESTAMP WITH TIME ZONE,
    last_successful_sync_at TIMESTAMP WITH TIME ZONE,
    sync_frequency_minutes  INTEGER DEFAULT 5,
    
    -- Metadata
    metadata                JSONB DEFAULT '{}',         -- Provider-specific data
    
    -- Timestamps
    connected_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    disconnected_at         TIMESTAMP WITH TIME ZONE,
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT unique_user_provider UNIQUE (user_id, provider_type, provider_id),
    CONSTRAINT valid_provider_type CHECK (provider_type IN ('brokerage', 'exchange', 'wallet')),
    CONSTRAINT valid_sync_status CHECK (sync_status IN ('pending', 'syncing', 'success', 'error'))
);

-- Indexes
CREATE INDEX idx_connections_user_id ON connections(user_id);
CREATE INDEX idx_connections_provider ON connections(provider_type, provider_id);
CREATE INDEX idx_connections_sync_status ON connections(sync_status);
CREATE INDEX idx_connections_last_sync ON connections(last_sync_at);
```

**Provider ID Values:**

| provider_type | provider_id | Description |
|--------------|-------------|-------------|
| brokerage | alpaca | Alpaca Trading |
| brokerage | ibkr | Interactive Brokers |
| exchange | coinbase | Coinbase |
| exchange | binance | Binance |
| exchange | kraken | Kraken |
| wallet | ethereum | Ethereum wallet (by address) |
| wallet | bitcoin | Bitcoin wallet (by address) |
| wallet | solana | Solana wallet (by address) |

---

#### 6.2.3 Holdings Table

```sql
-- Table: holdings
-- Purpose: Store user portfolio positions (stocks, ETFs, crypto)

CREATE TABLE holdings (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Keys
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    connection_id           UUID NOT NULL REFERENCES connections(id) ON DELETE CASCADE,
    
    -- Asset Identification
    asset_type              VARCHAR(20) NOT NULL,       -- 'stock', 'etf', 'crypto', 'token'
    symbol                  VARCHAR(20) NOT NULL,       -- Ticker symbol (AAPL, BTC, ETH)
    name                    VARCHAR(255),               -- Full name (Apple Inc., Bitcoin)
    
    -- For crypto tokens
    contract_address        VARCHAR(255),               -- Token contract address (if applicable)
    chain                   VARCHAR(20),                -- Blockchain (ethereum, solana, etc.)
    decimals                INTEGER,                    -- Token decimals
    
    -- Position Details
    quantity                DECIMAL(30, 18) NOT NULL,   -- High precision for crypto
    avg_cost_basis          DECIMAL(20, 8),             -- Average cost per unit
    
    -- Current Valuation (updated by scraper)
    current_price           DECIMAL(20, 8),
    market_value            DECIMAL(20, 4),             -- quantity * current_price
    cost_basis_total        DECIMAL(20, 4),             -- quantity * avg_cost_basis
    
    -- P&L Calculations
    unrealized_pl           DECIMAL(20, 4),             -- market_value - cost_basis_total
    unrealized_pl_percent   DECIMAL(10, 4),             -- (unrealized_pl / cost_basis_total) * 100
    day_pl                  DECIMAL(20, 4),             -- Today's P&L
    day_pl_percent          DECIMAL(10, 4),
    
    -- Source Data
    source_position_id      VARCHAR(255),               -- Provider's position ID
    last_synced_at          TIMESTAMP WITH TIME ZONE,
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT valid_asset_type CHECK (asset_type IN ('stock', 'etf', 'crypto', 'token')),
    CONSTRAINT positive_quantity CHECK (quantity >= 0)
);

-- Indexes
CREATE INDEX idx_holdings_user_id ON holdings(user_id);
CREATE INDEX idx_holdings_connection_id ON holdings(connection_id);
CREATE INDEX idx_holdings_symbol ON holdings(symbol);
CREATE INDEX idx_holdings_asset_type ON holdings(asset_type);
CREATE INDEX idx_holdings_user_symbol ON holdings(user_id, symbol);
```

---

#### 6.2.4 Portfolio Snapshots Table

```sql
-- Table: portfolio_snapshots
-- Purpose: Store daily portfolio value snapshots for historical tracking

CREATE TABLE portfolio_snapshots (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Snapshot Date
    snapshot_date           DATE NOT NULL,
    snapshot_time           TIMESTAMP WITH TIME ZONE NOT NULL,
    
    -- Portfolio Values
    total_value             DECIMAL(20, 4) NOT NULL,
    cash_balance            DECIMAL(20, 4) DEFAULT 0,
    invested_value          DECIMAL(20, 4),             -- total_value - cash_balance
    
    -- P&L
    total_cost_basis        DECIMAL(20, 4),
    total_unrealized_pl     DECIMAL(20, 4),
    day_pl                  DECIMAL(20, 4),
    day_pl_percent          DECIMAL(10, 4),
    
    -- Breakdown
    stocks_value            DECIMAL(20, 4) DEFAULT 0,
    crypto_value            DECIMAL(20, 4) DEFAULT 0,
    
    -- Holdings Count
    holdings_count          INTEGER DEFAULT 0,
    
    -- Detailed Holdings (JSON snapshot)
    holdings_snapshot       JSONB,                      -- Array of holdings at this point
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT unique_user_date UNIQUE (user_id, snapshot_date)
);

-- Indexes
CREATE INDEX idx_snapshots_user_date ON portfolio_snapshots(user_id, snapshot_date DESC);
CREATE INDEX idx_snapshots_date ON portfolio_snapshots(snapshot_date);
```

---

#### 6.2.5 Chat Tables

```sql
-- Table: chat_sessions
-- Purpose: Store AI chat conversation sessions

CREATE TABLE chat_sessions (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Session Info
    title                   VARCHAR(255),               -- Auto-generated or user-defined
    
    -- Status
    is_archived             BOOLEAN DEFAULT FALSE,
    is_pinned               BOOLEAN DEFAULT FALSE,
    
    -- Metadata
    message_count           INTEGER DEFAULT 0,
    total_tokens_used       INTEGER DEFAULT 0,
    
    -- Timestamps
    last_message_at         TIMESTAMP WITH TIME ZONE,
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_chat_sessions_user_id ON chat_sessions(user_id);
CREATE INDEX idx_chat_sessions_updated ON chat_sessions(user_id, updated_at DESC);


-- Table: chat_messages
-- Purpose: Store individual messages in chat sessions

CREATE TABLE chat_messages (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    session_id              UUID NOT NULL REFERENCES chat_sessions(id) ON DELETE CASCADE,
    
    -- Message Content
    role                    VARCHAR(20) NOT NULL,       -- 'user', 'assistant', 'system'
    content                 TEXT NOT NULL,
    
    -- AI Response Metadata
    citations               JSONB,                      -- Array of citation objects
    tool_calls              JSONB,                      -- Array of tool call records
    
    -- Usage Tracking
    model_used              VARCHAR(100),               -- 'claude-3-5-sonnet-20241022'
    input_tokens            INTEGER,
    output_tokens           INTEGER,
    processing_time_ms      INTEGER,
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT valid_role CHECK (role IN ('user', 'assistant', 'system'))
);

-- Indexes
CREATE INDEX idx_chat_messages_session ON chat_messages(session_id, created_at);
```

**Citation JSON Structure:**
```json
{
  "citations": [
    {
      "index": 1,
      "type": "stock_quote",
      "source": "Yahoo Finance",
      "symbol": "AAPL",
      "url": "https://finance.yahoo.com/quote/AAPL",
      "timestamp": "2025-11-27T10:30:00Z",
      "text": "AAPL trading at $175.50"
    },
    {
      "index": 2,
      "type": "news",
      "source": "Reuters",
      "title": "Apple announces new product",
      "url": "https://reuters.com/...",
      "publishedAt": "2025-11-27T09:00:00Z"
    }
  ]
}
```

**Tool Calls JSON Structure:**
```json
{
  "tool_calls": [
    {
      "id": "call_001",
      "tool": "get_portfolio_holdings",
      "input": {},
      "output": { "holdings": [...] },
      "duration_ms": 45
    },
    {
      "id": "call_002",
      "tool": "get_stock_quote",
      "input": { "symbol": "AAPL" },
      "output": { "price": 175.50, "change": 2.30 },
      "duration_ms": 120
    }
  ]
}
```

---

#### 6.2.6 Watchlists & Alerts Tables

```sql
-- Table: watchlists
-- Purpose: Store user-created watchlists

CREATE TABLE watchlists (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Watchlist Info
    name                    VARCHAR(100) NOT NULL,
    description             TEXT,
    color                   VARCHAR(7),                 -- Hex color (#FF5733)
    icon                    VARCHAR(50),                -- Icon identifier
    
    -- Display Order
    sort_order              INTEGER DEFAULT 0,
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_watchlists_user_id ON watchlists(user_id);


-- Table: watchlist_items
-- Purpose: Store items (stocks/crypto) in watchlists

CREATE TABLE watchlist_items (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    watchlist_id            UUID NOT NULL REFERENCES watchlists(id) ON DELETE CASCADE,
    
    -- Asset Info
    asset_type              VARCHAR(20) NOT NULL,       -- 'stock', 'crypto'
    symbol                  VARCHAR(20) NOT NULL,
    name                    VARCHAR(255),
    
    -- Notes
    notes                   TEXT,
    target_price            DECIMAL(20, 8),
    
    -- Display Order
    sort_order              INTEGER DEFAULT 0,
    
    -- Timestamps
    added_at                TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT unique_watchlist_symbol UNIQUE (watchlist_id, asset_type, symbol)
);

-- Indexes
CREATE INDEX idx_watchlist_items_watchlist ON watchlist_items(watchlist_id);
CREATE INDEX idx_watchlist_items_symbol ON watchlist_items(symbol);


-- Table: alerts
-- Purpose: Store price and event alerts

CREATE TABLE alerts (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Asset Info
    asset_type              VARCHAR(20) NOT NULL,       -- 'stock', 'crypto'
    symbol                  VARCHAR(20) NOT NULL,
    
    -- Alert Configuration
    alert_type              VARCHAR(30) NOT NULL,       -- 'price_above', 'price_below', 'percent_change', 'volume_spike'
    condition               VARCHAR(20) NOT NULL,       -- 'gt', 'lt', 'gte', 'lte', 'eq'
    threshold_value         DECIMAL(20, 8) NOT NULL,
    threshold_unit          VARCHAR(10) DEFAULT 'value', -- 'value', 'percent'
    
    -- Notification Settings
    notify_email            BOOLEAN DEFAULT TRUE,
    notify_push             BOOLEAN DEFAULT FALSE,
    notify_sms              BOOLEAN DEFAULT FALSE,
    
    -- Status
    is_active               BOOLEAN DEFAULT TRUE,
    is_repeating            BOOLEAN DEFAULT FALSE,      -- Trigger once or multiple times
    cooldown_minutes        INTEGER DEFAULT 60,         -- Min time between repeated triggers
    
    -- Trigger History
    last_triggered_at       TIMESTAMP WITH TIME ZONE,
    trigger_count           INTEGER DEFAULT 0,
    last_checked_price      DECIMAL(20, 8),
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at              TIMESTAMP WITH TIME ZONE,   -- Optional expiration
    
    -- Constraints
    CONSTRAINT valid_alert_type CHECK (alert_type IN ('price_above', 'price_below', 'percent_change_up', 'percent_change_down', 'volume_spike')),
    CONSTRAINT valid_condition CHECK (condition IN ('gt', 'lt', 'gte', 'lte', 'eq'))
);

-- Indexes
CREATE INDEX idx_alerts_user_id ON alerts(user_id);
CREATE INDEX idx_alerts_active ON alerts(is_active, symbol);
CREATE INDEX idx_alerts_symbol ON alerts(symbol);
```

---

#### 6.2.7 Market Data Cache Tables

```sql
-- Table: stock_quotes_cache
-- Purpose: Cache real-time stock quotes

CREATE TABLE stock_quotes_cache (
    -- Primary Key (symbol is unique)
    symbol                  VARCHAR(20) PRIMARY KEY,
    
    -- Company Info
    name                    VARCHAR(255),
    exchange                VARCHAR(50),
    
    -- Price Data
    price                   DECIMAL(20, 4) NOT NULL,
    open                    DECIMAL(20, 4),
    previous_close          DECIMAL(20, 4),
    change                  DECIMAL(20, 4),
    change_percent          DECIMAL(10, 4),
    
    -- Day Range
    day_high                DECIMAL(20, 4),
    day_low                 DECIMAL(20, 4),
    
    -- 52 Week Range
    year_high               DECIMAL(20, 4),
    year_low                DECIMAL(20, 4),
    
    -- Volume & Market Data
    volume                  BIGINT,
    avg_volume              BIGINT,
    market_cap              BIGINT,
    
    -- Valuation Metrics
    pe_ratio                DECIMAL(10, 4),
    eps                     DECIMAL(10, 4),
    dividend_yield          DECIMAL(10, 4),
    beta                    DECIMAL(10, 4),
    
    -- Data Source
    data_source             VARCHAR(50) NOT NULL,       -- 'yahoo_finance', 'finnhub', 'polygon'
    
    -- Timestamps
    quote_time              TIMESTAMP WITH TIME ZONE,   -- When the quote was generated
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Market Status
    market_state            VARCHAR(20)                 -- 'pre', 'regular', 'post', 'closed'
);

-- Indexes
CREATE INDEX idx_stock_quotes_fetched ON stock_quotes_cache(fetched_at);


-- Table: crypto_quotes_cache
-- Purpose: Cache real-time cryptocurrency quotes

CREATE TABLE crypto_quotes_cache (
    -- Primary Key (symbol is unique)
    symbol                  VARCHAR(20) PRIMARY KEY,
    
    -- Identifiers
    coingecko_id            VARCHAR(100),
    coinmarketcap_id        INTEGER,
    name                    VARCHAR(255),
    
    -- Price Data (in USD)
    price                   DECIMAL(30, 18) NOT NULL,   -- High precision for small-cap coins
    price_btc               DECIMAL(30, 18),            -- Price in BTC
    price_eth               DECIMAL(30, 18),            -- Price in ETH
    
    -- Changes
    change_1h               DECIMAL(10, 4),
    change_24h              DECIMAL(10, 4),
    change_7d               DECIMAL(10, 4),
    change_30d              DECIMAL(10, 4),
    
    -- Market Data
    market_cap              BIGINT,
    market_cap_rank         INTEGER,
    fully_diluted_valuation BIGINT,
    
    -- Volume
    volume_24h              BIGINT,
    volume_change_24h       DECIMAL(10, 4),
    
    -- Supply
    circulating_supply      DECIMAL(30, 8),
    total_supply            DECIMAL(30, 8),
    max_supply              DECIMAL(30, 8),
    
    -- All-Time Data
    ath                     DECIMAL(30, 18),
    ath_date                TIMESTAMP WITH TIME ZONE,
    ath_change_percent      DECIMAL(10, 4),
    atl                     DECIMAL(30, 18),
    atl_date                TIMESTAMP WITH TIME ZONE,
    atl_change_percent      DECIMAL(10, 4),
    
    -- Data Source
    data_source             VARCHAR(50) NOT NULL,       -- 'coingecko', 'binance', 'coinmarketcap'
    
    -- Timestamps
    last_updated            TIMESTAMP WITH TIME ZONE,   -- Provider's last update
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_crypto_quotes_fetched ON crypto_quotes_cache(fetched_at);
CREATE INDEX idx_crypto_quotes_coingecko ON crypto_quotes_cache(coingecko_id);
CREATE INDEX idx_crypto_quotes_rank ON crypto_quotes_cache(market_cap_rank);


-- Table: company_profiles_cache
-- Purpose: Cache company/token information

CREATE TABLE company_profiles_cache (
    -- Primary Key
    symbol                  VARCHAR(20) PRIMARY KEY,
    
    -- Basic Info
    name                    VARCHAR(255),
    asset_type              VARCHAR(20) NOT NULL,       -- 'stock', 'crypto'
    
    -- Stock-specific
    exchange                VARCHAR(50),
    sector                  VARCHAR(100),
    industry                VARCHAR(100),
    
    -- Description
    description             TEXT,
    
    -- Company Data (stocks)
    ceo                     VARCHAR(255),
    employees               INTEGER,
    headquarters            VARCHAR(255),
    founded                 INTEGER,                    -- Year
    
    -- Crypto-specific
    categories              TEXT[],                     -- Array of categories
    platforms               JSONB,                      -- Contract addresses per chain
    
    -- Links
    website                 VARCHAR(500),
    logo_url                VARCHAR(500),
    
    -- Data Source
    data_source             VARCHAR(50) NOT NULL,
    
    -- Timestamps
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_company_profiles_type ON company_profiles_cache(asset_type);
```

---

#### 6.2.8 News & Filings Cache Tables

```sql
-- Table: news_articles
-- Purpose: Cache news articles for stocks and crypto

CREATE TABLE news_articles (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Article Info
    title                   VARCHAR(500) NOT NULL,
    summary                 TEXT,
    content                 TEXT,                       -- Full content if available
    
    -- Source
    source_name             VARCHAR(100) NOT NULL,      -- 'Reuters', 'Bloomberg', etc.
    source_url              VARCHAR(1000) NOT NULL,
    url                     VARCHAR(1000) NOT NULL UNIQUE,
    
    -- Media
    image_url               VARCHAR(1000),
    
    -- Classification
    category                VARCHAR(50),                -- 'earnings', 'merger', 'general', etc.
    sentiment               VARCHAR(20),                -- 'positive', 'negative', 'neutral'
    sentiment_score         DECIMAL(5, 4),              -- -1.0 to 1.0
    
    -- Timestamps
    published_at            TIMESTAMP WITH TIME ZONE NOT NULL,
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_news_articles_published ON news_articles(published_at DESC);
CREATE INDEX idx_news_articles_url ON news_articles(url);


-- Table: news_article_symbols
-- Purpose: Junction table linking articles to symbols

CREATE TABLE news_article_symbols (
    -- Composite Primary Key
    article_id              UUID REFERENCES news_articles(id) ON DELETE CASCADE,
    asset_type              VARCHAR(20) NOT NULL,
    symbol                  VARCHAR(20) NOT NULL,
    
    -- Relevance
    is_primary              BOOLEAN DEFAULT FALSE,      -- Main subject of article
    relevance_score         DECIMAL(5, 4),              -- 0.0 to 1.0
    
    PRIMARY KEY (article_id, asset_type, symbol)
);

-- Indexes
CREATE INDEX idx_news_symbols_symbol ON news_article_symbols(symbol, asset_type);


-- Table: sec_filings
-- Purpose: Cache SEC EDGAR filings

CREATE TABLE sec_filings (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Company Identification
    cik                     VARCHAR(20) NOT NULL,       -- SEC Central Index Key
    symbol                  VARCHAR(20),                -- Ticker if mapped
    company_name            VARCHAR(255),
    
    -- Filing Info
    form_type               VARCHAR(20) NOT NULL,       -- '10-K', '10-Q', '8-K', etc.
    filing_date             DATE NOT NULL,
    accepted_date           TIMESTAMP WITH TIME ZONE,
    report_date             DATE,                       -- Period of report
    
    -- Document References
    accession_number        VARCHAR(30) NOT NULL UNIQUE,
    file_number             VARCHAR(30),
    
    -- URLs
    filing_url              VARCHAR(500) NOT NULL,      -- SEC index page
    primary_document_url    VARCHAR(500),               -- Main document
    
    -- Content (optional - for frequently accessed filings)
    primary_document_name   VARCHAR(255),
    extracted_sections      JSONB,                      -- Key sections extracted
    
    -- Timestamps
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_sec_filings_symbol ON sec_filings(symbol);
CREATE INDEX idx_sec_filings_cik ON sec_filings(cik);
CREATE INDEX idx_sec_filings_form ON sec_filings(form_type);
CREATE INDEX idx_sec_filings_date ON sec_filings(filing_date DESC);
CREATE UNIQUE INDEX idx_sec_filings_accession ON sec_filings(accession_number);
```

---

#### 6.2.9 Audit & Analytics Tables

```sql
-- Table: audit_logs
-- Purpose: Track security and important events

CREATE TABLE audit_logs (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Actor
    user_id                 UUID REFERENCES users(id) ON DELETE SET NULL,
    
    -- Event Info
    event_type              VARCHAR(50) NOT NULL,       -- 'login', 'logout', 'connection_added', etc.
    event_category          VARCHAR(30) NOT NULL,       -- 'auth', 'connection', 'portfolio', 'chat'
    
    -- Details
    description             TEXT,
    metadata                JSONB DEFAULT '{}',
    
    -- Request Context
    ip_address              INET,
    user_agent              VARCHAR(500),
    request_id              VARCHAR(100),
    
    -- Status
    status                  VARCHAR(20) NOT NULL,       -- 'success', 'failure', 'warning'
    error_message           TEXT,
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_type ON audit_logs(event_type);
CREATE INDEX idx_audit_logs_created ON audit_logs(created_at DESC);

-- Partitioning by month (for large-scale deployments)
-- Consider partitioning audit_logs by created_at for better performance


-- Table: api_usage_logs
-- Purpose: Track external API calls for rate limiting and cost monitoring

CREATE TABLE api_usage_logs (
    -- Primary Key
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Provider Info
    provider                VARCHAR(50) NOT NULL,       -- 'yahoo_finance', 'coingecko', 'anthropic'
    endpoint                VARCHAR(255),
    
    -- Request Details
    request_params          JSONB,
    
    -- Response
    status_code             INTEGER,
    response_time_ms        INTEGER,
    
    -- Costs (for paid APIs)
    tokens_used             INTEGER,                    -- For AI APIs
    estimated_cost          DECIMAL(10, 6),            -- In USD
    
    -- Context
    triggered_by            VARCHAR(50),                -- 'scheduler', 'user_request', 'webhook'
    user_id                 UUID,                       -- If user-triggered
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_api_usage_provider ON api_usage_logs(provider);
CREATE INDEX idx_api_usage_created ON api_usage_logs(created_at DESC);

-- Consider partitioning by day for high-volume scenarios
```

---

## 7. Data Transfer Objects (DTOs)

### 7.1 Authentication DTOs

#### Register

```typescript
// POST /api/auth/register

// Request DTO
interface RegisterRequestDto {
  email: string;                    // Required, valid email format
  password: string;                 // Required, min 8 chars, uppercase, lowercase, number
  firstName?: string;               // Optional, max 100 chars
  lastName?: string;                // Optional, max 100 chars
}

// Response DTO
interface RegisterResponseDto {
  success: boolean;
  data: {
    user: {
      id: string;                   // UUID
      email: string;
      firstName: string | null;
      lastName: string | null;
      currency: string;             // Default: 'USD'
      timezone: string;             // Default: 'UTC'
      createdAt: string;            // ISO 8601 timestamp
    };
    tokens: {
      accessToken: string;          // JWT, expires in 15 minutes
      refreshToken: string;         // JWT, expires in 7 days
      expiresIn: number;            // Seconds until access token expires
      tokenType: string;            // 'Bearer'
    };
  };
}

// Validation Rules
const registerValidation = {
  email: {
    required: true,
    format: 'email',
    maxLength: 255,
    unique: true
  },
  password: {
    required: true,
    minLength: 8,
    maxLength: 100,
    pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$/,
    message: 'Password must contain uppercase, lowercase, and number'
  },
  firstName: {
    required: false,
    maxLength: 100
  },
  lastName: {
    required: false,
    maxLength: 100
  }
};
```

#### Login

```typescript
// POST /api/auth/login

// Request DTO
interface LoginRequestDto {
  email: string;                    // Required
  password: string;                 // Required
  rememberMe?: boolean;             // Optional, extends refresh token
}

// Response DTO
interface LoginResponseDto {
  success: boolean;
  data: {
    user: {
      id: string;
      email: string;
      firstName: string | null;
      lastName: string | null;
      currency: string;
      timezone: string;
      twoFactorEnabled: boolean;
      lastLoginAt: string | null;
    };
    tokens: {
      accessToken: string;
      refreshToken: string;
      expiresIn: number;
      tokenType: string;
    };
  };
}

// Error Response
interface LoginErrorDto {
  success: false;
  error: {
    code: 'INVALID_CREDENTIALS' | 'ACCOUNT_LOCKED' | 'EMAIL_NOT_VERIFIED';
    message: string;
    remainingAttempts?: number;     // If close to lockout
    lockedUntil?: string;           // If locked
  };
}
```

#### Refresh Token

```typescript
// POST /api/auth/refresh

// Request DTO
interface RefreshTokenRequestDto {
  refreshToken: string;             // Required, valid refresh JWT
}

// Response DTO
interface RefreshTokenResponseDto {
  success: boolean;
  data: {
    accessToken: string;
    refreshToken: string;           // New refresh token (rotation)
    expiresIn: number;
    tokenType: string;
  };
}
```

#### Password Reset

```typescript
// POST /api/auth/forgot-password

// Request DTO
interface ForgotPasswordRequestDto {
  email: string;                    // Required
}

// Response DTO (always success to prevent email enumeration)
interface ForgotPasswordResponseDto {
  success: boolean;
  data: {
    message: string;                // "If email exists, reset link sent"
  };
}


// POST /api/auth/reset-password

// Request DTO
interface ResetPasswordRequestDto {
  token: string;                    // Required, from email link
  newPassword: string;              // Required, same rules as register
}

// Response DTO
interface ResetPasswordResponseDto {
  success: boolean;
  data: {
    message: string;                // "Password reset successful"
  };
}
```

---

### 7.2 Connection DTOs

#### List Connections

```typescript
// GET /api/connections

// Response DTO
interface ListConnectionsResponseDto {
  success: boolean;
  data: {
    connections: ConnectionDto[];
  };
}

interface ConnectionDto {
  id: string;                       // UUID
  providerType: 'brokerage' | 'exchange' | 'wallet';
  providerId: string;               // 'alpaca', 'coinbase', 'ethereum'
  providerName: string;             // 'Alpaca', 'Coinbase', 'Ethereum Wallet'
  providerLogo: string;             // URL to provider logo
  accountName: string | null;       // User's account name at provider
  
  // Wallet-specific
  walletAddress?: string;           // For wallet connections
  chain?: string;                   // 'ethereum', 'bitcoin', 'solana'
  
  // Status
  isActive: boolean;
  syncStatus: 'pending' | 'syncing' | 'success' | 'error';
  syncErrorMessage: string | null;
  lastSyncAt: string | null;        // ISO 8601
  
  // Timestamps
  connectedAt: string;              // ISO 8601
}
```

#### Initiate OAuth Connection

```typescript
// POST /api/connections/oauth/initiate

// Request DTO
interface InitiateOAuthRequestDto {
  providerId: string;               // 'alpaca', 'coinbase', 'binance', 'kraken'
  redirectUri?: string;             // Optional override
}

// Response DTO
interface InitiateOAuthResponseDto {
  success: boolean;
  data: {
    authorizationUrl: string;       // Redirect user to this URL
    state: string;                  // CSRF state token
    codeVerifier?: string;          // For PKCE (store in session)
  };
}
```

#### Complete OAuth Connection

```typescript
// POST /api/connections/oauth/callback

// Request DTO
interface OAuthCallbackRequestDto {
  providerId: string;               // Must match initiate
  code: string;                     // Authorization code from provider
  state: string;                    // CSRF state token
  codeVerifier?: string;            // For PKCE
}

// Response DTO
interface OAuthCallbackResponseDto {
  success: boolean;
  data: {
    connection: ConnectionDto;
    holdingsCount: number;          // Number of positions synced
    totalValue: number;             // Portfolio value from this connection
  };
}
```

#### Add Wallet Connection

```typescript
// POST /api/connections/wallet

// Request DTO
interface AddWalletRequestDto {
  chain: 'ethereum' | 'bitcoin' | 'solana';
  address: string;                  // Public wallet address
  name?: string;                    // Optional display name
}

// Validation Rules
const walletValidation = {
  chain: {
    required: true,
    enum: ['ethereum', 'bitcoin', 'solana']
  },
  address: {
    required: true,
    // Ethereum: 0x followed by 40 hex chars
    // Bitcoin: starts with 1, 3, or bc1
    // Solana: base58, 32-44 chars
    custom: 'validateBlockchainAddress'
  },
  name: {
    required: false,
    maxLength: 100
  }
};

// Response DTO
interface AddWalletResponseDto {
  success: boolean;
  data: {
    connection: ConnectionDto;
    holdingsCount: number;
    totalValue: number;
  };
}
```

#### Disconnect

```typescript
// DELETE /api/connections/:id

// Response DTO
interface DisconnectResponseDto {
  success: boolean;
  data: {
    message: string;                // "Connection removed successfully"
    holdingsRemoved: number;        // Number of holdings deleted
  };
}
```

#### Manual Sync

```typescript
// POST /api/connections/:id/sync

// Response DTO
interface SyncConnectionResponseDto {
  success: boolean;
  data: {
    connection: ConnectionDto;
    holdingsUpdated: number;
    newHoldings: number;
    removedHoldings: number;
    syncDurationMs: number;
  };
}
```

---

### 7.3 Portfolio DTOs

#### Portfolio Summary

```typescript
// GET /api/portfolio/summary

// Response DTO
interface PortfolioSummaryResponseDto {
  success: boolean;
  data: {
    summary: {
      // Total Values
      totalValue: number;           // USD
      cashBalance: number;
      investedValue: number;
      
      // P&L
      totalCostBasis: number;
      totalUnrealizedPl: number;
      totalUnrealizedPlPercent: number;
      dayPl: number;
      dayPlPercent: number;
      
      // Breakdown by Asset Type
      stocksValue: number;
      stocksPercent: number;
      cryptoValue: number;
      cryptoPercent: number;
      
      // Counts
      totalHoldings: number;
      totalConnections: number;
      
      // Last Update
      lastSyncAt: string;           // ISO 8601
    };
  };
}
```

#### Portfolio Holdings

```typescript
// GET /api/portfolio/holdings
// Query params: ?assetType=stock|crypto&sortBy=value|pl|symbol&order=asc|desc

// Request Query DTO
interface GetHoldingsQueryDto {
  assetType?: 'stock' | 'crypto' | 'all';   // Filter by type
  connectionId?: string;                     // Filter by connection
  sortBy?: 'value' | 'pl' | 'plPercent' | 'symbol' | 'quantity';
  order?: 'asc' | 'desc';
  page?: number;                             // Default: 1
  limit?: number;                            // Default: 50, max: 100
}

// Response DTO
interface GetHoldingsResponseDto {
  success: boolean;
  data: {
    holdings: HoldingDto[];
    pagination: {
      page: number;
      limit: number;
      total: number;
      totalPages: number;
      hasMore: boolean;
    };
    summary: {
      totalValue: number;
      totalPl: number;
      totalPlPercent: number;
    };
  };
}

interface HoldingDto {
  id: string;                       // UUID
  connectionId: string;             // Source connection
  providerName: string;             // 'Alpaca', 'Coinbase', etc.
  
  // Asset Info
  assetType: 'stock' | 'etf' | 'crypto' | 'token';
  symbol: string;                   // 'AAPL', 'BTC', 'ETH'
  name: string;                     // 'Apple Inc.', 'Bitcoin'
  logoUrl: string | null;
  
  // Position
  quantity: number;
  avgCostBasis: number | null;
  
  // Current Value
  currentPrice: number;
  marketValue: number;
  
  // P&L
  costBasisTotal: number | null;
  unrealizedPl: number | null;
  unrealizedPlPercent: number | null;
  dayPl: number | null;
  dayPlPercent: number | null;
  
  // Allocation
  allocationPercent: number;        // % of total portfolio
  
  // Timestamps
  lastSyncedAt: string;
}
```

#### Portfolio Performance (Historical)

```typescript
// GET /api/portfolio/performance
// Query params: ?period=1D|1W|1M|3M|6M|1Y|YTD|ALL

// Request Query DTO
interface GetPerformanceQueryDto {
  period: '1D' | '1W' | '1M' | '3M' | '6M' | '1Y' | 'YTD' | 'ALL';
  interval?: 'hour' | 'day' | 'week';   // Auto-selected based on period
}

// Response DTO
interface GetPerformanceResponseDto {
  success: boolean;
  data: {
    period: string;
    startDate: string;              // ISO 8601
    endDate: string;
    
    // Summary
    startValue: number;
    endValue: number;
    change: number;
    changePercent: number;
    highValue: number;
    lowValue: number;
    
    // Data Points
    dataPoints: PerformanceDataPointDto[];
  };
}

interface PerformanceDataPointDto {
  timestamp: string;                // ISO 8601
  totalValue: number;
  stocksValue: number;
  cryptoValue: number;
  dayPl: number;
  cumulativePl: number;
}
```

#### Portfolio Allocation

```typescript
// GET /api/portfolio/allocation

// Response DTO
interface GetAllocationResponseDto {
  success: boolean;
  data: {
    // By Asset Type
    byAssetType: AllocationItemDto[];
    
    // By Sector (stocks only)
    bySector: AllocationItemDto[];
    
    // By Category (crypto only)
    byCategory: AllocationItemDto[];
    
    // By Connection
    byConnection: AllocationItemDto[];
    
    // Top Holdings
    topHoldings: {
      symbol: string;
      name: string;
      value: number;
      percent: number;
    }[];
  };
}

interface AllocationItemDto {
  name: string;                     // 'Stocks', 'Technology', 'DeFi'
  value: number;                    // USD value
  percent: number;                  // % of total
  color: string;                    // Hex color for charts
}
```

---

### 7.4 Market Data DTOs

#### Stock Quote

```typescript
// GET /api/market/stocks/:symbol/quote

// Response DTO
interface StockQuoteResponseDto {
  success: boolean;
  data: {
    quote: {
      symbol: string;
      name: string;
      exchange: string;             // 'NASDAQ', 'NYSE'
      
      // Price
      price: number;
      open: number;
      previousClose: number;
      change: number;
      changePercent: number;
      
      // Range
      dayHigh: number;
      dayLow: number;
      yearHigh: number;
      yearLow: number;
      
      // Volume
      volume: number;
      avgVolume: number;
      
      // Valuation
      marketCap: number;
      peRatio: number | null;
      eps: number | null;
      dividendYield: number | null;
      beta: number | null;
      
      // Status
      marketState: 'pre' | 'regular' | 'post' | 'closed';
      
      // Timestamp
      quoteTime: string;            // When quote was generated
      dataSource: string;           // 'yahoo_finance'
    };
  };
}
```

#### Crypto Quote

```typescript
// GET /api/market/crypto/:symbol/quote

// Response DTO
interface CryptoQuoteResponseDto {
  success: boolean;
  data: {
    quote: {
      symbol: string;               // 'BTC', 'ETH'
      name: string;                 // 'Bitcoin', 'Ethereum'
      
      // Price
      price: number;                // USD
      priceBtc: number | null;      // Price in BTC
      
      // Changes
      change1h: number;
      change1hPercent: number;
      change24h: number;
      change24hPercent: number;
      change7d: number;
      change7dPercent: number;
      change30d: number | null;
      change30dPercent: number | null;
      
      // Market Data
      marketCap: number;
      marketCapRank: number;
      fullyDilutedValuation: number | null;
      
      // Volume
      volume24h: number;
      volumeChange24h: number | null;
      
      // Supply
      circulatingSupply: number;
      totalSupply: number | null;
      maxSupply: number | null;
      
      // All-Time
      ath: number;
      athDate: string;
      athChangePercent: number;
      atl: number;
      atlDate: string;
      atlChangePercent: number;
      
      // Timestamp
      lastUpdated: string;
      dataSource: string;           // 'coingecko'
    };
  };
}
```

#### Batch Quotes

```typescript
// POST /api/market/quotes/batch

// Request DTO
interface BatchQuotesRequestDto {
  stocks?: string[];                // Array of stock symbols, max 50
  crypto?: string[];                // Array of crypto symbols, max 100
}

// Response DTO
interface BatchQuotesResponseDto {
  success: boolean;
  data: {
    stocks: {
      [symbol: string]: {
        price: number;
        change: number;
        changePercent: number;
        volume: number;
        marketCap: number;
      };
    };
    crypto: {
      [symbol: string]: {
        price: number;
        change24h: number;
        change24hPercent: number;
        volume24h: number;
        marketCap: number;
      };
    };
    errors: {
      symbol: string;
      error: string;
    }[];
  };
}
```

#### News

```typescript
// GET /api/market/news
// Query params: ?symbols=AAPL,BTC&category=earnings&limit=20

// Request Query DTO
interface GetNewsQueryDto {
  symbols?: string;                 // Comma-separated symbols
  assetType?: 'stock' | 'crypto' | 'all';
  category?: string;                // 'earnings', 'merger', 'general'
  limit?: number;                   // Default: 20, max: 50
  page?: number;
}

// Response DTO
interface GetNewsResponseDto {
  success: boolean;
  data: {
    articles: NewsArticleDto[];
    pagination: {
      page: number;
      limit: number;
      total: number;
      hasMore: boolean;
    };
  };
}

interface NewsArticleDto {
  id: string;
  title: string;
  summary: string | null;
  url: string;
  imageUrl: string | null;
  source: string;                   // 'Reuters', 'Bloomberg'
  category: string | null;
  sentiment: 'positive' | 'negative' | 'neutral' | null;
  symbols: {
    symbol: string;
    assetType: string;
    isPrimary: boolean;
  }[];
  publishedAt: string;              // ISO 8601
}
```

#### SEC Filings

```typescript
// GET /api/market/stocks/:symbol/filings
// Query params: ?formType=10-K,10-Q&limit=10

// Request Query DTO
interface GetFilingsQueryDto {
  formType?: string;                // Comma-separated: '10-K,10-Q,8-K'
  startDate?: string;               // ISO date
  endDate?: string;
  limit?: number;                   // Default: 20
}

// Response DTO
interface GetFilingsResponseDto {
  success: boolean;
  data: {
    company: {
      cik: string;
      name: string;
      symbol: string;
    };
    filings: SecFilingDto[];
  };
}

interface SecFilingDto {
  id: string;
  formType: string;                 // '10-K', '10-Q', '8-K'
  filingDate: string;               // ISO date
  reportDate: string | null;        // Period of report
  accessionNumber: string;
  description: string | null;       // '8-K: Entry into Material Agreement'
  
  // URLs
  filingUrl: string;                // SEC index page
  documentUrl: string;              // Primary document
  
  // Extracted Content (if available)
  hasSummary: boolean;
  keyHighlights: string[] | null;
}

// GET /api/market/filings/:accessionNumber

// Response DTO (single filing with content)
interface GetFilingDetailResponseDto {
  success: boolean;
  data: {
    filing: SecFilingDto & {
      sections: {
        name: string;               // 'Risk Factors', 'MD&A'
        content: string;            // Extracted text
      }[];
    };
  };
}
```

---

### 7.5 Chat DTOs

#### Create Session

```typescript
// POST /api/chat/sessions

// Request DTO
interface CreateSessionRequestDto {
  title?: string;                   // Optional initial title
  initialMessage?: string;          // Optional first message
}

// Response DTO
interface CreateSessionResponseDto {
  success: boolean;
  data: {
    session: ChatSessionDto;
    message?: ChatMessageDto;       // If initialMessage provided
  };
}

interface ChatSessionDto {
  id: string;                       // UUID
  title: string | null;
  isArchived: boolean;
  isPinned: boolean;
  messageCount: number;
  lastMessageAt: string | null;
  createdAt: string;
  updatedAt: string;
}
```

#### List Sessions

```typescript
// GET /api/chat/sessions
// Query params: ?archived=false&limit=20

// Response DTO
interface ListSessionsResponseDto {
  success: boolean;
  data: {
    sessions: ChatSessionDto[];
    pagination: {
      page: number;
      limit: number;
      total: number;
      hasMore: boolean;
    };
  };
}
```

#### Get Session Messages

```typescript
// GET /api/chat/sessions/:id/messages
// Query params: ?limit=50&before=<messageId>

// Response DTO
interface GetMessagesResponseDto {
  success: boolean;
  data: {
    session: ChatSessionDto;
    messages: ChatMessageDto[];
    pagination: {
      hasMore: boolean;
      oldestMessageId: string | null;
    };
  };
}

interface ChatMessageDto {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  
  // AI Response Metadata (assistant messages only)
  citations?: CitationDto[];
  toolCalls?: ToolCallDto[];
  
  // Usage (assistant messages only)
  tokensUsed?: number;
  modelUsed?: string;
  processingTimeMs?: number;
  
  createdAt: string;
}

interface CitationDto {
  index: number;                    // Reference number in text [1]
  type: 'stock_quote' | 'crypto_quote' | 'news' | 'filing' | 'portfolio';
  source: string;                   // 'Yahoo Finance', 'CoinGecko'
  title?: string;                   // For news/filings
  symbol?: string;
  url?: string;
  timestamp: string;
  snippet?: string;                 // Relevant text snippet
}

interface ToolCallDto {
  id: string;
  tool: string;                     // Tool name
  input: Record<string, any>;
  output: Record<string, any>;
  durationMs: number;
}
```

#### Send Message

```typescript
// POST /api/chat/sessions/:id/messages

// Request DTO
interface SendMessageRequestDto {
  content: string;                  // Required, max 4000 chars
}

// Response DTO
interface SendMessageResponseDto {
  success: boolean;
  data: {
    userMessage: ChatMessageDto;
    assistantMessage: ChatMessageDto;
  };
}
```

#### Stream Message (SSE)

```typescript
// POST /api/chat/sessions/:id/messages/stream

// Request DTO (same as SendMessage)
interface StreamMessageRequestDto {
  content: string;
}

// SSE Events
type StreamEvent = 
  | { event: 'start'; data: { messageId: string } }
  | { event: 'token'; data: { token: string } }
  | { event: 'tool_start'; data: { tool: string; input: any } }
  | { event: 'tool_end'; data: { tool: string; output: any; durationMs: number } }
  | { event: 'citation'; data: CitationDto }
  | { event: 'done'; data: { message: ChatMessageDto } }
  | { event: 'error'; data: { code: string; message: string } };
```

---

### 7.6 Watchlist & Alert DTOs

#### Watchlists

```typescript
// POST /api/watchlists

// Request DTO
interface CreateWatchlistRequestDto {
  name: string;                     // Required, max 100 chars
  description?: string;
  color?: string;                   // Hex color
}

// Response DTO
interface CreateWatchlistResponseDto {
  success: boolean;
  data: {
    watchlist: WatchlistDto;
  };
}

interface WatchlistDto {
  id: string;
  name: string;
  description: string | null;
  color: string | null;
  itemCount: number;
  totalValue: number;               // Sum of current values
  dayChange: number;
  dayChangePercent: number;
  createdAt: string;
  updatedAt: string;
}


// GET /api/watchlists/:id

// Response DTO
interface GetWatchlistResponseDto {
  success: boolean;
  data: {
    watchlist: WatchlistDto;
    items: WatchlistItemDto[];
  };
}

interface WatchlistItemDto {
  id: string;
  assetType: 'stock' | 'crypto';
  symbol: string;
  name: string;
  logoUrl: string | null;
  
  // Current Data
  price: number;
  change: number;
  changePercent: number;
  marketCap: number;
  
  // User Notes
  notes: string | null;
  targetPrice: number | null;
  
  addedAt: string;
}


// POST /api/watchlists/:id/items

// Request DTO
interface AddWatchlistItemRequestDto {
  assetType: 'stock' | 'crypto';
  symbol: string;
  notes?: string;
  targetPrice?: number;
}
```

#### Alerts

```typescript
// POST /api/alerts

// Request DTO
interface CreateAlertRequestDto {
  assetType: 'stock' | 'crypto';
  symbol: string;
  alertType: 'price_above' | 'price_below' | 'percent_change_up' | 'percent_change_down';
  thresholdValue: number;
  thresholdUnit?: 'value' | 'percent';  // Default based on alertType
  
  // Notification Preferences
  notifyEmail?: boolean;            // Default: true
  notifyPush?: boolean;             // Default: false
  
  // Repeat Settings
  isRepeating?: boolean;            // Default: false
  cooldownMinutes?: number;         // Default: 60
  expiresAt?: string;               // ISO 8601, optional expiration
}

// Response DTO
interface CreateAlertResponseDto {
  success: boolean;
  data: {
    alert: AlertDto;
  };
}

interface AlertDto {
  id: string;
  assetType: 'stock' | 'crypto';
  symbol: string;
  name: string;
  
  // Configuration
  alertType: string;
  condition: string;
  thresholdValue: number;
  thresholdUnit: string;
  
  // Current State
  currentPrice: number;
  distanceToTrigger: number;        // How far from threshold
  distancePercent: number;
  
  // Notifications
  notifyEmail: boolean;
  notifyPush: boolean;
  
  // Status
  isActive: boolean;
  isRepeating: boolean;
  triggerCount: number;
  lastTriggeredAt: string | null;
  
  // Timestamps
  createdAt: string;
  expiresAt: string | null;
}


// GET /api/alerts

// Response DTO
interface ListAlertsResponseDto {
  success: boolean;
  data: {
    alerts: AlertDto[];
    summary: {
      total: number;
      active: number;
      triggered: number;
    };
  };
}
```

---

### 7.7 Error Response DTOs

```typescript
// Standard Error Response
interface ErrorResponseDto {
  success: false;
  error: {
    code: string;                   // Machine-readable code
    message: string;                // Human-readable message
    details?: Record<string, any>;  // Additional context
    field?: string;                 // For validation errors
    timestamp: string;              // ISO 8601
    requestId: string;              // For support/debugging
  };
}

// Validation Error Response
interface ValidationErrorResponseDto {
  success: false;
  error: {
    code: 'VALIDATION_ERROR';
    message: 'Validation failed';
    details: {
      field: string;
      message: string;
      value?: any;
    }[];
  };
}

// Error Codes
enum ErrorCode {
  // Auth Errors (1xxx)
  INVALID_CREDENTIALS = 'AUTH_1001',
  TOKEN_EXPIRED = 'AUTH_1002',
  TOKEN_INVALID = 'AUTH_1003',
  ACCOUNT_LOCKED = 'AUTH_1004',
  EMAIL_NOT_VERIFIED = 'AUTH_1005',
  
  // Connection Errors (2xxx)
  CONNECTION_NOT_FOUND = 'CONN_2001',
  OAUTH_FAILED = 'CONN_2002',
  SYNC_FAILED = 'CONN_2003',
  INVALID_WALLET_ADDRESS = 'CONN_2004',
  
  // Portfolio Errors (3xxx)
  HOLDING_NOT_FOUND = 'PORT_3001',
  INSUFFICIENT_DATA = 'PORT_3002',
  
  // Market Data Errors (4xxx)
  SYMBOL_NOT_FOUND = 'DATA_4001',
  QUOTE_UNAVAILABLE = 'DATA_4002',
  RATE_LIMITED = 'DATA_4003',
  
  // Chat Errors (5xxx)
  SESSION_NOT_FOUND = 'CHAT_5001',
  MESSAGE_TOO_LONG = 'CHAT_5002',
  AI_SERVICE_ERROR = 'CHAT_5003',
  
  // General Errors (9xxx)
  VALIDATION_ERROR = 'GEN_9001',
  NOT_FOUND = 'GEN_9002',
  INTERNAL_ERROR = 'GEN_9003',
  RATE_LIMIT_EXCEEDED = 'GEN_9004',
}
```

---

## 8. API Specifications

### 8.1 API Overview

**Base URL:** `https://api.sophia.ai/v1`

**Authentication:** Bearer token (JWT) in Authorization header
```
Authorization: Bearer <access_token>
```

**Content Type:** `application/json`

**Rate Limits:**
- Global: 1000 requests/hour per user
- Auth endpoints: 10 requests/minute per IP
- Chat messages: 20 messages/minute per user
- Market data: 100 requests/minute per user

### 8.2 Endpoint Summary

| Category | Method | Endpoint | Description |
|----------|--------|----------|-------------|
| **Auth** | POST | /auth/register | Create new account |
| | POST | /auth/login | Authenticate user |
| | POST | /auth/refresh | Refresh access token |
| | POST | /auth/logout | Invalidate tokens |
| | POST | /auth/forgot-password | Request password reset |
| | POST | /auth/reset-password | Reset password with token |
| | GET | /auth/me | Get current user profile |
| | PATCH | /auth/me | Update profile |
| **Connections** | GET | /connections | List user connections |
| | GET | /connections/providers | List available providers |
| | POST | /connections/oauth/initiate | Start OAuth flow |
| | POST | /connections/oauth/callback | Complete OAuth flow |
| | POST | /connections/wallet | Add wallet by address |
| | DELETE | /connections/:id | Remove connection |
| | POST | /connections/:id/sync | Manual sync |
| | GET | /connections/:id/status | Connection health |
| **Portfolio** | GET | /portfolio/summary | Portfolio overview |
| | GET | /portfolio/holdings | List all holdings |
| | GET | /portfolio/holdings/:symbol | Holding details |
| | GET | /portfolio/performance | Historical performance |
| | GET | /portfolio/allocation | Asset allocation |
| | GET | /portfolio/snapshots | Daily snapshots |
| **Market Data** | GET | /market/stocks/:symbol/quote | Stock quote |
| | GET | /market/stocks/:symbol/profile | Company profile |
| | GET | /market/stocks/:symbol/filings | SEC filings |
| | GET | /market/crypto/:symbol/quote | Crypto quote |
| | GET | /market/crypto/:symbol/profile | Token profile |
| | POST | /market/quotes/batch | Batch quotes |
| | GET | /market/news | News articles |
| | GET | /market/filings/:accession | Filing details |
| **Chat** | POST | /chat/sessions | Create session |
| | GET | /chat/sessions | List sessions |
| | GET | /chat/sessions/:id | Get session |
| | PATCH | /chat/sessions/:id | Update session |
| | DELETE | /chat/sessions/:id | Delete session |
| | GET | /chat/sessions/:id/messages | Get messages |
| | POST | /chat/sessions/:id/messages | Send message |
| | POST | /chat/sessions/:id/messages/stream | Stream message (SSE) |
| **Watchlists** | POST | /watchlists | Create watchlist |
| | GET | /watchlists | List watchlists |
| | GET | /watchlists/:id | Get watchlist |
| | PATCH | /watchlists/:id | Update watchlist |
| | DELETE | /watchlists/:id | Delete watchlist |
| | POST | /watchlists/:id/items | Add item |
| | DELETE | /watchlists/:id/items/:itemId | Remove item |
| **Alerts** | POST | /alerts | Create alert |
| | GET | /alerts | List alerts |
| | GET | /alerts/:id | Get alert |
| | PATCH | /alerts/:id | Update alert |
| | DELETE | /alerts/:id | Delete alert |
| **System** | GET | /health | Health check |
| | GET | /health/ready | Readiness check |

---

## 9. API Testing (api.http)

```http
### ==================================================
### SOPHIA API - HTTP Test File
### ==================================================
### Environment Variables (VS Code REST Client or IntelliJ)

@baseUrl = http://localhost:3000/api/v1
@accessToken = {{loginResponse.body.data.tokens.accessToken}}
@refreshToken = {{loginResponse.body.data.tokens.refreshToken}}
@userId = {{loginResponse.body.data.user.id}}

### ==================================================
### HEALTH CHECK
### ==================================================

### Health Check
GET {{baseUrl}}/health
Content-Type: application/json

### Readiness Check
GET {{baseUrl}}/health/ready
Content-Type: application/json


### ==================================================
### AUTHENTICATION
### ==================================================

### Register New User
# @name registerResponse
POST {{baseUrl}}/auth/register
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "SecurePass123!",
  "firstName": "John",
  "lastName": "Doe"
}

### Login
# @name loginResponse
POST {{baseUrl}}/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "SecurePass123!"
}

### Refresh Token
# @name refreshResponse
POST {{baseUrl}}/auth/refresh
Content-Type: application/json

{
  "refreshToken": "{{refreshToken}}"
}

### Get Current User Profile
GET {{baseUrl}}/auth/me
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Update Profile
PATCH {{baseUrl}}/auth/me
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "firstName": "John",
  "lastName": "Smith",
  "timezone": "America/New_York",
  "currency": "USD"
}

### Forgot Password
POST {{baseUrl}}/auth/forgot-password
Content-Type: application/json

{
  "email": "test@example.com"
}

### Reset Password (use token from email)
POST {{baseUrl}}/auth/reset-password
Content-Type: application/json

{
  "token": "reset-token-from-email",
  "newPassword": "NewSecurePass456!"
}

### Logout
POST {{baseUrl}}/auth/logout
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### CONNECTIONS
### ==================================================

### List Available Providers
GET {{baseUrl}}/connections/providers
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### List User Connections
# @name connectionsResponse
GET {{baseUrl}}/connections
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Initiate Alpaca OAuth
# @name alpacaOAuthResponse
POST {{baseUrl}}/connections/oauth/initiate
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "providerId": "alpaca"
}

### Complete Alpaca OAuth (use code from redirect)
POST {{baseUrl}}/connections/oauth/callback
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "providerId": "alpaca",
  "code": "authorization-code-from-redirect",
  "state": "{{alpacaOAuthResponse.body.data.state}}"
}

### Initiate Coinbase OAuth
# @name coinbaseOAuthResponse
POST {{baseUrl}}/connections/oauth/initiate
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "providerId": "coinbase"
}

### Add Ethereum Wallet
# @name walletResponse
POST {{baseUrl}}/connections/wallet
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "chain": "ethereum",
  "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f8fE0d",
  "name": "My Main Wallet"
}

### Add Bitcoin Wallet
POST {{baseUrl}}/connections/wallet
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "chain": "bitcoin",
  "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
  "name": "BTC Cold Storage"
}

### Add Solana Wallet
POST {{baseUrl}}/connections/wallet
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "chain": "solana",
  "address": "DRpbCBMxVnDK7maPMoAqzPHwsN4T9YJPX9Y8VW5M9JB7",
  "name": "SOL Wallet"
}

### Get Connection Status
@connectionId = {{connectionsResponse.body.data.connections[0].id}}
GET {{baseUrl}}/connections/{{connectionId}}/status
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Manual Sync Connection
POST {{baseUrl}}/connections/{{connectionId}}/sync
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Disconnect (Delete Connection)
DELETE {{baseUrl}}/connections/{{connectionId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### PORTFOLIO
### ==================================================

### Get Portfolio Summary
GET {{baseUrl}}/portfolio/summary
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get All Holdings
GET {{baseUrl}}/portfolio/holdings
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Holdings (Stocks Only)
GET {{baseUrl}}/portfolio/holdings?assetType=stock&sortBy=value&order=desc
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Holdings (Crypto Only)
GET {{baseUrl}}/portfolio/holdings?assetType=crypto&sortBy=plPercent&order=desc
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Holdings (Paginated)
GET {{baseUrl}}/portfolio/holdings?page=1&limit=10
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Single Holding Details
GET {{baseUrl}}/portfolio/holdings/AAPL
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Portfolio Performance (1 Month)
GET {{baseUrl}}/portfolio/performance?period=1M
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Portfolio Performance (1 Year)
GET {{baseUrl}}/portfolio/performance?period=1Y&interval=week
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Portfolio Performance (YTD)
GET {{baseUrl}}/portfolio/performance?period=YTD
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Asset Allocation
GET {{baseUrl}}/portfolio/allocation
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Portfolio Snapshots (Historical)
GET {{baseUrl}}/portfolio/snapshots?startDate=2025-01-01&endDate=2025-11-27
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### MARKET DATA - STOCKS
### ==================================================

### Get Stock Quote
GET {{baseUrl}}/market/stocks/AAPL/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Stock Quote (Different Symbol)
GET {{baseUrl}}/market/stocks/MSFT/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Stock Quote (TSLA)
GET {{baseUrl}}/market/stocks/TSLA/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Company Profile
GET {{baseUrl}}/market/stocks/AAPL/profile
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get SEC Filings (All Types)
GET {{baseUrl}}/market/stocks/AAPL/filings
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get SEC Filings (10-K Only)
GET {{baseUrl}}/market/stocks/AAPL/filings?formType=10-K&limit=5
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get SEC Filings (10-Q and 10-K)
GET {{baseUrl}}/market/stocks/MSFT/filings?formType=10-K,10-Q&limit=10
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Filing Details
GET {{baseUrl}}/market/filings/0000320193-24-000081
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### MARKET DATA - CRYPTO
### ==================================================

### Get Crypto Quote (Bitcoin)
GET {{baseUrl}}/market/crypto/BTC/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Crypto Quote (Ethereum)
GET {{baseUrl}}/market/crypto/ETH/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Crypto Quote (Solana)
GET {{baseUrl}}/market/crypto/SOL/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Token Profile
GET {{baseUrl}}/market/crypto/ETH/profile
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### MARKET DATA - BATCH & NEWS
### ==================================================

### Batch Quotes (Mixed)
POST {{baseUrl}}/market/quotes/batch
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "stocks": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
  "crypto": ["BTC", "ETH", "SOL", "XRP", "ADA"]
}

### Get News (General)
GET {{baseUrl}}/market/news?limit=20
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get News (Specific Symbols)
GET {{baseUrl}}/market/news?symbols=AAPL,MSFT,BTC&limit=10
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get News (Stocks Only)
GET {{baseUrl}}/market/news?assetType=stock&limit=15
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get News (Crypto Only)
GET {{baseUrl}}/market/news?assetType=crypto&limit=15
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### CHAT
### ==================================================

### Create New Chat Session
# @name createSessionResponse
POST {{baseUrl}}/chat/sessions
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "title": "Portfolio Analysis"
}

### Create Session with Initial Message
POST {{baseUrl}}/chat/sessions
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "initialMessage": "What's my portfolio looking like today?"
}

### List Chat Sessions
GET {{baseUrl}}/chat/sessions?limit=20
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### List Chat Sessions (Non-archived only)
GET {{baseUrl}}/chat/sessions?archived=false&limit=10
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Session Details
@sessionId = {{createSessionResponse.body.data.session.id}}
GET {{baseUrl}}/chat/sessions/{{sessionId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Session Messages
GET {{baseUrl}}/chat/sessions/{{sessionId}}/messages?limit=50
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Send Message - Portfolio Question
POST {{baseUrl}}/chat/sessions/{{sessionId}}/messages
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "content": "What's my total portfolio value and how did it perform today?"
}

### Send Message - Stock Research
POST {{baseUrl}}/chat/sessions/{{sessionId}}/messages
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "content": "Tell me about AAPL. What's the current price and recent news?"
}

### Send Message - Crypto Research
POST {{baseUrl}}/chat/sessions/{{sessionId}}/messages
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "content": "What's happening with Bitcoin today? Any significant news?"
}

### Send Message - SEC Filing Analysis
POST {{baseUrl}}/chat/sessions/{{sessionId}}/messages
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "content": "Can you summarize Apple's latest 10-K filing? What are the key risk factors?"
}

### Send Message - Comparison
POST {{baseUrl}}/chat/sessions/{{sessionId}}/messages
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "content": "Compare my stock holdings vs crypto holdings. Which performed better this month?"
}

### Send Message - Allocation Analysis
POST {{baseUrl}}/chat/sessions/{{sessionId}}/messages
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "content": "What's my current asset allocation? Am I too heavy in any sector?"
}

### Update Session Title
PATCH {{baseUrl}}/chat/sessions/{{sessionId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "title": "November Portfolio Review",
  "isPinned": true
}

### Archive Session
PATCH {{baseUrl}}/chat/sessions/{{sessionId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "isArchived": true
}

### Delete Session
DELETE {{baseUrl}}/chat/sessions/{{sessionId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### WATCHLISTS
### ==================================================

### Create Watchlist
# @name createWatchlistResponse
POST {{baseUrl}}/watchlists
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Tech Giants",
  "description": "Large cap tech stocks to watch",
  "color": "#4285F4"
}

### Create Another Watchlist
POST {{baseUrl}}/watchlists
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Crypto Opportunities",
  "description": "Cryptos I'm considering",
  "color": "#F7931A"
}

### List Watchlists
GET {{baseUrl}}/watchlists
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Watchlist Details
@watchlistId = {{createWatchlistResponse.body.data.watchlist.id}}
GET {{baseUrl}}/watchlists/{{watchlistId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Add Stock to Watchlist
# @name addItemResponse
POST {{baseUrl}}/watchlists/{{watchlistId}}/items
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "assetType": "stock",
  "symbol": "NVDA",
  "notes": "Strong AI growth potential",
  "targetPrice": 600
}

### Add Another Stock to Watchlist
POST {{baseUrl}}/watchlists/{{watchlistId}}/items
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "assetType": "stock",
  "symbol": "META",
  "notes": "Metaverse bet"
}

### Add Crypto to Watchlist
POST {{baseUrl}}/watchlists/{{watchlistId}}/items
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "assetType": "crypto",
  "symbol": "ETH",
  "notes": "Wait for dip to accumulate",
  "targetPrice": 2000
}

### Update Watchlist
PATCH {{baseUrl}}/watchlists/{{watchlistId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Tech Giants & AI",
  "description": "Updated focus on AI"
}

### Remove Item from Watchlist
@itemId = {{addItemResponse.body.data.item.id}}
DELETE {{baseUrl}}/watchlists/{{watchlistId}}/items/{{itemId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Delete Watchlist
DELETE {{baseUrl}}/watchlists/{{watchlistId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### ALERTS
### ==================================================

### Create Price Alert (Above)
# @name createAlertResponse
POST {{baseUrl}}/alerts
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "assetType": "stock",
  "symbol": "AAPL",
  "alertType": "price_above",
  "thresholdValue": 200,
  "notifyEmail": true,
  "notifyPush": true
}

### Create Price Alert (Below)
POST {{baseUrl}}/alerts
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "assetType": "crypto",
  "symbol": "BTC",
  "alertType": "price_below",
  "thresholdValue": 90000,
  "notifyEmail": true,
  "isRepeating": true,
  "cooldownMinutes": 120
}

### Create Percent Change Alert
POST {{baseUrl}}/alerts
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "assetType": "crypto",
  "symbol": "ETH",
  "alertType": "percent_change_up",
  "thresholdValue": 10,
  "thresholdUnit": "percent",
  "notifyEmail": true,
  "expiresAt": "2025-12-31T23:59:59Z"
}

### List Alerts
GET {{baseUrl}}/alerts
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### List Active Alerts Only
GET {{baseUrl}}/alerts?active=true
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Get Alert Details
@alertId = {{createAlertResponse.body.data.alert.id}}
GET {{baseUrl}}/alerts/{{alertId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Update Alert
PATCH {{baseUrl}}/alerts/{{alertId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "thresholdValue": 210,
  "isActive": true
}

### Disable Alert
PATCH {{baseUrl}}/alerts/{{alertId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "isActive": false
}

### Delete Alert
DELETE {{baseUrl}}/alerts/{{alertId}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}


### ==================================================
### ERROR TESTING
### ==================================================

### Invalid Login (Wrong Password)
POST {{baseUrl}}/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "WrongPassword123"
}

### Unauthorized Request (No Token)
GET {{baseUrl}}/portfolio/summary
Content-Type: application/json

### Unauthorized Request (Invalid Token)
GET {{baseUrl}}/portfolio/summary
Content-Type: application/json
Authorization: Bearer invalid-token-here

### Invalid Symbol
GET {{baseUrl}}/market/stocks/INVALID123/quote
Content-Type: application/json
Authorization: Bearer {{accessToken}}

### Validation Error (Missing Required Field)
POST {{baseUrl}}/auth/register
Content-Type: application/json

{
  "email": "incomplete@example.com"
}

### Validation Error (Invalid Email)
POST {{baseUrl}}/auth/register
Content-Type: application/json

{
  "email": "not-an-email",
  "password": "ValidPass123!"
}

### Validation Error (Weak Password)
POST {{baseUrl}}/auth/register
Content-Type: application/json

{
  "email": "test2@example.com",
  "password": "weak"
}

### Invalid Wallet Address
POST {{baseUrl}}/connections/wallet
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "chain": "ethereum",
  "address": "not-a-valid-address"
}

### Resource Not Found
GET {{baseUrl}}/chat/sessions/00000000-0000-0000-0000-000000000000
Content-Type: application/json
Authorization: Bearer {{accessToken}}
```

---

## 10. Security & Compliance

### 10.1 Security Requirements

#### Authentication & Authorization
- Passwords hashed with bcrypt (12 rounds)
- JWT access tokens: 15-minute expiry
- JWT refresh tokens: 7-day expiry (rotated on use)
- Rate limiting on auth endpoints (10/min per IP)
- Account lockout after 5 failed attempts (30 min)
- Session invalidation on password change

#### Data Encryption
- **At Rest:**
  - OAuth tokens encrypted with AES-256-GCM
  - Encryption key from environment variable
  - Database backups encrypted
- **In Transit:**
  - TLS 1.3 for all API traffic
  - Certificate pinning for mobile apps (future)

#### API Security
- CORS whitelist for frontend domains
- CSRF protection via SameSite cookies
- Input validation on all endpoints
- Parameterized queries (TypeORM)
- Request size limits (10MB)
- Rate limiting per user/IP

### 10.2 Compliance

- GDPR: Data export, deletion rights
- No financial advice (informational only)
- Read-only brokerage access (no trading)
- Audit logging for security events
- Privacy policy and terms of service

---

## 11. Implementation Plan

### Phase 1: Foundation (Weeks 1-2)
- Project setup (NestJS, PostgreSQL, Redis)
- Database schema and migrations
- Authentication module (JWT, registration, login)
- Basic user management

### Phase 2: Connections (Weeks 3-4)
- Alpaca OAuth integration
- Coinbase OAuth integration
- Wallet connection (Ethereum, Bitcoin, Solana)
- Token encryption
- Connection management API

### Phase 3: Portfolio (Weeks 5-6)
- Portfolio sync service
- Holdings aggregation
- Portfolio summary API
- Historical snapshots
- Background sync jobs (BullMQ)

### Phase 4: Market Data (Weeks 7-8)
- Stock data scrapers (Yahoo, Finnhub)
- Crypto data scrapers (CoinGecko, Binance)
- News scraper (Finnhub, CryptoPanic)
- SEC EDGAR scraper
- Caching layer
- Rate limiting

### Phase 5: AI Chat (Weeks 9-10)
- Claude integration
- RAG pipeline
- Tool definitions
- Citation system
- Chat API
- Streaming (SSE)

### Phase 6: Watchlists & Alerts (Week 11)
- Watchlist CRUD
- Alert CRUD
- Alert processing job
- Notification service (email)

### Phase 7: Polish & Deploy (Week 12)
- Testing (unit, integration, E2E)
- Error handling
- Logging & monitoring
- Documentation
- Deployment (Railway/Render)

---

## 12. Success Metrics

### MVP Launch Criteria
- [ ] Users can register/login
- [ ] Users can connect at least 1 brokerage + 1 exchange
- [ ] Portfolio syncs within 2 minutes
- [ ] Dashboard shows accurate values
- [ ] Chat responds in <5 seconds
- [ ] All AI responses have citations
- [ ] Market data <1 minute delay

### KPIs
- **Activation:** 70% connect at least 1 account
- **Engagement:** 5 chat messages per session average
- **Sync reliability:** >99% success rate
- **API performance:** p95 <200ms
- **AI quality:** 100% responses with valid citations

---

## Appendices

### A. Provider Configuration

| Provider | Type | Auth | Rate Limit | Notes |
|----------|------|------|------------|-------|
| Alpaca | Brokerage | OAuth 2.0 | 200/min | Paper trading for dev |
| Coinbase | Exchange | OAuth 2.0 | 10,000/hour | |
| Binance | Exchange | API Key | 1,200/min | |
| Yahoo Finance | Data | None | ~100/min | Unofficial |
| Finnhub | Data | API Key | 60/min (free) | |
| CoinGecko | Data | API Key | 50/min (free) | |
| SEC EDGAR | Data | None | 10/sec | User-Agent required |
| Anthropic | AI | API Key | 60/min | claude-3-5-sonnet |

### B. Environment Variables

```env
# Application
NODE_ENV=development
PORT=3000
API_VERSION=v1

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/sophia
DATABASE_SSL=false

# Redis
REDIS_URL=redis://localhost:6379

# JWT
JWT_SECRET=your-256-bit-secret
JWT_ACCESS_EXPIRY=15m
JWT_REFRESH_EXPIRY=7d

# Encryption
ENCRYPTION_KEY=your-32-byte-hex-key

# Alpaca
ALPACA_CLIENT_ID=
ALPACA_CLIENT_SECRET=
ALPACA_REDIRECT_URI=

# Coinbase
COINBASE_CLIENT_ID=
COINBASE_CLIENT_SECRET=
COINBASE_REDIRECT_URI=

# Binance
BINANCE_API_KEY=
BINANCE_API_SECRET=

# Market Data
FINNHUB_API_KEY=
COINGECKO_API_KEY=
POLYGON_API_KEY=

# Blockchain
ETHERSCAN_API_KEY=
SOLSCAN_API_KEY=

# AI
ANTHROPIC_API_KEY=

# Email (for alerts)
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=
EMAIL_FROM=

# Frontend
FRONTEND_URL=http://localhost:3001
```

---

**Document Version:** 1.0  
**Last Updated:** November 27, 2025
```
