# Alpaca API Template - Data Scraping Layer

## Service Overview
**Provider:** Alpaca Markets  
**Purpose:** Stock and crypto market data, portfolio positions  
**Base URL:** 
- Data API: `https://data.alpaca.markets`
- Trading API: `https://paper-api.alpaca.markets` (paper) / `https://api.alpaca.markets` (live)
**JavaScript SDK:** `npm install @alpacahq/alpaca-trade-api`

## Authentication
- **Type:** API Key + Secret
- **Headers:**
  - `APCA-API-KEY-ID`: API Key
  - `APCA-API-SECRET-KEY`: API Secret

## JavaScript Client Setup

```javascript
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca({
  keyId: "YOUR_API_KEY",
  secretKey: "YOUR_API_SECRET",
  paper: true, // Set to false for live trading
});
```

## Rate Limits
- **Limit:** Varies by endpoint and subscription tier
- **Window:** Per minute
- **Note:** Free tier has lower limits; paid tiers have higher limits

## Key Endpoints

### 1. Stock Bars (OHLCV Data)
**Endpoint:** `GET /v2/stocks/{symbol}/bars`

**Purpose:** Fetch historical bar data for stocks

**Parameters:**
- `symbol` (path, required): Stock symbol (e.g., AAPL)
- `feed` (query, optional): Data feed - 'sip' or 'iex' (default: best available)
- `timeframe` (query, required): Bar interval (e.g., '1Day', '1Hour', '5Minute')
- `start` (query, optional): Start date (YYYY-MM-DD)
- `end` (query, optional): End date (YYYY-MM-DD)
- `limit` (query, optional): Max bars to return (default: 100)
- `asof` (query, optional): Historical date for symbol lookup

**Response Structure:**
```typescript
{
  bars: Array<{
    t: string;        // Timestamp
    o: number;        // Open
    h: number;        // High
    l: number;        // Low
    c: number;        // Close
    v: number;        // Volume
    n: number;        // Trade count
    vw: number;       // VWAP
  }>;
  symbol: string;
  next_page_token?: string;
}
```

**Use Case:** Historical price data for portfolio analysis and charts

**JavaScript Example:**
```javascript
// Fetch stock bars using JavaScript SDK
alpaca.getBars("minute", "AAPL", {
  limit: 5,
}).then((barset) => {
  const bars = barset["AAPL"];
  bars.forEach((bar) => {
    console.log(bar);
  });
});
```

---

### 2. Crypto Bars
**Endpoint:** `GET /v2/crypto/{symbol}/bars`

**Purpose:** Fetch historical cryptocurrency bar data

**Parameters:**
- `symbol` (path, required): Crypto pair (e.g., BTC/USD)
- `start` (query, optional): Start date (YYYY-MM-DD)
- `end` (query, optional): End date (YYYY-MM-DD)
- `timeframe` (query, optional): Bar interval (e.g., '1Min', '1Hour', '1Day')

**Response Structure:**
```typescript
{
  [symbol: string]: Array<{
    t: number;        // Timestamp (milliseconds)
    o: number;       // Open
    h: number;       // High
    l: number;       // Low
    c: number;       // Close
    v: number;       // Volume
    n: number;       // Trade count
    vw: number;      // VWAP
  }>;
}
```

**Use Case:** Crypto historical price data

**JavaScript Example:**
```javascript
// Fetch crypto bars
const options = {
  start: '2022-09-01',
  end: '2022-09-06',
  timeframe: '1Day',
};

(async () => {
  const bars = await alpaca.getCryptoBars(["BTC/USD"], options);
  console.table(bars.get("BTC/USD"));
})();
```

---

### 3. Latest Stock Trade
**Endpoint:** `GET /v2/stocks/{symbol}/trades/latest`

**Purpose:** Get the latest trade for a stock

**Parameters:**
- `symbol` (path, required): Stock symbol

**Response Structure:**
```typescript
{
  trades: {
    [symbol: string]: {
      t: string;      // Timestamp
      x: string;      // Exchange
      p: number;      // Price
      s: number;      // Size
      c: string[];    // Conditions
      i: number;      // Trade ID
      z: string;      // Tape
    };
  };
}
```

**Use Case:** Real-time quote updates

**JavaScript Example:**
```javascript
// Fetch latest trade for a stock
alpaca.getLatestTrade("AAPL").then((trade) => {
  console.log(trade);
});
```

---

### 4. Latest Crypto Order Book
**Endpoint:** `GET /v1beta3/crypto/us/latest/orderbooks`

**Purpose:** Get latest order book data for crypto pairs

**Parameters:**
- `symbols` (query, required): Comma-separated list of symbols (e.g., BTC/USD,ETH/USD)

**Response Structure:**
```typescript
{
  orderbooks: {
    [symbol: string]: {
      bids: Array<[price: number, size: number]>;
      asks: Array<[price: number, size: number]>;
      timestamp: string;
    };
  };
}
```

**Use Case:** Real-time order book depth

---

### 5. Account Information
**Endpoint:** `GET /v2/account`

**Purpose:** Get trading account details (for portfolio sync)

**Response Structure:**
```typescript
{
  id: string;
  account_number: string;
  status: string;
  currency: string;
  buying_power: string;
  cash: string;
  portfolio_value: string;
  pattern_day_trader: boolean;
  // ... many more fields
}
```

**Use Case:** Portfolio sync - account balance and buying power

**JavaScript Example:**
```javascript
// Get account information
alpaca.getAccount().then((account) => {
  console.log(`Buying Power: ${account.buying_power}`);
  console.log(`Portfolio Value: ${account.portfolio_value}`);
});
```

---

### 6. Positions
**Endpoint:** `GET /v2/positions`

**Purpose:** Get all open positions

**Response Structure:**
```typescript
Array<{
  symbol: string;
  qty: string;
  side: 'long' | 'short';
  market_value: string;
  cost_basis: string;
  unrealized_pl: string;
  unrealized_plpc: string;
  current_price: string;
  asset_class: 'us_equity' | 'option' | 'crypto';
}>;
```

**Use Case:** Portfolio sync - current holdings

**JavaScript Example:**
```javascript
// Get position for a specific symbol
const aaplPosition = alpaca.getPosition("AAPL");

// Get all positions
alpaca.getPositions().then((portfolio) => {
  portfolio.forEach((position) => {
    console.log(`${position.qty} shares of ${position.symbol}`);
  });
});
```

---

### 7. Assets
**Endpoint:** `GET /v2/assets`

**Purpose:** Get list of tradable assets

**Parameters:**
- `status` (query, optional): 'active' | 'inactive'
- `asset_class` (query, optional): Filter by asset class

**Response Structure:**
```typescript
Array<{
  id: string;
  class: string;
  exchange: string;
  symbol: string;
  name: string;
  status: string;
  tradable: boolean;
  marginable: boolean;
  shortable: boolean;
  easy_to_borrow: boolean;
}>;
```

**Use Case:** Asset lookup and validation

**JavaScript Example:**
```javascript
// Get list of all active assets
const activeAssets = alpaca
  .getAssets({
    status: "active",
  })
  .then((activeAssets) => {
    // Filter assets by exchange
    const nasdaqAssets = activeAssets.filter(
      (asset) => asset.exchange == "NASDAQ"
    );
    console.log(nasdaqAssets);
  });
```

---

### 8. Options Contracts
**Endpoint:** `GET /v2/options/contracts`

**Purpose:** Get option contracts

**Parameters:**
- `underlying_symbols` (query, optional): Comma-separated underlying symbols
- `expiration_date_lte` (query, optional): Expiration date filter
- `expiration_date_gte` (query, optional): Expiration date filter
- `limit` (query, optional): Max results (default: 100)
- `page_token` (query, optional): Pagination token

**Response Structure:**
```typescript
{
  option_contracts: Array<{
    id: string;
    symbol: string;
    name: string;
    status: string;
    tradable: boolean;
    expiration_date: string;
    root_symbol: string;
    underlying_symbol: string;
    type: 'call' | 'put';
    style: 'american' | 'european';
    strike_price: string;
    size: string;
    open_interest: string;
    close_price: string;
  }>;
  page_token?: string;
  limit: number;
}
```

**Use Case:** Options data for advanced portfolio tracking

**JavaScript Example:**
```javascript
// Note: Options contracts endpoint may require direct REST API call
// Using fetch for options contracts
const fetch = require('node-fetch');

const apiKey = 'YOUR_API_KEY';
const apiSecret = 'YOUR_API_SECRET';

fetch('https://data.alpaca.markets/v2/options/contracts?underlying_symbols=AAPL,MSFT&expiration_date_lte=2024-01-19', {
  headers: {
    'APCA-API-KEY-ID': apiKey,
    'APCA-API-SECRET-KEY': apiSecret,
  },
})
  .then(res => res.json())
  .then(data => console.log(data));
```

---

### 9. Place Orders

**Endpoint:** `POST /v2/orders`

**Purpose:** Place trading orders (bracket, OTO, OCO orders)

**JavaScript Example:**
```javascript
const symbol = "AAPL";

// First, get current price
alpaca
  .getBars("minute", symbol, {
    limit: 5,
  })
  .then((barset) => {
    const currentPrice = barset[symbol].slice(-1)[0].closePrice;

    // Bracket order with stop-loss and take-profit
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "bracket",
      stop_loss: {
        stop_price: currentPrice * 0.95,
        limit_price: currentPrice * 0.94,
      },
      take_profit: {
        limit_price: currentPrice * 1.05,
      },
    });

    // OTO order (One-Triggers-Other) with stop-loss
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "oto",
      stop_loss: {
        stop_price: currentPrice * 0.95,
      },
    });

    // OCO order (One-Cancels-Other)
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "sell",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
      order_class: "oco",
      stop_loss: {
        stop_price: currentPrice * 0.95,
      },
      take_profit: {
        limit_price: currentPrice * 1.05,
      },
    });
  });
```

**Use Case:** Automated trading and portfolio management

---

## Error Handling

**Common Error Codes:**
- `403`: Invalid API credentials
- `422`: Invalid request parameters
- `429`: Rate limit exceeded
- `500`: Server error

**Error Response:**
```typescript
{
  code: number;
  message: string;
}
```

## Integration Notes

1. **Data Feeds:** 
   - IEX feed: Default, no subscription needed
   - SIP feed: Requires subscription, more comprehensive

2. **Crypto Data:** 
   - No API keys required for public crypto data endpoints
   - Trading endpoints require authentication

3. **Real-time Data:**
   - Use WebSocket streams for real-time updates
   - REST API for historical and snapshot data

4. **Pagination:**
   - Use `next_page_token` for paginated results
   - Set appropriate `limit` to control batch size

5. **Rate Limiting:**
   - Implement exponential backoff
   - Monitor rate limit headers if provided
   - Use job queue with concurrency limits

## Data Transfer Objects (DTOs)

### Request DTOs

```typescript
// Stock Bars Request
interface StockBarsRequestDTO {
  symbol: string;
  timeframe: '1Min' | '5Min' | '15Min' | '30Min' | '1Hour' | '1Day';
  start?: string; // YYYY-MM-DD
  end?: string; // YYYY-MM-DD
  limit?: number; // Default: 100
  feed?: 'iex' | 'sip';
  asof?: string; // Historical date for symbol lookup
}

// Crypto Bars Request
interface CryptoBarsRequestDTO {
  symbol: string; // e.g., "BTC/USD"
  start?: string; // YYYY-MM-DD
  end?: string; // YYYY-MM-DD
  timeframe?: '1Min' | '5Min' | '15Min' | '30Min' | '1Hour' | '1Day';
}

// Latest Trade Request
interface LatestTradeRequestDTO {
  symbol: string;
}

// Account Info Request
interface AccountInfoRequestDTO {
  // No parameters - uses authenticated account
}

// Positions Request
interface PositionsRequestDTO {
  symbol?: string; // Optional - filter by symbol
}

// Assets Request
interface AssetsRequestDTO {
  status?: 'active' | 'inactive';
  asset_class?: 'us_equity' | 'crypto' | 'option';
  exchange?: string;
}
```

### Response DTOs

```typescript
// Stock Bars Response
interface StockBarsResponseDTO {
  bars: Array<{
    t: string; // Timestamp (ISO 8601)
    o: number; // Open
    h: number; // High
    l: number; // Low
    c: number; // Close
    v: number; // Volume
    n: number; // Trade count
    vw: number; // VWAP
  }>;
  symbol: string;
  next_page_token?: string;
}

// Crypto Bars Response
interface CryptoBarsResponseDTO {
  [symbol: string]: Array<{
    t: number; // Timestamp (milliseconds)
    o: number;
    h: number;
    l: number;
    c: number;
    v: number;
    n: number;
    vw: number;
  }>;
}

// Latest Trade Response
interface LatestTradeResponseDTO {
  trades: {
    [symbol: string]: {
      t: string; // Timestamp
      x: string; // Exchange
      p: number; // Price
      s: number; // Size
      c: string[]; // Conditions
      i: number; // Trade ID
      z: string; // Tape
    };
  };
}

// Account Response
interface AccountResponseDTO {
  id: string;
  account_number: string;
  status: 'ACTIVE' | 'INACTIVE' | 'CLOSED';
  currency: string;
  buying_power: string;
  cash: string;
  portfolio_value: string;
  pattern_day_trader: boolean;
  trading_blocked: boolean;
  transfers_blocked: boolean;
  account_blocked: boolean;
  created_at: string;
  trade_suspended_by_user: boolean;
  multiplier: string;
  equity: string;
  last_equity: string;
  long_market_value: string;
  short_market_value: string;
}

// Position Response
interface PositionResponseDTO {
  symbol: string;
  qty: string;
  side: 'long' | 'short';
  market_value: string;
  cost_basis: string;
  unrealized_pl: string;
  unrealized_plpc: string;
  current_price: string;
  asset_class: 'us_equity' | 'option' | 'crypto';
}

// Asset Response
interface AssetResponseDTO {
  id: string;
  class: string;
  exchange: string;
  symbol: string;
  name: string;
  status: string;
  tradable: boolean;
  marginable: boolean;
  shortable: boolean;
  easy_to_borrow: boolean;
}
```

## Scraping Implementation

```typescript
import { Injectable, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { Alpaca } from '@alpacahq/alpaca-trade-api';
import { RateLimiter } from 'limiter';
import { RedisService } from '../redis/redis.service';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class AlpacaScraperService {
  private readonly logger = new Logger(AlpacaScraperService.name);
  private alpaca: Alpaca;
  private rateLimiter: RateLimiter;

  constructor(
    private configService: ConfigService,
    private redis: RedisService,
    private prisma: PrismaService,
  ) {
    this.alpaca = new Alpaca({
      keyId: this.configService.get('ALPACA_API_KEY'),
      secretKey: this.configService.get('ALPACA_API_SECRET'),
      paper: this.configService.get('ALPACA_PAPER', true),
    });

    // Rate limiter: 200 requests per minute
    this.rateLimiter = new RateLimiter({
      tokensPerInterval: 200,
      interval: 'minute',
    });
  }

  /**
   * Fetch stock bars with rate limiting and error handling
   */
  async fetchStockBars(
    request: StockBarsRequestDTO,
  ): Promise<StockBarsResponseDTO> {
    await this.rateLimiter.removeTokens(1);

    try {
      const params: any = {
        timeframe: request.timeframe,
        limit: request.limit || 100,
      };

      if (request.start) params.start = request.start;
      if (request.end) params.end = request.end;
      if (request.feed) params.feed = request.feed;
      if (request.asof) params.asof = request.asof;

      const bars = await this.alpaca.getBars(
        request.timeframe,
        request.symbol,
        params,
      );

      return {
        bars: bars[request.symbol].map((bar) => ({
          t: bar.t.toISOString(),
          o: bar.o,
          h: bar.h,
          l: bar.l,
          c: bar.c,
          v: bar.v,
          n: bar.n,
          vw: bar.vw,
        })),
        symbol: request.symbol,
      };
    } catch (error) {
      this.logger.error(`Error fetching stock bars for ${request.symbol}:`, error);
      throw this.handleError(error);
    }
  }

  /**
   * Fetch crypto bars
   */
  async fetchCryptoBars(
    request: CryptoBarsRequestDTO,
  ): Promise<CryptoBarsResponseDTO> {
    await this.rateLimiter.removeTokens(1);

    try {
      const options: any = {};
      if (request.start) options.start = request.start;
      if (request.end) options.end = request.end;
      if (request.timeframe) options.timeframe = request.timeframe;

      const bars = await this.alpaca.getCryptoBars([request.symbol], options);
      return bars;
    } catch (error) {
      this.logger.error(`Error fetching crypto bars for ${request.symbol}:`, error);
      throw this.handleError(error);
    }
  }

  /**
   * Fetch latest trade for real-time quotes
   */
  async fetchLatestTrade(
    request: LatestTradeRequestDTO,
  ): Promise<LatestTradeResponseDTO> {
    await this.rateLimiter.removeTokens(1);

    try {
      const trade = await this.alpaca.getLatestTrade(request.symbol);
      return {
        trades: {
          [request.symbol]: {
            t: trade.t.toISOString(),
            x: trade.x,
            p: trade.p,
            s: trade.s,
            c: trade.c || [],
            i: trade.i,
            z: trade.z,
          },
        },
      };
    } catch (error) {
      this.logger.error(`Error fetching latest trade for ${request.symbol}:`, error);
      throw this.handleError(error);
    }
  }

  /**
   * Fetch account information for portfolio sync
   */
  async fetchAccountInfo(): Promise<AccountResponseDTO> {
    await this.rateLimiter.removeTokens(1);

    try {
      const account = await this.alpaca.getAccount();
      return {
        id: account.id,
        account_number: account.account_number,
        status: account.status as any,
        currency: account.currency,
        buying_power: account.buying_power,
        cash: account.cash,
        portfolio_value: account.portfolio_value,
        pattern_day_trader: account.pattern_day_trader,
        trading_blocked: account.trading_blocked,
        transfers_blocked: account.transfers_blocked,
        account_blocked: account.account_blocked,
        created_at: account.created_at.toISOString(),
        trade_suspended_by_user: account.trade_suspended_by_user,
        multiplier: account.multiplier,
        equity: account.equity,
        last_equity: account.last_equity,
        long_market_value: account.long_market_value,
        short_market_value: account.short_market_value,
      };
    } catch (error) {
      this.logger.error('Error fetching account info:', error);
      throw this.handleError(error);
    }
  }

  /**
   * Fetch positions for portfolio sync
   */
  async fetchPositions(
    request?: PositionsRequestDTO,
  ): Promise<PositionResponseDTO[]> {
    await this.rateLimiter.removeTokens(1);

    try {
      let positions;
      if (request?.symbol) {
        const position = await this.alpaca.getPosition(request.symbol);
        positions = [position];
      } else {
        positions = await this.alpaca.getPositions();
      }

      return positions.map((pos) => ({
        symbol: pos.symbol,
        qty: pos.qty,
        side: pos.side as 'long' | 'short',
        market_value: pos.market_value,
        cost_basis: pos.cost_basis,
        unrealized_pl: pos.unrealized_pl,
        unrealized_plpc: pos.unrealized_plpc,
        current_price: pos.current_price,
        asset_class: pos.asset_class as any,
      }));
    } catch (error) {
      this.logger.error('Error fetching positions:', error);
      throw this.handleError(error);
    }
  }

  /**
   * Map stock bars to database entity
   */
  async mapStockBarsToCache(
    symbol: string,
    bars: StockBarsResponseDTO['bars'],
  ): Promise<void> {
    const latestBar = bars[bars.length - 1];
    const cacheKey = `alpaca:stock:${symbol}:bars:${latestBar.t}`;

    // Cache for 60 seconds
    await this.redis.setex(
      cacheKey,
      60,
      JSON.stringify(latestBar),
    );

    // Upsert to database
    await this.prisma.stockQuotesCache.upsert({
      where: { symbol },
      update: {
        price: latestBar.c,
        open: latestBar.o,
        day_high: latestBar.h,
        day_low: latestBar.l,
        volume: latestBar.v,
        quote_time: new Date(latestBar.t),
        data_source: 'alpaca',
        fetched_at: new Date(),
      },
      create: {
        symbol,
        price: latestBar.c,
        open: latestBar.o,
        day_high: latestBar.h,
        day_low: latestBar.l,
        volume: latestBar.v,
        quote_time: new Date(latestBar.t),
        data_source: 'alpaca',
        fetched_at: new Date(),
      },
    });
  }

  /**
   * Error handling with retry logic
   */
  private handleError(error: any): Error {
    if (error.statusCode === 403) {
      return new Error('Invalid Alpaca API credentials');
    } else if (error.statusCode === 422) {
      return new Error(`Invalid request parameters: ${error.message}`);
    } else if (error.statusCode === 429) {
      return new Error('Rate limit exceeded - implement exponential backoff');
    } else if (error.statusCode === 500) {
      return new Error('Alpaca server error - retry later');
    }
    return new Error(`Alpaca API error: ${error.message}`);
  }
}
```

## Cache Strategy
- **TTL:** 
  - Stock quotes: 60 seconds
  - Crypto quotes: 60 seconds
  - Account info: 300 seconds (5 minutes)
  - Positions: 60 seconds
- **Key Format:** 
  - `alpaca:stock:{symbol}:bars:{timeframe}`
  - `alpaca:crypto:{symbol}:bars:{timeframe}`
  - `alpaca:account:{account_id}`
  - `alpaca:positions:{user_id}`
- **Invalidation:** On new data fetch or manual cache clear

