# Product Requirements Document (PRD)
# Jaspers AI - Personalized Investment Copilot

**Version:** 1.0  
**Date:** November 7, 2025  
**Status:** MVP Development  
**Owner:** Engineering Team

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Product Overview](#product-overview)
3. [Goals & Success Metrics](#goals--success-metrics)
4. [User Personas & Use Cases](#user-personas--use-cases)
5. [Functional Requirements](#functional-requirements)
6. [Technical Architecture](#technical-architecture)
7. [Data Models](#data-models)
8. [API Specifications](#api-specifications)
9. [User Experience & UI](#user-experience--ui)
10. [Security & Compliance](#security--compliance)
11. [Implementation Plan](#implementation-plan)
12. [Dependencies & Integrations](#dependencies--integrations)
13. [Success Criteria](#success-criteria)
14. [Future Enhancements](#future-enhancements)

---

## 1. Executive Summary

Jaspers AI is a **personalized investment copilot** that connects to users' brokerage accounts and provides an AI-powered chat interface to answer questions about their portfolio, analyze holdings, and deliver insights backed by real-time financial data and SEC filings.

### Key Value Propositions:
- **Portfolio Aggregation**: Unified view across multiple brokerage accounts (Alpaca, Interactive Brokers)
- **AI-Powered Insights**: Natural language interface powered by Claude AI with RAG (Retrieval-Augmented Generation)
- **Cited Research**: All answers include sources (SEC filings, news articles, market data)
- **Real-Time Data**: Live portfolio syncing and market data integration
- **Secure & Private**: Bank-level encryption for brokerage credentials

### Target Users:
- Retail investors with multiple brokerage accounts
- Active traders seeking portfolio analytics
- Investors wanting AI-assisted research and insights

---

## 2. Product Overview

### 2.1 What is Jaspers AI?

Jaspers AI is a web application that allows investors to:
1. **Connect** their brokerage accounts via OAuth
2. **View** their aggregated portfolio in real-time
3. **Chat** with an AI assistant about their investments
4. **Research** stocks using natural language queries
5. **Track** performance with historical snapshots

### 2.2 Core Features

#### Feature 1: Brokerage Integration
- OAuth connection to Alpaca and Interactive Brokers
- Automatic portfolio synchronization every 15 minutes during market hours
- Secure credential storage with AES-256 encryption

#### Feature 2: Portfolio Dashboard
- Total portfolio value and P&L
- Holdings breakdown with allocation percentages
- Daily performance tracking
- Historical snapshots for charting

#### Feature 3: AI Chat Assistant
- Natural language Q&A about portfolio and stocks
- RAG pipeline with tool calling for data retrieval
- Cited sources for all claims (news, SEC filings, market data)
- Streaming responses for better UX

#### Feature 4: Financial Data Integration
- Real-time stock quotes from Yahoo Finance and Finnhub
- Company information and metrics
- News aggregation
- SEC EDGAR filing search and retrieval

---

## 3. Goals & Success Metrics

### 3.1 Business Goals
- Enable users to make informed investment decisions
- Reduce time spent switching between brokerage platforms
- Provide accurate, cited financial information via AI

### 3.2 User Goals
- Understand portfolio performance at a glance
- Get quick answers to investment questions
- Research stocks without leaving the platform
- Track P&L across multiple brokerages

### 3.3 Success Metrics

**MVP Launch Criteria:**
- Users can successfully connect Alpaca OR Interactive Brokers
- Portfolio syncs within 1 minute of connection
- Chat responds in <5 seconds (95th percentile)
- AI answers include at least 1 citation per response
- Mobile-responsive UI

**Key Performance Indicators (KPIs):**
- **User Activation:** % of users who connect at least 1 brokerage
- **Engagement:** Average chat messages per session
- **Sync Reliability:** % of successful portfolio syncs (target: >95%)
- **Response Quality:** % of AI responses with valid citations (target: 100%)
- **Performance:** API response time <200ms (p95)

---

## 4. User Personas & Use Cases

### Persona 1: Multi-Account Investor
**Profile:** Sarah, 32, holds accounts at Alpaca and Interactive Brokers
**Goal:** View total portfolio without logging into multiple platforms
**Use Case:** "Show me my total portfolio value and top performers this week"

### Persona 2: Research-Oriented Trader
**Profile:** Mike, 45, actively researches before trading
**Goal:** Quickly analyze company fundamentals and recent filings
**Use Case:** "What did Apple's latest 10-K say about revenue growth?"

### Persona 3: Performance Tracker
**Profile:** Jessica, 28, wants to track long-term performance
**Goal:** Understand historical returns and allocation changes
**Use Case:** "What's my portfolio performance over the last 6 months?"

### Key User Flows

#### Flow 1: Onboarding
1. User registers with email/password
2. User connects Alpaca account via OAuth
3. System syncs portfolio holdings
4. User sees dashboard with portfolio summary

#### Flow 2: Portfolio Check
1. User logs in
2. Dashboard displays aggregated holdings
3. User views specific stock details
4. User sees P&L and allocation breakdown

#### Flow 3: AI Research
1. User opens chat interface
2. User asks: "Why is TSLA down today?"
3. AI fetches news, price data, and market context
4. AI responds with analysis and cited sources
5. User clicks citation to view source

---

## 5. Functional Requirements

### 5.1 Authentication & User Management

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| AUTH-1 | Users can register with email/password | P0 | Must validate email format |
| AUTH-2 | Users can log in with JWT-based auth | P0 | Access token: 15min, Refresh: 7 days |
| AUTH-3 | Users can reset forgotten passwords | P1 | Email-based reset flow |
| AUTH-4 | Users can update profile information | P1 | Name, email, password |
| AUTH-5 | Users can enable email verification | P2 | Send verification email |

**Business Rules:**
- Passwords must be 8+ characters with uppercase, lowercase, number
- Login attempts limited to 5 per 15 minutes per IP
- Sessions invalidated on password change
- Audit log all authentication events

### 5.2 Brokerage Connections

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| BROK-1 | Users can connect Alpaca via OAuth 2.0 | P0 | Use PKCE flow |
| BROK-2 | Users can connect IBKR via Client Portal API | P1 | Session-based auth |
| BROK-3 | System encrypts tokens with AES-256 | P0 | Use environment encryption key |
| BROK-4 | Users can disconnect brokerage accounts | P0 | Delete tokens securely |
| BROK-5 | System auto-refreshes expired tokens | P0 | Handle token expiration |
| BROK-6 | Users can manually trigger portfolio sync | P1 | On-demand sync button |
| BROK-7 | System displays connection status | P1 | Show health check results |

**Business Rules:**
- One connection per brokerage provider per user
- Auto-sync every 15 minutes during market hours (9:30 AM - 4 PM ET)
- Retry failed syncs with exponential backoff (3 attempts max)
- Store sync errors in database for debugging
- Track last successful sync timestamp

### 5.3 Portfolio Management

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| PORT-1 | Display total portfolio value | P0 | Sum across all brokerages |
| PORT-2 | Display aggregated holdings list | P0 | Deduplicate same symbols |
| PORT-3 | Calculate unrealized P&L per holding | P0 | (current_price - avg_cost) * qty |
| PORT-4 | Calculate allocation percentages | P0 | holding_value / total_value * 100 |
| PORT-5 | Display cash balance | P1 | Sum from all accounts |
| PORT-6 | Show daily P&L change | P1 | Compare to previous close |
| PORT-7 | Track historical performance | P1 | Daily snapshots at market close |
| PORT-8 | Display holding details per symbol | P1 | Quantity, cost basis, current value |

**Business Rules:**
- Use average cost method for cost basis
- Cache portfolio summary for 30 seconds to reduce load
- Handle partial failures (show available data if one brokerage fails)
- Update holdings on every sync
- Create daily snapshot at 4 PM ET for historical tracking
- Display real-time prices during market hours

### 5.4 Financial Data

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FIN-1 | Provide real-time stock quotes | P0 | Yahoo Finance primary, Finnhub fallback |
| FIN-2 | Provide batch quote lookups | P0 | Support multiple symbols at once |
| FIN-3 | Provide historical price data | P1 | OHLCV data for charting |
| FIN-4 | Provide company profile information | P1 | Name, sector, industry, description |
| FIN-5 | Provide latest news for symbols | P1 | Finnhub and Yahoo Finance |
| FIN-6 | Search SEC EDGAR filings | P1 | 10-K, 10-Q, 8-K by symbol/CIK |
| FIN-7 | Retrieve filing content | P2 | Full filing text and sections |

**Business Rules:**
- **Caching Strategy:**
  - Quotes: 1-min TTL during market hours, 1-hour after hours
  - Company info: 24-hour TTL
  - News: 15-min TTL
  - EDGAR filings: Cache indefinitely (immutable)
- **Fallback Logic:** If primary API fails, use fallback source
- **Rate Limiting:** Track API usage to stay within quotas
  - Yahoo Finance: Unlimited (unofficial)
  - Finnhub: 60 calls/min (free tier)
  - SEC EDGAR: 10 requests/sec max
- Return cached data if live fetch fails (stale > none)

### 5.5 AI Chat

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| CHAT-1 | Users can create chat sessions | P0 | Auto-generate title from first message |
| CHAT-2 | Users can send messages and receive AI responses | P0 | Use Claude 3.5 Sonnet |
| CHAT-3 | AI responses include cited sources | P0 | Link to news, filings, data sources |
| CHAT-4 | System uses RAG pipeline for context | P0 | Fetch portfolio + market data |
| CHAT-5 | AI can call tools to retrieve data | P0 | Portfolio, quotes, news, EDGAR tools |
| CHAT-6 | Users can view chat history | P1 | Load previous messages |
| CHAT-7 | Users can delete chat sessions | P1 | Soft delete with archive flag |
| CHAT-8 | System streams responses in real-time | P2 | SSE for better UX |
| CHAT-9 | Users can edit session titles | P2 | Custom naming |

**Business Rules:**
- **RAG Pipeline:**
  1. Parse intent (extract tickers, time ranges, question type)
  2. Retrieve context (portfolio holdings, stock data, news, filings)
  3. Build structured context for Claude
  4. Call Claude with tools enabled
  5. Execute tool calls server-side
  6. Generate final response with citations
  7. Store message and tool calls in DB

- **Tool Definitions:**
  - `get_portfolio_holdings` - Retrieve user positions
  - `get_stock_quote` - Get current price/metrics
  - `search_company_news` - Find recent articles
  - `search_edgar_filings` - Search SEC filings
  - `get_portfolio_performance` - Historical data
  - `calculate_portfolio_metrics` - Custom calculations

- **Citation Format:**
  - `[Source: Yahoo Finance - AAPL Quote, 2024-10-27](url)`
  - `[Source: SEC 10-K Filing, Q4 2023](url)`
  - Store as JSON in `chat_messages.citations` field

- **Context Management:**
  - Include last 10 messages for conversation continuity
  - Track token usage per message
  - Log processing time for monitoring
  - Rate limit: 10 messages/min per session

### 5.6 Analytics & Monitoring

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| ANAL-1 | Track API usage per provider | P1 | Log all external API calls |
| ANAL-2 | Track Claude token usage and costs | P1 | Input/output tokens separately |
| ANAL-3 | Audit log security events | P0 | Login, brokerage changes, etc. |
| ANAL-4 | Health check endpoint | P0 | Monitor DB and external APIs |
| ANAL-5 | Display usage stats to users | P2 | Dashboard with API call counts |

**Business Rules:**
- Log every external API call with response time, status, cost
- Track IP addresses and user agents for security
- Detect anomalous patterns (excessive calls, failed logins)
- Alert on health check failures
- Store audit logs for 90 days minimum

---

## 6. Technical Architecture

### 6.1 System Architecture

```
┌─────────────┐
│   Browser   │
│  (Next.js)  │
└──────┬──────┘
       │ HTTPS/WSS
       ▼
┌─────────────────────────────────────────┐
│         Backend API (NestJS)            │
│  ┌────────────────────────────────┐    │
│  │  Auth │ Portfolio │ Chat │ ... │    │
│  └────────────────────────────────┘    │
│              │                          │
│         ┌────┴────┐                     │
│         ▼         ▼                     │
│    PostgreSQL   Redis (Cache)           │
└────────┬────────────────────────────────┘
         │
    ┌────┴─────────────────────────────────┐
    │      External APIs                   │
    ├────────────┬──────────────┬──────────┤
    │ Alpaca     │ Yahoo Finance│ Anthropic│
    │ IBKR       │ Finnhub      │ Claude   │
    │            │ SEC EDGAR    │          │
    └────────────┴──────────────┴──────────┘
```

### 6.2 Technology Stack

**Backend:**
- **Framework:** NestJS (TypeScript)
- **Database:** PostgreSQL 15+ with TypeORM
- **Cache:** Redis (optional for MVP)
- **Authentication:** JWT with Passport.js
- **Validation:** class-validator, class-transformer
- **HTTP Client:** Axios
- **Scheduling:** @nestjs/schedule (cron jobs)

**Frontend:**
- **Framework:** Next.js 14+ (App Router)
- **UI Library:** React 18+
- **Styling:** Tailwind CSS
- **State Management:** React Query + Context API
- **Chat UI:** @assistant-ui/react
- **HTTP Client:** Axios
- **Charts:** Recharts or Chart.js

**External Services:**
- **AI:** Anthropic Claude API (`claude-3-5-sonnet-20241022`)
- **Brokerages:** Alpaca REST API, IBKR Client Portal API
- **Financial Data:** Yahoo Finance, Finnhub, SEC EDGAR

**DevOps:**
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Hosting:** 
  - Backend: Railway, Render, or AWS
  - Frontend: Vercel
  - Database: AWS RDS, Supabase, or Railway
- **Monitoring:** Sentry (error tracking), Uptime Robot (uptime)

### 6.3 Module Structure

**Backend Modules:**
```
/backend/src/modules/
├── auth/                    # JWT authentication
├── users/                   # User management
├── brokerages/              # Brokerage integrations
│   └── providers/
│       ├── alpaca.service.ts
│       └── ibkr.service.ts
├── portfolio/               # Portfolio aggregation
├── financial-data/          # Stock quotes, news, EDGAR
│   └── providers/
│       ├── yahoo-finance.service.ts
│       ├── finnhub.service.ts
│       └── edgar.service.ts
├── chat/                    # AI chat & RAG
│   ├── claude.service.ts
│   ├── rag/
│   │   ├── intent-parser.service.ts
│   │   ├── context-builder.service.ts
│   │   └── citation-generator.service.ts
│   └── tools/
│       ├── portfolio-tool.ts
│       ├── quote-tool.ts
│       ├── news-tool.ts
│       └── edgar-tool.ts
├── analytics/               # Usage tracking, audit logs
└── health/                  # Health checks
```

**Frontend Structure:**
```
/frontend/app/
├── auth/
│   ├── login/
│   └── register/
├── dashboard/               # Portfolio overview
├── chat/                    # Chat interface
├── connect/                 # Brokerage connection
└── settings/                # User settings

/frontend/components/
├── PortfolioSummary.tsx
├── HoldingsTable.tsx
├── ChatInterface.tsx
├── AllocationChart.tsx
└── PerformanceChart.tsx
```

---

## 7. Data Models

### 7.1 Core Entities

#### User
```typescript
{
  id: uuid
  email: string (unique)
  passwordHash: string
  firstName?: string
  lastName?: string
  isActive: boolean
  emailVerified: boolean
  createdAt: timestamp
  updatedAt: timestamp
  lastLoginAt?: timestamp
}
```

#### BrokerageConnection
```typescript
{
  id: uuid
  userId: uuid (FK -> users.id)
  provider: 'alpaca' | 'ibkr'
  accountId?: string (external account ID)
  accessTokenEncrypted: string (AES-256)
  refreshTokenEncrypted?: string
  tokenExpiresAt?: timestamp
  isActive: boolean
  lastSyncAt?: timestamp
  syncStatus: 'pending' | 'syncing' | 'success' | 'error'
  syncErrorMessage?: string
  connectedAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### PortfolioHolding
```typescript
{
  id: uuid
  userId: uuid (FK -> users.id)
  brokerageConnectionId: uuid (FK -> brokerage_connections.id)
  symbol: string (ticker)
  assetType: 'stock' | 'etf' | 'crypto'
  quantity: decimal(20,8)
  averageCost: decimal(20,4)
  currentPrice: decimal(20,4)
  marketValue: decimal(20,4)  // quantity * currentPrice
  unrealizedPl: decimal(20,4)  // (currentPrice - averageCost) * quantity
  unrealizedPlPercent: decimal(10,4)
  costBasis: decimal(20,4)  // quantity * averageCost
  lastSyncedAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### ChatSession
```typescript
{
  id: uuid
  userId: uuid (FK -> users.id)
  title?: string
  isArchived: boolean
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### ChatMessage
```typescript
{
  id: uuid
  sessionId: uuid (FK -> chat_sessions.id)
  role: 'user' | 'assistant' | 'system'
  content: string
  citations?: json  // Array of citation objects
  tokensUsed?: number
  modelUsed?: string  // e.g., 'claude-3-5-sonnet-20241022'
  processingTimeMs?: number
  createdAt: timestamp
}
```

### 7.2 Cache Entities

#### StockQuoteCache
```typescript
{
  id: uuid
  symbol: string
  price: decimal(20,4)
  change: decimal(20,4)
  changePercent: decimal(10,4)
  volume: bigint
  marketCap?: bigint
  peRatio?: decimal(10,4)
  dayHigh: decimal(20,4)
  dayLow: decimal(20,4)
  yearHigh: decimal(20,4)
  yearLow: decimal(20,4)
  dataSource: 'yahoo' | 'finnhub'
  fetchedAt: timestamp
  createdAt: timestamp
}
```

#### EdgarFilingCache
```typescript
{
  id: uuid
  cik: string
  symbol?: string
  filingType: '10-K' | '10-Q' | '8-K' | etc.
  filingDate: date
  reportPeriod?: date
  accessionNumber: string (unique)
  filingUrl: string
  htmlUrl?: string
  extractedText?: text  // Key sections
  fetchedAt: timestamp
  createdAt: timestamp
}
```

### 7.3 Database Schema

See `jaspers.dbml` for complete schema with indexes and relationships.

**Key Indexes:**
- `users.email` (unique)
- `brokerage_connections(user_id, provider)` (unique)
- `portfolio_holdings(user_id, symbol)`
- `chat_messages(session_id, created_at)`
- `stock_quotes_cache(symbol, fetched_at)`
- `edgar_filings_cache(accession_number)` (unique)

**Relationships:**
- User → BrokerageConnection (one-to-many)
- User → PortfolioHolding (one-to-many)
- User → ChatSession (one-to-many)
- ChatSession → ChatMessage (one-to-many)
- BrokerageConnection → PortfolioHolding (one-to-many)

---

## 8. API Specifications

### 8.1 API Design Principles

**RESTful Conventions:**
- Use proper HTTP methods (GET, POST, PATCH, DELETE)
- Plural nouns for collections (`/api/holdings`)
- Nested resources where appropriate (`/api/chat/sessions/:id/messages`)
- Query params for filtering, sorting, pagination

**Response Format:**
```typescript
// Success response
{
  success: true,
  data: { ... },
  meta?: { page, limit, total, hasMore }
}

// Error response
{
  success: false,
  error: {
    code: "PORTFOLIO_SYNC_FAILED",
    message: "Unable to sync portfolio from Alpaca",
    details?: any
  }
}
```

**Authentication:**
- All endpoints (except `/api/auth/*` and `/api/health`) require JWT
- Header: `Authorization: Bearer <access_token>`
- Return `401 Unauthorized` for invalid/expired tokens
- Return `403 Forbidden` for insufficient permissions

**Rate Limiting:**
- Global: 1000 requests/hour per user
- Auth login: 5 attempts per 15 minutes per IP
- Chat messages: 10 messages/minute per session
- Portfolio sync: 4 syncs/hour per user

### 8.2 API Endpoints Summary

#### Authentication (10 endpoints)
- `POST /api/auth/register` - Create account
- `POST /api/auth/login` - Authenticate
- `POST /api/auth/refresh` - Refresh token
- `POST /api/auth/logout` - End session
- `POST /api/auth/verify-email` - Verify email
- `POST /api/auth/forgot-password` - Request reset
- `POST /api/auth/reset-password` - Reset password
- `GET /api/auth/me` - Get profile
- `PATCH /api/auth/me` - Update profile
- `POST /api/auth/change-password` - Change password

#### User Settings (2 endpoints)
- `GET /api/settings` - Get settings
- `PATCH /api/settings` - Update settings

#### Brokerage Connections (8 endpoints)
- `GET /api/brokerages` - List providers
- `GET /api/brokerages/connections` - User's connections
- `POST /api/brokerages/connect` - Initiate OAuth
- `GET /api/brokerages/callback` - OAuth callback
- `POST /api/brokerages/ibkr/connect` - IBKR connection
- `DELETE /api/brokerages/connections/:id` - Disconnect
- `POST /api/brokerages/connections/:id/sync` - Manual sync
- `GET /api/brokerages/connections/:id/status` - Health check

#### Portfolio (7 endpoints)
- `GET /api/portfolio/summary` - Overview stats
- `GET /api/portfolio/holdings` - All positions
- `GET /api/portfolio/holdings/:symbol` - Specific holding
- `GET /api/portfolio/performance` - Historical performance
- `GET /api/portfolio/snapshots` - Daily snapshots
- `GET /api/portfolio/allocation` - Asset breakdown
- `POST /api/portfolio/sync` - Force sync

#### Financial Data (13 endpoints)
- `GET /api/stocks/quote/:symbol` - Single quote
- `POST /api/stocks/quotes` - Batch quotes
- `GET /api/stocks/:symbol/history` - Historical prices
- `GET /api/stocks/:symbol/info` - Company profile
- `GET /api/stocks/:symbol/metrics` - Key metrics
- `GET /api/stocks/:symbol/earnings` - Earnings data
- `GET /api/stocks/:symbol/news` - Symbol news
- `GET /api/news` - General market news
- `GET /api/edgar/filings/:symbol` - Filings by ticker
- `GET /api/edgar/filings/:cik` - Filings by CIK
- `GET /api/edgar/filing/:accession` - Filing content
- `GET /api/edgar/search` - Search filings

#### Chat (8 endpoints)
- `POST /api/chat/sessions` - Create session
- `GET /api/chat/sessions` - List sessions
- `GET /api/chat/sessions/:id` - Get session
- `PATCH /api/chat/sessions/:id` - Update session
- `DELETE /api/chat/sessions/:id` - Delete session
- `GET /api/chat/sessions/:id/messages` - Message history
- `POST /api/chat/sessions/:id/messages` - Send message
- `GET /api/chat/sessions/:id/messages/stream` - SSE stream

#### Analytics & Health (4 endpoints)
- `GET /api/analytics/usage` - API usage stats
- `GET /api/analytics/costs` - Cost estimates
- `GET /api/audit/logs` - Audit trail
- `GET /api/health` - Health check

**Total: 60 API endpoints**

### 8.3 Key API Examples

#### Example 1: User Registration
```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123",
  "firstName": "John",
  "lastName": "Doe"
}

Response 201:
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe"
    },
    "tokens": {
      "accessToken": "eyJhbGciOiJIUzI1...",
      "refreshToken": "eyJhbGciOiJIUzI1...",
      "expiresIn": 900
    }
  }
}
```

#### Example 2: Get Portfolio Summary
```http
GET /api/portfolio/summary
Authorization: Bearer <token>

Response 200:
{
  "success": true,
  "data": {
    "totalValue": 125430.50,
    "cashBalance": 5430.50,
    "investedValue": 120000.00,
    "totalPl": 8430.50,
    "totalPlPercent": 7.03,
    "dayPl": 234.75,
    "dayPlPercent": 0.19,
    "lastSyncedAt": "2024-10-27T14:32:15Z"
  }
}
```

#### Example 3: Send Chat Message
```http
POST /api/chat/sessions/abc123/messages
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "What's my portfolio performance this week?"
}

Response 200:
{
  "success": true,
  "data": {
    "id": "msg-uuid",
    "sessionId": "abc123",
    "role": "assistant",
    "content": "Your portfolio is up 2.3% this week (+$2,450). Your top performer was AAPL with a 5.2% gain. [Source: Portfolio Holdings](internal)",
    "citations": [
      {
        "text": "Portfolio Holdings",
        "url": "internal",
        "timestamp": "2024-10-27T14:30:00Z"
      }
    ],
    "tokensUsed": 1250,
    "processingTimeMs": 3420,
    "createdAt": "2024-10-27T14:30:05Z"
  }
}
```

---

## 9. User Experience & UI

### 9.1 Key Pages

#### 1. Login/Register Page
- Email/password forms
- Form validation
- "Forgot password" link
- Error messaging

#### 2. Brokerage Connection Page
- List of supported providers (Alpaca, IBKR)
- "Connect" buttons for each
- OAuth flow with popup/redirect
- Connection status indicators
- "Disconnect" option for connected accounts

#### 3. Portfolio Dashboard
**Layout:**
- **Header:** Total value, day P&L, total P&L
- **Holdings Table:** Symbol, quantity, price, value, P&L, allocation%
- **Allocation Pie Chart:** Visual breakdown by holding
- **Performance Line Chart:** Historical value over time
- **Auto-refresh:** Every 30 seconds during market hours

#### 4. Chat Interface
**Layout:**
- **Left Sidebar:** Session history with titles
- **Main Area:** Message thread with user/AI bubbles
- **Input Area:** Textarea with send button
- **Features:**
  - Citation badges in AI messages (clickable)
  - Loading spinner during AI response
  - Suggested prompts: "Portfolio overview?", "Top performers?"
  - Session title editing
  - New session button

#### 5. Settings Page
- Profile update (name, email)
- Password change
- Notification preferences
- Currency and timezone settings

### 9.2 Design System

**Colors:**
- Primary: Blue/Indigo for actions
- Success: Green for positive P&L
- Danger: Red for negative P&L
- Neutral: Gray for text and backgrounds

**Typography:**
- Headings: Bold, large font
- Body: Regular weight, readable size
- Monospace: For numbers and tickers

**Components:**
- Buttons: Primary, secondary, danger variants
- Cards: Elevated with shadows
- Tables: Sortable, filterable
- Charts: Interactive with tooltips
- Badges: For citations and tags

**Responsiveness:**
- Mobile-first design
- Breakpoints: 640px (mobile), 768px (tablet), 1024px (desktop)
- Collapsible sidebar on mobile
- Stacked layout for small screens

---

## 10. Security & Compliance

### 10.1 Security Requirements

#### Authentication Security
- Passwords hashed with bcrypt (10+ rounds)
- JWT access tokens: 15-minute expiry
- JWT refresh tokens: 7-day expiry, stored securely
- Rate limiting on login (5 attempts per 15 min per IP)
- Account lockout after 10 failed attempts
- Session invalidation on password change

#### Data Encryption
- **At Rest:**
  - Brokerage tokens encrypted with AES-256
  - Encryption key stored in environment variable (32-byte hex)
  - Database backups encrypted
- **In Transit:**
  - HTTPS only in production (TLS 1.2+)
  - Secure WebSocket (WSS) for streaming

#### API Security
- CORS properly configured (whitelist frontend domain)
- CSRF protection for state-changing operations
- Input validation on all endpoints (class-validator)
- SQL injection prevention (TypeORM parameterized queries)
- XSS prevention (sanitize HTML outputs)
- Rate limiting per user/IP
- Request size limits (prevent DoS)

#### Sensitive Data Handling
- Never log passwords, tokens, or PII
- Mask sensitive data in error messages
- Audit log all security events (login, brokerage changes, etc.)
- Store audit logs for 90+ days

### 10.2 Compliance Considerations

**Data Privacy:**
- Users own their data
- Support data export (GDPR compliance)
- Support account deletion with data purge
- Clear privacy policy and terms of service

**Financial Data:**
- No trading execution (reduces regulatory burden)
- Read-only brokerage access
- Disclose data sources and limitations
- No financial advice (AI is informational only)

**Third-Party APIs:**
- Comply with API terms of service:
  - Alpaca: OAuth best practices
  - SEC EDGAR: 10 requests/sec limit, User-Agent header
  - Anthropic: Token usage tracking, content policies
  - Finnhub: API key security, rate limits

### 10.3 Security Checklist

- [ ] All passwords hashed with bcrypt
- [ ] JWT tokens with short expiry
- [ ] Brokerage tokens encrypted at rest (AES-256)
- [ ] HTTPS only in production
- [ ] CORS properly configured
- [ ] Rate limiting enabled
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (TypeORM)
- [ ] XSS prevention (sanitize outputs)
- [ ] CSRF protection for state changes
- [ ] Environment variables never committed
- [ ] Audit logging for sensitive operations
- [ ] Secure headers (Helmet.js)
- [ ] Database connection pooling
- [ ] Error handling doesn't leak sensitive info

---

## 11. Implementation Plan

### Phase 1: Infrastructure & Setup (Week 1)
**Goal:** Set up development environment and core infrastructure

**Tasks:**
- Initialize monorepo with `/backend` (NestJS) and `/frontend` (Next.js)
- Configure TypeScript, ESLint, Prettier
- Create Docker Compose for PostgreSQL and Redis
- Set up database schema and migrations
- Create `.env.example` files
- Install all dependencies

**Deliverables:**
- ✅ NestJS backend running on `localhost:3000`
- ✅ Next.js frontend running on `localhost:3001`
- ✅ PostgreSQL database with initial schema
- ✅ Docker Compose setup for local dev

### Phase 2: Authentication Module (Week 2)
**Goal:** Implement secure user authentication

**Tasks:**
- Build JWT authentication with Passport
- Create registration, login, refresh endpoints
- Implement password hashing with bcrypt
- Add auth guards and decorators
- Create login/register UI pages
- Implement auth context in frontend

**Deliverables:**
- ✅ Users can register and log in
- ✅ JWT tokens issued and validated
- ✅ Protected routes require authentication
- ✅ Frontend auth flow complete

### Phase 3: Brokerage Integration (Week 3)
**Goal:** Connect Alpaca brokerage (IBKR optional)

**Tasks:**
- Implement Alpaca OAuth 2.0 flow
- Build token encryption utility (AES-256)
- Create brokerage connection endpoints
- Build connection UI page
- Implement token refresh logic
- Add connection health checks

**Deliverables:**
- ✅ Users can connect Alpaca account
- ✅ Tokens stored encrypted in database
- ✅ OAuth flow functional from UI
- ✅ Connection status visible

### Phase 4: Portfolio Module (Week 4)
**Goal:** Sync and display portfolio data

**Tasks:**
- Build Alpaca API wrapper for positions/account
- Implement portfolio sync service
- Create cron job for auto-sync (15-min intervals)
- Build portfolio aggregation logic (multi-brokerage)
- Create portfolio summary/holdings endpoints
- Build portfolio dashboard UI
- Implement holdings table and charts

**Deliverables:**
- ✅ Portfolio syncs automatically from Alpaca
- ✅ Dashboard displays total value, P&L, holdings
- ✅ Allocation chart rendered
- ✅ Performance tracking functional

### Phase 5: Financial Data Module (Week 5)
**Goal:** Integrate stock quotes, news, and EDGAR data

**Tasks:**
- Implement Yahoo Finance service (quotes, company info)
- Implement Finnhub service (quotes, metrics, news)
- Implement SEC EDGAR service (filing search, retrieval)
- Build caching layer for all data sources
- Create financial data endpoints
- Add fallback logic for API failures

**Deliverables:**
- ✅ Stock quotes API functional
- ✅ Company info API functional
- ✅ News API functional
- ✅ EDGAR filing search functional
- ✅ Caching reduces redundant API calls

### Phase 6: AI Chat Module (Week 6-7)
**Goal:** Build AI assistant with RAG pipeline

**Tasks:**
- Integrate Anthropic Claude API
- Build RAG pipeline:
  - Intent parser (extract tickers, time ranges)
  - Context builder (fetch portfolio/market data)
  - Citation generator (track sources)
- Define AI tools:
  - Portfolio holdings tool
  - Stock quote tool
  - News search tool
  - EDGAR search tool
- Implement tool executor service
- Build chat endpoints
- Create chat UI with message history
- Implement citation rendering

**Deliverables:**
- ✅ Users can create chat sessions
- ✅ AI responds to portfolio questions
- ✅ AI uses tools to fetch real data
- ✅ Responses include cited sources
- ✅ Chat UI functional with history

### Phase 7: Analytics & Monitoring (Week 8)
**Goal:** Add usage tracking, audit logs, health checks

**Tasks:**
- Implement API usage logging
- Build audit log service
- Create health check endpoints
- Add error tracking (Sentry)
- Implement rate limiting
- Add global exception filter
- Build logging interceptor

**Deliverables:**
- ✅ All API calls logged with metrics
- ✅ Security events audited
- ✅ Health checks monitor system status
- ✅ Rate limiting prevents abuse
- ✅ Errors tracked in Sentry

### Phase 8: Testing & Polish (Week 8)
**Goal:** Ensure quality and reliability

**Tasks:**
- Write unit tests for core services
- Write integration tests for modules
- Write E2E tests for critical flows
- Fix any bugs or linter errors
- Optimize performance (database queries, caching)
- Mobile responsiveness testing
- Accessibility audit

**Deliverables:**
- ✅ Test coverage >80% for services
- ✅ All critical flows tested E2E
- ✅ No critical bugs
- ✅ Mobile-friendly UI
- ✅ Performance targets met

### Phase 9: Deployment (Week 9)
**Goal:** Deploy to production

**Tasks:**
- Set up production PostgreSQL (AWS RDS/Supabase)
- Deploy backend to Railway/Render
- Deploy frontend to Vercel
- Configure CI/CD with GitHub Actions
- Set up monitoring (Uptime Robot)
- Configure environment variables
- Run database migrations in production
- Set up backups

**Deliverables:**
- ✅ Backend deployed and accessible
- ✅ Frontend deployed and accessible
- ✅ Database production-ready with backups
- ✅ CI/CD pipeline functional
- ✅ Monitoring active

---

## 12. Dependencies & Integrations

### 12.1 Backend Dependencies

**Core:**
- `@nestjs/core`, `@nestjs/common`, `@nestjs/platform-express`
- `@nestjs/config` - Environment config
- `@nestjs/typeorm`, `typeorm`, `pg` - Database
- `@nestjs/jwt`, `@nestjs/passport`, `passport`, `passport-jwt` - Auth
- `bcrypt`, `@types/bcrypt` - Password hashing
- `class-validator`, `class-transformer` - Validation

**External APIs:**
- `@anthropic-ai/sdk` - Claude AI
- `axios` - HTTP client for external APIs

**Utilities:**
- `dayjs` - Date manipulation
- `crypto-js` - Encryption
- `@nestjs/schedule` - Cron jobs
- `@nestjs/throttler` - Rate limiting
- `@nestjs/terminus` - Health checks

**Optional:**
- `@nestjs/cache-manager`, `cache-manager`, `redis` - Caching
- `winston` or `pino` - Logging

### 12.2 Frontend Dependencies

**Core:**
- `next`, `react`, `react-dom` - Framework
- `@tanstack/react-query` - Data fetching
- `axios` - HTTP client
- `tailwindcss` - Styling

**UI Components:**
- `@assistant-ui/react` - Chat interface (initialize with `npx assistant-ui init`)
- `recharts` or `chart.js` - Charts
- `@headlessui/react` - Unstyled components
- `react-hook-form` - Forms
- `zod` - Validation

**Utilities:**
- `date-fns` or `dayjs` - Date formatting
- `clsx` - Class names

### 12.3 External API Requirements

#### 1. Anthropic Claude
- **Purpose:** AI chat assistant
- **API Key:** Required (paid service)
- **Model:** `claude-3-5-sonnet-20241022`
- **Pricing:** ~$3/1M input tokens, ~$15/1M output tokens
- **Docs:** https://docs.anthropic.com/

#### 2. Alpaca
- **Purpose:** Brokerage integration
- **API Key:** OAuth client ID/secret
- **Auth:** OAuth 2.0 with PKCE
- **Environment:** Use paper trading for MVP
- **Docs:** https://alpaca.markets/docs/

#### 3. Interactive Brokers (IBKR)
- **Purpose:** Brokerage integration (optional for MVP)
- **API:** Client Portal Gateway (self-hosted)
- **Auth:** Session-based with tickle endpoint
- **Docs:** https://www.interactivebrokers.com/api/doc.html

#### 4. Yahoo Finance
- **Purpose:** Stock quotes, historical prices, news
- **API Key:** Not required (unofficial API)
- **Rate Limit:** None officially
- **Note:** Use with caution, no official support
- **Library:** `yahoo-finance2` (npm)

#### 5. Finnhub
- **Purpose:** Real-time quotes, company data, news
- **API Key:** Required (free tier available)
- **Rate Limit:** 60 calls/min (free), 300/min (paid)
- **Pricing:** Free tier sufficient for MVP
- **Docs:** https://finnhub.io/docs/api

#### 6. SEC EDGAR
- **Purpose:** SEC filings (10-K, 10-Q, 8-K)
- **API Key:** Not required
- **Rate Limit:** 10 requests/second
- **Requirements:** Must include User-Agent header
- **Docs:** https://www.sec.gov/edgar/sec-api-documentation

### 12.4 Environment Variables

**Backend (.env):**
```env
# Database
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=postgres
DATABASE_NAME=jaspers_ai

# JWT
JWT_SECRET=your-super-secret-jwt-key
JWT_EXPIRES_IN=15m
JWT_REFRESH_SECRET=your-refresh-secret
JWT_REFRESH_EXPIRES_IN=7d

# Alpaca
ALPACA_CLIENT_ID=your-client-id
ALPACA_CLIENT_SECRET=your-client-secret
ALPACA_REDIRECT_URI=http://localhost:3001/connect/callback
ALPACA_API_BASE=https://paper-api.alpaca.markets

# IBKR (optional)
IBKR_GATEWAY_URL=https://localhost:5000

# Financial Data
YAHOO_FINANCE_API_KEY=  # Not required
FINNHUB_API_KEY=your-finnhub-key

# AI
ANTHROPIC_API_KEY=your-anthropic-key

# App
PORT=3000
NODE_ENV=development
ENCRYPTION_KEY=your-32-byte-hex-key-for-aes-256

# Frontend URL (for CORS)
FRONTEND_URL=http://localhost:3001
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_URL=http://localhost:3000/api
```

---

## 13. Success Criteria

### 13.1 MVP Launch Criteria

**Functional Requirements:**
- ✅ Users can register and log in
- ✅ Users can connect Alpaca account via OAuth
- ✅ Portfolio syncs within 1 minute of connection
- ✅ Dashboard displays accurate portfolio summary and holdings
- ✅ Chat interface responds to basic questions
- ✅ AI responses include at least 1 citation per response
- ✅ Users can view chat history

**Non-Functional Requirements:**
- ✅ API response time <200ms (p95)
- ✅ Chat response time <5 seconds
- ✅ Mobile-responsive UI
- ✅ No critical security vulnerabilities
- ✅ Test coverage >80%
- ✅ Uptime >99.5%

### 13.2 Key Performance Indicators (KPIs)

**User Activation:**
- Target: 80% of registered users connect at least 1 brokerage
- Measurement: `connected_users / total_users`

**Engagement:**
- Target: Average 5 chat messages per session
- Measurement: `total_messages / total_sessions`

**Sync Reliability:**
- Target: >95% successful portfolio syncs
- Measurement: `successful_syncs / total_syncs`

**Response Quality:**
- Target: 100% of AI responses include citations
- Measurement: `messages_with_citations / total_assistant_messages`

**Performance:**
- Target: API p95 <200ms, Chat p95 <5s
- Measurement: Prometheus metrics

**Cost Efficiency:**
- Target: <$0.10 per chat message (Claude tokens)
- Measurement: `total_costs / total_messages`

### 13.3 Acceptance Tests

**Test 1: End-to-End User Flow**
1. User registers account
2. User connects Alpaca account
3. Portfolio syncs successfully
4. User views dashboard with holdings
5. User asks chat: "What's my top holding?"
6. AI responds with correct answer and citation

**Expected Result:** All steps complete without errors

**Test 2: Multi-Brokerage Aggregation**
1. User connects Alpaca account with AAPL holding
2. User connects IBKR account with AAPL holding
3. Dashboard shows combined AAPL holding
4. Allocation percentages calculated correctly

**Expected Result:** Holdings properly aggregated

**Test 3: Citation Accuracy**
1. User asks: "What's AAPL's current price?"
2. AI fetches quote from Yahoo Finance
3. Response includes price and citation
4. Citation links to data source

**Expected Result:** Citation present and accurate

**Test 4: Error Handling**
1. Disconnect brokerage API (simulate outage)
2. User triggers portfolio sync
3. System shows error message
4. Cached data still displayed
5. Audit log captures error

**Expected Result:** Graceful degradation

---

## 14. Future Enhancements

### Post-MVP Features (Prioritized)

#### Phase 2 Enhancements (3-6 months)
1. **Interactive Brokers Full Integration**
   - Complete IBKR Client Portal API implementation
   - Session management and tickle endpoint
   - Support for international markets

2. **Streaming Responses**
   - Server-Sent Events (SSE) for chat
   - Real-time typing indicators
   - Progressive response rendering

3. **Advanced Portfolio Analytics**
   - Sector/industry allocation
   - Risk metrics (beta, Sharpe ratio)
   - Dividend tracking
   - Tax lot management (FIFO, LIFO)

4. **Real-Time Updates**
   - WebSocket for live portfolio updates
   - Push notifications for price alerts
   - Real-time chat indicators

5. **Enhanced RAG Pipeline**
   - Vector embeddings for filing search
   - Semantic search across historical filings
   - Multi-document synthesis

#### Phase 3 Enhancements (6-12 months)
1. **Trading Capabilities**
   - Place orders through connected brokerages
   - Order confirmation flow
   - Trade history tracking

2. **Collaborative Features**
   - Family accounts (multi-user)
   - Shared portfolios
   - Advisor access

3. **Advanced AI Features**
   - Portfolio recommendations
   - Rebalancing suggestions
   - Tax-loss harvesting identification
   - Automated alerts (earnings, filings)

4. **Billing & Subscriptions**
   - Tiered pricing (free, pro, enterprise)
   - Usage quotas per tier
   - Payment processing (Stripe)

5. **Admin Dashboard**
   - User management
   - Platform analytics
   - Cost monitoring
   - Feature flags

#### Long-Term Vision (12+ months)
- Multi-currency support
- International brokerage integrations (Robinhood, Fidelity, Schwab)
- Mobile apps (iOS, Android)
- API for third-party developers
- Institutional features (wealth management firms)

---

## Appendices

### Appendix A: Glossary

- **RAG:** Retrieval-Augmented Generation - AI technique that fetches relevant data before generating response
- **P&L:** Profit & Loss - Gain or loss on investment
- **CIK:** Central Index Key - SEC identifier for companies
- **EDGAR:** Electronic Data Gathering, Analysis, and Retrieval - SEC filing system
- **10-K:** Annual report filed with SEC
- **10-Q:** Quarterly report filed with SEC
- **8-K:** Current report for major events
- **OAuth:** Open Authorization - Secure third-party access protocol
- **PKCE:** Proof Key for Code Exchange - OAuth security extension
- **JWT:** JSON Web Token - Authentication token format
- **SSE:** Server-Sent Events - Streaming protocol
- **CORS:** Cross-Origin Resource Sharing - Browser security mechanism
- **CSRF:** Cross-Site Request Forgery - Security vulnerability

### Appendix B: References

**Technical Documentation:**
- [NestJS Docs](https://docs.nestjs.com/)
- [Next.js Docs](https://nextjs.org/docs)
- [TypeORM Docs](https://typeorm.io/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Alpaca API](https://alpaca.markets/docs/)
- [SEC EDGAR API](https://www.sec.gov/edgar/sec-api-documentation)

**Best Practices:**
- [REST API Design](https://restfulapi.net/)
- [OAuth 2.0 Security](https://oauth.net/2/)
- [PostgreSQL Performance](https://www.postgresql.org/docs/current/performance-tips.html)

### Appendix C: Change Log

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-07 | Initial PRD | Engineering Team |

---

## Questions & Support

For questions about this PRD, contact the engineering team.

**Last Updated:** November 7, 2025

