# CoinGecko API Template - Data Scraping Layer

## Service Overview
**Provider:** CoinGecko  
**Purpose:** Cryptocurrency market data, prices, market caps, historical data  
**Base URL:** 
- Free: `https://api.coingecko.com/api/v3`
- Pro: `https://pro-api.coingecko.com/api/v3`

## Authentication
- **Type:** API Key (for Pro tier)
- **Header:** `x-cg-pro-api-key: {API_KEY}` or `x_cg_pro_api_key: {API_KEY}`
- **Note:** Free tier has rate limits; Pro tier has higher limits and additional endpoints

## Rate Limits
- **Free Tier:** 10-50 requests per minute (varies by endpoint)
- **Pro Tier:** Higher limits (varies by plan)
- **Window:** Per minute
- **Note:** Implement rate limiting and respect rate limit headers

## Key Endpoints

### 1. Coin Markets
**Endpoint:** `GET /coins/markets`

**Purpose:** Get market data for multiple coins

**Parameters:**
- `vs_currency` (required): Target currency (e.g., 'usd')
- `ids` (optional): Comma-separated coin IDs (e.g., 'bitcoin,ethereum')
- `names` (optional): Comma-separated coin names
- `symbols` (optional): Comma-separated symbols (e.g., 'btc,eth')
- `category` (optional): Filter by category (e.g., 'layer-1')
- `order` (optional): Sort order - `market_cap_desc`, `market_cap_asc`, `volume_desc`, `volume_asc`, `id_asc`, `id_desc` (default: `market_cap_desc`)
- `per_page` (optional): Results per page (1-250, default: 100)
- `page` (optional): Page number (default: 1)
- `sparkline` (optional): Include 7-day sparkline (default: false)
- `price_change_percentage` (optional): Include price change % - `1h,24h,7d,14d,30d,200d,1y` (comma-separated)
- `precision` (optional): Price precision - `full` or `0-18` (default: `full`)

**Response Structure:**
```typescript
Array<{
  id: string;
  symbol: string;
  name: string;
  image: string;
  current_price: number;
  market_cap: number;
  market_cap_rank: number;
  fully_diluted_valuation: number;
  total_volume: number;
  high_24h: number;
  low_24h: number;
  price_change_24h: number;
  price_change_percentage_24h: number;
  market_cap_change_24h: number;
  market_cap_change_percentage_24h: number;
  circulating_supply: number;
  total_supply: number;
  max_supply: number;
  ath: number;
  ath_change_percentage: number;
  ath_date: string;
  atl: number;
  atl_change_percentage: number;
  atl_date: string;
  sparkline_in_7d?: {
    price: number[];
  };
  price_change_percentage_1h_in_currency?: number;
  price_change_percentage_24h_in_currency?: number;
  price_change_percentage_7d_in_currency?: number;
  price_change_percentage_30d_in_currency?: number;
  price_change_percentage_1y_in_currency?: number;
}>;
```

**Use Case:** Batch quote fetching for crypto holdings and watchlists

---

### 2. Coin Market Chart
**Endpoint:** `GET /coins/{id}/market_chart`

**Purpose:** Get historical market data (prices, market caps, volumes)

**Parameters:**
- `id` (path, required): Coin ID (e.g., 'bitcoin')
- `vs_currency` (required): Target currency (e.g., 'usd')
- `days` (required): Number of days of data (integer or 'max')
- `interval` (optional): Data interval - `5m`, `hourly`, `daily` (empty for auto)
- `precision` (optional): Price precision - `full` or `0-18`

**Response Structure:**
```typescript
{
  prices: Array<[timestamp: number, price: number]>;
  market_caps: Array<[timestamp: number, market_cap: number]>;
  total_volumes: Array<[timestamp: number, volume: number]>;
}
```

**Use Case:** Historical price charts and analysis

---

### 3. Coin Market Chart Range
**Endpoint:** `GET /coins/{id}/market_chart/range`

**Purpose:** Get historical market data within date range (Pro endpoint)

**Parameters:**
- `id` (path, required): Coin ID
- `vs_currency` (required): Target currency
- `from` (required): Start date (ISO date string or UNIX timestamp)
- `to` (required): End date (ISO date string or UNIX timestamp)
- `interval` (optional): `5m`, `hourly`, `daily`
- `precision` (optional): Price precision

**Response Structure:**
```typescript
{
  prices: Array<[timestamp: number, price: number]>;
  market_caps: Array<[timestamp: number, market_cap: number]>;
  total_volumes: Array<[timestamp: number, volume: number]>;
}
```

**Use Case:** Precise date range historical data

---

### 4. Contract Address Market Chart
**Endpoint:** `GET /coins/{id}/contract/{contract_address}/market_chart`

**Purpose:** Get historical market data for token contract

**Parameters:**
- `id` (path, required): Asset platform ID (e.g., 'ethereum')
- `contract_address` (path, required): Token contract address
- `vs_currency` (required): Target currency
- `days` (required): Number of days (integer or 'max')
- `interval` (optional): `5m`, `hourly`, `daily`
- `precision` (optional): Price precision

**Response Structure:**
```typescript
{
  prices: Array<[timestamp: number, price: number]>;
  market_caps: Array<[timestamp: number, market_cap: number]>;
  total_volumes: Array<[timestamp: number, volume: number]>;
}
```

**Use Case:** ERC-20 token historical data

---

### 5. Circulating Supply Chart
**Endpoint:** `GET /coins/{id}/circulating_supply_chart`

**Purpose:** Get historical circulating supply

**Parameters:**
- `id` (path, required): Coin ID
- `days` (required): Number of days (integer or 'max')
- `interval` (optional): `5m`, `hourly`, `daily`

**Response Structure:**
```typescript
{
  circulating_supply: Array<[timestamp: number, supply: string]>;
}
```

**Use Case:** Supply tracking and analysis

---

### 6. NFT Collection Data
**Endpoint:** `GET /nfts/{id}`

**Purpose:** Get NFT collection market data

**Parameters:**
- `id` (path, required): NFT collection ID (e.g., 'pudgy-penguins')

**Response Structure:**
```typescript
{
  id: string;
  contract_address: string;
  asset_platform_id: string;
  name: string;
  symbol: string;
  floor_price: {
    native_currency: number;
    usd: number;
  };
  market_cap: {
    native_currency: number;
    usd: number;
  };
  volume_24h: {
    native_currency: number;
    usd: number;
  };
  floor_price_24h_percentage_change: {
    usd: number;
    native_currency: number;
  };
  market_cap_24h_percentage_change: {
    usd: number;
    native_currency: number;
  };
  number_of_unique_addresses: number;
  total_supply: number;
  one_day_sales: number;
  one_day_average_sale_price: number;
  // ... many more fields
}
```

**Use Case:** NFT collection tracking

---

### 7. On-Chain Token Data
**Endpoint:** `GET /networks/{network}/tokens/multi/{addresses}`

**Purpose:** Get on-chain data for token contracts

**Parameters:**
- `network` (path, required): Network ID (e.g., 'solana')
- `addresses` (path, required): Comma-separated contract addresses
- `include` (optional): Attributes to include - `top_pools`
- `include_composition` (optional): Include pool composition (default: false)

**Response Structure:**
```typescript
{
  data: Array<{
    id: string;
    type: string;
    attributes: {
      address: string;
      name: string;
      symbol: string;
      decimals: number;
      image_url: string;
      coingecko_coin_id: string;
      total_supply: string;
      price_usd: string;
      fdv_usd: string;
      total_reserve_in_usd: string;
      volume_usd: {
        h24: string;
      };
      market_cap_usd: string;
    };
    relationships: {
      top_pools?: {
        data: Array<{
          id: string;
          type: string;
        }>;
      };
    };
  }>;
  included?: Array<any>;
}
```

**Use Case:** On-chain token metrics and liquidity data

---

### 8. Derivatives Exchange Data
**Endpoint:** `GET /derivatives/exchanges/{id}`

**Purpose:** Get derivatives exchange data

**Parameters:**
- `id` (path, required): Exchange ID (e.g., 'binance_futures')

**Response Structure:**
```typescript
{
  name: string;
  open_interest: number;
  url: string;
  country: string;
  image: string;
  trading_volume_24h_btc: number;
}
```

**Use Case:** Derivatives market data

---

## Error Handling

**Common Error Codes:**
- `400`: Bad request (invalid parameters)
- `401`: Unauthorized (invalid API key)
- `404`: Resource not found
- `429`: Rate limit exceeded
- `500`: Server error

**Error Response:**
```typescript
{
  error?: string;  // Error message
  status?: {
    error_code: number;
    error_message: string;
  };
}
```

## Integration Notes

1. **Coin IDs:**
   - Use `/coins/list` endpoint to get all coin IDs
   - Coin IDs are lowercase (e.g., 'bitcoin', 'ethereum')
   - Symbols are uppercase (e.g., 'BTC', 'ETH')

2. **Date Formats:**
   - ISO 8601: `YYYY-MM-DD` or `YYYY-MM-DDTHH:mm:ss`
   - UNIX timestamp: milliseconds for some endpoints

3. **Pagination:**
   - Use `page` and `per_page` parameters
   - Max `per_page`: 250
   - Default `per_page`: 100

4. **Rate Limiting:**
   - Free tier: 10-50 requests/minute
   - Implement exponential backoff
   - Use job queue with concurrency: 3-5 workers
   - Cache aggressively (1 minute TTL for quotes)

5. **Data Precision:**
   - Use `precision` parameter to control decimal places
   - `full` returns maximum precision
   - Numbers 0-18 limit decimal places

6. **Sparklines:**
   - 7-day price sparkline available
   - Useful for quick visualizations
   - Reduces need for separate historical calls

## Scraping Implementation

```typescript
// Example: CoinGecko Crypto Scraper
class CoinGeckoScraper {
  async fetchMarketData(symbols: string[], vsCurrency: string = 'usd') {
    // Map symbols to coin IDs
    // Fetch market data
    // Parse and cache results
  }
  
  async fetchHistoricalData(coinId: string, days: number | 'max', vsCurrency: string = 'usd') {
    // Fetch market chart
    // Parse price, market cap, volume arrays
  }
  
  async fetchContractData(platformId: string, contractAddress: string, vsCurrency: string = 'usd') {
    // Fetch contract-specific data
    // Map to on-chain metrics
  }
  
  async fetchNFTData(collectionId: string) {
    // Fetch NFT collection data
  }
}
```

## Cache Strategy
- **TTL:** 
  - Market data: 60 seconds
  - Historical data: 1 hour (for same day)
  - NFT data: 5 minutes
- **Key Format:** 
  - `coingecko:market:{symbols}:{vsCurrency}`
  - `coingecko:chart:{coinId}:{days}:{vsCurrency}`
  - `coingecko:contract:{platform}:{address}:{vsCurrency}`
  - `coingecko:nft:{collectionId}`

## Data Mapping to crypto_quotes_cache

```typescript
// Map CoinGecko response to crypto_quotes_cache table
const cryptoQuote = {
  symbol: marketData.symbol.toUpperCase(),
  coingecko_id: marketData.id,
  name: marketData.name,
  price: marketData.current_price,
  change_24h: marketData.price_change_percentage_24h,
  market_cap: marketData.market_cap,
  market_cap_rank: marketData.market_cap_rank,
  volume_24h: marketData.total_volume,
  circulating_supply: marketData.circulating_supply,
  total_supply: marketData.total_supply,
  max_supply: marketData.max_supply,
  ath: marketData.ath,
  ath_date: new Date(marketData.ath_date),
  atl: marketData.atl,
  atl_date: new Date(marketData.atl_date),
  data_source: 'coingecko',
  last_updated: new Date(),
  fetched_at: new Date()
};
```

