# Binance API Template - Data Scraping Layer

## Service Overview
**Provider:** Binance  
**Purpose:** Cryptocurrency market data, prices, order books, portfolio sync  
**Base URL:** 
- Spot: `https://api.binance.com/api/v3`
- Futures: `https://fapi.binance.com/fapi/v1`
- Data: `https://data-api.binance.vision/api/v1`

## Authentication
- **Type:** API Key + Secret (for private endpoints)
- **Headers:** 
  - `X-MBX-APIKEY`: API Key
  - Signature required for private endpoints
- **Note:** Public endpoints don't require authentication

## Rate Limits
- **Spot API:** 1200 requests per minute (weight-based)
- **Futures API:** 2400 requests per minute (weight-based)
- **Window:** Per minute
- **Note:** Rate limits are weight-based; different endpoints have different weights

## Key Endpoints

### 1. 24hr Ticker Statistics
**Endpoint:** `GET /api/v3/ticker/24hr`

**Purpose:** Get 24-hour price change statistics

**Parameters:**
- `symbol` (optional): Trading pair (e.g., 'BTCUSDT') - if omitted, returns all symbols
- `symbols` (optional): Comma-separated symbols for multiple pairs

**Response Structure:**
```typescript
{
  symbol: string;
  priceChange: string;
  priceChangePercent: string;
  weightedAvgPrice: string;
  prevClosePrice: string;
  lastPrice: string;
  lastQty: string;
  bidPrice: string;
  bidQty: string;
  askPrice: string;
  askQty: string;
  openPrice: string;
  highPrice: string;
  lowPrice: string;
  volume: string;
  quoteVolume: string;
  openTime: number;      // Unix timestamp (ms)
  closeTime: number;    // Unix timestamp (ms)
  firstId: number;      // First trade ID
  lastId: number;       // Last trade ID
  count: number;        // Trade count
}
```

**Use Case:** Real-time crypto quotes and 24h statistics

---

### 2. Exchange Information
**Endpoint:** `GET /api/v3/exchangeInfo`

**Purpose:** Get exchange trading rules and symbol information

**Parameters:**
- `symbol` (optional): Single symbol
- `symbols` (optional): Comma-separated symbols

**Response Structure:**
```typescript
{
  timezone: string;
  serverTime: number;   // Unix timestamp (ms)
  rateLimits: Array<{
    rateLimitType: string;
    interval: string;
    intervalNum: number;
    limit: number;
  }>;
  exchangeFilters: Array<any>;
  symbols: Array<{
    symbol: string;
    status: string;
    baseAsset: string;
    baseAssetPrecision: number;
    quoteAsset: string;
    quotePrecision: number;
    orderTypes: string[];
    icebergAllowed: boolean;
    ocoAllowed: boolean;
    isSpotTradingAllowed: boolean;
    isMarginTradingAllowed: boolean;
    filters: Array<{
      filterType: string;
      // Various filter properties
    }>;
    permissions: string[];
  }>;
}
```

**Use Case:** Symbol validation and trading rules

---

### 3. Kline/Candlestick Data
**Endpoint:** `GET /api/v3/klines`

**Purpose:** Get historical candlestick data

**Parameters:**
- `symbol` (required): Trading pair
- `interval` (required): `1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M`
- `startTime` (optional): Start time (Unix timestamp ms)
- `endTime` (optional): End time (Unix timestamp ms)
- `limit` (optional): Number of results (default: 500, max: 1000)

**Response Structure:**
```typescript
Array<[
  number,  // Open time (ms)
  string,  // Open price
  string,  // High price
  string,  // Low price
  string,  // Close price
  string,  // Volume
  number,  // Close time (ms)
  string,  // Quote asset volume
  number,  // Number of trades
  string,  // Taker buy base volume
  string,  // Taker buy quote volume
  string   // Ignore
]>;
```

**Use Case:** Historical price charts and analysis

---

### 4. Order Book
**Endpoint:** `GET /api/v3/depth`

**Purpose:** Get order book depth

**Parameters:**
- `symbol` (required): Trading pair
- `limit` (optional): Number of levels (5, 10, 20, 50, 100, 500, 1000, 5000)

**Response Structure:**
```typescript
{
  lastUpdateId: number;
  bids: Array<[string, string]>;  // [price, quantity]
  asks: Array<[string, string]>;  // [price, quantity]
}
```

**Use Case:** Order book depth and liquidity analysis

---

### 5. Recent Trades
**Endpoint:** `GET /api/v3/trades`

**Purpose:** Get recent trades

**Parameters:**
- `symbol` (required): Trading pair
- `limit` (optional): Number of results (default: 500, max: 1000)

**Response Structure:**
```typescript
Array<{
  id: number;
  price: string;
  qty: string;
  quoteQty: string;
  time: number;        // Unix timestamp (ms)
  isBuyerMaker: boolean;
  isBestMatch: boolean;
}>;
```

**Use Case:** Recent trading activity

---

### 6. Account Information (Private)
**Endpoint:** `GET /api/v3/account`

**Purpose:** Get account information (for portfolio sync)

**Parameters:**
- Requires signature
- `timestamp` (required): Current timestamp (ms)
- `recvWindow` (optional): Receive window (ms)

**Response Structure:**
```typescript
{
  makerCommission: number;
  takerCommission: number;
  buyerCommission: number;
  sellerCommission: number;
  canTrade: boolean;
  canWithdraw: boolean;
  canDeposit: boolean;
  updateTime: number;
  accountType: string;
  balances: Array<{
    asset: string;
    free: string;      // Available balance
    locked: string;   // Locked balance
  }>;
  permissions: string[];
}
```

**Use Case:** Portfolio sync - account balances

---

### 7. Account Trade List (Private)
**Endpoint:** `GET /api/v3/myTrades`

**Purpose:** Get account trade history

**Parameters:**
- Requires signature
- `symbol` (required): Trading pair
- `startTime` (optional): Start time (ms)
- `endTime` (optional): End time (ms)
- `limit` (optional): Number of results (default: 500, max: 1000)
- `fromId` (optional): Trade ID to fetch from

**Response Structure:**
```typescript
Array<{
  symbol: string;
  id: number;
  orderId: number;
  orderListId: number;
  price: string;
  qty: string;
  quoteQty: string;
  commission: string;
  commissionAsset: string;
  time: number;        // Unix timestamp (ms)
  isBuyer: boolean;
  isMaker: boolean;
  isBestMatch: boolean;
}>;
```

**Use Case:** Trade history and P&L calculation

---

### 8. Current Open Orders (Private)
**Endpoint:** `GET /api/v3/openOrders`

**Purpose:** Get all open orders

**Parameters:**
- Requires signature
- `symbol` (optional): Filter by symbol
- `timestamp` (required): Current timestamp (ms)

**Response Structure:**
```typescript
Array<{
  symbol: string;
  orderId: number;
  orderListId: number;
  clientOrderId: string;
  price: string;
  origQty: string;
  executedQty: string;
  cummulativeQuoteQty: string;
  status: string;      // NEW, PARTIALLY_FILLED, FILLED, etc.
  timeInForce: string;
  type: string;        // LIMIT, MARKET, etc.
  side: string;        // BUY, SELL
  stopPrice: string;
  icebergQty: string;
  time: number;       // Unix timestamp (ms)
  updateTime: number;
  isWorking: boolean;
  origQuoteOrderQty: string;
}>;
```

**Use Case:** Open orders tracking

---

### 9. Server Time
**Endpoint:** `GET /api/v3/time`

**Purpose:** Get server time

**Response Structure:**
```typescript
{
  serverTime: number;  // Unix timestamp (ms)
}
```

**Use Case:** Time synchronization for signed requests

---

### 10. Price Ticker
**Endpoint:** `GET /api/v3/ticker/price`

**Purpose:** Get current price for symbol(s)

**Parameters:**
- `symbol` (optional): Single symbol
- `symbols` (optional): Comma-separated symbols

**Response Structure:**
```typescript
// Single symbol
{
  symbol: string;
  price: string;
}

// Multiple symbols
Array<{
  symbol: string;
  price: string;
}>;
```

**Use Case:** Simple price lookup

---

### 11. Book Ticker
**Endpoint:** `GET /api/v3/ticker/bookTicker`

**Purpose:** Get best bid/ask prices

**Parameters:**
- `symbol` (optional): Single symbol
- `symbols` (optional): Comma-separated symbols

**Response Structure:**
```typescript
{
  symbol: string;
  bidPrice: string;
  bidQty: string;
  askPrice: string;
  askQty: string;
}
```

**Use Case:** Best bid/ask for order book

---

## WebSocket Endpoints

### 1. Trade Stream
**Endpoint:** `wss://stream.binance.com:9443/ws/{symbol}@trade`

**Purpose:** Real-time trade stream

**Message Format:**
```typescript
{
  e: string;      // Event type
  E: number;      // Event time (ms)
  s: string;      // Symbol
  t: number;      // Trade ID
  p: string;      // Price
  q: string;      // Quantity
  b: number;      // Buyer order ID
  a: number;      // Seller order ID
  T: number;      // Trade time (ms)
  m: boolean;     // Is buyer maker
  M: boolean;     // Ignore
}
```

**Use Case:** Real-time price updates

---

### 2. Ticker Stream
**Endpoint:** `wss://stream.binance.com:9443/ws/{symbol}@ticker`

**Purpose:** 24hr ticker statistics stream

**Use Case:** Real-time 24h statistics

---

### 3. Kline Stream
**Endpoint:** `wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}`

**Purpose:** Real-time candlestick updates

**Use Case:** Real-time chart updates

---

## Error Handling

**Common Error Codes:**
- `-1000`: Unknown error
- `-1001`: Disconnected
- `-1002`: Unauthorized
- `-1003`: Too many requests
- `-1021`: Timestamp outside recvWindow
- `-2010`: Insufficient balance
- `-2011`: Unknown order

**Error Response:**
```typescript
{
  code: number;
  msg: string;
}
```

## Integration Notes

1. **Symbol Format:**
   - Base + Quote asset (e.g., 'BTCUSDT', 'ETHBTC')
   - Uppercase required

2. **Timestamps:**
   - All timestamps in milliseconds (Unix epoch)
   - Use server time for signed requests
   - `recvWindow`: 5000ms default, max 60000ms

3. **Rate Limiting:**
   - Weight-based system
   - Different endpoints have different weights
   - Monitor `X-MBX-USED-WEIGHT-1m` header
   - Implement exponential backoff

4. **Signature:**
   - Required for private endpoints
   - HMAC SHA256 of query string + secret
   - Include timestamp and recvWindow

5. **WebSocket:**
   - Use for real-time data
   - Combine multiple streams: `wss://stream.binance.com:9443/stream?streams=btcusdt@trade/ethusdt@trade`
   - Reconnect on disconnect

6. **Data Types:**
   - All prices/quantities as strings (precision)
   - Convert to numbers for calculations
   - Use decimal.js for precise calculations

## Scraping Implementation

```typescript
// Example: Binance Crypto Scraper
class BinanceScraper {
  async fetch24hrTicker(symbol: string) {
    // Fetch 24hr statistics
    // Map to crypto_quotes_cache format
  }
  
  async fetchKlines(symbol: string, interval: string, startTime?: number, endTime?: number) {
    // Fetch historical candlestick data
    // Parse array format
  }
  
  async fetchOrderBook(symbol: string, limit: number = 100) {
    // Fetch order book depth
  }
  
  async fetchAccountInfo(apiKey: string, apiSecret: string) {
    // Fetch account balances (for portfolio sync)
    // Requires signature
  }
  
  async fetchMyTrades(symbol: string, apiKey: string, apiSecret: string) {
    // Fetch trade history
  }
  
  async connectWebSocket(symbols: string[], onMessage: (data: any) => void) {
    // Connect to WebSocket streams
    // Handle reconnection
  }
}
```

## Cache Strategy
- **TTL:** 
  - 24hr ticker: 60 seconds
  - Klines: 1 minute (for current interval)
  - Order book: 5 seconds
  - Account info: 5 minutes (for portfolio sync)
- **Key Format:** 
  - `binance:ticker:{symbol}`
  - `binance:klines:{symbol}:{interval}:{startTime}:{endTime}`
  - `binance:orderbook:{symbol}:{limit}`
  - `binance:account:{userId}`

## Data Mapping to crypto_quotes_cache

```typescript
// Map Binance 24hr ticker to crypto_quotes_cache table
const cryptoQuote = {
  symbol: ticker.symbol.replace('USDT', '').replace('BTC', ''),
  name: getCoinName(ticker.symbol),
  price: parseFloat(ticker.lastPrice),
  change_24h: parseFloat(ticker.priceChangePercent),
  market_cap: null,  // Not provided by Binance
  volume_24h: parseFloat(ticker.volume),
  high_24h: parseFloat(ticker.highPrice),
  low_24h: parseFloat(ticker.lowPrice),
  open_24h: parseFloat(ticker.openPrice),
  data_source: 'binance',
  last_updated: new Date(ticker.closeTime),
  fetched_at: new Date()
};
```

