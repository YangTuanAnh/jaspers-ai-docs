# Finnhub API Template - Data Scraping Layer

## Service Overview
**Provider:** Finnhub  
**Purpose:** Stock market data, news, company fundamentals, economic data  
**Base URL:** `https://finnhub.io/api/v1`  
**JavaScript Client:** `npm install finnhub --save`

## Authentication
- **Type:** API Key
- **Parameter:** `token` (query parameter)
- **Note:** Free tier available; premium features require paid subscription

## JavaScript Client Setup

```javascript
const finnhub = require('finnhub');
const finnhubClient = new finnhub.DefaultApi("<API_key>"); // Replace with your API key
```

## Rate Limits
- **Free Tier:** 60 requests per minute
- **Premium Tier:** Higher limits (varies by plan)
- **Window:** Per minute
- **Note:** Many endpoints require premium access

## Key Endpoints

### 1. Stock Quote (Real-time)
**Endpoint:** `GET /quote`

**Purpose:** Get real-time quote for US stocks

**Parameters:**
- `symbol` (required): Stock symbol (e.g., 'AAPL')
- `token` (required): API key

**Response Structure:**
```typescript
{
  c: number;    // Current price
  h: number;    // High price of the day
  l: number;    // Low price of the day
  o: number;    // Open price of the day
  pc: number;   // Previous close price
  t: number;   // Unix timestamp (seconds)
}
```

**Use Case:** Real-time stock quotes

**JavaScript Example:**
```javascript
finnhubClient.quote('AAPL', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 2. Stock Candles (OHLCV)
**Endpoint:** `GET /stock/candle`

**Purpose:** Get candlestick data for stocks

**Parameters:**
- `symbol` (required): Stock symbol
- `resolution` (required): `1, 5, 15, 30, 60, D, W, M` (1=1min, D=daily, etc.)
- `from` (required): UNIX timestamp (seconds)
- `to` (required): UNIX timestamp (seconds)
- `token` (required): API key
- `adjusted` (optional): `true` for adjusted data (default: true)

**Response Structure:**
```typescript
{
  c: number[];  // Close prices
  h: number[];  // High prices
  l: number[];  // Low prices
  o: number[];  // Open prices
  s: string;    // Status: 'ok' | 'no_data'
  t: number[];  // Timestamps (Unix seconds)
  v: number[];  // Volumes
}
```

**Use Case:** Historical price data and charts

**JavaScript Example:**
```javascript
finnhubClient.stockCandles("AAPL", "D", 1590988249, 1591852249, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 3. Company Profile
**Endpoint:** `GET /stock/profile2`

**Purpose:** Get company profile and basic information

**Parameters:**
- `symbol` (required): Stock symbol
- `token` (required): API key

**Response Structure:**
```typescript
{
  country: string;
  currency: string;
  exchange: string;
  finnhubIndustry: string;
  ipo: string;           // IPO date
  logo: string;
  marketCapitalization: number;
  name: string;
  phone: string;
  shareOutstanding: number;
  ticker: string;
  weburl: string;
}
```

**Use Case:** Company information for profiles

**JavaScript Example:**
```javascript
finnhubClient.companyProfile({'symbol': 'AAPL'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});

// Alternative: Using ISIN or CUSIP
finnhubClient.companyProfile({'isin': 'US0378331005'}, (error, data, response) => {
    console.log(data);
});

finnhubClient.companyProfile({'cusip': '037833100'}, (error, data, response) => {
    console.log(data);
});
```

---

### 4. Company News
**Endpoint:** `GET /company-news`

**Purpose:** Get company news

**Parameters:**
- `symbol` (required): Stock symbol
- `from` (required): Start date (YYYY-MM-DD)
- `to` (required): End date (YYYY-MM-DD)
- `token` (required): API key

**Response Structure:**
```typescript
Array<{
  category: string;
  datetime: number;      // Unix timestamp (seconds)
  headline: string;
  id: number;
  image: string;
  related: string;       // Related symbols
  source: string;
  summary: string;
  url: string;
}>;
```

**Use Case:** News aggregation for stocks

**JavaScript Example:**
```javascript
finnhubClient.companyNews("AAPL", "2020-01-01", "2020-05-01", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 5. Market News
**Endpoint:** `GET /news`

**Purpose:** Get general market news

**Parameters:**
- `category` (required): `general, forex, crypto, merger`
- `token` (required): API key
- `minId` (optional): Minimum news ID for pagination

**Response Structure:**
```typescript
Array<{
  category: string;
  datetime: number;
  headline: string;
  id: number;
  image: string;
  related: string;
  source: string;
  summary: string;
  url: string;
}>;
```

**Use Case:** General market news feed

---

### 6. Company Earnings
**Endpoint:** `GET /stock/earnings`

**Purpose:** Get company earnings data

**Parameters:**
- `symbol` (required): Stock symbol
- `token` (required): API key

**Response Structure:**
```typescript
Array<{
  actual: number;
  estimate: number;
  period: string;        // YYYY-MM-DD
  surprise: number;
  surprisePercent: number;
  symbol: string;
}>;
```

**Use Case:** Earnings tracking and analysis

**JavaScript Example:**
```javascript
finnhubClient.companyEarnings("AAPL", {'limit': 10}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 7. Financial Statements
**Endpoint:** `GET /stock/financials-reported`

**Purpose:** Get financial statements as reported

**Parameters:**
- `symbol` (required): Stock symbol
- `freq` (required): `annual` | `quarterly`
- `token` (required): API key

**Response Structure:**
```typescript
{
  symbol: string;
  cik: string;
  data: Array<{
    accessNumber: string;
    symbol: string;
    cik: string;
    year: number;
    quarter: number;
    form: string;
    startDate: string;
    endDate: string;
    filedDate: string;
    acceptedDate: string;
    report: {
      // Financial statement data
      bs?: {...};      // Balance sheet
      ic?: {...};      // Income statement
      cf?: {...};      // Cash flow
    };
  }>;
}
```

**Use Case:** Financial analysis (Premium feature)

**JavaScript Example:**
```javascript
finnhubClient.financials("AAPL", "ic", "annual", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});

// Financials as reported
finnhubClient.financialsReported({"symbol": "AAPL"}, (error, data, response) => {
    console.log(data);
});
```

---

### 8. Company Peers
**Endpoint:** `GET /stock/peers`

**Purpose:** Get peer companies

**Parameters:**
- `symbol` (required): Stock symbol
- `token` (required): API key

**Response Structure:**
```typescript
string[];  // Array of peer symbols
```

**Use Case:** Comparative analysis

---

### 9. Recommendation Trends
**Endpoint:** `GET /stock/recommendation`

**Purpose:** Get analyst recommendation trends

**Parameters:**
- `symbol` (required): Stock symbol
- `token` (required): API key

**Response Structure:**
```typescript
Array<{
  symbol: string;
  date: string;         // YYYY-MM-DD
  strongBuy: number;
  buy: number;
  hold: number;
  sell: number;
  strongSell: number;
}>;
```

**Use Case:** Analyst sentiment tracking

**JavaScript Example:**
```javascript
finnhubClient.recommendationTrends("AAPL", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 10. Price Target
**Endpoint:** `GET /stock/price-target`

**Purpose:** Get analyst price targets (Premium)

**Parameters:**
- `symbol` (required): Stock symbol
- `token` (required): API key

**Response Structure:**
```typescript
{
  symbol: string;
  targetHigh: number;
  targetLow: number;
  targetMean: number;
  targetMedian: number;
  lastUpdated: string;
}
```

**Use Case:** Price target consensus

---

### 11. Insider Transactions
**Endpoint:** `GET /stock/insider-transactions`

**Purpose:** Get insider transactions (Premium)

**Parameters:**
- `symbol` (required): Stock symbol
- `from` (required): Start date (YYYY-MM-DD)
- `to` (required): End date (YYYY-MM-DD)
- `token` (required): API key

**Response Structure:**
```typescript
{
  data: Array<{
    name: string;
    share: number;
    change: number;
    filingDate: string;
    transactionDate: string;
    transactionCode: string;
    transactionPrice: number;
  }>;
}
```

**Use Case:** Insider trading tracking

**JavaScript Example:**
```javascript
finnhubClient.insiderTransactions('AAPL', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 12. Social Sentiment
**Endpoint:** `GET /stock/social-sentiment`

**Purpose:** Get social sentiment from Reddit and Twitter (Premium)

**Parameters:**
- `symbol` (required): Stock symbol
- `token` (required): API key
- `from` (optional): Start date (YYYY-MM-DD)
- `to` (optional): End date (YYYY-MM-DD)

**Response Structure:**
```typescript
{
  reddit: Array<{
    atTime: string;
    mention: number;
    positiveScore: number;
    negativeScore: number;
    positiveMention: number;
    negativeMention: number;
    score: number;
  }>;
  twitter: Array<{
    atTime: string;
    mention: number;
    positiveScore: number;
    negativeScore: number;
    positiveMention: number;
    negativeMention: number;
    score: number;
  }>;
}
```

**Use Case:** Social sentiment analysis

**JavaScript Example:**
```javascript
finnhubClient.socialSentiment('GME', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 13. Stock Splits
**Endpoint:** `GET /stock/split`

**Purpose:** Get stock split history (Premium)

**Parameters:**
- `symbol` (required): Stock symbol
- `from` (required): Start date (YYYY-MM-DD)
- `to` (required): End date (YYYY-MM-DD)
- `token` (required): API key

**Response Structure:**
```typescript
Array<{
  date: string;         // YYYY-MM-DD
  fromFactor: number;
  toFactor: number;
  symbol: string;
}>;
```

**Use Case:** Historical split tracking

**JavaScript Example:**
```javascript
finnhubClient.stockSplits("AAPL", "2000-01-01", "2020-06-15", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 14. Economic Calendar
**Endpoint:** `GET /calendar/economic`

**Purpose:** Get economic calendar (Premium)

**Parameters:**
- `token` (required): API key
- `from` (optional): Start date (YYYY-MM-DD)
- `to` (optional): End date (YYYY-MM-DD)

**Response Structure:**
```typescript
Array<{
  actual: number;
  estimate: number;
  country: string;
  event: string;
  impact: string;        // 'low', 'medium', 'high'
  prev: number;
  time: string;         // HH:mm
  unit: string;
}>;
```

**Use Case:** Economic event tracking

---

### 15. Crypto Candles
**Endpoint:** `GET /crypto/candle`

**Purpose:** Get cryptocurrency candlestick data (Premium)

**Parameters:**
- `symbol` (required): Crypto symbol (e.g., 'BINANCE:BTCUSDT')
- `resolution` (required): `1, 5, 15, 30, 60, D, W, M`
- `from` (required): UNIX timestamp (seconds)
- `to` (required): UNIX timestamp (seconds)
- `token` (required): API key

**Response Structure:**
```typescript
{
  c: number[];  // Close prices
  h: number[];  // High prices
  l: number[];  // Low prices
  o: number[];  // Open prices
  s: string;    // Status
  t: number[];  // Timestamps
  v: number[];  // Volumes
}
```

**Use Case:** Crypto historical data

**JavaScript Example:**
```javascript
finnhubClient.cryptoCandles("BINANCE:BTCUSDT", "D", 1590988249, 1591852249, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 16. Stock Tick Data
**Endpoint:** `GET /stock/tick`

**Purpose:** Get raw tick-level data for high-frequency analysis (Premium)

**Parameters:**
- `symbol` (required): Stock symbol
- `date` (required): Date (YYYY-MM-DD)
- `limit` (required): Number of ticks to return
- `skip` (optional): Number of ticks to skip
- `token` (required): API key

**JavaScript Example:**
```javascript
finnhubClient.stockTick("AAPL", "2020-03-25", 500, 0, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

**Use Case:** High-frequency trading analysis, market microstructure studies

---

### 17. Company Executives
**Endpoint:** `GET /stock/executive`

**Purpose:** Get company executive information

**JavaScript Example:**
```javascript
finnhubClient.companyExecutive("AAPL", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 18. Revenue Estimates
**Endpoint:** `GET /stock/revenue-estimate`

**Purpose:** Get revenue estimates for a company

**JavaScript Example:**
```javascript
finnhubClient.companyRevenueEstimates("AAPL", {}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 19. EPS Estimates
**Endpoint:** `GET /stock/eps-estimate`

**Purpose:** Get earnings per share estimates

**JavaScript Example:**
```javascript
finnhubClient.companyEpsEstimates("AAPL", {}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 20. EBITDA Estimates
**Endpoint:** `GET /stock/ebitda-estimate`

**Purpose:** Get EBITDA estimates

**JavaScript Example:**
```javascript
finnhubClient.companyEbitdaEstimates("AAPL", {"freq": "annual"}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 21. EBIT Estimates
**Endpoint:** `GET /stock/ebit-estimate`

**Purpose:** Get EBIT estimates

**JavaScript Example:**
```javascript
finnhubClient.companyEbitEstimates("AAPL", {"freq": "annual"}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 22. Basic Financials
**Endpoint:** `GET /stock/metric`

**Purpose:** Get basic financial metrics (e.g., margins)

**JavaScript Example:**
```javascript
finnhubClient.companyBasicFinancials("AAPL", "margin", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 23. Upgrade/Downgrade
**Endpoint:** `GET /stock/upgrade-downgrade`

**Purpose:** Get analyst upgrade and downgrade history

**JavaScript Example:**
```javascript
finnhubClient.upgradeDowngrade({"symbol": "AAPL"}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 24. Stock Dividends
**Endpoint:** `GET /stock/dividend`

**Purpose:** Get historical dividend data

**JavaScript Example:**
```javascript
finnhubClient.stockDividends("KO", "2019-01-01", "2020-06-30", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 25. Earnings Calendar
**Endpoint:** `GET /calendar/earnings`

**Purpose:** Get earnings calendar for a date range

**JavaScript Example:**
```javascript
finnhubClient.earningsCalendar({"from": "2020-06-01", "to": "2020-06-30"}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 26. Technical Indicators
**Endpoint:** `GET /indicator`

**Purpose:** Calculate technical indicators (e.g., MACD, RSI)

**JavaScript Example:**
```javascript
finnhubClient.technicalIndicator("AAPL", "D", 1580988249, 1591852249, "macd", {}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 27. Aggregate Indicator
**Endpoint:** `GET /stock/aggregate-indicator`

**Purpose:** Get aggregate technical indicator data

**JavaScript Example:**
```javascript
finnhubClient.aggregateIndicator("AAPL", "D", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 28. Support and Resistance
**Endpoint:** `GET /scan/support-resistance`

**Purpose:** Calculate support and resistance levels

**JavaScript Example:**
```javascript
finnhubClient.supportResistance("AAPL", "D", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 29. Forex Candles
**Endpoint:** `GET /forex/candle`

**Purpose:** Get forex candlestick data

**JavaScript Example:**
```javascript
finnhubClient.forexCandles("OANDA:EUR_USD", "D", 1590988249, 1591852249, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 30. Company ESG Score
**Endpoint:** `GET /stock/esg-score`

**Purpose:** Get ESG (Environmental, Social, Governance) scores

**JavaScript Example:**
```javascript
finnhubClient.companyEsgScore('AAPL', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 31. Earnings Quality Score
**Endpoint:** `GET /stock/earnings-quality`

**Purpose:** Get earnings quality score

**JavaScript Example:**
```javascript
finnhubClient.companyEarningsQualityScore('AAPL', 'quarterly', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 32. Revenue Breakdown
**Endpoint:** `GET /stock/revenue-breakdown`

**Purpose:** Get revenue breakdown by segment/product

**JavaScript Example:**
```javascript
finnhubClient.revenueBreakdown({'symbol': 'AAPL'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 33. Supply Chain Relationships
**Endpoint:** `GET /stock/supply-chain`

**Purpose:** Get supply chain relationships

**JavaScript Example:**
```javascript
finnhubClient.supplyChainRelationships('AAPL', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 34. USPTO Patents
**Endpoint:** `GET /stock/uspto-patent`

**Purpose:** Get USPTO patent data

**JavaScript Example:**
```javascript
finnhubClient.stockUsptoPatent('NVDA', '2021-01-01', '2021-12-31', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 35. Visa Applications (H1-B)
**Endpoint:** `GET /stock/visa-application`

**Purpose:** Get H1-B visa application data

**JavaScript Example:**
```javascript
finnhubClient.stockVisaApplication('AAPL', '2021-01-01', '2021-12-31', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 36. ETF Profile
**Endpoint:** `GET /etf/profile`

**Purpose:** Get ETF profile information

**JavaScript Example:**
```javascript
finnhubClient.etfsProfile({'symbol': 'SPY'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 37. ETF Holdings
**Endpoint:** `GET /etf/holdings`

**Purpose:** Get ETF holdings

**JavaScript Example:**
```javascript
finnhubClient.etfsHoldings({'symbol': 'ARKK'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 38. ETF Sector Exposure
**Endpoint:** `GET /etf/sector-exposure`

**Purpose:** Get ETF sector exposure

**JavaScript Example:**
```javascript
finnhubClient.etfsSectorExposure('SPY', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 39. ETF Country Exposure
**Endpoint:** `GET /etf/country-exposure`

**Purpose:** Get ETF country exposure

**JavaScript Example:**
```javascript
finnhubClient.etfsCountryExposure('SPY', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 40. Mutual Fund Profile
**Endpoint:** `GET /mutual-fund/profile`

**Purpose:** Get mutual fund profile

**JavaScript Example:**
```javascript
finnhubClient.mutualFundProfile({'symbol': 'VTSAX'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 41. Mutual Fund Holdings
**Endpoint:** `GET /mutual-fund/holdings`

**Purpose:** Get mutual fund holdings

**JavaScript Example:**
```javascript
finnhubClient.mutualFundHoldings({'symbol': 'VTSAX'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 42. Mutual Fund Sector Exposure
**Endpoint:** `GET /mutual-fund/sector-exposure`

**Purpose:** Get mutual fund sector exposure

**JavaScript Example:**
```javascript
finnhubClient.mutualFundSectorExposure('VTSAX', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 43. Mutual Fund Country Exposure
**Endpoint:** `GET /mutual-fund/country-exposure`

**Purpose:** Get mutual fund country exposure

**JavaScript Example:**
```javascript
finnhubClient.mutualFundCountryExposure('VTSAX', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 44. Index Constituents
**Endpoint:** `GET /index/constituents`

**Purpose:** Get index constituents (e.g., S&P 500)

**JavaScript Example:**
```javascript
finnhubClient.indicesConstituents("^GSPC", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 45. Historical Index Constituents
**Endpoint:** `GET /index/historical-constituents`

**Purpose:** Get historical index constituents

**JavaScript Example:**
```javascript
finnhubClient.indicesHistoricalConstituents("^GSPC", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 46. Earnings Call Transcripts
**Endpoint:** `GET /stock/transcripts`

**Purpose:** Get earnings call transcripts

**JavaScript Example:**
```javascript
// List available transcripts
finnhubClient.transcriptsList("AAPL", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});

// Get specific transcript
finnhubClient.transcripts("AAPL_162777", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 47. Crypto Profile
**Endpoint:** `GET /crypto/profile`

**Purpose:** Get cryptocurrency profile

**JavaScript Example:**
```javascript
finnhubClient.cryptoProfile('BTC', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 48. Crypto Exchanges
**Endpoint:** `GET /crypto/exchange`

**Purpose:** Get list of crypto exchanges

**JavaScript Example:**
```javascript
finnhubClient.cryptoExchanges((error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 49. Crypto Symbols
**Endpoint:** `GET /crypto/symbol`

**Purpose:** Get crypto symbols for an exchange

**JavaScript Example:**
```javascript
finnhubClient.cryptoSymbols("BINANCE", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 50. Stock Symbols
**Endpoint:** `GET /stock/symbol`

**Purpose:** Get list of stock symbols for an exchange

**JavaScript Example:**
```javascript
finnhubClient.stockSymbols("US", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 51. Economic Data
**Endpoint:** `GET /economic`

**Purpose:** Get economic data by code

**JavaScript Example:**
```javascript
finnhubClient.economicData("MA-USA-656880", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 52. Economic Codes
**Endpoint:** `GET /economic/code`

**Purpose:** Get list of economic codes

**JavaScript Example:**
```javascript
finnhubClient.economicCode((error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 53. Investment Themes
**Endpoint:** `GET /stock/investment-theme`

**Purpose:** Get investment theme data

**JavaScript Example:**
```javascript
finnhubClient.investmentThemes('financialExchangesData', (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 54. Company Profile 2
**Endpoint:** `GET /stock/profile`

**Purpose:** Get alternative company profile

**JavaScript Example:**
```javascript
finnhubClient.companyProfile2({'symbol': 'AAPL'}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 55. Ownership Data
**Endpoint:** `GET /stock/ownership`

**Purpose:** Get investor ownership data

**JavaScript Example:**
```javascript
let optsLimit = {'limit': 10};
finnhubClient.ownership("AAPL", optsLimit, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 56. Filings
**Endpoint:** `GET /stock/filings`

**Purpose:** Get company filings

**JavaScript Example:**
```javascript
finnhubClient.filings({"symbol": "AAPL"}, (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 57. Forex Exchanges
**Endpoint:** `GET /forex/exchange`

**Purpose:** Get list of forex exchanges

**JavaScript Example:**
```javascript
finnhubClient.forexExchanges((error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 58. Countries
**Endpoint:** `GET /country`

**Purpose:** Get list of supported countries

**JavaScript Example:**
```javascript
finnhubClient.country((error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

### 59. COVID-19 Data
**Endpoint:** `GET /covid19`

**Purpose:** Get COVID-19 related data

**JavaScript Example:**
```javascript
finnhubClient.covid19((error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

---

## Error Handling

**Common Error Codes:**
- `200`: Success
- `400`: Bad request
- `401`: Unauthorized (invalid API key)
- `429`: Rate limit exceeded
- `500`: Server error

**Error Response:**
```typescript
{
  error?: string;  // Error message
}
```

## Integration Notes

1. **Symbol Format:**
   - US stocks: Standard ticker (e.g., 'AAPL')
   - Crypto: Exchange prefix (e.g., 'BINANCE:BTCUSDT')
   - Forex: Pair format (e.g., 'OANDA:EUR_USD')

2. **Timestamps:**
   - Most endpoints use Unix timestamp in seconds
   - Date parameters use YYYY-MM-DD format

3. **Resolution Codes:**
   - Minutes: `1, 5, 15, 30, 60`
   - Daily: `D`
   - Weekly: `W`
   - Monthly: `M`

4. **Rate Limiting:**
   - Free tier: 60 requests/minute
   - Implement exponential backoff
   - Use job queue with concurrency: 5 workers
   - Cache aggressively (60 seconds for quotes)

5. **Premium Features:**
   - Many advanced features require premium subscription
   - Check subscription level before calling premium endpoints
   - Fallback to free alternatives when possible

6. **Data Adjustments:**
   - Stock candles can be adjusted for splits/dividends
   - Use `adjusted=true` for accurate historical analysis

## Scraping Implementation

```typescript
// Example: Finnhub Stock Scraper
class FinnhubScraper {
  async fetchQuote(symbol: string) {
    // Fetch real-time quote
    // Map to stock_quotes_cache format
  }
  
  async fetchCandles(symbol: string, resolution: string, from: number, to: number) {
    // Fetch historical OHLCV data
    // Parse arrays into time series
  }
  
  async fetchCompanyProfile(symbol: string) {
    // Fetch company information
    // Map to company_profiles_cache
  }
  
  async fetchNews(symbol: string, from: string, to: string) {
    // Fetch company news
    // Parse and deduplicate
  }
  
  async fetchMarketNews(category: string) {
    // Fetch general market news
  }
}
```

## Cache Strategy
- **TTL:** 
  - Quotes: 60 seconds
  - Company profiles: 24 hours
  - News: 5 minutes
  - Candles: 1 hour (for same day)
- **Key Format:** 
  - `finnhub:quote:{symbol}`
  - `finnhub:candles:{symbol}:{resolution}:{from}:{to}`
  - `finnhub:profile:{symbol}`
  - `finnhub:news:{symbol}:{from}:{to}`

## Data Mapping to stock_quotes_cache

```typescript
// Map Finnhub quote to stock_quotes_cache table
const stockQuote = {
  symbol: symbol,
  price: quote.c,
  open: quote.o,
  previous_close: quote.pc,
  change: quote.c - quote.pc,
  change_percent: ((quote.c - quote.pc) / quote.pc) * 100,
  day_high: quote.h,
  day_low: quote.l,
  quote_time: new Date(quote.t * 1000),
  data_source: 'finnhub',
  fetched_at: new Date()
};
```

