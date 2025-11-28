# Data Scraping Layer API Templates

This directory contains API templates for each service used in the SOPHIA data scraping layer. Each template provides:

- Service overview and authentication
- Rate limits and constraints
- Key endpoints with request/response structures
- Error handling patterns
- Integration notes
- Scraping implementation examples
- Cache strategies
- Data mapping to database entities

## Available Templates

### Stock Market Data

1. **[Alpaca API Template](./alpaca_api_template.md)**
   - **Purpose:** Stock and crypto market data, portfolio positions
   - **Key Features:** Historical bars, real-time quotes, account sync, options data
   - **Rate Limit:** Varies by subscription tier
   - **Use Cases:** Stock quotes, historical data, portfolio sync

2. **[Yahoo Finance API Template](./yahoo_finance_api_template.md)**
   - **Purpose:** Stock market data, quotes, historical data, company information
   - **Key Features:** Quote summary, historical OHLCV, company profiles, options chains
   - **Rate Limit:** ~100 requests/minute (recommended)
   - **Use Cases:** Stock quotes, company profiles, historical charts

3. **[Finnhub API Template](./finnhub_api_template.md)**
   - **Purpose:** Stock market data, news, company fundamentals, economic data
   - **Key Features:** Real-time quotes, candles, company news, earnings, financials
   - **Rate Limit:** 60 requests/minute (free tier)
   - **Use Cases:** Stock quotes, news aggregation, fundamental data

### Cryptocurrency Market Data

4. **[CoinGecko API Template](./coingecko_api_template.md)**
   - **Purpose:** Cryptocurrency market data, prices, market caps, historical data
   - **Key Features:** Market data, historical charts, NFT data, on-chain token data
   - **Rate Limit:** 10-50 requests/minute (free tier)
   - **Use Cases:** Crypto quotes, historical data, market analysis

5. **[Binance API Template](./binance_api_template.md)**
   - **Purpose:** Cryptocurrency market data, prices, order books, portfolio sync
   - **Key Features:** 24hr ticker, klines, order book, account sync, WebSocket streams
   - **Rate Limit:** 1200 requests/minute (weight-based)
   - **Use Cases:** Crypto quotes, real-time data, portfolio sync

6. **[Coinbase API Template](./coinbase_api_template.md)**
   - **Purpose:** Cryptocurrency market data, prices, portfolio sync
   - **Key Features:** Product ticker, candles, order book, account sync, WebSocket
   - **Rate Limit:** Varies by endpoint
   - **Use Cases:** Crypto quotes, portfolio sync

### SEC Filings & Company Data

7. **[SEC EDGAR API Template](./sec_edgar_api_template.md)**
   - **Purpose:** SEC filings, company data, insider trading, ownership data
   - **Key Features:** Filing search, insider trading, 13F/13D holdings, executive compensation
   - **Rate Limit:** Varies by subscription tier
   - **Use Cases:** SEC filings, insider trading tracking, institutional holdings

### On-Chain Data

8. **[Etherscan API Template](./etherscan_api_template.md)**
   - **Purpose:** Ethereum blockchain data, on-chain metrics, token data
   - **Key Features:** Token transfers, event logs, gas oracle, network statistics
   - **Rate Limit:** 5 requests/second (free tier)
   - **Use Cases:** On-chain metrics, wallet tracking, token transfers

9. **[Glassnode API Template](./glassnode_api_template.md)**
   - **Purpose:** On-chain analytics and blockchain metrics
   - **Key Features:** NUPL, MVRV, SOPR indicators, market data, options analytics, mining metrics
   - **Rate Limit:** Varies by subscription tier
   - **Use Cases:** On-chain analytics, market sentiment, mining health, options flow

## Services Needing Documentation

The following services are mentioned in the PRD but don't have documentation files yet. Templates should be created when documentation becomes available:

### Stock Market Data
- **Polygon.io** - Stock market data provider

### Cryptocurrency Data
- **CoinMarketCap** - Cryptocurrency market data

### News Services
- **CryptoPanic** - Cryptocurrency news aggregation
- **NewsAPI** - General news API

### On-Chain Services
- **Blockchain.com** - Bitcoin blockchain data
- **Solscan** - Solana blockchain explorer

## Template Structure

Each template follows this structure:

1. **Service Overview** - Provider, purpose, base URL
2. **Authentication** - Auth type and requirements
3. **Rate Limits** - Limits and windows
4. **Key Endpoints** - Detailed endpoint documentation with:
   - Purpose
   - Parameters
   - Request structure
   - Response structure
   - Use cases
5. **Error Handling** - Common errors and handling patterns
6. **Integration Notes** - Implementation considerations
7. **Scraping Implementation** - Example code structure
8. **Cache Strategy** - TTL and key formats
9. **Data Mapping** - Mapping to database entities

## Usage

These templates serve as:

1. **Implementation Guides** - For developers building scrapers
2. **API Reference** - Quick lookup for endpoints and parameters
3. **Integration Documentation** - Notes on rate limiting, caching, error handling
4. **Data Mapping Reference** - How to map API responses to database entities

## Next Steps

1. Implement scrapers based on these templates
2. Create templates for missing services when documentation is available
3. Update templates as APIs evolve
4. Add service-specific error handling and retry logic
5. Implement rate limiting per service
6. Set up monitoring and alerting for API health

