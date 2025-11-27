# Product Requirements Document (PRD)
# SOPHIA — Your Intelligent Market Mind

**Version:** 2.0  
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
- On-chain analytics (Etherscan, Blockchain.com, Glassnode APIs)

#### Feature 3: AI Chat Assistant (Sophia)
- Portfolio analysis and Q&A
- Stock and crypto research
- News summarization
- Comparative analysis
- All responses include cited sources
- Powered by Anthropic Claude with Portkey observability

#### Feature 4: Watchlists & Alerts
- Custom watchlists (mixed stocks + crypto)
- Price threshold alerts
- News mention alerts
- Volume spike alerts
- Portfolio change notifications
- Multi-channel delivery via Novu (email, push, SMS)

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

### 3.2 User Stories with Route Mapping

#### Epic 1: User Authentication & Onboarding

| ID | Story | Priority | Routes | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| AUTH-01 | As a new user, I want to register with email/password so I can create an account | P0 | `POST /auth/register` | Email validated, password meets requirements, account created |
| AUTH-02 | As a user, I want to log in securely so I can access my portfolio | P0 | `POST /auth/login` | JWT issued, session established, redirect to dashboard |
| AUTH-03 | As a user, I want to reset my password if I forget it | P1 | `POST /auth/forgot-password`<br>`POST /auth/reset-password` | Reset email sent, link expires in 1 hour, password updated |
| AUTH-04 | As a user, I want to enable 2FA for extra security | P2 | `POST /auth/2fa/setup`<br>`POST /auth/2fa/verify`<br>`POST /auth/2fa/disable`<br>`GET /auth/2fa/backup-codes`<br>`POST /auth/2fa/backup-codes/regenerate` | TOTP setup, backup codes generated, login requires 2FA |
| AUTH-05 | As a user, I want to update my profile information | P1 | `GET /auth/me`<br>`PATCH /auth/me` | Name, timezone, currency preference saved |

**Supporting Routes:**
- `POST /auth/refresh` — Refresh access token
- `POST /auth/logout` — Invalidate tokens

---

#### Epic 2: Brokerage & Exchange Connections

| ID | Story | Priority | Routes | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| CONN-01 | As a user, I want to connect my Alpaca account via OAuth | P0 | `POST /connections/oauth/initiate`<br>`POST /connections/oauth/callback` | OAuth flow completes, tokens stored encrypted, positions synced |
| CONN-02 | As a user, I want to connect my Coinbase account via OAuth | P0 | `POST /connections/oauth/initiate`<br>`POST /connections/oauth/callback` | OAuth flow completes, balances synced within 1 minute |
| CONN-03 | As a user, I want to add a crypto wallet by public address | P0 | `POST /connections/wallet` | Address validated, balances fetched from blockchain |
| CONN-04 | As a user, I want to see connection status for all accounts | P1 | `GET /connections`<br>`GET /connections/:id/status` | Health indicator shown, last sync time displayed |
| CONN-05 | As a user, I want to disconnect an account and remove its data | P0 | `DELETE /connections/:id` | Tokens deleted, holdings removed, confirmation shown |
| CONN-06 | As a user, I want to manually trigger a portfolio sync | P1 | `POST /connections/:id/sync` | Sync initiated, progress shown, completion confirmed |

**Supporting Routes:**
- `GET /connections/providers` — List available providers

---

#### Epic 3: Portfolio Management

| ID | Story | Priority | Routes | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| PORT-01 | As a user, I want to see my total portfolio value | P0 | `GET /portfolio/summary` | Sum of all holdings displayed in preferred currency |
| PORT-02 | As a user, I want to see all my holdings in one table | P0 | `GET /portfolio/holdings` | Holdings listed with symbol, quantity, price, value, P&L |
| PORT-03 | As a user, I want to see my asset allocation breakdown | P0 | `GET /portfolio/allocation` | Pie chart showing stocks vs crypto vs cash |
| PORT-04 | As a user, I want to track daily P&L changes | P1 | `GET /portfolio/summary` | Today's gain/loss shown with percentage |
| PORT-05 | As a user, I want to view historical portfolio performance | P1 | `GET /portfolio/performance` | Line chart with selectable time ranges (1D, 1W, 1M, 1Y) |
| PORT-06 | As a user, I want to see holdings grouped by source | P1 | `GET /portfolio/holdings?connectionId=<id>` | Expandable sections per brokerage/exchange |

**Supporting Routes:**
- `GET /portfolio/holdings/:symbol` — Single holding details
- `GET /portfolio/snapshots` — Daily snapshots for history

---

#### Epic 4: Market Data & Research

| ID | Story | Priority | Routes | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| DATA-01 | As a user, I want to see real-time quotes for any stock | P0 | `GET /market/stocks/:symbol/quote` | Price, change, volume displayed with <1 min delay |
| DATA-02 | As a user, I want to see real-time prices for any crypto | P0 | `GET /market/crypto/:symbol/quote` | Price in USD, 24h change, market cap shown |
| DATA-03 | As a user, I want to read recent news for a ticker | P1 | `GET /market/news?symbols=<symbol>` | Latest 10 articles shown with source and timestamp |
| DATA-04 | As a user, I want to view SEC filings for a stock | P1 | `GET /market/stocks/:symbol/filings`<br>`GET /market/filings/:accession` | List of 10-K, 10-Q, 8-K filings with links |
| DATA-05 | As a user, I want to see company/token information | P1 | `GET /market/stocks/:symbol/profile`<br>`GET /market/crypto/:symbol/profile` | Description, sector, metrics displayed |
| DATA-06 | As a user, I want to see on-chain metrics for crypto | P2 | `GET /market/crypto/:symbol/onchain` | Active addresses, transaction volume, whale activity shown |

**Supporting Routes:**
- `POST /market/quotes/batch` — Batch quotes for multiple symbols

---

#### Epic 5: AI Chat Assistant

| ID | Story | Priority | Routes | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| CHAT-01 | As a user, I want to ask questions about my portfolio | P0 | `POST /chat/sessions/:id/messages` | AI responds with accurate portfolio data |
| CHAT-02 | As a user, I want AI responses to include sources | P0 | Response includes `citations[]` | Every claim has a citation with link |
| CHAT-03 | As a user, I want to research stocks via chat | P0 | `POST /chat/sessions/:id/messages` | AI fetches and analyzes stock data |
| CHAT-04 | As a user, I want to research crypto via chat | P0 | `POST /chat/sessions/:id/messages` | AI fetches and analyzes crypto data |
| CHAT-05 | As a user, I want to see my chat history | P1 | `GET /chat/sessions`<br>`GET /chat/sessions/:id/messages` | Previous sessions listed, messages loadable |
| CHAT-06 | As a user, I want AI to summarize SEC filings | P1 | `POST /chat/sessions/:id/messages` | Key points extracted with section citations |

**Supporting Routes:**
- `POST /chat/sessions` — Create new session
- `GET /chat/sessions/:id` — Get session details
- `PATCH /chat/sessions/:id` — Update session (title, archive, pin)
- `DELETE /chat/sessions/:id` — Delete session
- `POST /chat/sessions/:id/messages/stream` — Stream message (SSE)

---

#### Epic 6: Watchlists & Alerts

| ID | Story | Priority | Routes | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| WATCH-01 | As a user, I want to create custom watchlists | P1 | `POST /watchlists`<br>`POST /watchlists/:id/items` | Watchlist created with name, tickers added |
| WATCH-02 | As a user, I want to set price alerts | P1 | `POST /alerts` | Alert triggers when price crosses threshold |
| WATCH-03 | As a user, I want to receive notifications for alerts | P2 | Novu Integration (background) | Push/email notification sent within 1 minute |
| WATCH-04 | As a user, I want to see all my active alerts | P1 | `GET /alerts` | List of alerts with status and trigger conditions |

**Supporting Routes:**
- `GET /watchlists` — List all watchlists
- `GET /watchlists/:id` — Get watchlist with items
- `PATCH /watchlists/:id` — Update watchlist
- `DELETE /watchlists/:id` — Delete watchlist
- `DELETE /watchlists/:id/items/:itemId` — Remove item
- `GET /alerts/:id` — Get alert details
- `PATCH /alerts/:id` — Update alert
- `DELETE /alerts/:id` — Delete alert

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
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
         ▼                         ▼                         ▼
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│       NOVU          │  │      PORTKEY        │  │   DATA SCRAPING     │
│  (Notifications)    │  │  (AI Observability) │  │      LAYER          │
│                     │  │                     │  │                     │
│ • Email             │  │ • Request Logging   │  │ • Stock Scrapers    │
│ • Push              │  │ • Token Tracking    │  │ • Crypto Scrapers   │
│ • SMS               │  │ • Cost Analytics    │  │ • News Scrapers     │
│ • In-App            │  │ • Prompt Caching    │  │ • Filing Scrapers   │
│ • Digest            │  │ • Fallback/Retry    │  │ • On-Chain Scrapers │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EXTERNAL SERVICES                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  BROKERAGES        │  EXCHANGES         │  AI                       │   │
│  │  • Alpaca          │  • Coinbase        │  • Anthropic Claude       │   │
│  │  • Interactive     │  • Binance         │    (via Portkey)          │   │
│  │    Brokers         │  • Kraken          │                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  MARKET DATA       │  BLOCKCHAIN        │  NEWS/FILINGS             │   │
│  │  • Yahoo Finance   │  • Etherscan       │  • SEC EDGAR              │   │
│  │  • Finnhub         │  • Blockchain.com  │  • Finnhub News           │   │
│  │  • CoinGecko       │  • Solscan         │  • CryptoPanic            │   │
│  │  • CoinMarketCap   │  • Glassnode       │  • NewsAPI                │   │
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
| Blockchain | Etherscan, Blockchain.com, Solscan, Glassnode | Wallet balance & on-chain analytics |
| News | Finnhub, CryptoPanic, NewsAPI | Market news |
| Filings | SEC EDGAR | Company filings |
| AI | Anthropic Claude (via Portkey) | Chat assistant |
| Notifications | Novu | Multi-channel notifications |
| AI Observability | Portkey | LLM logging, analytics, caching |

### 4.3 Novu Integration (Notifications)

Novu handles all notification delivery for SOPHIA, providing:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           NOVU INTEGRATION                                  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      NOTIFICATION TRIGGERS                          │   │
│  │                                                                     │   │
│  │  • Alert Triggered (price threshold crossed)                       │   │
│  │  • Portfolio Sync Completed/Failed                                 │   │
│  │  • Daily Portfolio Summary                                         │   │
│  │  • News Mention for Holdings                                       │   │
│  │  • System Announcements                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       NOVU WORKFLOWS                                │   │
│  │                                                                     │   │
│  │  Workflow: alert-triggered                                         │   │
│  │  ├── Email (immediate)                                             │   │
│  │  ├── Push (immediate)                                              │   │
│  │  └── In-App (immediate)                                            │   │
│  │                                                                     │   │
│  │  Workflow: daily-summary                                           │   │
│  │  ├── Email (digest at 8am user timezone)                           │   │
│  │  └── In-App (immediate)                                            │   │
│  │                                                                     │   │
│  │  Workflow: sync-status                                             │   │
│  │  ├── In-App (immediate)                                            │   │
│  │  └── Email (only on failure)                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      DELIVERY CHANNELS                              │   │
│  │                                                                     │   │
│  │  📧 Email      → SendGrid / AWS SES                                │   │
│  │  📱 Push       → Firebase Cloud Messaging                          │   │
│  │  💬 In-App     → Novu Inbox Component                              │   │
│  │  📲 SMS        → Twilio (future)                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Novu Configuration:**
```typescript
// novu.service.ts
import { Novu } from '@novu/node';

const novu = new Novu(process.env.NOVU_API_KEY);

// Trigger alert notification
await novu.trigger('alert-triggered', {
  to: {
    subscriberId: userId,
    email: user.email,
  },
  payload: {
    alertType: 'price_above',
    symbol: 'BTC',
    threshold: 100000,
    currentPrice: 100500,
    changePercent: 5.2,
  },
});
```

**Subscriber Management:**
- Users are registered as Novu subscribers on account creation
- Preferences synced: `novu.subscribers.setCredentials()` for push tokens
- Preference center: Users can manage channels via Novu's preference API

### 4.4 Portkey Integration (AI Observability)

Portkey provides a unified gateway for AI/LLM operations:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PORTKEY INTEGRATION                                │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      AI REQUEST FLOW                                │   │
│  │                                                                     │   │
│  │   SOPHIA Backend                                                   │   │
│  │        │                                                           │   │
│  │        ▼                                                           │   │
│  │   ┌─────────────────────────────────────────────────────────────┐  │   │
│  │   │                    PORTKEY GATEWAY                          │  │   │
│  │   │                                                             │  │   │
│  │   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │  │   │
│  │   │  │   Logging   │  │   Caching   │  │  Fallbacks  │         │  │   │
│  │   │  │  & Tracing  │  │  (Prompts)  │  │  & Retries  │         │  │   │
│  │   │  └─────────────┘  └─────────────┘  └─────────────┘         │  │   │
│  │   │                                                             │  │   │
│  │   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │  │   │
│  │   │  │   Budget    │  │   Rate      │  │   Load      │         │  │   │
│  │   │  │   Limits    │  │   Limiting  │  │  Balancing  │         │  │   │
│  │   │  └─────────────┘  └─────────────┘  └─────────────┘         │  │   │
│  │   └─────────────────────────────────────────────────────────────┘  │   │
│  │        │                                                           │   │
│  │        ▼                                                           │   │
│  │   Anthropic Claude API                                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    PORTKEY DASHBOARD                                │   │
│  │                                                                     │   │
│  │  📊 Analytics                                                      │   │
│  │  ├── Requests per day/hour                                         │   │
│  │  ├── Token usage (input/output)                                    │   │
│  │  ├── Cost tracking ($)                                             │   │
│  │  ├── Latency percentiles (p50, p95, p99)                          │   │
│  │  └── Error rates                                                   │   │
│  │                                                                     │   │
│  │  🔍 Logs & Traces                                                  │   │
│  │  ├── Full request/response logs                                    │   │
│  │  ├── Tool call traces                                              │   │
│  │  ├── User session correlation                                      │   │
│  │  └── Searchable by user, session, metadata                        │   │
│  │                                                                     │   │
│  │  ⚙️ Configs                                                        │   │
│  │  ├── Virtual keys (per environment)                                │   │
│  │  ├── Fallback chains (Claude → GPT-4 backup)                      │   │
│  │  └── Rate limit policies                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Portkey Configuration:**
```typescript
// portkey.config.ts
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: process.env.PORTKEY_API_KEY,
  virtualKey: process.env.PORTKEY_VIRTUAL_KEY_ANTHROPIC,
});

// Chat completion with automatic logging
const response = await portkey.chat.completions.create({
  model: 'claude-3-5-sonnet-20241022',
  messages: [...],
  metadata: {
    userId: user.id,
    sessionId: session.id,
    feature: 'portfolio_analysis',
  },
});
```

**Key Features Used:**
- **Request Logging**: All AI requests automatically logged with metadata
- **Token Tracking**: Input/output tokens tracked per request
- **Cost Analytics**: Real-time cost monitoring per user/feature
- **Prompt Caching**: Cache identical prompts to reduce costs
- **Fallback Config**: Automatic retry with backup models if primary fails
- **Rate Limiting**: Per-user rate limits enforced at gateway level

### 4.5 Module Structure

```
/backend/src/
├── main.ts
├── app.module.ts
├── config/
│   ├── database.config.ts
│   ├── redis.config.ts
│   ├── novu.config.ts              # Novu configuration
│   └── portkey.config.ts           # Portkey configuration
│
├── common/
│   ├── decorators/
│   ├── filters/
│   ├── guards/
│   ├── interceptors/
│   └── pipes/
│
├── modules/
│   ├── auth/
│   │   ├── auth.module.ts
│   │   ├── auth.controller.ts
│   │   ├── auth.service.ts
│   │   ├── two-factor/             # 2FA submodule
│   │   │   ├── two-factor.service.ts
│   │   │   └── two-factor.controller.ts
│   │   ├── strategies/
│   │   │   ├── jwt.strategy.ts
│   │   │   └── local.strategy.ts
│   │   ├── guards/
│   │   │   └── jwt-auth.guard.ts
│   │   └── dto/
│   │
│   ├── users/
│   │   ├── users.module.ts
│   │   ├── users.service.ts
│   │   ├── entities/
│   │   │   └── user.entity.ts
│   │   └── dto/
│   │
│   ├── connections/
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
│   ├── portfolio/
│   │   ├── portfolio.module.ts
│   │   ├── portfolio.controller.ts
│   │   ├── portfolio.service.ts
│   │   ├── holdings.service.ts
│   │   ├── snapshots.service.ts
│   │   ├── entities/
│   │   │   ├── holding.entity.ts
│   │   │   └── portfolio-snapshot.entity.ts
│   │   └── dto/
│   │
│   ├── market-data/
│   │   ├── market-data.module.ts
│   │   ├── stocks.controller.ts
│   │   ├── crypto.controller.ts
│   │   ├── news.controller.ts
│   │   ├── filings.controller.ts
│   │   ├── services/
│   │   │   ├── stock-quote.service.ts
│   │   │   ├── crypto-quote.service.ts
│   │   │   ├── onchain.service.ts      # On-chain metrics
│   │   │   ├── news.service.ts
│   │   │   └── filings.service.ts
│   │   ├── entities/
│   │   │   ├── stock-quote-cache.entity.ts
│   │   │   ├── crypto-quote-cache.entity.ts
│   │   │   ├── crypto-onchain-cache.entity.ts  # On-chain cache
│   │   │   ├── company-profile.entity.ts
│   │   │   ├── news-article.entity.ts
│   │   │   └── sec-filing.entity.ts
│   │   └── dto/
│   │
│   ├── chat/
│   │   ├── chat.module.ts
│   │   ├── chat.controller.ts
│   │   ├── chat.service.ts
│   │   ├── ai/
│   │   │   ├── claude.service.ts       # Uses Portkey
│   │   │   ├── rag.service.ts
│   │   │   └── tools/
│   │   │       ├── portfolio.tool.ts
│   │   │       ├── stock-quote.tool.ts
│   │   │       ├── crypto-quote.tool.ts
│   │   │       ├── onchain.tool.ts     # On-chain tool
│   │   │       ├── news.tool.ts
│   │   │       └── filing.tool.ts
│   │   ├── entities/
│   │   │   ├── chat-session.entity.ts
│   │   │   └── chat-message.entity.ts
│   │   └── dto/
│   │
│   ├── watchlists/
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
│   ├── notifications/
│   │   ├── notifications.module.ts
│   │   ├── novu.service.ts             # Novu integration
│   │   └── templates/                  # Notification templates
│   │       ├── alert-triggered.ts
│   │       ├── daily-summary.ts
│   │       └── sync-status.ts
│   │
│   └── analytics/
│       ├── analytics.module.ts
│       ├── analytics.service.ts
│       └── entities/
│           └── audit-log.entity.ts
│
├── jobs/
│   ├── jobs.module.ts
│   ├── processors/
│   │   ├── sync.processor.ts
│   │   ├── scraper.processor.ts
│   │   ├── alert.processor.ts          # Triggers Novu
│   │   └── onchain.processor.ts        # On-chain scraper
│   └── schedulers/
│       ├── portfolio-sync.scheduler.ts
│       ├── market-data.scheduler.ts
│       └── onchain-data.scheduler.ts
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
│  │  • onchain-metrics (priority: medium, concurrency: 3)              │   │
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
│  │  Glassnode         │ 10 requests        │ per minute               │   │
│  │  Anthropic         │ via Portkey        │ managed                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Scraper Workers

#### On-Chain Metrics Scraper (New)

```
┌───────────────────────────────────────────────────────────────────┐
│                    ON-CHAIN METRICS SCRAPER                       │
│                                                                   │
│  Input: List of crypto symbols from holdings + watchlists        │
│                                                                   │
│  Flow:                                                           │
│  1. Collect unique crypto symbols                                │
│  2. Map symbols to chain (BTC→bitcoin, ETH→ethereum, etc.)      │
│  3. Fetch from primary provider based on chain:                  │
│     • Ethereum/ERC-20: Etherscan + Glassnode                    │
│     • Bitcoin: Blockchain.com + Glassnode                        │
│     • Solana: Solscan                                            │
│  4. Parse response → OnChainMetrics entity                       │
│  5. Upsert to crypto_onchain_cache table                         │
│  6. Publish to Redis channel: crypto:onchain:{symbol}            │
│                                                                   │
│  Output: OnChainMetrics {                                        │
│    symbol, chain,                                                │
│    activeAddresses24h, transactionCount24h, transactionVolume,   │
│    avgTransactionFee, totalHolders, top10HoldersPercent,        │
│    exchangeInflow24h, exchangeOutflow24h, exchangeNetflow24h,   │
│    whaleTransactions24h, tvl, dataSource, timestamp              │
│  }                                                               │
└───────────────────────────────────────────────────────────────────┘
```

### 5.3 Provider Configuration

```typescript
scraperConfig = {
  stocks: {
    providers: ['yahoo_finance', 'finnhub', 'polygon'];
    schedule: {
      marketHours: '*/1 * * * *';    // Every minute
      afterHours: '*/15 * * * *';    // Every 15 minutes
    };
    batchSize: 10;
    cacheTtl: 60;
  };
  
  crypto: {
    providers: ['coingecko', 'binance', 'coinmarketcap'];
    schedule: '*/1 * * * *';         // Every minute (24/7)
    batchSize: 100;
    cacheTtl: 60;
  };
  
  onchain: {
    providers: {
      ethereum: ['etherscan', 'glassnode'];
      bitcoin: ['blockchain.com', 'glassnode'];
      solana: ['solscan'];
    };
    schedule: '*/5 * * * *';         // Every 5 minutes
    cacheTtl: 300;
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
}
```

---

## 6. Database Schema

### 6.1 Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ENTITY RELATIONSHIP DIAGRAM                           │
│                                                                             │
│  ┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐ │
│  │      users       │       │   connections    │       │    holdings      │ │
│  ├──────────────────┤       ├──────────────────┤       ├──────────────────┤ │
│  │ id (PK)          │──┐    │ id (PK)          │──┐    │ id (PK)          │ │
│  │ email            │  │    │ user_id (FK)     │  │    │ user_id (FK)     │ │
│  │ password_hash    │  └───▶│ provider_type    │  │    │ connection_id(FK)│ │
│  │ first_name       │       │ provider_id      │  └───▶│ asset_type       │ │
│  │ two_factor_*     │       │ access_token_enc │       │ symbol           │ │
│  │ ...              │       │ ...              │       │ quantity         │ │
│  └──────────────────┘       └──────────────────┘       │ ...              │ │
│         │                                              └──────────────────┘ │
│         │                                                                   │
│         │  ┌──────────────────┐                                             │
│         │  │ two_factor_      │                                             │
│         │  │ backup_codes     │                                             │
│         │  ├──────────────────┤                                             │
│         └─▶│ id (PK)          │                                             │
│            │ user_id (FK)     │                                             │
│            │ code_hash        │                                             │
│            │ is_used          │                                             │
│            │ ...              │                                             │
│            └──────────────────┘                                             │
│                                                                             │
│         │               ┌──────────────────┐       ┌──────────────────┐    │
│         │               │  chat_sessions   │       │  chat_messages   │    │
│         │               ├──────────────────┤       ├──────────────────┤    │
│         │               │ id (PK)          │──┐    │ id (PK)          │    │
│         └──────────────▶│ user_id (FK)     │  │    │ session_id (FK)  │    │
│                         │ title            │  └───▶│ role             │    │
│                         │ ...              │       │ content          │    │
│                         └──────────────────┘       │ citations (JSON) │    │
│                                                    │ ...              │    │
│         │               ┌──────────────────┐       └──────────────────┘    │
│         │               │   watchlists     │                               │
│         │               ├──────────────────┤       ┌──────────────────┐    │
│         │               │ id (PK)          │──┐    │ watchlist_items  │    │
│         └──────────────▶│ user_id (FK)     │  │    ├──────────────────┤    │
│                         │ name             │  │    │ id (PK)          │    │
│                         │ ...              │  └───▶│ watchlist_id(FK) │    │
│                         └──────────────────┘       │ symbol           │    │
│                                                    │ ...              │    │
│         │               ┌──────────────────┐       └──────────────────┘    │
│         │               │     alerts       │                               │
│         │               ├──────────────────┤                               │
│         └──────────────▶│ id (PK)          │                               │
│                         │ user_id (FK)     │                               │
│                         │ symbol           │                               │
│                         │ alert_type       │                               │
│                         │ ...              │                               │
│                         └──────────────────┘                               │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                         CACHE TABLES                                 │  │
│  │                                                                      │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │  │
│  │  │ stock_quotes_   │  │ crypto_quotes_  │  │ crypto_onchain_ │      │  │
│  │  │ cache           │  │ cache           │  │ cache           │      │  │
│  │  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤      │  │
│  │  │ symbol (PK)     │  │ symbol (PK)     │  │ symbol (PK)     │      │  │
│  │  │ price           │  │ price           │  │ active_addr_24h │      │  │
│  │  │ change          │  │ change_24h      │  │ tx_count_24h    │      │  │
│  │  │ volume          │  │ market_cap      │  │ exchange_flow   │      │  │
│  │  │ ...             │  │ ...             │  │ whale_activity  │      │  │
│  │  │ fetched_at      │  │ fetched_at      │  │ fetched_at      │      │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘      │  │
│  │                                                                      │  │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │  │
│  │  │ company_        │  │ news_articles   │  │ sec_filings     │      │  │
│  │  │ profiles_cache  │  ├─────────────────┤  ├─────────────────┤      │  │
│  │  ├─────────────────┤  │ id (PK)         │  │ id (PK)         │      │  │
│  │  │ symbol (PK)     │  │ title           │  │ cik             │      │  │
│  │  │ name            │  │ url (UNIQUE)    │  │ symbol          │      │  │
│  │  │ sector          │  │ sentiment       │  │ form_type       │      │  │
│  │  │ ...             │  │ published_at    │  │ filing_date     │      │  │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                         AUDIT TABLE                                  │  │
│  │                                                                      │  │
│  │  ┌─────────────────┐                                                │  │
│  │  │ audit_logs      │   Note: AI API logs handled by Portkey        │  │
│  │  ├─────────────────┤         Notifications handled by Novu         │  │
│  │  │ id (PK)         │                                                │  │
│  │  │ user_id (FK)    │                                                │  │
│  │  │ event_type      │                                                │  │
│  │  │ event_category  │                                                │  │
│  │  │ metadata        │                                                │  │
│  │  │ created_at      │                                                │  │
│  │  └─────────────────┘                                                │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Detailed Table Schemas

#### 6.2.1 Users Table

```sql
CREATE TABLE users (
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
    preferred_currency  VARCHAR(3) DEFAULT 'USD',
    timezone            VARCHAR(50) DEFAULT 'UTC',
    locale              VARCHAR(10) DEFAULT 'en-US',
    
    -- Two-Factor Authentication
    two_factor_enabled  BOOLEAN DEFAULT FALSE,
    two_factor_secret   VARCHAR(255),              -- Encrypted TOTP secret
    
    -- Security
    failed_login_count  INTEGER DEFAULT 0,
    locked_until        TIMESTAMP WITH TIME ZONE,
    last_login_at       TIMESTAMP WITH TIME ZONE,
    last_login_ip       INET,
    
    -- Novu Integration
    novu_subscriber_id  VARCHAR(255),              -- Novu subscriber ID
    
    -- Status
    is_active           BOOLEAN DEFAULT TRUE,
    deleted_at          TIMESTAMP WITH TIME ZONE,
    
    -- Timestamps
    created_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_novu_subscriber ON users(novu_subscriber_id);
```

---

#### 6.2.2 Two-Factor Backup Codes Table (New)

```sql
CREATE TABLE two_factor_backup_codes (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Foreign Key
    user_id             UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Backup Code (hashed)
    code_hash           VARCHAR(255) NOT NULL,     -- bcrypt hash of code
    
    -- Status
    is_used             BOOLEAN DEFAULT FALSE,
    used_at             TIMESTAMP WITH TIME ZONE,
    used_ip             INET,
    
    -- Timestamps
    created_at          TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at          TIMESTAMP WITH TIME ZONE,
    
    CONSTRAINT unique_user_code UNIQUE (user_id, code_hash)
);

CREATE INDEX idx_backup_codes_user ON two_factor_backup_codes(user_id);
CREATE INDEX idx_backup_codes_unused ON two_factor_backup_codes(user_id, is_used) 
    WHERE is_used = FALSE;
```

---

#### 6.2.3 Connections Table

```sql
CREATE TABLE connections (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Provider Identification
    provider_type           VARCHAR(20) NOT NULL,
    provider_id             VARCHAR(50) NOT NULL,
    
    -- Account Info
    external_account_id     VARCHAR(255),
    account_name            VARCHAR(255),
    
    -- OAuth Tokens (encrypted)
    access_token_encrypted  TEXT,
    refresh_token_encrypted TEXT,
    token_expires_at        TIMESTAMP WITH TIME ZONE,
    token_scope             VARCHAR(500),
    
    -- Wallet-specific
    wallet_address          VARCHAR(255),
    chain                   VARCHAR(20),
    
    -- Sync Status
    is_active               BOOLEAN DEFAULT TRUE,
    sync_status             VARCHAR(20) DEFAULT 'pending',
    sync_error_message      TEXT,
    last_sync_at            TIMESTAMP WITH TIME ZONE,
    last_successful_sync_at TIMESTAMP WITH TIME ZONE,
    sync_frequency_minutes  INTEGER DEFAULT 5,
    
    -- Metadata
    metadata                JSONB DEFAULT '{}',
    
    -- Timestamps
    connected_at            TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    disconnected_at         TIMESTAMP WITH TIME ZONE,
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT unique_user_provider UNIQUE (user_id, provider_type, provider_id),
    CONSTRAINT valid_provider_type CHECK (provider_type IN ('brokerage', 'exchange', 'wallet')),
    CONSTRAINT valid_sync_status CHECK (sync_status IN ('pending', 'syncing', 'success', 'error'))
);

CREATE INDEX idx_connections_user_id ON connections(user_id);
CREATE INDEX idx_connections_provider ON connections(provider_type, provider_id);
CREATE INDEX idx_connections_sync_status ON connections(sync_status);
```

---

#### 6.2.4 Holdings Table

```sql
CREATE TABLE holdings (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    connection_id           UUID NOT NULL REFERENCES connections(id) ON DELETE CASCADE,
    
    -- Asset Identification
    asset_type              VARCHAR(20) NOT NULL,
    symbol                  VARCHAR(20) NOT NULL,
    name                    VARCHAR(255),
    
    -- Crypto-specific
    contract_address        VARCHAR(255),
    chain                   VARCHAR(20),
    decimals                INTEGER,
    
    -- Position Details
    quantity                DECIMAL(30, 18) NOT NULL,
    avg_cost_basis          DECIMAL(20, 8),
    
    -- Current Valuation
    current_price           DECIMAL(20, 8),
    market_value            DECIMAL(20, 4),
    cost_basis_total        DECIMAL(20, 4),
    
    -- P&L
    unrealized_pl           DECIMAL(20, 4),
    unrealized_pl_percent   DECIMAL(10, 4),
    day_pl                  DECIMAL(20, 4),
    day_pl_percent          DECIMAL(10, 4),
    
    -- Source
    source_position_id      VARCHAR(255),
    last_synced_at          TIMESTAMP WITH TIME ZONE,
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT valid_asset_type CHECK (asset_type IN ('stock', 'etf', 'crypto', 'token')),
    CONSTRAINT positive_quantity CHECK (quantity >= 0)
);

CREATE INDEX idx_holdings_user_id ON holdings(user_id);
CREATE INDEX idx_holdings_connection_id ON holdings(connection_id);
CREATE INDEX idx_holdings_symbol ON holdings(symbol);
CREATE INDEX idx_holdings_user_symbol ON holdings(user_id, symbol);
```

---

#### 6.2.5 Portfolio Snapshots Table

```sql
CREATE TABLE portfolio_snapshots (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Snapshot Date
    snapshot_date           DATE NOT NULL,
    snapshot_time           TIMESTAMP WITH TIME ZONE NOT NULL,
    
    -- Portfolio Values
    total_value             DECIMAL(20, 4) NOT NULL,
    cash_balance            DECIMAL(20, 4) DEFAULT 0,
    invested_value          DECIMAL(20, 4),
    
    -- P&L
    total_cost_basis        DECIMAL(20, 4),
    total_unrealized_pl     DECIMAL(20, 4),
    day_pl                  DECIMAL(20, 4),
    day_pl_percent          DECIMAL(10, 4),
    
    -- Breakdown
    stocks_value            DECIMAL(20, 4) DEFAULT 0,
    crypto_value            DECIMAL(20, 4) DEFAULT 0,
    holdings_count          INTEGER DEFAULT 0,
    holdings_snapshot       JSONB,
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT unique_user_date UNIQUE (user_id, snapshot_date)
);

CREATE INDEX idx_snapshots_user_date ON portfolio_snapshots(user_id, snapshot_date DESC);
```

---

#### 6.2.6 Chat Tables

```sql
CREATE TABLE chat_sessions (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    title                   VARCHAR(255),
    is_archived             BOOLEAN DEFAULT FALSE,
    is_pinned               BOOLEAN DEFAULT FALSE,
    message_count           INTEGER DEFAULT 0,
    total_tokens_used       INTEGER DEFAULT 0,
    
    last_message_at         TIMESTAMP WITH TIME ZONE,
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_chat_sessions_user_id ON chat_sessions(user_id);
CREATE INDEX idx_chat_sessions_updated ON chat_sessions(user_id, updated_at DESC);


CREATE TABLE chat_messages (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id              UUID NOT NULL REFERENCES chat_sessions(id) ON DELETE CASCADE,
    
    -- Message Content
    role                    VARCHAR(20) NOT NULL,
    content                 TEXT NOT NULL,
    
    -- AI Metadata
    citations               JSONB,
    tool_calls              JSONB,
    
    -- Usage (logged to Portkey, summary stored here)
    model_used              VARCHAR(100),
    input_tokens            INTEGER,
    output_tokens           INTEGER,
    processing_time_ms      INTEGER,
    portkey_trace_id        VARCHAR(100),          -- Link to Portkey trace
    
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT valid_role CHECK (role IN ('user', 'assistant', 'system'))
);

CREATE INDEX idx_chat_messages_session ON chat_messages(session_id, created_at);
```

---

#### 6.2.7 Watchlists & Alerts Tables

```sql
CREATE TABLE watchlists (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    name                    VARCHAR(100) NOT NULL,
    description             TEXT,
    color                   VARCHAR(7),
    icon                    VARCHAR(50),
    sort_order              INTEGER DEFAULT 0,
    
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_watchlists_user_id ON watchlists(user_id);


CREATE TABLE watchlist_items (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    watchlist_id            UUID NOT NULL REFERENCES watchlists(id) ON DELETE CASCADE,
    
    asset_type              VARCHAR(20) NOT NULL,
    symbol                  VARCHAR(20) NOT NULL,
    name                    VARCHAR(255),
    notes                   TEXT,
    target_price            DECIMAL(20, 8),
    sort_order              INTEGER DEFAULT 0,
    added_at                TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT unique_watchlist_symbol UNIQUE (watchlist_id, asset_type, symbol)
);

CREATE INDEX idx_watchlist_items_watchlist ON watchlist_items(watchlist_id);
CREATE INDEX idx_watchlist_items_symbol ON watchlist_items(symbol);


CREATE TABLE alerts (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Asset
    asset_type              VARCHAR(20) NOT NULL,
    symbol                  VARCHAR(20) NOT NULL,
    
    -- Configuration
    alert_type              VARCHAR(30) NOT NULL,
    condition               VARCHAR(20) NOT NULL,
    threshold_value         DECIMAL(20, 8) NOT NULL,
    threshold_unit          VARCHAR(10) DEFAULT 'value',
    
    -- Notification (via Novu)
    notify_email            BOOLEAN DEFAULT TRUE,
    notify_push             BOOLEAN DEFAULT FALSE,
    notify_sms              BOOLEAN DEFAULT FALSE,
    
    -- Status
    is_active               BOOLEAN DEFAULT TRUE,
    is_repeating            BOOLEAN DEFAULT FALSE,
    cooldown_minutes        INTEGER DEFAULT 60,
    
    -- Trigger History
    last_triggered_at       TIMESTAMP WITH TIME ZONE,
    trigger_count           INTEGER DEFAULT 0,
    last_checked_price      DECIMAL(20, 8),
    
    -- Timestamps
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at              TIMESTAMP WITH TIME ZONE,
    
    CONSTRAINT valid_alert_type CHECK (alert_type IN (
        'price_above', 'price_below', 
        'percent_change_up', 'percent_change_down', 
        'volume_spike'
    )),
    CONSTRAINT valid_condition CHECK (condition IN ('gt', 'lt', 'gte', 'lte', 'eq'))
);

CREATE INDEX idx_alerts_user_id ON alerts(user_id);
CREATE INDEX idx_alerts_active ON alerts(is_active, symbol);
```

---

#### 6.2.8 Market Data Cache Tables

```sql
-- Stock Quotes Cache
CREATE TABLE stock_quotes_cache (
    symbol                  VARCHAR(20) PRIMARY KEY,
    name                    VARCHAR(255),
    exchange                VARCHAR(50),
    
    price                   DECIMAL(20, 4) NOT NULL,
    open                    DECIMAL(20, 4),
    previous_close          DECIMAL(20, 4),
    change                  DECIMAL(20, 4),
    change_percent          DECIMAL(10, 4),
    
    day_high                DECIMAL(20, 4),
    day_low                 DECIMAL(20, 4),
    year_high               DECIMAL(20, 4),
    year_low                DECIMAL(20, 4),
    
    volume                  BIGINT,
    avg_volume              BIGINT,
    market_cap              BIGINT,
    
    pe_ratio                DECIMAL(10, 4),
    eps                     DECIMAL(10, 4),
    dividend_yield          DECIMAL(10, 4),
    beta                    DECIMAL(10, 4),
    
    data_source             VARCHAR(50) NOT NULL,
    quote_time              TIMESTAMP WITH TIME ZONE,
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    market_state            VARCHAR(20)
);

CREATE INDEX idx_stock_quotes_fetched ON stock_quotes_cache(fetched_at);


-- Crypto Quotes Cache
CREATE TABLE crypto_quotes_cache (
    symbol                  VARCHAR(20) PRIMARY KEY,
    coingecko_id            VARCHAR(100),
    coinmarketcap_id        INTEGER,
    name                    VARCHAR(255),
    
    price                   DECIMAL(30, 18) NOT NULL,
    price_btc               DECIMAL(30, 18),
    price_eth               DECIMAL(30, 18),
    
    change_1h               DECIMAL(10, 4),
    change_24h              DECIMAL(10, 4),
    change_7d               DECIMAL(10, 4),
    change_30d              DECIMAL(10, 4),
    
    market_cap              BIGINT,
    market_cap_rank         INTEGER,
    fully_diluted_valuation BIGINT,
    
    volume_24h              BIGINT,
    volume_change_24h       DECIMAL(10, 4),
    
    circulating_supply      DECIMAL(30, 8),
    total_supply            DECIMAL(30, 8),
    max_supply              DECIMAL(30, 8),
    
    ath                     DECIMAL(30, 18),
    ath_date                TIMESTAMP WITH TIME ZONE,
    ath_change_percent      DECIMAL(10, 4),
    atl                     DECIMAL(30, 18),
    atl_date                TIMESTAMP WITH TIME ZONE,
    atl_change_percent      DECIMAL(10, 4),
    
    data_source             VARCHAR(50) NOT NULL,
    last_updated            TIMESTAMP WITH TIME ZONE,
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_crypto_quotes_fetched ON crypto_quotes_cache(fetched_at);
CREATE INDEX idx_crypto_quotes_rank ON crypto_quotes_cache(market_cap_rank);
```

---

#### 6.2.9 On-Chain Metrics Cache Table (New)

```sql
CREATE TABLE crypto_onchain_cache (
    symbol                      VARCHAR(20) PRIMARY KEY,
    chain                       VARCHAR(20) NOT NULL,
    contract_address            VARCHAR(255),
    
    -- Activity Metrics
    active_addresses_24h        BIGINT,
    active_addresses_7d         BIGINT,
    transaction_count_24h       BIGINT,
    transaction_volume_24h      DECIMAL(30, 8),
    transaction_volume_usd_24h  DECIMAL(20, 4),
    
    -- Network Metrics
    avg_transaction_fee         DECIMAL(20, 8),
    avg_transaction_fee_usd     DECIMAL(10, 4),
    avg_block_time              DECIMAL(10, 2),
    hashrate                    DECIMAL(30, 4),
    
    -- Holder Distribution
    total_holders               BIGINT,
    top_10_holders_percent      DECIMAL(6, 2),
    top_100_holders_percent     DECIMAL(6, 2),
    
    -- Exchange Flows
    exchange_inflow_24h         DECIMAL(30, 8),
    exchange_outflow_24h        DECIMAL(30, 8),
    exchange_netflow_24h        DECIMAL(30, 8),
    exchange_reserve            DECIMAL(30, 8),
    
    -- Whale Activity
    whale_transactions_24h      INTEGER,
    whale_volume_24h            DECIMAL(30, 8),
    
    -- DeFi Metrics
    tvl                         DECIMAL(20, 4),
    tvl_change_24h              DECIMAL(10, 4),
    
    -- Data Source
    data_source                 VARCHAR(50) NOT NULL,
    last_updated                TIMESTAMP WITH TIME ZONE,
    fetched_at                  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_onchain_chain ON crypto_onchain_cache(chain);
CREATE INDEX idx_onchain_fetched ON crypto_onchain_cache(fetched_at);
```

---

#### 6.2.10 Company Profiles & News Tables

```sql
CREATE TABLE company_profiles_cache (
    symbol                  VARCHAR(20) PRIMARY KEY,
    name                    VARCHAR(255),
    asset_type              VARCHAR(20) NOT NULL,
    exchange                VARCHAR(50),
    sector                  VARCHAR(100),
    industry                VARCHAR(100),
    description             TEXT,
    ceo                     VARCHAR(255),
    employees               INTEGER,
    headquarters            VARCHAR(255),
    founded                 INTEGER,
    categories              TEXT[],
    platforms               JSONB,
    website                 VARCHAR(500),
    logo_url                VARCHAR(500),
    data_source             VARCHAR(50) NOT NULL,
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_company_profiles_type ON company_profiles_cache(asset_type);


CREATE TABLE news_articles (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title                   VARCHAR(500) NOT NULL,
    summary                 TEXT,
    content                 TEXT,
    source_name             VARCHAR(100) NOT NULL,
    source_url              VARCHAR(1000) NOT NULL,
    url                     VARCHAR(1000) NOT NULL UNIQUE,
    image_url               VARCHAR(1000),
    category                VARCHAR(50),
    sentiment               VARCHAR(20),
    sentiment_score         DECIMAL(5, 4),
    published_at            TIMESTAMP WITH TIME ZONE NOT NULL,
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_news_articles_published ON news_articles(published_at DESC);


CREATE TABLE news_article_symbols (
    article_id              UUID REFERENCES news_articles(id) ON DELETE CASCADE,
    asset_type              VARCHAR(20) NOT NULL,
    symbol                  VARCHAR(20) NOT NULL,
    is_primary              BOOLEAN DEFAULT FALSE,
    relevance_score         DECIMAL(5, 4),
    PRIMARY KEY (article_id, asset_type, symbol)
);

CREATE INDEX idx_news_symbols_symbol ON news_article_symbols(symbol, asset_type);


CREATE TABLE sec_filings (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cik                     VARCHAR(20) NOT NULL,
    symbol                  VARCHAR(20),
    company_name            VARCHAR(255),
    form_type               VARCHAR(20) NOT NULL,
    filing_date             DATE NOT NULL,
    accepted_date           TIMESTAMP WITH TIME ZONE,
    report_date             DATE,
    accession_number        VARCHAR(30) NOT NULL UNIQUE,
    file_number             VARCHAR(30),
    filing_url              VARCHAR(500) NOT NULL,
    primary_document_url    VARCHAR(500),
    primary_document_name   VARCHAR(255),
    extracted_sections      JSONB,
    fetched_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_sec_filings_symbol ON sec_filings(symbol);
CREATE INDEX idx_sec_filings_form ON sec_filings(form_type);
CREATE INDEX idx_sec_filings_date ON sec_filings(filing_date DESC);
```

---

#### 6.2.11 Audit Log Table

```sql
-- Note: AI API logs are handled by Portkey
-- Note: Notification logs are handled by Novu

CREATE TABLE audit_logs (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id                 UUID REFERENCES users(id) ON DELETE SET NULL,
    
    event_type              VARCHAR(50) NOT NULL,
    event_category          VARCHAR(30) NOT NULL,
    description             TEXT,
    metadata                JSONB DEFAULT '{}',
    
    ip_address              INET,
    user_agent              VARCHAR(500),
    request_id              VARCHAR(100),
    
    status                  VARCHAR(20) NOT NULL,
    error_message           TEXT,
    
    created_at              TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_type ON audit_logs(event_type);
CREATE INDEX idx_audit_logs_created ON audit_logs(created_at DESC);
```

---

### 6.3 Database Summary

| Table | Purpose |
|-------|---------|
| users | User accounts with 2FA and Novu subscriber |
| two_factor_backup_codes | 2FA recovery codes |
| connections | Brokerage/exchange/wallet connections |
| holdings | Portfolio positions | 
| portfolio_snapshots | Daily portfolio snapshots | 
| chat_sessions | AI chat sessions | 
| chat_messages | Chat messages with Portkey trace ID | 
| watchlists | User watchlists | 
| watchlist_items | Watchlist items | 
| alerts | Price/volume alerts | 
| stock_quotes_cache | Stock quote cache |
| crypto_quotes_cache | Crypto quote cache | 
| crypto_onchain_cache | On-chain metrics cache | 
| company_profiles_cache | Company/token profiles |
| news_articles | News article cache | 
| news_article_symbols | News-symbol junction | 
| sec_filings | SEC filing cache | 
| audit_logs | Security audit logs | 

**Total Tables: 18**

**Removed Tables:**
- `api_usage_logs` — Replaced by Portkey dashboard
- `notifications` — Replaced by Novu
- `notification_settings` — Replaced by Novu preference center

---

## 7. Data Transfer Objects (DTOs)

### 7.1 Authentication DTOs

#### Register

```typescript
// POST /auth/register

interface RegisterRequestDto {
  email: string;                    // Required, valid email
  password: string;                 // Required, min 8 chars
  firstName?: string;
  lastName?: string;
}

interface RegisterResponseDto {
  success: boolean;
  data: {
    user: UserDto;
    tokens: TokensDto;
  };
}
```

#### Login

```typescript
// POST /auth/login

interface LoginRequestDto {
  email: string;
  password: string;
  totpCode?: string;                // Required if 2FA enabled
  rememberMe?: boolean;
}

interface LoginResponseDto {
  success: boolean;
  data: {
    user: UserDto;
    tokens: TokensDto;
    requiresTwoFactor?: boolean;    // If 2FA enabled but no code provided
  };
}
```

#### Two-Factor Authentication (New)

```typescript
// POST /auth/2fa/setup
interface Setup2FAResponseDto {
  success: boolean;
  data: {
    secret: string;                 // Base32 encoded
    qrCodeDataUrl: string;          // Data URL for QR code
    manualEntryKey: string;         // For manual entry
  };
}

// POST /auth/2fa/verify
interface Verify2FARequestDto {
  code: string;                     // 6-digit TOTP code
}

interface Verify2FAResponseDto {
  success: boolean;
  data: {
    enabled: boolean;
    backupCodes: string[];          // Show once, 10 codes
  };
}

// POST /auth/2fa/disable
interface Disable2FARequestDto {
  password: string;
  code: string;                     // Current TOTP code
}

// GET /auth/2fa/backup-codes
interface GetBackupCodesResponseDto {
  success: boolean;
  data: {
    codes: {
      code: string;                 // Masked: "XXXX-1234"
      isUsed: boolean;
      usedAt: string | null;
    }[];
    remainingCount: number;
  };
}

// POST /auth/2fa/backup-codes/regenerate
interface RegenerateBackupCodesRequestDto {
  password: string;
  code: string;                     // Current TOTP code
}

interface RegenerateBackupCodesResponseDto {
  success: boolean;
  data: {
    backupCodes: string[];          // New codes, show once
  };
}
```

---

### 7.2 Connection DTOs

```typescript
// POST /connections/oauth/initiate
interface InitiateOAuthRequestDto {
  providerId: 'alpaca' | 'coinbase' | 'binance' | 'kraken' | 'ibkr';
}

interface InitiateOAuthResponseDto {
  success: boolean;
  data: {
    authorizationUrl: string;
    state: string;
    expiresAt: string;
  };
}

// POST /connections/oauth/callback
interface OAuthCallbackRequestDto {
  providerId: string;
  code: string;
  state: string;
}

// POST /connections/wallet
interface AddWalletRequestDto {
  chain: 'ethereum' | 'bitcoin' | 'solana';
  address: string;
  label?: string;
}

// DELETE /connections/:id
interface DisconnectResponseDto {
  success: boolean;
  data: {
    message: string;
    holdingsRemoved: number;
  };
}

// POST /connections/:id/sync
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

```typescript
// GET /portfolio/summary
interface PortfolioSummaryResponseDto {
  success: boolean;
  data: {
    summary: {
      totalValue: number;
      cashBalance: number;
      investedValue: number;
      totalCostBasis: number;
      totalUnrealizedPl: number;
      totalUnrealizedPlPercent: number;
      dayPl: number;
      dayPlPercent: number;
      stocksValue: number;
      stocksPercent: number;
      cryptoValue: number;
      cryptoPercent: number;
      totalHoldings: number;
      totalConnections: number;
      lastSyncAt: string;
    };
  };
}

// GET /portfolio/holdings
interface GetHoldingsQueryDto {
  assetType?: 'stock' | 'crypto' | 'all';
  connectionId?: string;
  sortBy?: 'value' | 'pl' | 'plPercent' | 'symbol' | 'quantity';
  order?: 'asc' | 'desc';
  page?: number;
  limit?: number;
}

interface GetHoldingsResponseDto {
  success: boolean;
  data: {
    holdings: HoldingDto[];
    pagination: PaginationDto;
    summary: {
      totalValue: number;
      totalPl: number;
      totalPlPercent: number;
    };
  };
}

// GET /portfolio/performance
interface GetPerformanceQueryDto {
  period: '1D' | '1W' | '1M' | '3M' | '6M' | '1Y' | 'YTD' | 'ALL';
  interval?: 'hour' | 'day' | 'week';
}

// GET /portfolio/allocation
interface GetAllocationResponseDto {
  success: boolean;
  data: {
    byAssetType: AllocationItemDto[];
    bySector: AllocationItemDto[];
    byCategory: AllocationItemDto[];
    byConnection: AllocationItemDto[];
    topHoldings: TopHoldingDto[];
  };
}
```

---

### 7.4 Market Data DTOs

```typescript
// GET /market/stocks/:symbol/quote
interface StockQuoteResponseDto {
  success: boolean;
  data: {
    quote: {
      symbol: string;
      name: string;
      exchange: string;
      price: number;
      open: number;
      previousClose: number;
      change: number;
      changePercent: number;
      dayHigh: number;
      dayLow: number;
      yearHigh: number;
      yearLow: number;
      volume: number;
      avgVolume: number;
      marketCap: number;
      peRatio: number | null;
      eps: number | null;
      dividendYield: number | null;
      beta: number | null;
      marketState: 'pre' | 'regular' | 'post' | 'closed';
      quoteTime: string;
      dataSource: string;
    };
  };
}

// GET /market/crypto/:symbol/quote
interface CryptoQuoteResponseDto {
  success: boolean;
  data: {
    quote: {
      symbol: string;
      name: string;
      price: number;
      priceBtc: number | null;
      change1h: number;
      change1hPercent: number;
      change24h: number;
      change24hPercent: number;
      change7d: number;
      change7dPercent: number;
      change30d: number | null;
      change30dPercent: number | null;
      marketCap: number;
      marketCapRank: number;
      fullyDilutedValuation: number | null;
      volume24h: number;
      volumeChange24h: number | null;
      circulatingSupply: number;
      totalSupply: number | null;
      maxSupply: number | null;
      ath: number;
      athDate: string;
      athChangePercent: number;
      atl: number;
      atlDate: string;
      atlChangePercent: number;
      lastUpdated: string;
      dataSource: string;
    };
  };
}

// GET /market/crypto/:symbol/onchain (New)
interface OnChainMetricsResponseDto {
  success: boolean;
  data: {
    symbol: string;
    chain: string;
    
    // Activity
    activeAddresses24h: number;
    activeAddresses7d: number;
    transactionCount24h: number;
    transactionVolume24h: number;
    transactionVolumeUsd24h: number;
    
    // Network
    avgTransactionFee: number;
    avgTransactionFeeUsd: number;
    avgBlockTime: number;
    
    // Holders
    totalHolders: number | null;
    top10HoldersPercent: number | null;
    top100HoldersPercent: number | null;
    
    // Exchange Flows
    exchangeInflow24h: number | null;
    exchangeOutflow24h: number | null;
    exchangeNetflow24h: number | null;
    
    // Whale Activity
    whaleTransactions24h: number | null;
    whaleVolume24h: number | null;
    
    // DeFi
    tvl: number | null;
    tvlChange24h: number | null;
    
    lastUpdated: string;
    dataSource: string;
  };
}

// GET /market/news
interface GetNewsQueryDto {
  symbols?: string;
  assetType?: 'stock' | 'crypto' | 'all';
  category?: string;
  limit?: number;
  page?: number;
}

// GET /market/stocks/:symbol/filings
interface GetFilingsQueryDto {
  formType?: string;
  startDate?: string;
  endDate?: string;
  limit?: number;
}
```

---

### 7.5 Chat DTOs

```typescript
// POST /chat/sessions
interface CreateSessionRequestDto {
  title?: string;
  initialMessage?: string;
}

interface CreateSessionResponseDto {
  success: boolean;
  data: {
    session: ChatSessionDto;
    message?: ChatMessageDto;
  };
}

// GET /chat/sessions/:id/messages
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
  citations?: CitationDto[];
  toolCalls?: ToolCallDto[];
  tokensUsed?: number;
  modelUsed?: string;
  processingTimeMs?: number;
  portkeyTraceId?: string;          // Link to Portkey for debugging
  createdAt: string;
}

interface CitationDto {
  index: number;
  type: 'stock_quote' | 'crypto_quote' | 'onchain' | 'news' | 'filing' | 'portfolio';
  source: string;
  title?: string;
  symbol?: string;
  url?: string;
  timestamp: string;
  snippet?: string;
}

// POST /chat/sessions/:id/messages
interface SendMessageRequestDto {
  content: string;                  // Max 4000 chars
}

// POST /chat/sessions/:id/messages/stream (SSE)
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

```typescript
// POST /watchlists
interface CreateWatchlistRequestDto {
  name: string;
  description?: string;
  color?: string;
}

// POST /watchlists/:id/items
interface AddWatchlistItemRequestDto {
  assetType: 'stock' | 'crypto';
  symbol: string;
  notes?: string;
  targetPrice?: number;
}

// POST /alerts
interface CreateAlertRequestDto {
  assetType: 'stock' | 'crypto';
  symbol: string;
  alertType: 'price_above' | 'price_below' | 'percent_change_up' | 'percent_change_down';
  thresholdValue: number;
  thresholdUnit?: 'value' | 'percent';
  notifyEmail?: boolean;            // Delivered via Novu
  notifyPush?: boolean;             // Delivered via Novu
  isRepeating?: boolean;
  cooldownMinutes?: number;
  expiresAt?: string;
}

interface AlertDto {
  id: string;
  assetType: 'stock' | 'crypto';
  symbol: string;
  name: string;
  alertType: string;
  condition: string;
  thresholdValue: number;
  thresholdUnit: string;
  currentPrice: number;
  distanceToTrigger: number;
  distancePercent: number;
  notifyEmail: boolean;
  notifyPush: boolean;
  isActive: boolean;
  isRepeating: boolean;
  triggerCount: number;
  lastTriggeredAt: string | null;
  createdAt: string;
  expiresAt: string | null;
}
```

---

## 8. API Specifications

### 8.1 API Overview

**Base URL:** `https://api.sophia.ai/v1`

**Authentication:** Bearer token (JWT)
```
Authorization: Bearer <access_token>
```

**Content Type:** `application/json`

**Rate Limits:**
- Global: 1000 requests/hour per user
- Auth endpoints: 10 requests/minute per IP
- Chat messages: 20 messages/minute per user
- Market data: 100 requests/minute per user

### 8.2 Complete Endpoint Summary

| Category | Method | Endpoint | Story | Description |
|----------|--------|----------|-------|-------------|
| **Health** | GET | /health | - | Health check |
| | GET | /health/ready | - | Readiness check |
| **Auth** | POST | /auth/register | AUTH-01 | Create account |
| | POST | /auth/login | AUTH-02 | Authenticate |
| | POST | /auth/refresh | AUTH-02 | Refresh token |
| | POST | /auth/logout | AUTH-02 | Invalidate tokens |
| | POST | /auth/forgot-password | AUTH-03 | Request reset |
| | POST | /auth/reset-password | AUTH-03 | Reset password |
| | GET | /auth/me | AUTH-05 | Get profile |
| | PATCH | /auth/me | AUTH-05 | Update profile |
| | POST | /auth/2fa/setup | AUTH-04 | Initialize 2FA |
| | POST | /auth/2fa/verify | AUTH-04 | Enable 2FA |
| | POST | /auth/2fa/disable | AUTH-04 | Disable 2FA |
| | GET | /auth/2fa/backup-codes | AUTH-04 | Get backup codes |
| | POST | /auth/2fa/backup-codes/regenerate | AUTH-04 | Regenerate codes |
| **Connections** | GET | /connections | CONN-04 | List connections |
| | GET | /connections/providers | CONN-01 | Available providers |
| | POST | /connections/oauth/initiate | CONN-01, CONN-02 | Start OAuth |
| | POST | /connections/oauth/callback | CONN-01, CONN-02 | Complete OAuth |
| | POST | /connections/wallet | CONN-03 | Add wallet |
| | DELETE | /connections/:id | CONN-05 | Disconnect |
| | POST | /connections/:id/sync | CONN-06 | Manual sync |
| | GET | /connections/:id/status | CONN-04 | Connection health |
| **Portfolio** | GET | /portfolio/summary | PORT-01, PORT-04 | Overview |
| | GET | /portfolio/holdings | PORT-02, PORT-06 | List holdings |
| | GET | /portfolio/holdings/:symbol | PORT-02 | Holding detail |
| | GET | /portfolio/performance | PORT-05 | Historical |
| | GET | /portfolio/allocation | PORT-03 | Allocation |
| | GET | /portfolio/snapshots | PORT-05 | Snapshots |
| **Market Data** | GET | /market/stocks/:symbol/quote | DATA-01 | Stock quote |
| | GET | /market/stocks/:symbol/profile | DATA-05 | Company profile |
| | GET | /market/stocks/:symbol/filings | DATA-04 | SEC filings |
| | GET | /market/crypto/:symbol/quote | DATA-02 | Crypto quote |
| | GET | /market/crypto/:symbol/profile | DATA-05 | Token profile |
| | GET | /market/crypto/:symbol/onchain | DATA-06 | On-chain metrics |
| | POST | /market/quotes/batch | DATA-01, DATA-02 | Batch quotes |
| | GET | /market/news | DATA-03 | News articles |
| | GET | /market/filings/:accession | DATA-04 | Filing detail |
| **Chat** | POST | /chat/sessions | CHAT-01 | Create session |
| | GET | /chat/sessions | CHAT-05 | List sessions |
| | GET | /chat/sessions/:id | CHAT-05 | Get session |
| | PATCH | /chat/sessions/:id | CHAT-05 | Update session |
| | DELETE | /chat/sessions/:id | CHAT-05 | Delete session |
| | GET | /chat/sessions/:id/messages | CHAT-05 | Get messages |
| | POST | /chat/sessions/:id/messages | CHAT-01-04, CHAT-06 | Send message |
| | POST | /chat/sessions/:id/messages/stream | CHAT-01-04, CHAT-06 | Stream (SSE) |
| **Watchlists** | POST | /watchlists | WATCH-01 | Create watchlist |
| | GET | /watchlists | WATCH-01 | List watchlists |
| | GET | /watchlists/:id | WATCH-01 | Get watchlist |
| | PATCH | /watchlists/:id | WATCH-01 | Update |
| | DELETE | /watchlists/:id | WATCH-01 | Delete |
| | POST | /watchlists/:id/items | WATCH-01 | Add item |
| | DELETE | /watchlists/:id/items/:itemId | WATCH-01 | Remove item |
| **Alerts** | POST | /alerts | WATCH-02 | Create alert |
| | GET | /alerts | WATCH-04 | List alerts |
| | GET | /alerts/:id | WATCH-04 | Get alert |
| | PATCH | /alerts/:id | WATCH-02 | Update alert |
| | DELETE | /alerts/:id | WATCH-02 | Delete alert |

**Total Routes: 57** (up from 51)

---

## 9. API Testing (api.http)

```http
### ==================================================
### SOPHIA API - HTTP Test File (v2.0)
### ==================================================

@baseUrl = http://localhost:3000/api/v1
@accessToken = {{loginResponse.body.data.tokens.accessToken}}
@refreshToken = {{loginResponse.body.data.tokens.refreshToken}}

### ==================================================
### HEALTH CHECK
### ==================================================

### Health Check
GET {{baseUrl}}/health

### Readiness Check
GET {{baseUrl}}/health/ready


### ==================================================
### AUTHENTICATION
### ==================================================

### Register
# @name registerResponse
POST {{baseUrl}}/auth/register
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "SecurePass123!",
  "firstName": "John",
  "lastName": "Doe"
}

### Login (without 2FA)
# @name loginResponse
POST {{baseUrl}}/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "SecurePass123!"
}

### Login (with 2FA)
POST {{baseUrl}}/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "SecurePass123!",
  "totpCode": "123456"
}

### Refresh Token
POST {{baseUrl}}/auth/refresh
Content-Type: application/json

{
  "refreshToken": "{{refreshToken}}"
}

### Get Profile
GET {{baseUrl}}/auth/me
Authorization: Bearer {{accessToken}}

### Update Profile
PATCH {{baseUrl}}/auth/me
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "firstName": "John",
  "lastName": "Smith",
  "timezone": "America/New_York"
}


### ==================================================
### TWO-FACTOR AUTHENTICATION (New)
### ==================================================

### Setup 2FA
# @name setup2FA
POST {{baseUrl}}/auth/2fa/setup
Authorization: Bearer {{accessToken}}

### Verify 2FA (enable)
POST {{baseUrl}}/auth/2fa/verify
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "code": "123456"
}

### Get Backup Codes
GET {{baseUrl}}/auth/2fa/backup-codes
Authorization: Bearer {{accessToken}}

### Regenerate Backup Codes
POST {{baseUrl}}/auth/2fa/backup-codes/regenerate
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "password": "SecurePass123!",
  "code": "123456"
}

### Disable 2FA
POST {{baseUrl}}/auth/2fa/disable
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "password": "SecurePass123!",
  "code": "123456"
}


### ==================================================
### CONNECTIONS
### ==================================================

### List Providers
GET {{baseUrl}}/connections/providers
Authorization: Bearer {{accessToken}}

### List Connections
GET {{baseUrl}}/connections
Authorization: Bearer {{accessToken}}

### Initiate Alpaca OAuth
# @name alpacaOAuth
POST {{baseUrl}}/connections/oauth/initiate
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "providerId": "alpaca"
}

### Complete OAuth Callback
POST {{baseUrl}}/connections/oauth/callback
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "providerId": "alpaca",
  "code": "auth-code-here",
  "state": "{{alpacaOAuth.body.data.state}}"
}

### Add Wallet
POST {{baseUrl}}/connections/wallet
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "chain": "ethereum",
  "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f0Ab3d",
  "label": "My Main Wallet"
}

### Manual Sync
POST {{baseUrl}}/connections/{{connectionId}}/sync
Authorization: Bearer {{accessToken}}

### Connection Status
GET {{baseUrl}}/connections/{{connectionId}}/status
Authorization: Bearer {{accessToken}}

### Disconnect
DELETE {{baseUrl}}/connections/{{connectionId}}
Authorization: Bearer {{accessToken}}


### ==================================================
### PORTFOLIO
### ==================================================

### Portfolio Summary
GET {{baseUrl}}/portfolio/summary
Authorization: Bearer {{accessToken}}

### List Holdings
GET {{baseUrl}}/portfolio/holdings?assetType=all&sortBy=value&order=desc
Authorization: Bearer {{accessToken}}

### Holding Detail
GET {{baseUrl}}/portfolio/holdings/AAPL
Authorization: Bearer {{accessToken}}

### Historical Performance
GET {{baseUrl}}/portfolio/performance?period=1M
Authorization: Bearer {{accessToken}}

### Allocation
GET {{baseUrl}}/portfolio/allocation
Authorization: Bearer {{accessToken}}

### Snapshots
GET {{baseUrl}}/portfolio/snapshots?startDate=2025-01-01&endDate=2025-11-27
Authorization: Bearer {{accessToken}}


### ==================================================
### MARKET DATA
### ==================================================

### Stock Quote
GET {{baseUrl}}/market/stocks/AAPL/quote
Authorization: Bearer {{accessToken}}

### Stock Profile
GET {{baseUrl}}/market/stocks/AAPL/profile
Authorization: Bearer {{accessToken}}

### Stock Filings
GET {{baseUrl}}/market/stocks/AAPL/filings?formType=10-K,10-Q&limit=10
Authorization: Bearer {{accessToken}}

### Crypto Quote
GET {{baseUrl}}/market/crypto/BTC/quote
Authorization: Bearer {{accessToken}}

### Crypto Profile
GET {{baseUrl}}/market/crypto/ETH/profile
Authorization: Bearer {{accessToken}}

### On-Chain Metrics (New)
GET {{baseUrl}}/market/crypto/ETH/onchain
Authorization: Bearer {{accessToken}}

### Batch Quotes
POST {{baseUrl}}/market/quotes/batch
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "stocks": ["AAPL", "GOOGL", "MSFT"],
  "crypto": ["BTC", "ETH", "SOL"]
}

### News
GET {{baseUrl}}/market/news?symbols=AAPL,BTC&limit=20
Authorization: Bearer {{accessToken}}

### Filing Detail
GET {{baseUrl}}/market/filings/0000320193-25-000001
Authorization: Bearer {{accessToken}}


### ==================================================
### CHAT (AI via Portkey)
### ==================================================

### Create Session
# @name createSession
POST {{baseUrl}}/chat/sessions
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "title": "Portfolio Analysis"
}

### List Sessions
GET {{baseUrl}}/chat/sessions
Authorization: Bearer {{accessToken}}

### Get Session
GET {{baseUrl}}/chat/sessions/{{createSession.body.data.session.id}}
Authorization: Bearer {{accessToken}}

### Send Message
POST {{baseUrl}}/chat/sessions/{{createSession.body.data.session.id}}/messages
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "content": "What's my best performing holding this month?"
}

### Stream Message (SSE)
POST {{baseUrl}}/chat/sessions/{{createSession.body.data.session.id}}/messages/stream
Authorization: Bearer {{accessToken}}
Accept: text/event-stream
Content-Type: application/json

{
  "content": "Summarize the latest SEC filing for Apple"
}

### Update Session
PATCH {{baseUrl}}/chat/sessions/{{createSession.body.data.session.id}}
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "title": "Q4 Portfolio Review",
  "isPinned": true
}

### Delete Session
DELETE {{baseUrl}}/chat/sessions/{{createSession.body.data.session.id}}
Authorization: Bearer {{accessToken}}


### ==================================================
### WATCHLISTS
### ==================================================

### Create Watchlist
# @name createWatchlist
POST {{baseUrl}}/watchlists
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "name": "Tech Stocks",
  "description": "Technology sector watchlist",
  "color": "#3B82F6"
}

### List Watchlists
GET {{baseUrl}}/watchlists
Authorization: Bearer {{accessToken}}

### Get Watchlist
GET {{baseUrl}}/watchlists/{{createWatchlist.body.data.watchlist.id}}
Authorization: Bearer {{accessToken}}

### Add Item to Watchlist
POST {{baseUrl}}/watchlists/{{createWatchlist.body.data.watchlist.id}}/items
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "assetType": "stock",
  "symbol": "NVDA",
  "notes": "AI chip leader",
  "targetPrice": 600
}

### Remove Item
DELETE {{baseUrl}}/watchlists/{{createWatchlist.body.data.watchlist.id}}/items/{{itemId}}
Authorization: Bearer {{accessToken}}

### Delete Watchlist
DELETE {{baseUrl}}/watchlists/{{createWatchlist.body.data.watchlist.id}}
Authorization: Bearer {{accessToken}}


### ==================================================
### ALERTS (Notifications via Novu)
### ==================================================

### Create Alert
# @name createAlert
POST {{baseUrl}}/alerts
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "assetType": "crypto",
  "symbol": "BTC",
  "alertType": "price_above",
  "thresholdValue": 100000,
  "notifyEmail": true,
  "notifyPush": true,
  "isRepeating": false
}

### List Alerts
GET {{baseUrl}}/alerts
Authorization: Bearer {{accessToken}}

### Get Alert
GET {{baseUrl}}/alerts/{{createAlert.body.data.alert.id}}
Authorization: Bearer {{accessToken}}

### Update Alert
PATCH {{baseUrl}}/alerts/{{createAlert.body.data.alert.id}}
Authorization: Bearer {{accessToken}}
Content-Type: application/json

{
  "thresholdValue": 110000,
  "isActive": true
}

### Delete Alert
DELETE {{baseUrl}}/alerts/{{createAlert.body.data.alert.id}}
Authorization: Bearer {{accessToken}}
```

---

## 10. Security & Compliance

### 10.1 Security Requirements

#### Authentication & Authorization
- Passwords hashed with bcrypt (12 rounds)
- JWT access tokens: 15-minute expiry
- JWT refresh tokens: 7-day expiry (rotated on use)
- TOTP-based 2FA with encrypted secrets
- Backup codes hashed with bcrypt
- Rate limiting on auth endpoints (10/min per IP)
- Account lockout after 5 failed attempts (30 min)
- Session invalidation on password change

#### Data Encryption
- **At Rest:**
  - OAuth tokens encrypted with AES-256-GCM
  - 2FA secrets encrypted with AES-256-GCM
  - Encryption key from environment variable
  - Database backups encrypted
- **In Transit:**
  - TLS 1.3 for all API traffic
  - Certificate pinning for mobile apps (future)

#### Third-Party Security
- **Portkey:** SOC 2 compliant, no prompt storage (optional)
- **Novu:** SOC 2 compliant, EU data residency available
- API keys stored encrypted, rotated quarterly

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
- **2FA module (TOTP, backup codes)**
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
- **On-chain data scrapers (Etherscan, Glassnode)**
- News scraper (Finnhub, CryptoPanic)
- SEC EDGAR scraper
- Caching layer

### Phase 5: AI Chat (Weeks 9-10)
- **Portkey integration (gateway, logging)**
- Claude integration via Portkey
- RAG pipeline
- Tool definitions (incl. on-chain tool)
- Citation system
- Chat API with streaming (SSE)

### Phase 6: Watchlists & Alerts (Week 11)
- Watchlist CRUD
- Alert CRUD
- Alert processing job
- **Novu integration (email, push, in-app)**
- Notification workflows

### Phase 7: Polish & Deploy (Week 12-13)
- Testing (unit, integration, E2E)
- Error handling
- Logging & monitoring
- Documentation
- Deployment (Railway/Render)

---

## 12. Success Metrics

### MVP Launch Criteria
- [ ] Users can register/login with optional 2FA
- [ ] Users can connect at least 1 brokerage + 1 exchange
- [ ] Portfolio syncs within 2 minutes
- [ ] Dashboard shows accurate values
- [ ] Chat responds in <5 seconds (tracked in Portkey)
- [ ] All AI responses have citations
- [ ] Market data <1 minute delay
- [ ] On-chain metrics available for top 20 cryptos
- [ ] Alerts trigger notifications via Novu within 1 minute

### KPIs
- **Activation:** 70% connect at least 1 account
- **Engagement:** 5 chat messages per session average
- **Sync reliability:** >99% success rate
- **API performance:** p95 <200ms
- **AI quality:** 100% responses with valid citations
- **AI cost efficiency:** <$0.10 per chat session (via Portkey)
- **Notification delivery:** >99% success rate (via Novu)

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
| Etherscan | Blockchain | API Key | 5/sec | |
| Glassnode | On-Chain | API Key | 10/min | Paid for full data |
| SEC EDGAR | Data | None | 10/sec | User-Agent required |
| Anthropic | AI | via Portkey | 60/min | claude-3-5-sonnet |
| Portkey | AI Gateway | API Key | Unlimited | Manages AI routing |
| Novu | Notifications | API Key | 10,000/hour | Multi-channel |

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

# Blockchain / On-Chain
ETHERSCAN_API_KEY=
SOLSCAN_API_KEY=
GLASSNODE_API_KEY=

# AI (via Portkey)
PORTKEY_API_KEY=
PORTKEY_VIRTUAL_KEY_ANTHROPIC=

# Notifications (Novu)
NOVU_API_KEY=
NOVU_APP_ID=

# Frontend
FRONTEND_URL=http://localhost:3001
```

### C. Third-Party Service Setup

#### Portkey Setup
1. Create account at portkey.ai
2. Create virtual key for Anthropic
3. Configure logging preferences
4. Set up alerting for errors/costs
5. Add `PORTKEY_API_KEY` and `PORTKEY_VIRTUAL_KEY_ANTHROPIC` to env

#### Novu Setup
1. Create account at novu.co
2. Create notification workflows:
   - `alert-triggered`
   - `daily-summary`
   - `sync-status`
3. Configure email provider (SendGrid/SES)
4. Configure push provider (FCM)
5. Add `NOVU_API_KEY` and `NOVU_APP_ID` to env

---

**Document Version:** 2.0  
**Last Updated:** November 27, 2025  
**Changes from v1.0:**
- Added 2FA routes and `two_factor_backup_codes` table
- Added on-chain metrics route and `crypto_onchain_cache` table
- Integrated Novu for notifications (removed notification tables)
- Integrated Portkey for AI observability (removed `api_usage_logs` table)
- Added `portkeyTraceId` to chat messages
- Added `novuSubscriberId` to users
- Aligned all routes with user stories
- Updated architecture diagrams
