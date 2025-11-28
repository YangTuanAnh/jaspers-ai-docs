# Yahoo Finance API Template - Data Scraping Layer

## Service Overview
**Provider:** Yahoo Finance (via yahoo-finance2 library)  
**Purpose:** Stock market data, quotes, historical data, company information  
**Base URL:** N/A (uses yahoo-finance2 npm package)

## Authentication
- **Type:** None required (public data)
- **Note:** Uses unofficial Yahoo Finance API via yahoo-finance2 library

## Rate Limits
- **Limit:** ~100 requests per minute (recommended)
- **Window:** Per minute
- **Note:** No official rate limits; be respectful to avoid IP blocking

## Key Endpoints (via yahoo-finance2)

### 1. Quote Summary
**Method:** `yahooFinance.quoteSummary(symbol, options)`

**Purpose:** Get comprehensive quote data with multiple modules

**Parameters:**
- `symbol` (required): Stock symbol (e.g., 'AAPL')
- `options` (optional): Object with `modules` array

**Available Modules:**
- `price`: Current price and market data
- `summaryDetail`: Trading details
- `assetProfile`: Company profile
- `financialData`: Financial metrics
- `defaultKeyStatistics`: Key statistics
- `calendarEvents`: Earnings and events
- `secFilings`: SEC filings list
- `upgradeDowngradeHistory`: Analyst actions
- `institutionOwnership`: Institutional ownership
- `fundOwnership`: Fund ownership
- `majorDirectHolders`: Major holders
- `majorHoldersBreakdown`: Holder breakdown
- `insiderTransactions`: Insider transactions
- `insiderHolders`: Insider holders
- `netSharePurchaseActivity`: Share purchase activity
- `earnings`: Earnings data
- `earningsHistory`: Earnings history
- `earningsTrend`: Earnings trend
- `industryTrend`: Industry trend
- `indexTrend`: Index trend
- `sectorTrend`: Sector trend

**Response Structure:**
```typescript
{
  price: {
    regularMarketPrice: number;
    regularMarketChange: number;
    regularMarketChangePercent: number;
    regularMarketTime: Date;
    regularMarketDayHigh: number;
    regularMarketDayLow: number;
    regularMarketVolume: number;
    regularMarketPreviousClose: number;
    marketState: string;
    exchange: string;
    quoteType: string;
    symbol: string;
    currency: string;
    // ... many more fields
  };
  summaryDetail: {
    previousClose: number;
    open: number;
    dayLow: number;
    dayHigh: number;
    regularMarketPreviousClose: number;
    regularMarketOpen: number;
    regularMarketDayLow: number;
    regularMarketDayHigh: number;
    dividendRate: number;
    dividendYield: number;
    exDividendDate: Date;
    payoutRatio: number;
    beta: number;
    trailingPE: number;
    forwardPE: number;
    volume: number;
    averageVolume: number;
    averageVolume10days: number;
    averageDailyVolume10Day: number;
    bid: number;
    ask: number;
    bidSize: number;
    askSize: number;
    marketCap: number;
    // ... more fields
  };
  assetProfile: {
    address1: string;
    city: string;
    state: string;
    zip: string;
    country: string;
    phone: string;
    website: string;
    industry: string;
    sector: string;
    longBusinessSummary: string;
    fullTimeEmployees: number;
    companyOfficers: Array<{
      name: string;
      title: string;
      yearBorn: number;
      fiscalYear: number;
      totalPay: number;
    }>;
    // ... more fields
  };
  // ... other modules
}
```

**Use Case:** Comprehensive stock data in single call

---

### 2. Quote (Simple)
**Method:** `yahooFinance.quote(symbol)`

**Purpose:** Get basic quote data

**Parameters:**
- `symbol` (required): Stock symbol

**Response Structure:**
```typescript
{
  regularMarketPrice: number;
  regularMarketChange: number;
  regularMarketChangePercent: number;
  regularMarketTime: Date;
  regularMarketDayHigh: number;
  regularMarketDayLow: number;
  regularMarketVolume: number;
  regularMarketPreviousClose: number;
  marketState: string;
  exchange: string;
  quoteType: string;
  symbol: string;
  currency: string;
  longName: string;
  shortName: string;
  // ... more fields
}
```

**Use Case:** Quick price lookup

---

### 3. Historical Data
**Method:** `yahooFinance.historical(symbol, options)`

**Purpose:** Get historical OHLCV data

**Parameters:**
- `symbol` (required): Stock symbol
- `options` (optional): Object with:
  - `period1`: Start date (Date or string)
  - `period2`: End date (Date or string, default: now)
  - `interval`: `1d, 1wk, 1mo` (default: `1d`)
  - `events`: `history, dividend, split` (default: `history`)

**Response Structure:**
```typescript
Array<{
  date: Date;
  open: number;
  high: number;
  low: number;
  close: number;
  adjClose: number;  // Adjusted for splits/dividends
  volume: number;
}>;
```

**Use Case:** Historical price charts and analysis

---

### 4. Search
**Method:** `yahooFinance.search(query, options)`

**Purpose:** Search for symbols

**Parameters:**
- `query` (required): Search query (symbol or company name)
- `options` (optional): Search options

**Response Structure:**
```typescript
{
  Result: Array<{
    symbol: string;
    shortname: string;
    longname: string;
    typeDisp: string;
    isYahooFinance: boolean;
    exch: string;
    exchDisp: string;
  }>;
}
```

**Use Case:** Symbol lookup and validation

---

### 5. Options Chain
**Method:** `yahooFinance.options(symbol, options)`

**Purpose:** Get options chain data

**Parameters:**
- `symbol` (required): Stock symbol
- `options` (optional): Object with `date` (expiration date)

**Response Structure:**
```typescript
{
  expirationDates: number[];
  strikes: number[];
  hasMiniOptions: boolean;
  quote: {
    // Current quote data
  };
  options: Array<{
    expirationDate: number;
    hasMiniOptions: boolean;
    calls: Array<{
      contractSymbol: string;
      strike: number;
      currency: string;
      lastPrice: number;
      change: number;
      percentChange: number;
      volume: number;
      openInterest: number;
      bid: number;
      ask: number;
      contractSize: string;
      expiration: number;
      lastTradeDate: number;
      impliedVolatility: number;
      inTheMoney: boolean;
    }>;
    puts: Array<{
      // Same structure as calls
    }>;
  }>;
}
```

**Use Case:** Options data for advanced analysis

---

### 6. Recommendations
**Method:** `yahooFinance.recommendationsBySymbol(symbol)`

**Purpose:** Get analyst recommendations

**Parameters:**
- `symbol` (required): Stock symbol

**Response Structure:**
```typescript
Array<{
  symbol: string;
  recommendedSymbol: string;
  score: number;
  numberOfAnalysts: number;
}>;
```

**Use Case:** Analyst sentiment tracking

---

### 7. Trending
**Method:** `yahooFinance.trendingSymbols(country)`

**Purpose:** Get trending symbols

**Parameters:**
- `country` (optional): Country code (default: 'US')

**Response Structure:**
```typescript
Array<{
  symbol: string;
  quoteType: string;
  shortName: string;
  longName: string;
  // ... more fields
}>;
```

**Use Case:** Trending stocks discovery

---

## Error Handling

**Common Errors:**
- `FailedYahooValidationError`: Data validation failed (partial data may be available)
- `HTTPError`: Network or HTTP error
- `Error`: Generic error

**Error Handling:**
```typescript
try {
  const result = await yahooFinance.quote(symbol);
} catch (error) {
  if (error instanceof yahooFinance.errors.FailedYahooValidationError) {
    // Partial data available in error.result
  } else if (error instanceof yahooFinance.errors.HTTPError) {
    // HTTP error - retry or skip
  }
}
```

## Integration Notes

1. **Library Usage:**
   - Install: `npm install yahoo-finance2`
   - Import: `import YahooFinance from 'yahoo-finance2'`
   - Instantiate: `const yahooFinance = new YahooFinance()`

2. **Symbol Format:**
   - US stocks: Standard ticker (e.g., 'AAPL')
   - International: May include exchange suffix
   - ETFs: Standard ticker format

3. **Date Handling:**
   - Dates returned as Date objects
   - Use Date objects for period1/period2
   - Historical data dates are Date objects

4. **Rate Limiting:**
   - No official limits
   - Recommended: 100 requests/minute
   - Implement delays between requests
   - Use job queue with concurrency: 5-10 workers

5. **Data Validation:**
   - Library validates responses by default
   - Can disable validation for experimental features
   - Validation errors may contain partial data

6. **Caching:**
   - Yahoo Finance data changes frequently
   - Cache quotes for 60 seconds
   - Cache profiles for 24 hours
   - Historical data is immutable (cache longer)

7. **Concurrency:**
   - Library has internal concurrency limit
   - Configure: `new YahooFinance({ queue: { concurrency: 8 } })`
   - Default concurrency: reasonable for most use cases

## Scraping Implementation

```typescript
// Example: Yahoo Finance Stock Scraper
import YahooFinance from 'yahoo-finance2';

class YahooFinanceScraper {
  private yahooFinance: YahooFinance;
  
  constructor() {
    this.yahooFinance = new YahooFinance({
      queue: { concurrency: 8 },  // Control concurrency
      validation: { 
        logErrors: false  // Disable verbose error logging
      }
    });
  }
  
  async fetchQuote(symbol: string) {
    try {
      const quote = await this.yahooFinance.quote(symbol);
      return this.mapToStockQuote(quote);
    } catch (error) {
      // Handle errors
      throw error;
    }
  }
  
  async fetchQuoteSummary(symbol: string, modules?: string[]) {
    try {
      const summary = await this.yahooFinance.quoteSummary(symbol, {
        modules: modules || ['price', 'summaryDetail', 'assetProfile']
      });
      return summary;
    } catch (error) {
      throw error;
    }
  }
  
  async fetchHistorical(symbol: string, startDate: Date, endDate: Date, interval: string = '1d') {
    try {
      const history = await this.yahooFinance.historical(symbol, {
        period1: startDate,
        period2: endDate,
        interval: interval
      });
      return history;
    } catch (error) {
      throw error;
    }
  }
  
  async searchSymbols(query: string) {
    try {
      const results = await this.yahooFinance.search(query);
      return results.Result;
    } catch (error) {
      throw error;
    }
  }
  
  private mapToStockQuote(quote: any) {
    return {
      symbol: quote.symbol,
      price: quote.regularMarketPrice,
      change: quote.regularMarketChange,
      change_percent: quote.regularMarketChangePercent,
      volume: quote.regularMarketVolume,
      day_high: quote.regularMarketDayHigh,
      day_low: quote.regularMarketDayLow,
      previous_close: quote.regularMarketPreviousClose,
      market_state: quote.marketState,
      exchange: quote.exchange,
      quote_time: quote.regularMarketTime,
      data_source: 'yahoo_finance',
      fetched_at: new Date()
    };
  }
}
```

## Cache Strategy
- **TTL:** 
  - Quotes: 60 seconds
  - Quote summary: 60 seconds
  - Company profiles: 24 hours
  - Historical data: 1 hour (for same day), 24 hours (for past dates)
  - Options: 5 minutes
- **Key Format:** 
  - `yahoo:quote:{symbol}`
  - `yahoo:summary:{symbol}:{modules}`
  - `yahoo:historical:{symbol}:{interval}:{startDate}:{endDate}`
  - `yahoo:profile:{symbol}`

## Data Mapping to stock_quotes_cache

```typescript
// Map Yahoo Finance quote to stock_quotes_cache table
const stockQuote = {
  symbol: quote.symbol,
  name: quote.longName || quote.shortName,
  exchange: quote.exchange,
  price: quote.regularMarketPrice,
  open: quote.regularMarketOpen,
  previous_close: quote.regularMarketPreviousClose,
  change: quote.regularMarketChange,
  change_percent: quote.regularMarketChangePercent,
  day_high: quote.regularMarketDayHigh,
  day_low: quote.regularMarketDayLow,
  volume: quote.regularMarketVolume,
  avg_volume: quote.averageDailyVolume10Day,
  market_cap: quote.marketCap,
  pe_ratio: quote.trailingPE,
  dividend_yield: quote.dividendYield,
  beta: quote.beta,
  quote_time: quote.regularMarketTime,
  market_state: quote.marketState,
  data_source: 'yahoo_finance',
  fetched_at: new Date()
};
```

## Data Mapping to company_profiles_cache

```typescript
// Map Yahoo Finance assetProfile to company_profiles_cache table
const companyProfile = {
  symbol: symbol,
  name: profile.longName,
  asset_type: 'stock',
  exchange: quote.exchange,
  sector: profile.sector,
  industry: profile.industry,
  description: profile.longBusinessSummary,
  ceo: profile.companyOfficers?.[0]?.name,
  employees: profile.fullTimeEmployees,
  headquarters: `${profile.address1}, ${profile.city}, ${profile.state} ${profile.zip}`,
  website: profile.website,
  logo_url: null,  // Not directly available
  data_source: 'yahoo_finance',
  fetched_at: new Date()
};
```

