# Jaspers AI - Documentation Repository

**Personalized Investment Copilot - Technical Documentation & Assessment Materials**

---

## 📚 Repository Contents

This repository contains comprehensive documentation for building Jaspers AI, an AI-powered investment portfolio assistant.

### Core Documents

| Document | Description | Lines |
|----------|-------------|-------|
| **[PRD.md](./PRD.md)** | Complete Product Requirements Document for engineers | 1,431 |
| **[test.md](./test.md)** | Technical assessment for hiring full-stack engineers | 606 |
| **[apis.md](./apis.md)** | Complete API architecture and endpoint specifications | 370 |
| **[backend-implementation-plan.md](./backend-implementation-plan.md)** | Detailed backend development plan with NestJS | 1,203 |
| **[jaspers-ai-mvp.plan.md](./jaspers-ai-mvp.plan.md)** | MVP implementation roadmap with tech stack | 314 |
| **[jaspers.dbml](./jaspers.dbml)** | Database schema in DBML format (for dbdiagram.io) | 353 |

---

## 🎯 What is Jaspers AI?

Jaspers AI is a personalized investment copilot that:
- 📊 Connects to brokerage accounts (Alpaca, Interactive Brokers)
- 💬 Provides AI-powered chat about your portfolio using Claude
- 📈 Displays real-time portfolio analytics
- 🔍 Cites sources from SEC filings, news, and market data
- 🔒 Securely stores brokerage credentials with encryption

---

## 🏗️ Tech Stack

**Backend:**
- NestJS (TypeScript)
- PostgreSQL with TypeORM
- JWT Authentication
- Anthropic Claude API

**Frontend:**
- Next.js 14+ (App Router)
- React 18+
- Tailwind CSS
- React Query

**Integrations:**
- Alpaca API (OAuth 2.0)
- Yahoo Finance
- Finnhub
- SEC EDGAR

---

## 📖 How to Use This Repository

### For Engineers Building Jaspers AI

1. **Start with [PRD.md](./PRD.md)**
   - Complete product requirements
   - User personas and use cases
   - Technical architecture
   - All API specifications

2. **Follow [backend-implementation-plan.md](./backend-implementation-plan.md)**
   - 11 phases of development
   - Module structure
   - Code examples
   - Testing strategy

3. **Reference [apis.md](./apis.md)**
   - All 60+ API endpoints
   - Request/response examples
   - Business logic
   - Rate limiting rules

4. **Use [jaspers.dbml](./jaspers.dbml)**
   - Complete database schema
   - View at: https://dbdiagram.io/
   - All relationships and indexes

### For Hiring Engineers

Use **[test.md](./test.md)** as the technical assessment:
- 6-8 hour coding challenge
- Tests full-stack skills
- Simplified MVP version
- Clear evaluation criteria

---

## 🚀 Quick Start

To start building Jaspers AI:

```bash
# 1. Clone this repository
git clone <repository-url>
cd jaspers-ai-docs

# 2. Read the PRD
open PRD.md

# 3. Follow the implementation plan
open backend-implementation-plan.md

# 4. View database schema
# Upload jaspers.dbml to https://dbdiagram.io/
```

---

## 📋 Document Summaries

### Product Requirements Document (PRD.md)
Complete specification including:
- Executive summary
- User personas and flows
- 60+ functional requirements
- Database models
- API specifications
- Security requirements
- Implementation timeline
- Success criteria

### Technical Assessment (test.md)
Hiring test covering:
- Simple authentication
- Alpaca API integration
- Portfolio display
- AI chat with Claude
- Evaluation rubric (100 points)

### API Architecture (apis.md)
Comprehensive API docs with:
- Authentication & user management
- Brokerage connections
- Portfolio management
- Financial data integration
- AI chat with RAG pipeline
- Analytics & monitoring

### Backend Plan (backend-implementation-plan.md)
Step-by-step implementation:
- Project structure
- Module breakdown
- Code examples
- Security checklist
- Deployment guide

### MVP Plan (jaspers-ai-mvp.plan.md)
High-level roadmap:
- Tech stack decisions
- 6 implementation phases
- Weekly deliverables
- Success metrics

### Database Schema (jaspers.dbml)
Complete data model:
- 10+ tables
- All relationships
- Indexes and constraints
- DBML format for visualization

---

## 🎓 For Technical Assessments

If you're a candidate who received **test.md**:

1. **Read the entire assessment** (606 lines)
2. **Estimated time:** 6-8 hours
3. **What to build:**
   - User authentication
   - Alpaca portfolio integration
   - Simple AI chat interface
4. **Submit:**
   - GitHub repository
   - Working application
   - Clear README

**Good luck!** 🚀

---

## 📊 Project Status

- ✅ PRD Complete
- ✅ API Documentation Complete
- ✅ Backend Plan Complete
- ✅ Database Schema Complete
- ✅ Technical Assessment Ready
- ⏳ Implementation: Not Started

---

## 🤝 Contributing

This is documentation for building Jaspers AI. To contribute:

1. Fork the repository
2. Make your changes
3. Submit a pull request with clear description

---

## 📞 Contact

For questions or clarifications, please contact:
- Email: [your-email@company.com]
- GitHub Issues: [Link to issues]

---

## 📄 License

[Specify your license here]

---

*Last Updated: November 7, 2025*

