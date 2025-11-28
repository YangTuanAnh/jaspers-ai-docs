# Glassnode API Template

## Service Overview

**Provider:** Glassnode  
**Purpose:** On-chain analytics and blockchain metrics  
**Base URL:** `https://api.glassnode.com/v1/metrics/`  
**Documentation:** https://docs.glassnode.com/

Glassnode provides comprehensive on-chain analytics for Bitcoin, Ethereum, and other cryptocurrencies. The API offers metrics including network activity, market indicators, mining data, and options analytics.

## Authentication

Glassnode API uses API key authentication. The API key can be provided via:

1. **Query Parameter:** `api_key=YOUR_API_KEY`
2. **Header:** `x-api-key: YOUR_API_KEY`
3. **Authorization Header:** `Authorization: Bearer YOUR_API_KEY` or `Authorization: ApiKey YOUR_API_KEY` or `Authorization: ApiKeyAuth YOUR_API_KEY`

**Note:** Different endpoints may accept different authentication methods. It's recommended to use the `x-api-key` header for consistency.

## Rate Limits

- **Free Tier:** Limited requests per day
- **Paid Tiers:** Higher rate limits based on subscription
- **Recommendation:** Implement rate limiting with exponential backoff
- **Best Practice:** Cache responses aggressively as on-chain metrics don't change frequently

## Key Endpoints

### 1. Indicators Endpoints

#### GET /v1/metrics/indicators/net_unrealized_profit_loss

**Description:** Retrieves Net Unrealized Profit/Loss (NUPL) data, which measures the difference between market cap and realized cap.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/net_unrealized_profit_loss`

**Parameters:**
- **a** (string) - Required - Asset identifier (e.g., 'btc', 'eth')
- **api_key** (string) - Required - API key (can be in query or header)
- **s** (integer) - Optional - Start timestamp (Unix epoch)
- **u** (integer) - Optional - End timestamp (Unix epoch)
- **i** (string) - Optional - Interval (e.g., '24h', '1w', '1month')
- **f** (string) - Optional - Format ('json', 'csv')

**Request Example:**
```javascript
const apiKey = 'YOUR_API_KEY';
const assetId = 'BTC';
const url = `https://api.glassnode.com/v1/metrics/indicators/net_unrealized_profit_loss?a=${assetId}&api_key=${apiKey}`;

fetch(url, {
  method: 'GET',
  headers: {
    'Accept': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

**Response:**
```json
[
  {
    "t": 1640995200,
    "v": 0.45
  },
  {
    "t": 1641081600,
    "v": 0.47
  }
]
```

**Use Cases:**
- Market sentiment analysis
- Identifying market tops and bottoms
- On-chain metrics dashboard

---

#### GET /v1/metrics/indicators/nupl_more_155 (LTH-NUPL)

**Description:** Long-Term Holder Net Unrealized Profit/Loss for addresses holding coins for more than 155 days.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/nupl_more_155`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Request Example:**
```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC';
const url = `https://api.glassnode.com/v1/metrics/indicators/nupl_more_155?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Use Cases:**
- Long-term holder behavior analysis
- Market cycle identification

---

#### GET /v1/metrics/indicators/nupl_less_155 (STH-NUPL)

**Description:** Short-Term Holder Net Unrealized Profit/Loss for addresses holding coins for less than 155 days.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/nupl_less_155`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Short-term holder sentiment
- Trading activity analysis

---

#### GET /v1/metrics/indicators/mvrv_z_score

**Description:** MVRV Z-Score measures how overvalued or undervalued the market is relative to its realized value.

**Method:** GET

**Endpoint:** `/v1/metrics/market/mvrv_z_score`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Request Example:**
```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC';
const url = `https://api.glassnode.com/v1/metrics/market/mvrv_z_score?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Use Cases:**
- Market valuation analysis
- Buy/sell signal generation

---

#### GET /v1/metrics/indicators/nvt (NVT Ratio)

**Description:** Network Value to Transactions ratio, measuring the relationship between market cap and transaction volume.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/nvt`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Network utilization analysis
- Market efficiency metrics

---

#### GET /v1/metrics/indicators/sopr_more_155 (LTH-SOPR)

**Description:** Long-Term Holder Spent Output Profit Ratio.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/sopr_more_155`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Long-term holder profit-taking behavior

---

#### GET /v1/metrics/indicators/realized_profit

**Description:** Realized profit from on-chain transactions.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/realized_profit`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Profit realization tracking
- Market cycle analysis

---

#### GET /v1/metrics/indicators/realized_loss

**Description:** Realized loss from on-chain transactions.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/realized_loss`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Loss realization tracking
- Capitulation analysis

---

#### GET /v1/metrics/indicators/hash_ribbon

**Description:** Hash Ribbon indicator for mining health analysis.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/hash_ribbon`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Mining health monitoring
- Network security analysis

---

#### GET /v1/metrics/indicators/pi_cycle_top

**Description:** Pi Cycle Top indicator for identifying market tops.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/pi_cycle_top`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Market top identification
- Cycle analysis

---

### 2. Market Data Endpoints

#### GET /v1/metrics/market/price_usd_ohlc

**Description:** OHLC (Open, High, Low, Close) price data.

**Method:** GET

**Endpoint:** `/v1/metrics/market/price_usd_ohlc`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key
- **i** (string) - Optional - Interval

**Request Example:**
```javascript
fetch('https://api.glassnode.com/v1/metrics/market/price_usd_ohlc?a=BTC&api_keystring=YOUR_API_KEY')
  .then(response => response.json())
  .then(data => console.log(data));
```

**Use Cases:**
- Price history
- Charting data

---

#### GET /v1/metrics/market/marketcap_usd

**Description:** Market capitalization in USD.

**Method:** GET

**Endpoint:** `/v1/metrics/market/marketcap_usd`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Market cap tracking
- Valuation metrics

---

#### GET /v1/metrics/market/spot_volume_daily_sum

**Description:** Daily spot trading volume.

**Method:** GET

**Endpoint:** `/v1/metrics/market/spot_volume_daily_sum`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Volume analysis
- Liquidity metrics

---

#### GET /v1/metrics/market/realized_volatility_1_year

**Description:** 1-year realized volatility.

**Method:** GET

**Endpoint:** `/v1/metrics/market/realized_volatility_1_year`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Volatility analysis
- Risk metrics

---

#### GET /v1/metrics/market/spot_accumulation_distribution_line

**Description:** Spot Accumulation/Distribution Line (ADL).

**Method:** GET

**Endpoint:** `/v1/metrics/market/spot_accumulation_distribution_line`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Accumulation/distribution analysis
- Trend identification

---

#### GET /v1/metrics/market/spot_on_balance_volume

**Description:** Spot On-Balance Volume (OBV).

**Method:** GET

**Endpoint:** `/v1/metrics/market/spot_on_balance_volume`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Volume-price relationship analysis

---

#### GET /v1/metrics/market/mvrv_more_155

**Description:** Long-Term Holder MVRV (Market Value to Realized Value).

**Method:** GET

**Endpoint:** `/v1/metrics/market/mvrv_more_155`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Long-term holder valuation metrics

---

#### GET /v1/metrics/market/hodl_cave

**Description:** HODL Cave metric for long-term holder behavior.

**Method:** GET

**Endpoint:** `/v1/metrics/market/hodl_cave`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **i** (string) - Optional - Interval (e.g., '1w')
- **api_key** (string) - Required - API key

**Use Cases:**
- Long-term holder analysis

---

### 3. Options Endpoints

#### GET /v1/metrics/options/combo_premiums_sellers

**Description:** Options combo premiums from sellers.

**Method:** GET

**Endpoint:** `/v1/metrics/options/combo_premiums_sellers`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Request Example:**
```javascript
async function getComboPremiumsSellers(assetId) {
  const apiKey = 'YOUR_API_KEY';
  const url = `https://api.glassnode.com/v1/metrics/options/combo_premiums_sellers?a=${assetId}`;

  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
```

**Use Cases:**
- Options market analysis
- Derivatives sentiment

---

#### GET /v1/metrics/options/premiums_strike_heatmap

**Description:** Options net premium strike heatmap.

**Method:** GET

**Endpoint:** `/v1/metrics/options/premiums_strike_heatmap`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **period** (string) - Optional - Period (e.g., '1y')
- **api_key** (string) - Required - API key

**Use Cases:**
- Options flow analysis
- Strike price distribution

---

### 4. Mining Endpoints

#### GET /v1/metrics/mining/revenue_sum

**Description:** Total miner revenue.

**Method:** GET

**Endpoint:** `/v1/metrics/mining/revenue_sum`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Mining economics
- Network security metrics

---

### 5. Additional Indicators

#### GET /v1/metrics/indicators/investor_capitalization

**Description:** Investor capitalization metric.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/investor_capitalization`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Capital flow analysis

---

#### GET /v1/metrics/indicators/average_dormancy

**Description:** Average dormancy of coins.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/average_dormancy`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **api_key** (string) - Required - API key

**Use Cases:**
- Coin age analysis
- HODL behavior

---

#### GET /v1/metrics/indicators/cost_basis_distribution_heatmap

**Description:** Cost basis distribution heatmap.

**Method:** GET

**Endpoint:** `/v1/metrics/indicators/cost_basis_distribution_heatmap`

**Parameters:**
- **a** (string) - Required - Asset identifier
- **period** (string) - Optional - Period (e.g., '1month')
- **api_key** (string) - Required - API key

**Use Cases:**
- Cost basis analysis
- Support/resistance levels

---

## Error Handling

### Common Error Responses

**401 Unauthorized:**
```json
{
  "error": "Invalid API key"
}
```

**429 Too Many Requests:**
```json
{
  "error": "Rate limit exceeded"
}
```

**400 Bad Request:**
```json
{
  "error": "Invalid parameters"
}
```

### Error Handling Pattern

```javascript
async function fetchGlassnodeMetric(endpoint, params) {
  const apiKey = process.env.GLASSNODE_API_KEY;
  const url = `https://api.glassnode.com/v1/metrics/${endpoint}?${new URLSearchParams({
    ...params,
    api_key: apiKey
  })}`;

  try {
    const response = await fetch(url, {
      headers: {
        'Accept': 'application/json'
      }
    });

    if (!response.ok) {
      if (response.status === 401) {
        throw new Error('Invalid API key');
      } else if (response.status === 429) {
        throw new Error('Rate limit exceeded');
      } else {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    }

    return await response.json();
  } catch (error) {
    console.error('Glassnode API error:', error);
    throw error;
  }
}
```

## Integration Notes

### Asset Identifiers

Common asset identifiers:
- `btc` - Bitcoin
- `eth` - Ethereum
- `ltc` - Litecoin
- `bch` - Bitcoin Cash

### Time Intervals

Common interval values:
- `1h` - 1 hour
- `24h` - 24 hours (daily)
- `1w` - 1 week
- `1month` - 1 month
- `1y` - 1 year

### Timestamp Formats

- Unix epoch timestamps (seconds)
- Use `s` parameter for start time
- Use `u` parameter for end time

### Response Format

Most endpoints return arrays of objects with:
- `t` - Timestamp (Unix epoch)
- `v` - Value

## Scraping Implementation

### Example Scraper Structure

```typescript
interface GlassnodeScraperConfig {
  apiKey: string;
  assets: string[];
  metrics: string[];
  interval: string;
  cacheTtl: number;
}

class GlassnodeScraper {
  private config: GlassnodeScraperConfig;
  private baseUrl = 'https://api.glassnode.com/v1/metrics';

  constructor(config: GlassnodeScraperConfig) {
    this.config = config;
  }

  async fetchMetric(metric: string, asset: string, params?: Record<string, any>) {
    const url = `${this.baseUrl}/${metric}?a=${asset}&api_key=${this.config.apiKey}`;
    
    // Add additional parameters
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        url += `&${key}=${value}`;
      });
    }

    const response = await fetch(url, {
      headers: {
        'Accept': 'application/json',
        'x-api-key': this.config.apiKey
      }
    });

    if (!response.ok) {
      throw new Error(`Glassnode API error: ${response.status}`);
    }

    return await response.json();
  }

  async scrapeOnChainMetrics() {
    const results = [];

    for (const asset of this.config.assets) {
      for (const metric of this.config.metrics) {
        try {
          const data = await this.fetchMetric(metric, asset, {
            i: this.config.interval
          });
          
          results.push({
            asset,
            metric,
            data,
            timestamp: Date.now()
          });

          // Rate limiting
          await this.delay(1000);
        } catch (error) {
          console.error(`Error fetching ${metric} for ${asset}:`, error);
        }
      }
    }

    return results;
  }

  private delay(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

## Cache Strategy

### Recommended Cache TTL

- **Indicators (NUPL, MVRV, SOPR):** 300 seconds (5 minutes)
- **Market Data (Price, Volume):** 60 seconds (1 minute)
- **Options Data:** 300 seconds (5 minutes)
- **Mining Data:** 600 seconds (10 minutes)

### Cache Key Format

```
glassnode:{metric}:{asset}:{interval}:{timestamp}
```

Example:
```
glassnode:net_unrealized_profit_loss:btc:24h:1640995200
```

## Data Mapping

### Mapping to Database Entities

```typescript
interface OnChainMetric {
  id: string;
  asset: string;
  metric: string;
  value: number;
  timestamp: Date;
  source: 'glassnode';
  metadata?: {
    interval?: string;
    additionalParams?: Record<string, any>;
  };
}

function mapGlassnodeResponse(
  response: Array<{ t: number; v: number }>,
  asset: string,
  metric: string
): OnChainMetric[] {
  return response.map((point) => ({
    id: `glassnode_${asset}_${metric}_${point.t}`,
    asset: asset.toUpperCase(),
    metric,
    value: point.v,
    timestamp: new Date(point.t * 1000),
    source: 'glassnode'
  }));
}
```

## Use Cases in SOPHIA

1. **On-Chain Metrics Dashboard:**
   - NUPL, MVRV, SOPR for market sentiment
   - Real-time on-chain indicators

2. **Market Analysis:**
   - Cost basis distribution for support/resistance
   - Realized profit/loss for market cycles

3. **Risk Assessment:**
   - Volatility metrics
   - Mining health indicators

4. **Trading Signals:**
   - Hash Ribbon for mining signals
   - Pi Cycle Top for market tops
   - MVRV Z-Score for valuation

5. **Portfolio Analytics:**
   - Long-term vs short-term holder metrics
   - Accumulation/distribution patterns

## Notes

- Glassnode provides premium on-chain analytics that complement price data
- Most metrics are calculated with delays (on-chain data requires block confirmations)
- Consider subscription tier for production use
- Implement aggressive caching as metrics don't change frequently
- Use appropriate intervals to balance data freshness and API limits
- Combine with other data sources (price, volume) for comprehensive analysis

