# Coinbase API Template - Data Scraping Layer

## Service Overview
**Provider:** Coinbase  
**Purpose:** Cryptocurrency market data, prices, portfolio sync  
**Base URL:** 
- Advanced Trade: `https://api.coinbase.com/api/v3/brokerage`
- Exchange: `https://api.exchange.coinbase.com`
- App API: `https://api.coinbase.com/v2`

## Authentication
- **Type:** API Key + Secret + Passphrase
- **Headers:**
  - `CB-ACCESS-KEY`: API Key
  - `CB-ACCESS-SIGN`: HMAC SHA256 signature
  - `CB-ACCESS-TIMESTAMP`: Unix timestamp (seconds)
  - `CB-ACCESS-PASSPHRASE`: Passphrase
- **Note:** Public endpoints don't require authentication

## Rate Limits
- **Limit:** Varies by endpoint and subscription
- **Window:** Per second/minute
- **Note:** Rate limits are endpoint-specific

## Key Endpoints

### 1. Product Ticker
**Endpoint:** `GET /api/v3/brokerage/market/products/{product_id}/ticker`

**Purpose:** Get 24hr ticker statistics for a product

**Parameters:**
- `product_id` (path, required): Product ID (e.g., 'BTC-USD')

**Response Structure:**
```typescript
{
  trades: Array<{
    trade_id: string;
    product_id: string;
    price: string;
    size: string;
    time: string;      // RFC3339 timestamp
    side: 'BUY' | 'SELL';
    bid: string;
  }>;
  best_bid: string;
  best_ask: string;
}
```

**Use Case:** Real-time price and order book data

---

### 2. Product Order Book
**Endpoint:** `GET /api/v3/brokerage/market/product_book`

**Purpose:** Get order book for a product

**Parameters:**
- `product_id` (required): Product ID
- `limit` (optional): Number of price levels (default: 50)

**Response Structure:**
```typescript
{
  pricebook: {
    bids: Array<{
      price: string;
      size: string;
    }>;
    asks: Array<{
      price: string;
      size: string;
    }>;
    product_id: string;
    time: string;
  };
}
```

**Use Case:** Order book depth

---

### 3. Product Candles
**Endpoint:** `GET /api/v3/brokerage/market/products/{product_id}/candles`

**Purpose:** Get historical candlestick data

**Parameters:**
- `product_id` (path, required): Product ID
- `start` (required): Start time (ISO 8601 or Unix timestamp)
- `end` (required): End time (ISO 8601 or Unix timestamp)
- `granularity` (required): `ONE_MINUTE, FIVE_MINUTE, FIFTEEN_MINUTE, THIRTY_MINUTE, ONE_HOUR, TWO_HOUR, SIX_HOUR, ONE_DAY`

**Response Structure:**
```typescript
{
  candles: Array<{
    start: string;     // ISO 8601 timestamp
    low: string;
    high: string;
    open: string;
    close: string;
    volume: string;
  }>;
}
```

**Use Case:** Historical price charts

---

### 4. Products List
**Endpoint:** `GET /api/v3/brokerage/market/products`

**Purpose:** Get list of available products

**Parameters:**
- `limit` (optional): Number of results (default: 250)
- `offset` (optional): Pagination offset
- `product_type` (optional): Filter by type

**Response Structure:**
```typescript
{
  products: Array<{
    product_id: string;
    price: string;
    price_percentage_change_24h: string;
    volume_24h: string;
    volume_percentage_change_24h: string;
    base_increment: string;
    quote_increment: string;
    quote_min_size: string;
    quote_max_size: string;
    base_min_size: string;
    base_max_size: string;
    base_name: string;
    quote_name: string;
    status: string;
    product_type: string;
    base_currency_id: string;
    quote_currency_id: string;
    mid_market_price: string;
    display_name: string;
  }>;
  num_products: number;
}
```

**Use Case:** Product discovery and validation

---

### 5. Product Details
**Endpoint:** `GET /api/v3/brokerage/market/products/{product_id}`

**Purpose:** Get detailed product information

**Parameters:**
- `product_id` (path, required): Product ID

**Response Structure:**
```typescript
{
  product_id: string;
  price: string;
  price_percentage_change_24h: string;
  volume_24h: string;
  volume_percentage_change_24h: string;
  base_increment: string;
  quote_increment: string;
  quote_min_size: string;
  quote_max_size: string;
  base_min_size: string;
  base_max_size: string;
  base_name: string;
  quote_name: string;
  watched: boolean;
  is_disabled: boolean;
  new: boolean;
  status: string;
  cancel_only: boolean;
  limit_only: boolean;
  post_only: boolean;
  trading_disabled: boolean;
  auction_mode: boolean;
  product_type: string;
  quote_currency_id: string;
  base_currency_id: string;
  mid_market_price: string;
  display_name: string;
  product_venue: string;
  approximate_quote_24h_volume: string;
}
```

**Use Case:** Product information and trading rules

---

### 6. Accounts (Private)
**Endpoint:** `GET /api/v3/brokerage/accounts`

**Purpose:** Get list of accounts (for portfolio sync)

**Parameters:**
- Requires authentication
- `limit` (optional): Number of results
- `cursor` (optional): Pagination cursor

**Response Structure:**
```typescript
{
  accounts: Array<{
    uuid: string;
    name: string;
    currency: string;
    available_balance: {
      value: string;
      currency: string;
    };
    default: boolean;
    active: boolean;
    created_at: string;
    updated_at: string;
    deleted_at: string;
    type: string;
    ready: boolean;
    hold: {
      value: string;
      currency: string;
    };
  }>;
  has_next: boolean;
  cursor: string;
  size: number;
}
```

**Use Case:** Portfolio sync - account balances

---

### 7. Account Details (Private)
**Endpoint:** `GET /api/v3/brokerage/accounts/{account_uuid}`

**Purpose:** Get specific account details

**Parameters:**
- `account_uuid` (path, required): Account UUID
- Requires authentication

**Response Structure:**
```typescript
{
  uuid: string;
  name: string;
  currency: string;
  available_balance: {
    value: string;
    currency: string;
  };
  default: boolean;
  active: boolean;
  created_at: string;
  updated_at: string;
  deleted_at: string;
  type: string;
  ready: boolean;
  hold: {
    value: string;
    currency: string;
  };
}
```

**Use Case:** Account details for portfolio sync

---

### 8. Best Bid/Ask
**Endpoint:** `GET /api/v3/brokerage/best_bid_ask`

**Purpose:** Get best bid/ask for products

**Parameters:**
- `product_ids` (optional): Comma-separated product IDs

**Response Structure:**
```typescript
{
  pricebooks: Array<{
    product_id: string;
    bids: Array<{
      price: string;
      size: string;
    }>;
    asks: Array<{
      price: string;
      size: string;
    }>;
    time: string;
  }>;
}
```

**Use Case:** Quick bid/ask lookup

---

### 9. Market Trades
**Endpoint:** `GET /api/v3/brokerage/market/products/{product_id}/ticker`

**Purpose:** Get recent market trades

**Parameters:**
- `product_id` (path, required): Product ID
- `limit` (optional): Number of trades (default: 100)

**Response Structure:**
```typescript
{
  trades: Array<{
    trade_id: string;
    product_id: string;
    price: string;
    size: string;
    time: string;      // RFC3339 timestamp
    side: 'BUY' | 'SELL';
  }>;
  best_bid: string;
  best_ask: string;
}
```

**Use Case:** Recent trading activity

---

### 10. Exchange Rates
**Endpoint:** `GET /v2/exchange-rates`

**Purpose:** Get current exchange rates

**Parameters:**
- `currency` (optional): Base currency (default: 'USD')

**Response Structure:**
```typescript
{
  currency: string;
  rates: {
    [currency: string]: string;  // Exchange rate
  };
}
```

**Use Case:** Currency conversion

---

## WebSocket Endpoints

### 1. Market Data WebSocket
**Endpoint:** `wss://advanced-trade-ws.coinbase.com`

**Purpose:** Real-time market data streams

**Subscription:**
```typescript
{
  type: "subscribe";
  product_ids: string[];
  channel: string;  // "ticker", "level2", "market_trades", "candles"
}
```

**Message Format:**
```typescript
{
  channel: string;
  client_id?: string;
  timestamp: string;
  sequence_num: number;
  events: Array<{
    type: string;
    product_id: string;
    // Event-specific data
  }>;
}
```

**Use Case:** Real-time price updates

---

## Error Handling

**Common Error Codes:**
- `400`: Bad request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not found
- `429`: Rate limit exceeded
- `500`: Internal server error

**Error Response:**
```typescript
{
  error: string;
  error_details?: string;
  message?: string;
  preview_failure_reason?: string;
}
```

## Integration Notes

1. **Product ID Format:**
   - Base-Quote (e.g., 'BTC-USD', 'ETH-USD')
   - Hyphen-separated, uppercase

2. **Timestamps:**
   - ISO 8601 format: `YYYY-MM-DDTHH:mm:ssZ`
   - Or Unix timestamp (seconds or milliseconds depending on endpoint)

3. **Authentication:**
   - Use HMAC SHA256 for signature
   - Include timestamp, method, request path, and body
   - Passphrase required (set during API key creation)

4. **Rate Limiting:**
   - Varies by endpoint
   - Monitor rate limit headers
   - Implement exponential backoff

5. **Pagination:**
   - Use `cursor` for paginated endpoints
   - `has_next` indicates more results
   - `limit` controls page size

6. **Data Types:**
   - All prices/amounts as strings (precision)
   - Convert to numbers for calculations
   - Use decimal.js for precise calculations

## Scraping Implementation

```typescript
// Example: Coinbase Crypto Scraper
class CoinbaseScraper {
  async fetchProductTicker(productId: string) {
    // Fetch 24hr ticker
    // Map to crypto_quotes_cache format
  }
  
  async fetchProductCandles(productId: string, start: string, end: string, granularity: string) {
    // Fetch historical candles
    // Parse time series
  }
  
  async fetchProducts(limit?: number) {
    // Fetch product list
    // Cache for symbol mapping
  }
  
  async fetchAccountInfo(apiKey: string, apiSecret: string, passphrase: string) {
    // Fetch account balances (for portfolio sync)
    // Requires authentication
  }
  
  async connectWebSocket(productIds: string[], channels: string[], onMessage: (data: any) => void) {
    // Connect to WebSocket
    // Subscribe to channels
    // Handle reconnection
  }
}
```

## Cache Strategy
- **TTL:** 
  - Ticker: 60 seconds
  - Candles: 1 minute (for current interval)
  - Order book: 5 seconds
  - Account info: 5 minutes (for portfolio sync)
- **Key Format:** 
  - `coinbase:ticker:{productId}`
  - `coinbase:candles:{productId}:{granularity}:{start}:{end}`
  - `coinbase:orderbook:{productId}`
  - `coinbase:account:{userId}`

## Data Mapping to crypto_quotes_cache

```typescript
// Map Coinbase ticker to crypto_quotes_cache table
const cryptoQuote = {
  symbol: productId.split('-')[0],  // Extract base currency
  name: getCoinName(productId.split('-')[0]),
  price: parseFloat(ticker.price),
  change_24h: parseFloat(ticker.price_percentage_change_24h),
  volume_24h: parseFloat(ticker.volume_24h),
  high_24h: null,  // Not in ticker response
  low_24h: null,   // Not in ticker response
  data_source: 'coinbase',
  last_updated: new Date(),
  fetched_at: new Date()
};
```

