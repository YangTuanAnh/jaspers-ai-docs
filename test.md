# Full-Stack Engineer Technical Assessment
# Jaspers AI - Portfolio Chat MVP

**Estimated Time:** 6-8 hours  
**Position:** Full-Stack Engineer  
**Technologies:** TypeScript, Node.js (NestJS or Express), React (Next.js or Vite), PostgreSQL

---

## Overview

Build a minimal working version of **Jaspers AI** - a simple portfolio chat application that:
1. Allows users to register and login
2. Connects to Alpaca API to fetch portfolio holdings
3. Provides an AI chat interface to ask questions about the portfolio

This is a **simplified assessment** focused on core full-stack skills: backend API development, database design, external API integration, and building a functional React frontend.

---

## Project Requirements

### Core Features (Must Have)

#### 1. Simple User Authentication
- User registration with email/password
- Login with JWT tokens
- Password hashing with bcrypt
- Protected API routes
- **Note:** Simple access token only (no refresh token needed)

#### 2. Alpaca Portfolio Integration
- Use Alpaca API with hardcoded API keys (no OAuth required)
- Fetch user's portfolio positions from Alpaca
- Store portfolio holdings in database
- Manual sync button to refresh portfolio data

#### 3. Portfolio Display
- Dashboard showing:
  - Total portfolio value
  - Cash balance
  - List of holdings: symbol, quantity, current price, market value
  - Simple P&L calculation

#### 4. AI Chat Interface
- Simple chat where users can ask questions about their portfolio
- Integrate with Claude API (or OpenAI)
- Pass portfolio data as context to the LLM
- Display chat history
- **No RAG pipeline required** - just send portfolio data with each message

---

## Technical Requirements

### Backend

**Framework:** Your choice (NestJS, Express, Fastify)

**Database:** PostgreSQL

**Required Tables:**
```sql
users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
)

portfolio_holdings (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  symbol VARCHAR(20) NOT NULL,
  quantity DECIMAL(20,8) NOT NULL,
  average_cost DECIMAL(20,4),
  current_price DECIMAL(20,4),
  market_value DECIMAL(20,4),
  updated_at TIMESTAMP DEFAULT NOW()
)

chat_messages (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  role VARCHAR(20) NOT NULL, -- 'user' or 'assistant'
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
)
```

**Required API Endpoints:**
```
POST   /api/auth/register       - Register new user
POST   /api/auth/login          - Login, return JWT
GET    /api/auth/me             - Get current user (protected)

GET    /api/portfolio           - Get portfolio holdings
POST   /api/portfolio/sync      - Sync from Alpaca API

GET    /api/chat/messages       - Get chat history
POST   /api/chat/messages       - Send message, get AI response
```

**External APIs:**
- **Alpaca API:** Use API key authentication (not OAuth)
  - `GET /v2/account` - Get account info
  - `GET /v2/positions` - Get holdings
  - Base URL: `https://paper-api.alpaca.markets`
  
- **Claude API:** Or OpenAI if you prefer
  - Just send portfolio context with each message
  - No tool calling required

### Frontend

**Framework:** React (Next.js, Vite, or Create React App)

**Required Pages:**

1. **Login/Register Page** (`/auth`)
   - Email/password forms
   - Basic validation

2. **Portfolio Dashboard** (`/dashboard`)
   - Summary: total value, cash balance
   - Holdings table: symbol, quantity, price, value
   - "Sync Portfolio" button

3. **Chat Page** (`/chat`)
   - Message history (user/AI bubbles)
   - Input field to send messages
   - Loading indicator

**Styling:** Any CSS framework or plain CSS (not evaluated heavily)

---

## Detailed Implementation Guide

### 1. Authentication

**Registration:**
```typescript
POST /api/auth/register
{
  "email": "user@example.com",
  "password": "SecurePass123"
}

Response 201:
{
  "user": {
    "id": 1,
    "email": "user@example.com"
  },
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

**Login:**
```typescript
POST /api/auth/login
{
  "email": "user@example.com",
  "password": "SecurePass123"
}

Response 200:
{
  "user": { "id": 1, "email": "user@example.com" },
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

**Implementation:**
- Hash passwords with bcrypt (10 rounds)
- Sign JWT with secret from environment variable
- Token expiry: 24 hours is fine
- Middleware to verify JWT on protected routes

### 2. Alpaca Integration

**Get Portfolio:**
```typescript
// Call Alpaca API
const response = await axios.get('https://paper-api.alpaca.markets/v2/positions', {
  headers: {
    'APCA-API-KEY-ID': process.env.ALPACA_API_KEY,
    'APCA-API-SECRET-KEY': process.env.ALPACA_SECRET_KEY
  }
});

// Parse and store in database
const holdings = response.data.map(position => ({
  symbol: position.symbol,
  quantity: position.qty,
  average_cost: position.avg_entry_price,
  current_price: position.current_price,
  market_value: position.market_value
}));

// Save to database (upsert by symbol)
```

**API Response:**
```typescript
GET /api/portfolio
Response 200:
{
  "summary": {
    "totalValue": 25430.50,
    "cashBalance": 5430.50,
    "investedValue": 20000.00
  },
  "holdings": [
    {
      "symbol": "AAPL",
      "quantity": 10,
      "averageCost": 150.00,
      "currentPrice": 175.50,
      "marketValue": 1755.00
    }
  ]
}
```

### 3. AI Chat

**Simple Implementation:**
```typescript
POST /api/chat/messages
{
  "message": "What's my biggest holding?"
}

// Backend logic:
1. Get user's portfolio from database
2. Build simple context:
   const context = `
   User's Portfolio:
   - AAPL: 10 shares, value $1,755
   - TSLA: 5 shares, value $1,200
   - Cash: $5,430
   Total: $25,430
   
   User question: ${userMessage}
   
   Answer the question based on the portfolio data above.
   `;

3. Call Claude/OpenAI:
   const aiResponse = await anthropic.messages.create({
     model: 'claude-3-5-sonnet-20241022',
     max_tokens: 500,
     messages: [{
       role: 'user',
       content: context
     }]
   });

4. Save both messages to database
5. Return AI response

Response 200:
{
  "userMessage": { /* saved message */ },
  "aiMessage": {
    "id": 123,
    "role": "assistant",
    "content": "Your biggest holding is AAPL with $1,755 (69% of portfolio).",
    "createdAt": "2024-11-07T10:30:00Z"
  }
}
```

**No complex RAG needed** - just concatenate portfolio data and user question.

---

## Environment Setup

### 1. Get Alpaca API Keys
1. Sign up at https://alpaca.markets/
2. Navigate to **Paper Trading**
3. Generate **API Key** and **Secret Key**
4. Test:
   ```bash
   curl "https://paper-api.alpaca.markets/v2/account" \
     -H "APCA-API-KEY-ID: YOUR_KEY" \
     -H "APCA-API-SECRET-KEY: YOUR_SECRET"
   ```

### 2. Get Claude API Key
1. Visit https://console.anthropic.com/
2. Create API key
3. Or use OpenAI: https://platform.openai.com/

### 3. Setup PostgreSQL
```bash
# Using Docker
docker run --name postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=jaspers_test \
  -p 5432:5432 -d postgres:15
```

### 4. Environment Variables
```env
# Backend .env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/jaspers_test

JWT_SECRET=your-secret-key-at-least-32-characters

ALPACA_API_KEY=your-alpaca-key
ALPACA_SECRET_KEY=your-alpaca-secret
ALPACA_BASE_URL=https://paper-api.alpaca.markets

ANTHROPIC_API_KEY=your-claude-key
# OR
OPENAI_API_KEY=your-openai-key

PORT=3000
```

---

## Project Structure

### Backend (Example with NestJS)
```
backend/
├── src/
│   ├── auth/
│   │   ├── auth.controller.ts
│   │   ├── auth.service.ts
│   │   └── jwt.strategy.ts
│   ├── portfolio/
│   │   ├── portfolio.controller.ts
│   │   └── portfolio.service.ts
│   ├── chat/
│   │   ├── chat.controller.ts
│   │   └── chat.service.ts
│   ├── database/
│   │   └── entities/
│   └── main.ts
├── .env
└── package.json
```

### Frontend (Example with Next.js)
```
frontend/
├── app/
│   ├── auth/
│   │   ├── login/page.tsx
│   │   └── register/page.tsx
│   ├── dashboard/page.tsx
│   └── chat/page.tsx
├── components/
│   ├── HoldingsTable.tsx
│   └── ChatInterface.tsx
└── lib/
    └── api.ts
```

---

## Deliverables

### 1. Code Repository
- Git repository (GitHub, GitLab)
- Clean, readable TypeScript code
- `.gitignore` (no node_modules, .env)
- Basic error handling

### 2. Documentation (README.md)
**Must include:**
- Project description
- Prerequisites (Node.js, PostgreSQL)
- Installation instructions:
  ```bash
  # Backend
  cd backend
  npm install
  cp .env.example .env
  # Edit .env with your keys
  npm run start
  
  # Frontend
  cd frontend
  npm install
  npm run dev
  ```
- Environment variables template
- API endpoints list
- How to create database tables

### 3. Working Application
- Backend running on `http://localhost:3000`
- Frontend running on `http://localhost:3001`
- All features working end-to-end

### 4. Database Setup
- SQL script to create tables
- OR migration files
- OR instructions to run migrations

---

## Evaluation Criteria

### Functionality (50%)
- ✅ User can register and login (10%)
- ✅ Portfolio syncs from Alpaca API (15%)
- ✅ Dashboard displays portfolio correctly (10%)
- ✅ Chat sends messages and gets AI responses (10%)
- ✅ AI answers are relevant to portfolio (5%)

### Code Quality (25%)
- ✅ Clean, organized code (8%)
- ✅ Proper TypeScript usage (7%)
- ✅ Error handling (5%)
- ✅ No major security issues (5%)

### Architecture (15%)
- ✅ Logical project structure (5%)
- ✅ Proper separation of concerns (5%)
- ✅ RESTful API design (5%)

### Documentation (10%)
- ✅ Clear README with setup instructions (7%)
- ✅ Code comments where needed (3%)

### Bonus Points (+10%)
- 🌟 Docker Compose for database (+2%)
- 🌟 Input validation (+2%)
- 🌟 Unit tests (+3%)
- 🌟 Clean, polished UI (+3%)

**Minimum Pass: 70/100**

---

## Submission

### Timeline
- **Deadline:** [Specify: typically 5-7 days from assignment]
- **Estimated effort:** 6-8 hours

### How to Submit
1. Push code to **public** GitHub repository
2. Email submission to: [your-email@company.com]
3. Include:
   - Repository URL
   - Your name and email
   - Time spent
   - Any notes or assumptions

**Email Subject:** `Technical Assessment - [Your Name]`

### Pre-Submission Checklist
- [ ] Code runs without errors
- [ ] User can register and login
- [ ] Portfolio syncs from Alpaca
- [ ] Chat responds with AI answers
- [ ] README has complete setup instructions
- [ ] No API keys committed to repo
- [ ] Database schema included

---

## Tips for Success

### Do's ✅
- **Start simple:** Get authentication working first
- **Test as you go:** Make sure each feature works before moving on
- **Focus on functionality:** Working code > perfect code
- **Document clearly:** Write setup instructions as you build
- **Commit frequently:** Clear commit messages
- **Handle errors:** At least basic try-catch blocks

### Don'ts ❌
- **Don't over-engineer:** Keep it simple
- **Don't skip error handling:** At least handle API failures
- **Don't commit secrets:** Use environment variables
- **Don't submit broken code:** Test everything before submitting
- **Don't spend too long on UI:** Functionality over design

### Priority Order
1. **Authentication** (2 hours)
   - Register/login endpoints
   - JWT generation
   - Frontend auth forms

2. **Alpaca Integration** (2 hours)
   - Call Alpaca API
   - Parse and store holdings
   - Portfolio endpoint

3. **Portfolio Dashboard** (1.5 hours)
   - Display holdings table
   - Show summary stats
   - Sync button

4. **Chat Interface** (2.5 hours)
   - Chat UI
   - Call Claude/OpenAI with context
   - Save messages to database
   - Display chat history

5. **Polish** (30 min)
   - Error messages
   - Loading states
   - README

---

## Example Chat Interactions

Your AI should handle basic questions like:

**User:** "What stocks do I own?"  
**AI:** "You own 3 stocks: AAPL (10 shares), TSLA (5 shares), and GOOGL (8 shares)."

**User:** "What's my biggest holding?"  
**AI:** "Your biggest holding is AAPL with a market value of $1,755, which is 69% of your portfolio."

**User:** "How much cash do I have?"  
**AI:** "You have $5,430.50 in cash."

**User:** "What's my total portfolio value?"  
**AI:** "Your total portfolio value is $25,430.50."

---

## Technical Resources

- **Alpaca API:** https://alpaca.markets/docs/api-references/trading-api/
- **Claude API:** https://docs.anthropic.com/
- **OpenAI API:** https://platform.openai.com/docs/guides/text-generation
- **NestJS:** https://docs.nestjs.com/ (if using)
- **Next.js:** https://nextjs.org/docs (if using)

---

## FAQ

**Q: Can I use Express instead of NestJS?**  
A: Yes, any Node.js framework is fine.

**Q: Can I use OpenAI instead of Claude?**  
A: Yes, either LLM is acceptable.

**Q: Do I need OAuth for Alpaca?**  
A: No, just use API key authentication (simpler).

**Q: How should I handle database setup?**  
A: Provide SQL script or migration instructions in README.

**Q: Do I need to deploy the app?**  
A: No, it should run locally following your README.

**Q: What if I can't finish everything?**  
A: Submit what you have. Working partial solution > broken complete code.

---

## What We're Looking For

**Technical Skills:**
- Ability to integrate external APIs
- Database design and queries
- Backend API development
- Frontend React skills
- TypeScript proficiency

**Problem Solving:**
- Logical approach to requirements
- Handling edge cases
- Basic error handling

**Code Quality:**
- Clean, readable code
- Organized project structure
- Clear variable/function names

**Communication:**
- Clear documentation
- Code comments where helpful
- Ability to explain decisions

---

## Good Luck! 🚀

This is a straightforward assessment focused on core full-stack skills. Keep it simple, make sure it works, and document clearly.

Remember: **Functionality > Perfection**

We're excited to see what you build!

---

*Assessment Version: 2.0 (Simplified)*  
*Last Updated: November 7, 2025*
