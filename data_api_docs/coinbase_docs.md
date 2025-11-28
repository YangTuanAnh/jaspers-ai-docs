### Get Aggregated Candles Data

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Fetches aggregated candle data for a given instrument and granularity within a specified time range.

```APIDOC
export interface GetINTXAggregatedCandlesData {
  instrument: string;
  granularity: string;
  start: string;
  end?: string;
}
```

--------------------------------

### Execute Spot Tickers Example

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Shows how to run a JavaScript example for fetching tickers from the spot market using Node.js. This is useful for retrieving current market data.

```javascript
node ./examples/spot/getTickers.js
```

--------------------------------

### Coinbase App - Public REST API Example (TypeScript)

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Demonstrates fetching public data using the Coinbase App REST API. This includes retrieving general information available without authentication.

```typescript
import { CBAppClient } from "../src/CBAppClient";

// Assuming you have initialized the client elsewhere
// const client = new CBAppClient();

// Example: Get all public REST data
async function cbAppPublicRestAllExample(client: CBAppClient) {
  try {
    const response = await client.cbappPublicRestAll();
    console.log("Coinbase App Public REST All Response:", response);
  } catch (error) {
    console.error("Error getting Coinbase App public REST data:", error);
  }
}

```

--------------------------------

### Coinbase Data Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides methods for retrieving market data, including fiat and cryptocurrency lists, exchange rates, buy/sell/spot prices, and API server time.

```APIDOC
getFiatCurrencies(): Promise<any>
  - Lists known fiat currencies, conforming to ISO 4217 where possible.

getCryptocurrencies(): Promise<CBAppCryptocurrency[]>
  - Lists known cryptocurrencies supported by Coinbase.

getExchangeRates(params?: any): Promise<any>
  - Retrieves current exchange rates, with an optional base currency parameter (defaults to USD).

getBuyPrice(params: any): Promise<any>
  - Gets the total price to buy one unit of Bitcoin or Ether.

getSellPrice(params: any): Promise<any>
  - Gets the total price to sell one unit of Bitcoin or Ether.

getSpotPrice(params: any): Promise<any>
  - Retrieves the current market price for Bitcoin.

getCurrentTime(): Promise<any>
  - Fetches the current API server time.
```

--------------------------------

### Get Orders

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Demonstrates how to fetch order information using the Coinbase Advanced Trade API. Includes client initialization with API keys.

```typescript
import { CBAdvancedTradeClient } from '../../../src/index.js';

/**
 * import { CBAdvancedTradeClient } from 'coinbase-api';
 * const { CBAdvancedTradeClient } = require('coinbase-api');
 */

// initialise the client
/**
 * You can add both ED25519 and ECDSA keys, client will recognize both types of keys
 *
 * ECDSA:
 *
 * {
 *   apiKey: 'organizations/your_org_id/apiKeys/your_api_key_id',
 *   apiSecret:
 *     '-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIPT/TTZPxw0kDGvpuCENJp9A4/2INAt9/QKKfyidTWM8oAoGCCqGSM49\nAwEHoUQDQgAEd+cnxrKl536ly5eYBi+8dvXt1MJXYRo+/v38h9HrFKVGBRndU9DY\npV357xIfqeJEzb/MBuk3EW8cG9RTrYBwjg==\n-----END EC PRIVATE KEY-----\n',
 * }
 *
 * ED25519:
 * {
 *   apiKey: 'your-api-key-id',
 *   apiSecret: 'yourExampleApiSecretEd25519Version==',
 * }
 */

async function getOrders() {
  // Get all orders
  // Get order details
}
```

--------------------------------

### Subscribe to Coinbase Market Data Websocket

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Demonstrates how to subscribe to various market data topics using the WebsocketClient. This includes subscribing to single topics with string identifiers or structured objects, and handling multiple subscriptions.

```javascript
const { WebsocketClient } = require('coinbase-api');

// Subscribe to a single topic with a string identifier
// client.subscribe('status', 'exchangeMarketData');

// Subscribe to a single topic with a structured object
// const tickerSubscribeRequest = {
//   topic: 'ticker',
//   payload: {
//     product_ids: ['ETH-USD', 'ETH-EUR'],
//   },
// };
// client.subscribe(tickerSubscribeRequest, 'exchangeMarketData');

// Subscribe to multiple topics with an array of structured objects
// client.subscribe([level2SubscribeRequest, anotherRequest, etc], 'advTradeMarketData');
```

```typescript
import { WebsocketClient } from 'coinbase-api';

// Subscribe to a single topic with a string identifier
// client.subscribe('status', 'exchangeMarketData');

// Subscribe to a single topic with a structured object
// const tickerSubscribeRequest: WsTopicRequest = {
//   topic: 'ticker',
//   payload: {
//     product_ids: ['ETH-USD', 'ETH-EUR'],
//   },
// };
// client.subscribe(tickerSubscribeRequest, 'exchangeMarketData');

// Subscribe to multiple topics with an array of structured objects
// client.subscribe([level2SubscribeRequest, anotherRequest, etc], 'advTradeMarketData');
```

--------------------------------

### Get Portfolio Fills

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Fetches trade fills for a specific portfolio, with options to filter by order ID, client order ID, and time.

```APIDOC
export interface GetINTXPortfolioFillsRequest {
  portfolio: string;
  order_id?: string;
  client_order_id?: string;
  ref_datetime?: string;
  result_limit?: number;
  result_offset?: number;
  time_from?: string;
}
```

--------------------------------

### Public Market Data Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides access to public market data, including product details, order books, trades, and historical candle data. Requires product ID for most operations.

```APIDOC
getServerTime(): Promise<any>

getPublicProductBook(params: {
    product_id: string;
    limit?: number;
    aggregation_price_increment?: string;
}): Promise<any>

getPublicProducts(params?: any): Promise<any>

getPublicProduct(params: {
    product_id: string;
}): Promise<any>

getPublicProductCandles(
    params: any,
): Promise<any>

getPublicMarketTrades(
    params: any,
): Promise<any>
```

--------------------------------

### Coinbase Exchange Product Candles Request

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Defines the request parameters for retrieving historical candle data for a product on Coinbase Exchange. Requires product ID and granularity, with optional start and end times.

```APIDOC
GetCBExchProductCandles:
  product_id: string (required)
  granularity: number (required)
  start?: string
  end?: string
```

--------------------------------

### Coinbase Exchange Public API Calls

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Demonstrates how to initialize and use the CBExchangeClient for public API calls. This includes fetching data like currencies, trading pairs, and product volumes without requiring authentication.

```typescript
import { CBExchangeClient } from '../../src/index.js';

// Initialize the client, you can pass in api keys here if you have them but they are not required for public endpoints

async function publicExchangeCalls() {
  // Get all known currencies
  // Get a single currency by id
  // Get all known trading pairs
  // Get all product volume
  // Get all wrapped assets
  // ... implementation details ...
}
```

--------------------------------

### Coinbase International Exchange - Public REST API Example (TypeScript)

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Demonstrates using the Coinbase International Exchange public REST API to fetch market data and information. This includes getting product details and order books.

```typescript
import { CBInternationalClient } from "../src/CBInternationalClient";
import {
  GetProductRequest as GetIntlProductRequest,
  GetProductResponse as GetIntlProductResponse,
  GetProductsRequest as GetIntlProductsRequest,
  GetProductsResponse as GetIntlProductsResponse,
  GetCandlesRequest as GetIntlCandlesRequest,
  GetTradesRequest as GetIntlTradesRequest,
  GetTradesResponse as GetIntlTradesResponse,
} from "../src/types/request/coinbase-international";

// Assuming you have initialized the client elsewhere
// const client = new CBInternationalClient();

// Example: Get all products (Public)
async function getIntlProductsExample(client: CBInternationalClient) {
  const request: GetIntlProductsRequest = {};
  try {
    const response: GetIntlProductsResponse = await client.getProducts(request);
    console.log("International Exchange Products:", response.data.slice(0, 5));
  } catch (error) {
    console.error("Error getting international exchange products:", error);
  }
}

// Example: Get a specific product (Public)
async function getIntlProductExample(client: CBInternationalClient, productId: string) {
  const request: GetIntlProductRequest = { productId };
  try {
    const response: GetIntlProductResponse = await client.getProduct(request);
    console.log(`International Exchange Product ${productId}:`, response.data);
  } catch (error) {
    console.error(`Error getting international exchange product ${productId}:`, error);
  }
}

// Example: Get candles (Public)
async function getIntlCandlesExample(client: CBInternationalClient, productId: string) {
  const request: GetIntlCandlesRequest = {
    productId,
    start: new Date(Date.now() - 3600000).toISOString(), // Last hour
    end: new Date().toISOString(),
    granularity: "ONE_HOUR",
  };
  try {
    const response = await client.getCandles(request);
    console.log(`International Exchange Candles for ${productId}:`, response.data.slice(0, 5));
  } catch (error) {
    console.error(`Error getting international exchange candles for ${productId}:`, error);
  }
}

// Example: Get trades (Public)
async function getIntlTradesExample(client: CBInternationalClient, productId: string) {
  const request: GetIntlTradesRequest = {
    productId,
    limit: 5,
  };
  try {
    const response: GetIntlTradesResponse = await client.getTrades(request);
    console.log(`International Exchange Trades for ${productId}:`, response.data);
  } catch (error) {
    console.error(`Error getting international exchange trades for ${productId}:`, error);
  }
}

```

--------------------------------

### Coinbase International (INTX) Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides methods for accessing Coinbase International (INTX) data, specifically for index composition history and historical candle data.

```APIDOC
GetINTXIndexCompositionHistory(params: GetINTXIndexCompositionHistory): Promise<any>
  - Retrieves the historical composition of a specified index.
  - Parameters:
    - index: The index symbol (e.g., 'BTCUSD').
    - time_from: Optional start timestamp for the history.
    - result_limit: Optional limit for the number of results.
    - result_offset: Optional offset for pagination.

GetINTXIndexCandlesRequest(params: GetINTXIndexCandlesRequest): Promise<any>
  - Retrieves historical candle (OHLCV) data for a specified index.
  - Parameters:
    - index: The index symbol (e.g., 'BTCUSD').
    - granularity: The time interval for each candle (e.g., 'ONE_HOUR', 'ONE_DAY').
    - start: The start timestamp for the candle data.
    - end: Optional end timestamp for the candle data.
```

--------------------------------

### Execute Spot Tickers Example

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/examples/README.md

Shows how to execute a JavaScript example for fetching spot tickers from the Coinbase API using Node.js. This snippet assumes the file has been renamed to .js.

```bash
node ./examples/spot/getTickers.js
```

--------------------------------

### WebSocket Overview

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides an overview of different Coinbase WebSocket feeds, including Market Data, User Order Data, Coinbase Exchange, Coinbase Direct Market Data, INTX, and Prime feeds. Explains authentication requirements and data types.

```APIDOC
/**
   * Market Data is the traditional feed that provides updates for both orders and trades.
   * Most channels are now available without authentication.
   *
   * https://docs.cdp.coinbase.com/advanced-trade/docs/ws-overview
   */

/**
   * User Order Data provides updates for the orders of the user.
   *
   * https://docs.cdp.coinbase.com/advanced-trade/docs/ws-overview
   */

/**
   * Coinbase Market Data (part of Coinbase Exchange API) is the traditional feed which is available without authentication.
   *
   * https://docs.cdp.coinbase.com/exchange/docs/websocket-overview
   */

/**
   * Coinbase Direct Market Data has direct access to Coinbase Exchange servers and requires Authentication.
   *
   * https://docs.cdp.coinbase.com/exchange/docs/websocket-overview
   */

/**
   * The INTX WebSocket feed is publicly available and provides real-time market data updates for orders and trades.
   * The SDK must authenticate when subscribing to the WebSocket Feed the very first time.
   *
   * https://docs.cdp.coinbase.com/intx/docs/websocket-overview
   */

/**
   * The Prime WebSocket feed provides real-time market data updates for orders and trades. To begin
   * receiving feed messages, you must send a signed subscribe message to the server indicating
   * which channels and products to receive. The SDK will handle this automatically.
   *
   * https://docs.cdp.coinbase.com/prime/docs/websocket-feed
   */
```

--------------------------------

### Coinbase API: Market Data Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/docs/endpointFunctionList.md

Provides access to public market data, including product order books, product lists, individual product details, candle data, and ticker information. These endpoints are useful for market analysis.

```APIDOC
GET /api/v3/brokerage/market/product_book
  - Retrieves the order book for a product.

GET /api/v3/brokerage/market/products
  - Retrieves a list of available products.

GET /api/v3/brokerage/market/products/{product_id}
  - Retrieves details for a specific product.

GET /api/v3/brokerage/market/products/{product_id}/candles
  - Retrieves historical candle data for a product.

GET /api/v3/brokerage/market/products/{product_id}/ticker
  - Retrieves ticker information for a product.
```

--------------------------------

### Product and Market Data Interfaces

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Defines structures for product information, pricebooks, candles, and market trades.

```typescript
interface PriceLevel {
  price: string;
  size: string;
}

export interface AdvTradePricebook {
  product_id: string;
  bids: PriceLevel[];
  asks: PriceLevel[];
  time: string;
}

interface FCMTradingSessionDetails {
  is_session_open: boolean;
  open_time: string;
  close_time: string;
  session_state: string;
  after_hours_order_entry_disabled: boolean;
}

interface PerpetualDetails {
  open_interest: string;
  funding_rate: string;
  funding_time: string;
  max_leverage: string;
  base_asset_uuid: string;
  underlying_type: string;
}

interface FutureProductDetails {
  venue: string;
  contract_code: string;
  contract_expiry: string;
  contract_size: string;
  contract_root_unit: string;
  group_description: string;
  contract_expiry_timezone: string;
  group_short_description: string;
  risk_managed_by: string;
  contract_expiry_type: string;
  perpetual_details: PerpetualDetails;
  contract_display_name: string;
  time_to_expiry_ms: string;
  non_crypto: boolean;
  contract_expiry_name: string;
}

export interface AdvTradeProduct {
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
  fcm_trading_session_details: FCMTradingSessionDetails;
  mid_market_price: string;
  alias: string;
  alias_to: string[];
  base_display_symbol: string;
  quote_display_symbol: string;
  view_only: boolean;
  price_increment: string;
  display_name: string;
  product_venue: string;
  approximate_quote_24h_volume: string;
  future_product_details: FutureProductDetails;
}

export interface AdvTradeCandle {
  start: string;
  low: string;
  high: string;
  open: string;
  close: string;
  volume: string;
}

interface Trade {
  trade_id: string;
  product_id: string;
  price: string;
  size: string;
  time: string; // RFC3339 Timestamp
  side: 'BUY' | 'SELL';
}

export interface AdvTradeMarketTrades {
  trades: Trade[];
  best_bid: string;
  best_ask: string;
}
```

--------------------------------

### Coinbase Exchange - REST API Examples (TypeScript)

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides examples for interacting with the Coinbase Exchange REST API for both public and private endpoints. This includes fetching market data and managing trades.

```typescript
import { CBExchangeClient } from "../src/CBExchangeClient";
import {
  GetCandlesRequest,
  GetProductRequest,
  GetProductsRequest,
  GetServerTimeRequest,
  GetTimeInForceRequest,
  GetTimeInForceResponse,
  GetTIFsRequest,
  GetTIFsResponse,
  GetTradesRequest,
  ListOrdersRequest,
  OrderSide,
  OrderType,
  PlaceOrderRequest,
  PlaceOrderResponse,
  CancelOrderRequest,
  CancelOrderResponse,
  GetOrderRequest,
  GetOrderResponse,
  ListOrdersResponse,
  GetTradesResponse,
  GetProductResponse,
  GetProductsResponse,
  GetServerTimeResponse,
} from "../src/types/request/coinbase-exchange";

// Assuming you have initialized the client elsewhere
// const client = new CBExchangeClient(apiKey, apiSecret, passphrase);

// Example: Get server time (Public)
async function getServerTimeExample(client: CBExchangeClient) {
  const request: GetServerTimeRequest = {};
  try {
    const response: GetServerTimeResponse = await client.getServerTime(request);
    console.log("Server Time:", response.data.iso);
  } catch (error) {
    console.error("Error getting server time:", error);
  }
}

// Example: Get all products (Public)
async function getProductsExample(client: CBExchangeClient) {
  const request: GetProductsRequest = {};
  try {
    const response: GetProductsResponse = await client.getProducts(request);
    console.log("Products:", response.data.slice(0, 5)); // Log first 5 products
  } catch (error) {
    console.error("Error getting products:", error);
  }
}

// Example: Get a specific product (Public)
async function getProductExample(client: CBExchangeClient, productId: string) {
  const request: GetProductRequest = { productId };
  try {
    const response: GetProductResponse = await client.getProduct(request);
    console.log(`Product ${productId}:`, response.data);
  } catch (error) {
    console.error(`Error getting product ${productId}:`, error);
  }
}

// Example: Get candles (Public)
async function getCandlesExample(client: CBExchangeClient, productId: string) {
  const request: GetCandlesRequest = {
    productId,
    start: new Date(Date.now() - 3600000).toISOString(), // Last hour
    end: new Date().toISOString(),
    granularity: "ONE_HOUR",
  };
  try {
    const response = await client.getCandles(request);
    console.log(`Candles for ${productId}:`, response.data.slice(0, 5)); // Log first 5 candles
  } catch (error) {
    console.error(`Error getting candles for ${productId}:`, error);
  }
}

// Example: Get trades (Public)
async function getTradesExample(client: CBExchangeClient, productId: string) {
  const request: GetTradesRequest = {
    productId,
    limit: 5, // Get last 5 trades
  };
  try {
    const response: GetTradesResponse = await client.getTrades(request);
    console.log(`Trades for ${productId}:`, response.data);
  } catch (error) {
    console.error(`Error getting trades for ${productId}:`, error);
  }
}

// Example: Place a limit order (Private)
async function placeLimitOrderExample(client: CBExchangeClient, productId: string) {
  const request: PlaceOrderRequest = {
    productId,
    side: OrderSide.BUY,
    orderType: OrderType.LIMIT,
    baseSize: "0.01",
    limitPrice: "50000",
    timeInForce: "GTC", // Good 'Til Cancelled
  };
  try {
    const response: PlaceOrderResponse = await client.placeOrder(request);
    console.log("Place Order Response:", response.data);
  } catch (error) {
    console.error("Error placing order:", error);
  }
}

// Example: Cancel an order (Private)
async function cancelOrderExample(client: CBExchangeClient, orderId: string) {
  const request: CancelOrderRequest = { orderId };
  try {
    const response: CancelOrderResponse = await client.cancelOrder(request);
    console.log("Cancel Order Response:", response.data);
  } catch (error) {
    console.error(`Error cancelling order ${orderId}:`, error);
  }
}

// Example: Get a specific order (Private)
async function getOrderExample(client: CBExchangeClient, orderId: string) {
  const request: GetOrderRequest = { orderId };
  try {
    const response: GetOrderResponse = await client.getOrder(request);
    console.log(`Order ${orderId}:`, response.data);
  } catch (error) {
    console.error(`Error getting order ${orderId}:`, error);
  }
}

// Example: List all orders (Private)
async function listOrdersExample(client: CBExchangeClient, productId: string) {
  const request: ListOrdersRequest = {
    productId,
    limit: 10, // Get last 10 orders
  };
  try {
    const response: ListOrdersResponse = await client.listOrders(request);
    console.log(`Orders for ${productId}:`, response.data);
  } catch (error) {
    console.error(`Error listing orders for ${productId}:`, error);
  }
}

// Example: Get Time In Force options (Public)
async function getTimeInForceExample(client: CBExchangeClient) {
  const request: GetTIFsRequest = {};
  try {
    const response: GetTIFsResponse = await client.getTimeInForce(request);
    console.log("Time In Force Options:", response.data);
  } catch (error) {
    console.error("Error getting Time In Force options:", error);
  }
}

```

--------------------------------

### Coinbase API - Futures Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

This section details the API endpoints for managing and retrieving futures trading information, including balance and position data.

```APIDOC
/**
 * Futures Endpoints
 */

// Interface for futures balance information
export interface AdvTradeFuturesBalance {
  futures_buying_power: {
    // Example properties (actual properties may vary):
    amount: string;
    currency: string;
    // Additional fields like leverage, margin, etc. might be present
  };
  // Other relevant balance details might be included here
}

// GET /futures/balance
// Retrieves the user's futures trading balance information, including buying power.
// Response:
//   200 OK: Returns AdvTradeFuturesBalance object.
//   401 Unauthorized: Authentication failed.
//   500 Internal Server Error: Server error occurred.

// GET /futures/positions
// Retrieves a list of the user's open futures positions.
// Response:
//   200 OK: Returns an array of FuturesAdvTradePortfolioPosition objects.
//   401 Unauthorized: Authentication failed.
//   404 Not Found: No futures positions found.

// GET /perpetual/positions
// Retrieves a list of the user's open perpetual futures positions.
// Response:
//   200 OK: Returns an array of PerpAdvTradePortfolioPosition objects.
//   401 Unauthorized: Authentication failed.
//   404 Not Found: No perpetual futures positions found.
```

--------------------------------

### Coinbase App Client Currency and Pricing Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/docs/endpointFunctionList.md

Provides information about supported currencies and real-time pricing data. This includes fetching fiat currencies, cryptocurrencies, exchange rates, and buy/sell/spot prices for currency pairs.

```APIDOC
GET /v2/currencies

- **Description**: Retrieves a list of supported fiat currencies.
- **Authentication**: Not required.
- **Method**: GET

GET /v2/currencies/crypto

- **Description**: Retrieves a list of supported cryptocurrencies.
- **Authentication**: Not required.
- **Method**: GET

GET /v2/exchange-rates

- **Description**: Retrieves current exchange rates for various currencies.
- **Authentication**: Not required.
- **Method**: GET

GET /v2/prices/{currencyPair}/buy

- **Description**: Retrieves the current buy price for a given currency pair.
- **Parameters**: currencyPair (string, required)
- **Authentication**: Not required.
- **Method**: GET

GET /v2/prices/{currencyPair}/sell

- **Description**: Retrieves the current sell price for a given currency pair.
- **Parameters**: currencyPair (string, required)
- **Authentication**: Not required.
- **Method**: GET

GET /v2/prices/{currencyPair}/spot

- **Description**: Retrieves the current spot price for a given currency pair.
- **Parameters**: currencyPair (string, required)
- **Authentication**: Not required.
- **Method**: GET
```

--------------------------------

### Coinbase International Exchange - WebSocket Example (TypeScript)

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Demonstrates connecting to Coinbase International Exchange WebSockets for real-time market data streams. This includes subscribing to ticker and trade data.

```typescript
import { CBInternationalClient } from "../src/CBInternationalClient";
import { WsRequest } from "../src/types/request/websockets/requests";

// Assuming you have initialized the client elsewhere
// const client = new CBInternationalClient();

async function cbIntlWsExample(client: CBInternationalClient) {
  const wsClient = client.newWebSocketClient();

  const subscribeRequest: WsRequest = {
    type: "subscribe",
    channels: [
      { name: "ticker", product_ids: ["BTC-USD"] },
      { name: "trades", product_ids: ["BTC-USD"] },
    ],
  };

  wsClient.on("message", (message) => {
    console.log("Coinbase International WS Message:", message);
  });

  wsClient.on("error", (error) => {
    console.error("Coinbase International WS Error:", error);
  });

  wsClient.on("close", () => {
    console.log("Coinbase International WS Closed");
  });

  await wsClient.connect();
  await wsClient.send(JSON.stringify(subscribeRequest));
}

```

--------------------------------

### Coinbase API Portfolio Data Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/docs/endpointFunctionList.md

Provides access to various portfolio-specific data, including accruals, buying power, locates, margin conversions, and withdrawal power. All endpoints require authentication.

```APIDOC
GET /v1/portfolios/{portfolio_id}/accruals
  - Retrieves accruals for a specific portfolio.
  - Requires authentication.

GET /v1/portfolios/{portfolio_id}/buying_power
  - Retrieves buying power for a specific portfolio.
  - Requires authentication.

GET /v1/portfolios/{portfolio_id}/locates
  - Retrieves locates for a specific portfolio.
  - Requires authentication.

GET /v1/portfolios/{portfolio_id}/margin_conversions
  - Retrieves margin conversions for a specific portfolio.
  - Requires authentication.

GET /v1/portfolios/{portfolio_id}/withdrawal_power
  - Retrieves withdrawal power for a specific portfolio.
  - Requires authentication.
```

--------------------------------

### API Documentation - Coinbase Client Methods

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides an overview of the available methods for interacting with the Coinbase API, including public and private endpoints for various operations like data retrieval and order management.

```APIDOC
BaseRestClient:
  getClientType(): RestClientType
    - Defines the client type (affecting how requests & signatures behave).

  constructor(restClientOptions: RestClientOptions = {}, networkOptions: AxiosRequestConfig = {})
    - Creates an instance of the REST client.
    - Parameters:
      - restClientOptions: Options to configure REST API connectivity.
      - networkOptions: HTTP networking options for axios.

  getSignTimestampMs(): number
    - Timestamp used to sign the request. Override this method to implement your own timestamp/sync mechanism.

  get(endpoint: string, params?: object)
    - Makes a GET request to a public endpoint.

  post(endpoint: string, params?: ParamsInRequest)
    - Makes a POST request to a public endpoint.

  getPrivate(endpoint: string, params?: object)
    - Makes a GET request to a private endpoint (automatically signed).

  postPrivate(endpoint: string, params?: ParamsInRequest)
    - Makes a POST request to a private endpoint (automatically signed).

  deletePrivate(endpoint: string, params?: ParamsInRequest)
    - Makes a DELETE request to a private endpoint (automatically signed).

  putPrivate(endpoint: string, params?: ParamsInRequest)
    - Makes a PUT request to a private endpoint (automatically signed).

  patchPrivate(endpoint: string, params?: ParamsInRequest)
    - Makes a PATCH request to a private endpoint (automatically signed).

  _call(method: Method, endpoint: string, params?: ParamsInRequest, isPublicApi?: boolean): Promise<any>
    - Private method to make an HTTP request to a specific endpoint. Private endpoint API calls are automatically signed.
```

--------------------------------

### Coinbase API Entity Data Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/docs/endpointFunctionList.md

Provides access to various entity-specific data, including accruals, locate availabilities, margin information, tiered fees, aggregate positions, general positions, assets, and payment methods. All endpoints require authentication.

```APIDOC
GET /v1/entities/{entity_id}/accruals
  - Retrieves accruals for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/locates_availability
  - Retrieves locate availabilities for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/margin
  - Retrieves margin information for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/margin_summaries
  - Retrieves margin summaries for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/tf_tiered_fees
  - Retrieves tiered fees for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/aggregate_positions
  - Retrieves aggregate positions for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/positions
  - Retrieves positions for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/assets
  - Retrieves assets for a specific entity.
  - Requires authentication.

GET /v1/entities/{entity_id}/payment-methods
  - Retrieves payment methods for a specific entity.
  - Requires authentication.
```

--------------------------------

### Subscribe to Public Websocket Topics

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Shows how to subscribe to various public market data topics using the client.subscribe method. Topics can be simple strings or structured objects with payloads for specific parameters like product IDs.

```javascript
// Subscribe to heartbeats for advanced trade market data
client.subscribe('heartbeats', 'advTradeMarketData');

// Subscribe to user data for futures balance summary
client.subscribe('futures_balance_summary', 'advTradeUserData');

// Subscribe to ticker data with specific product IDs
const tickerSubscribeRequest = {
  topic: 'ticker',
  payload: {
    product_ids: ['ETH-USD', 'BTC-USD'],
  },
};
client.subscribe(tickerSubscribeRequest, 'advTradeMarketData');

// Subscribe to multiple topics at once
client.subscribe([
  {
    topic: 'candles',
    payload: {
      product_ids: ['ETH-USD'],
    },
  },
  {
    topic: 'market_trades',
    payload: {
      product_ids: ['ETH-USD', 'BTC-USD'],
    },
  },
  {
    topic: 'ticker',
    payload: {
      product_ids: ['ETH-USD', 'BTC-USD'],
    },
  },
  {
    topic: 'ticker_batch',
    payload: {
      product_ids: ['ETH-USD', 'BTC-USD'],
    },
  },
  {
    topic: 'level2',
    payload: {
      product_ids: ['ETH-USD', 'BTC-USD'],
    },
  },
], 'advTradeMarketData');
```

--------------------------------

### Coinbase Advanced Trade Client Methods

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides documentation for methods within the CBAdvancedTradeClient class, covering functionalities like fetching latency, managing accounts, and retrieving product information.

```APIDOC
CBAdvancedTradeClient
  extends BaseRestClient

  constructor(restClientOptions: RestClientOptions = {}, requestOptions: AxiosRequestConfig = {})

  /**
   * Custom SDK functions
   */
  fetchLatencySummary(): Promise<any>
    // This method is used to get the latency and time sync between the client and the server.
    // This is not official API endpoint and is only used for internal testing purposes.
    // Use this method to check the latency and time sync between the client and the server.
    // Final values might vary slightly, but it should be within few ms difference.
    // If you have any suggestions or improvements to this measurement, please create an issue or pull request on GitHub.

  getClientType(): RestClientType

  /**
   * Account Endpoints
   */
  /**
   * List Accounts
   *
   * Get a list of authenticated accounts for the current user.
   */
  getAccounts(params?: {
    limit?: number;
    cursor?: string;
    retail_portfolio_id?: string; // deprecated
  }): Promise<AdvTradeAccountsList>

  /**
   * Get Account
   *
   * Get a list of information about single account, given an account UUID.
   * Tip: Use List Accounts (getAccounts funcion) to find account UUIDs.
   */
  getAccount(params: {
    accountId: string;
  }): Promise<AdvTradeAccount>

  /**
   * Products Endpoints
   */
  /**
   * Get Best Bid/Ask
   *
   * Get the best bid/ask for all products. A subset of all products can be returned instead by using the product_ids input.
   */
  getBestBidAsk(params?: {
    product_ids?: string[];
  }): Promise<AdvTradePricebook>
```

--------------------------------

### Coinbase Currencies API

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides information about currencies supported by Coinbase. Includes endpoints to retrieve a comprehensive list of all known currencies and to fetch details for a specific currency by its ID.

```APIDOC
getCurrencies(): Promise<any>
  - Get all known currencies.
  - Gets a list of all known currencies. Note: Not all currencies may be currently in use for trading.

getCurrency(currency_id: string): Promise<any>
  - Get a currency.
  - Gets a single currency by id.
```

--------------------------------

### Coinbase Accounts API

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Provides methods to interact with Coinbase wallets. Specifically, it allows fetching all of a user's available Coinbase wallets, which are used for buying and selling on the Coinbase platform.

```APIDOC
getCoinbaseWallets(): Promise<any>
  - Get all Coinbase wallets.
  - Gets all the user's available Coinbase wallets. These are the wallets/accounts that are used for buying and selling on www.coinbase.com.
```

--------------------------------

### Coinbase Advanced Trade - WebSocket Examples (TypeScript)

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Shows how to connect to Coinbase Advanced Trade WebSockets for private and public data streams. This includes subscribing to market data and account updates.

```typescript
import { CoinbaseAdvancedTradeClient } from "../src/CBAdvancedTradeClient";
import { WsRequest } from "../src/types/request/websockets/requests";

// Assuming you have initialized the client elsewhere with your API keys for private streams
// const client = new CoinbaseAdvancedTradeClient(apiKey, apiSecret, passphrase);

// Example: Connect to private WebSocket
async function privateWsExample(client: CoinbaseAdvancedTradeClient) {
  const wsClient = client.newWebSocketClient();

  const subscribeRequest: WsRequest = {
    type: "subscribe",
    channels: [
      { name: "user" }, // Example channel for user events
      // Add other private channels as needed
    ],
  };

  wsClient.on("message", (message) => {
    console.log("Private WS Message:", message);
  });

  wsClient.on("error", (error) => {
    console.error("Private WS Error:", error);
  });

  wsClient.on("close", () => {
    console.log("Private WS Closed");
  });

  await wsClient.connect();
  await wsClient.send(JSON.stringify(subscribeRequest));
}

// Example: Connect to public WebSocket
async function publicWsExample(client: CoinbaseAdvancedTradeClient) {
  const wsClient = client.newWebSocketClient();

  const subscribeRequest: WsRequest = {
    type: "subscribe",
    channels: [
      { name: "level2", product_ids: ["BTC-USD"] }, // Example channel for L2 order book
      // Add other public channels as needed
    ],
  };

  wsClient.on("message", (message) => {
    console.log("Public WS Message:", message);
  });

  wsClient.on("error", (error) => {
    console.error("Public WS Error:", error);
  });

  wsClient.on("close", () => {
    console.log("Public WS Closed");
  });

  await wsClient.connect();
  await wsClient.send(JSON.stringify(subscribeRequest));
}

```

--------------------------------

### Account Interfaces

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Defines the structure for account-related data, including balance, available funds, and account status.

```typescript
interface Balance {
  value: string;
  currency: string;
}

export interface AdvTradeAccount {
  uuid: string;
  name: string;
  currency: string;
  available_balance: Balance;
  default: boolean;
  active: boolean;
  created_at: string;
  updated_at: string;
  deleted_at: string;
  type: string;
  ready: boolean;
  hold: Balance;
  retail_portfolio_id: string;
  platform: string;
}

export interface AdvTradeAccountsList {
  accounts: AdvTradeAccount[];
  has_next: boolean;
  cursor: string;
  size: number;
}
```

--------------------------------

### Coinbase API Endpoints

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

This section details various endpoints available in the Coinbase API for managing trading data, orders, portfolios, and loans. It includes descriptions of their functionality, parameters, and return types.

```APIDOC
Trading Data Endpoints:

getDailyTradingVolumes(params: GetINTXDailyTradingVolumes): Promise<any>
  Retrieves the trading volumes for each instrument separated by day.

getAggregatedCandlesData(params: GetINTXAggregatedCandlesData): Promise<any>
  Retrieves a list of aggregated candles data for a given instrument, granularity, and time range.

getHistoricalFundingRates(params: { instrument: string; result_limit?: number; result_offset?: number; }): Promise<any>
  Retrieves the historical funding rates for a specific instrument.

Position Offsets Endpoints:

getPositionOffsets(): Promise<any>
  Returns all active position offsets.

Orders Endpoints:

submitOrder(params: SubmitINTXOrderRequest): Promise<any>
  Creates a new order.

getOpenOrders(params?: GetINTXOpenOrdersRequest): Promise<any>
  Returns a list of active orders resting on the order book matching the requested criteria. Does not return any rejected, cancelled, or fully filled orders as they are not active.

cancelOrders(params: CancelINTXOrdersRequest): Promise<any>
  Cancels all orders matching the requested criteria.

updateOpenOrder(params: UpdateINTXOpenOrderRequest): Promise<any>
  Modifies an open order.

getOrderDetails(params: ...): Promise<any>
  Retrieves a single order. The order retrieved can be either active or inactive.

cancelOrder(params: ...): Promise<any>
  Cancels a single open order.

Portfolios Endpoints:

getUserPortfolios(): Promise<any>
  Returns all of the user's portfolios.

createPortfolio(params: ...): Promise<any>
  Create a new portfolio. Request will fail if no name is provided or if user already has max number of portfolios. Max number of portfolios is 20.

updatePortfolioParameters(params: UpdateINTXPortfolioParametersRequest): Promise<any>
  Update parameters for existing portfolio.

getUserPortfolio(params: ...): Promise<any>
  Returns the user's specified portfolio.

updatePortfolio(params: ...): Promise<any>
  Update existing user portfolio.

getPortfolioDetails(params: ...): Promise<any>
  Retrieves the summary, positions, and balances of a portfolio.

getPortfolioSummary(params: ...): Promise<any>
  Retrieves the high level overview of a portfolio.

getPortfolioBalances(params: ...): Promise<any>
  Returns all of the balances for a given portfolio.
getBalanceForPortfolioAsset(params: { portfolio: string; asset: string; }): Promise<any>
  Retrieves the balance for a given portfolio and asset.

getActiveLoansForPortfolio(params: ...): Promise<any>
  Retrieves all loan info for a given portfolio.

getLoanInfoForPortfolioAsset(params: { portfolio: string; asset: string; }): Promise<any>
  Retrieves the loan info for a given portfolio and asset.

acquireOrRepayLoan(params: { portfolio: string; asset: string; amount: number; action: 'ACQUIRE' | 'REPAY'; }): Promise<any>
  Acquire or repay loan for a given portfolio and asset.

previewLoanUpdate(params: { portfolio: string; asset: string; action: 'ACQUIRE' | 'REPAY'; amount: string; }): Promise<any>
  Preview acquire or repay loan for a given portfolio and asset.

getMaxLoanAvailability(params: { portfolio: string; asset: string; }): Promise<any>
  View the maximum amount of loan that could be acquired now for a given portfolio and asset.

getPortfolioPositions(params: ...): Promise<any>
  Returns all of the positions for a given portfolio.

getPositionForPortfolioInstrument(params: { portfolio: string; instrument: string; }): Promise<any>
  Retrieves the position for a given portfolio and symbol.

get total open position limit(params: ...): Promise<any>
  Retrieves the total open position limit across instruments for a given portfolio.
```

--------------------------------

### Coinbase API - Stake-Wraps

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Endpoints for managing stake-wraps on Coinbase. This includes retrieving all stake-wraps, creating new stake-wraps by staking and wrapping funds, and fetching details for a specific stake-wrap.

```APIDOC
getAllStakeWraps(params?: GetCBExchAllStakeWraps): Promise<any>
  - Get all stake-wraps
  - Get details for all stake-wraps in the profile associated with the API key.
```

```APIDOC
createStakeWrap(params: {
    from_currency: string;
    to_currency: string;
    amount: string;
}): Promise<any>
  - Create a new stake-wrap
  - Stakes and wraps from_currency to to_currency. Funds are stake-wrapped in the profile associated with the API key.
```

```APIDOC
getStakeWrap(params: any): Promise<any>
  - Get a single stake-wrap
  - Get details for a specific stake-wrap in the profile associated with the API key.
```

--------------------------------

### Coinbase API: Report Management

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/docs/endpointFunctionList.md

Endpoints for generating and retrieving various reports. Supports creating new reports and fetching existing ones by ID.

```APIDOC
GET /reports
  - Retrieves all available reports.

POST /reports
  - Creates a new report.

GET /reports/{report_id}
  - Retrieves a specific report by its ID.
  - Parameters:
    - report_id: The ID of the report to retrieve.
```

--------------------------------

### Coinbase App Travel Rule Data

Source: https://github.com/tiagosiebler/coinbase-api/blob/master/llms.txt

Specifies the data structure for travel rule compliance in the Coinbase App, including wallet type, self-declaration, beneficiary details, and transfer purpose.

```typescript
export interface CBAppTravelRuleData {
  beneficiary_wallet_type: 'WALLET_TYPE_SELF_HOSTED' | 'WALLET_TYPE_EXCHANGE';
  is_self: 'IS_SELF_FALSE' | 'IS_SELF_TRUE';
  beneficiary_name: string;
  beneficiary_address: CBAppBeneficiaryAddress;
  beneficiary_financial_institution: string;
  transfer_purpose: string;
}
```