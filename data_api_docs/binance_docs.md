### Initialize Binance MainClient and Fetch Data (JavaScript)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Demonstrates initializing the MainClient for Spot, Margin, and other core Binance products. It shows how to optionally provide API keys for private calls and includes examples for fetching account trade lists and exchange information. Error handling is included via .catch().

```javascript
import { MainClient } from 'binance';

// or, if you prefer `require()`:
// const { MainClient } = require('binance');

const API_KEY = 'xxx';
const API_SECRET = 'yyy';

const client = new MainClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  // Connect to testnet environment
  // testnet: true,
});

client
  .getAccountTradeList({ symbol: 'BTCUSDT' })
  .then((result) => {
    console.log('getAccountTradeList result: ', result);
  })
  .catch((err) => {
    console.error('getAccountTradeList error: ', err);
  });

client
  .getExchangeInfo()
  .then((result) => {
    console.log('getExchangeInfo inverse result: ', result);
  })
  .catch((err) => {
    console.error('getExchangeInfo inverse error: ', err);
  });
```

--------------------------------

### Fetch 24hr Price Change Statistics using Binance SDK

Source: https://context7.com/tiagosiebler/binance/llms.txt

Shows how to retrieve 24-hour price change statistics for a single symbol or multiple symbols using the Binance SDK's MainClient. This returns data like price change, volume, and weighted average price.

```javascript
// Get 24hr price change statistics for a single symbol
client.get24hrChangeStatistics({ symbol: 'BTCUSDT' })
  .then(result => {
    console.log('BTC/USDT 24h stats:', result);
    // Result includes: priceChange, priceChangePercent, weightedAvgPrice,
    // prevClosePrice, lastPrice, volume, quoteVolume, etc.
  })
  .catch(err => console.error('Error:', err));

// Get 24hr stats for multiple symbols
client.get24hrChangeStatistics({ symbols: ['BTCUSDT', 'ETHUSDT'] })
  .then(results => console.log('Multiple tickers:', results))
  .catch(err => console.error('Error:', err));
```

--------------------------------

### Retrieve Binance Exchange Information using SDK

Source: https://context7.com/tiagosiebler/binance/llms.txt

Illustrates how to fetch comprehensive exchange information, including trading rules, supported symbols, and filters, using the `getExchangeInfo` method of the Binance SDK's MainClient. This data is crucial for understanding trading parameters.

```javascript
// Get exchange information including trading rules
client.getExchangeInfo()
  .then(info => {
    console.log('Exchange timezone:', info.timezone);
    console.log('Available symbols:', info.symbols.length);
    // Use info.symbols to find trading pairs, filters, permissions
  })
  .catch(err => console.error('Error:', err));
```

--------------------------------

### Fetch Account Trade History using Binance SDK

Source: https://context7.com/tiagosiebler/binance/llms.txt

Demonstrates how to retrieve a user's account trade history for a specific symbol using the `getAccountTradeList` method. The example fetches the last 10 trades for BTCUSDT and logs details for each trade.

```javascript
// Get account trade history
client.getAccountTradeList({ symbol: 'BTCUSDT', limit: 10 })
  .then(trades => {
    trades.forEach(trade => {
      console.log(`Trade ${trade.id}: ${trade.qty} @ ${trade.price}`);
    });
  })
  .catch(err => console.error('Error:', err));
```

--------------------------------

### Subscribe to User Data Streams in JavaScript

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Demonstrates how to subscribe to various user data streams including spot, margin, isolated margin, USD futures, and portfolio margin streams.

```javascript
wsClient.subscribeSpotUserDataStream();
wsClient.subscribeMarginUserDataStream();
wsClient.subscribeIsolatedMarginUserDataStream('BTCUSDT');
wsClient.subscribeUsdFuturesUserDataStream();
wsClient.subscribePortfolioMarginUserDataStream();
```

--------------------------------

### Initialize Binance Coin-M Futures Client and Fetch Ticker (JavaScript)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

This snippet demonstrates initializing the CoinMClient for Binance Coin-Margined Futures. API credentials are optional but required for private calls. It includes an example of fetching the order book ticker for a symbol and includes error handling.

```javascript
import { CoinMClient } from 'binance';

// or, if you prefer `require()`:
// const { CoinMClient } = require('binance');

const API_KEY = 'xxx';
const API_SECRET = 'yyy';

const client = new CoinMClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  // Connect to testnet environment
  // testnet: true,
});

client
  .getSymbolOrderBookTicker()
  .then((result) => {
    console.log('getSymbolOrderBookTicker result: ', result);
  })
  .catch((err) => {
    console.error('getSymbolOrderBookTicker error: ', err);
  });
```

--------------------------------

### Subscribe to Public Topics in JavaScript

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Illustrates how to subscribe to public market data streams for futures and spot markets. Topics can be subscribed individually or in batches.

```javascript
wsClient.subscribe('btcusd@indexPrice', 'coinm');
wsClient.subscribe('btcusd@miniTicker', 'coinm');

wsClient.subscribe(
  ['btcusdt@aggTrade', 'btcusdt@markPrice', '!ticker@arr', '!miniTicker@arr'],
  'usdm'
);

wsClient.subscribe(
  [
    '!ticker_1h@arr',
    'btcusdt@bookTicker',
    'btcusdt@avgPrice',
    'btcusdt@depth10@100ms',
    'btcusdt@depth'
  ],
  'main'
);
```

--------------------------------

### Execute Spot Trading Operations via WebSocket (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Demonstrates various Spot market trading operations using the initialized WebsocketAPIClient. This includes fetching server time, exchange information, order books, recent trades, testing and submitting orders, checking order status, canceling orders, retrieving account information, and fetching trade history.

```javascript
// Async/await pattern - feels like REST API
async function tradeExample() {
  try {
    // Get server time
    const serverTime = await wsApiClient.getSpotServerTime();
    console.log('Server time:', serverTime.serverTime);

    // Get exchange info
    const exchangeInfo = await wsApiClient.getSpotExchangeInfo();
    console.log('Trading symbols:', exchangeInfo.symbols.length);

    // Get order book
    const orderBook = await wsApiClient.getSpotOrderBook({
      symbol: 'BTCUSDT',
      limit: 10,
    });
    console.log('Best bid:', orderBook.bids[0]);
    console.log('Best ask:', orderBook.asks[0]);

    // Get recent trades
    const trades = await wsApiClient.getSpotRecentTrades({
      symbol: 'BTCUSDT',
      limit: 5,
    });
    trades.forEach(trade => {
      console.log(`Trade: ${trade.price} x ${trade.qty}`);
    });

    // Test order (doesn't execute, just validates)
    const testResult = await wsApiClient.testSpotOrder({
      symbol: 'BTCUSDT',
      side: 'BUY',
      type: 'LIMIT',
      timeInForce: 'GTC',
      price: '30000.00',
      quantity: '0.001',
      timestamp: Date.now(),
    });
    console.log('Test order valid:', testResult);

    // Submit real order
    const order = await wsApiClient.submitNewSpotOrder({
      symbol: 'BTCUSDT',
      side: 'BUY',
      type: 'LIMIT',
      timeInForce: 'GTC',
      price: '30000.00',
      quantity: '0.001',
    });
    console.log('Order placed:', order.orderId);
    console.log('Status:', order.status);

    // Check order status
    const orderStatus = await wsApiClient.getSpotOrderStatus({
      symbol: 'BTCUSDT',
      orderId: order.orderId,
      timestamp: Date.now(),
    });
    console.log('Order status:', orderStatus.status);
    console.log('Executed:', orderStatus.executedQty);

    // Cancel order
    const cancelResult = await wsApiClient.cancelSpotOrder({
      symbol: 'BTCUSDT',
      orderId: order.orderId,
      timestamp: Date.now(),
    });
    console.log('Order cancelled:', cancelResult.orderId);

    // Get account information
    const accountInfo = await wsApiClient.getSpotAccountInformation({
      timestamp: Date.now(),
    });
    console.log('Account balances:');
    accountInfo.balances.forEach(balance => {
      if (parseFloat(balance.free) > 0 || parseFloat(balance.locked) > 0) {
        console.log(`${balance.asset}: ${balance.free} (locked: ${balance.locked})`);
      }
    });

    // Get trade history
    const myTrades = await wsApiClient.getSpotMyTrades({
      symbol: 'BTCUSDT',
      limit: 10,
    });
    myTrades.forEach(trade => {
      console.log(`Trade ${trade.id}: ${trade.qty} @ ${trade.price}`);
      console.log(`  Commission: ${trade.commission} ${trade.commissionAsset}`);
    });

  } catch (error) {
    console.error('Error:', error);
  }
}
```

--------------------------------

### Initialize and Use Binance Portfolio Margin Client (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Initializes the PortfolioClient with API credentials and demonstrates how to fetch account balances, submit new USD-M orders, and retrieve account information using the Binance REST API. Requires the 'binance' library. Outputs account-specific data and order details.

```javascript
import { PortfolioClient } from 'binance';

const portfolioClient = new PortfolioClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  // Optional: connect to testnet
  // testnet: true,
});

// Get portfolio margin account balance
portfolioClient.getBalance()
  .then(balances => {
    balances.forEach(balance => {
      console.log(`${balance.asset}: ${balance.balance}`);
    });
  })
  .catch(err => console.error('Error:', err));

// Submit a new USD-M order via portfolio margin account
portfolioClient.submitNewUMOrder({
  symbol: 'BTCUSDT',
  side: 'SELL',
  type: 'MARKET',
  quantity: 0.001,
})
  .then(order => {
    console.log('Portfolio margin order:', order.orderId);
    console.log('Status:', order.status);
  })
  .catch(err => console.error('Error:', err));

// Get account information
portfolioClient.getAccountInformation()
  .then(account => {
    console.log('Max withdraw:', account.maxWithdrawAmount);
    console.log('Total margin balance:', account.totalMarginBalance);
    console.log('Total position value:', account.totalPositionInitialMargin);
  })
  .catch(err => console.error('Error:', err));

```

--------------------------------

### Initialize Binance Portfolio Margin Client and Submit Order (JavaScript)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Details initializing the PortfolioClient for Binance Portfolio Margin trading. API keys are optional but necessary for private endpoints. The example shows fetching account balances and submitting a new UM order, with included error handling.

```javascript
import { PortfolioClient } from 'binance';

// or, if you prefer `require()`:
// const { PortfolioClient } = require('binance');

const API_KEY = 'xxx';
const API_SECRET = 'yyy';

const client = new PortfolioClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  // Connect to testnet environment
  // testnet: true,
});

client
  .getBalance()
  .then((result) => {
    console.log('getBalance result: ', result);
  })
  .catch((err) => {
    console.error('getBalance error: ', err);
  });

client
  .submitNewUMOrder({
    side: 'SELL',
    symbol: 'BTCUSDT',
    type: 'MARKET',
    quantity: 0.001,
  })
  .then((result) => {
    console.log('submitNewUMOrder result: ', result);
  })
  .catch((err) => {
    console.error('submitNewUMOrder error: ', err);
  });
```

--------------------------------

### Connect and Consume Binance WebSocket Streams (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Establishes a WebSocket connection using the 'binance' library to receive real-time market and user data. It handles raw and formatted messages, connection lifecycle events, and various subscription types for different Binance products. Requires API credentials for user data streams.

```javascript
import { WebsocketClient } from 'binance';

const wsClient = new WebsocketClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  // Automatically format incoming data to readable objects
  beautify: true,
  // Optional: connect to testnet
  // testnet: false,
});

// Listen to raw WebSocket messages
wsClient.on('message', data => {
  console.log('Raw message:', JSON.stringify(data, null, 2));
});

// Listen to formatted messages (requires beautify: true)
wsClient.on('formattedMessage', data => {
  console.log('Formatted message:', data);
});

// Monitor connection lifecycle events
wsClient.on('open', data => {
  console.log('WebSocket connected:', data.wsKey);
});

wsClient.on('reconnecting', data => {
  console.log('Reconnecting...', data.wsKey);
});

wsClient.on('reconnected', data => {
  console.log('Reconnected successfully:', data.wsKey);
  // Good time to sync missed data via REST API
});

wsClient.on('exception', data => {
  console.error('WebSocket error:', data);
});

// Subscribe to spot market streams (multiple topics at once)
wsClient.subscribe([
  // 24hr rolling window statistics
  'btcusdt@ticker',
  // Best bid/ask updates
  'btcusdt@bookTicker',
  // Trade streams
  'btcusdt@trade',
  // Kline/candlestick updates
  'btcusdt@kline_1m',
  // Order book depth updates
  'btcusdt@depth',
], 'main'); // 'main' connects to spot WebSocket

// Subscribe to USD-M futures streams
wsClient.subscribe([
  // Aggregate trade streams
  'btcusdt@aggTrade',
  // Mark price updates
  'btcusdt@markPrice',
  // All market mini tickers
  '!miniTicker@arr',
], 'usdm'); // 'usdm' connects to USD-M futures WebSocket

// Subscribe to COIN-M futures streams
wsClient.subscribe([
  'btcusd_perp@ticker',
  'btcusd_perp@depth10',
], 'coinm'); // 'coinm' connects to COIN-M futures WebSocket

// Subscribe to spot user data stream (requires API credentials)
wsClient.subscribeSpotUserDataStream();

// Subscribe to margin user data stream
wsClient.subscribeMarginUserDataStream();

// Subscribe to isolated margin user data stream
wsClient.subscribeIsolatedMarginUserDataStream('BTCUSDT');

// Subscribe to USD-M futures user data stream
wsClient.subscribeUsdFuturesUserDataStream();

// Subscribe to portfolio margin user data stream
wsClient.subscribePortfolioMarginUserDataStream();

// Handle specific event types with beautified data
wsClient.on('formattedMessage', event => {
  if (event.eventType === 'executionReport') {
    // Order update
    console.log(`Order ${event.orderId}: ${event.orderStatus}`);
    console.log(`Side: ${event.side}, Type: ${event.orderType}`);
    console.log(`Executed: ${event.executedQuantity}/${event.quantity}`);
  } else if (event.eventType === 'outboundAccountPosition') {
    // Balance update
    console.log('Account balances updated');
    event.balances.forEach(balance => {
      console.log(`${balance.asset}: ${balance.free} free, ${balance.locked} locked`);
    });
  } else if (event.eventType === 'trade') {
    // Public trade stream
    console.log(`Trade: ${event.price} x ${event.quantity}`);
    console.log(`Buyer was maker: ${event.buyerIsMaker}`);
  } else if (event.eventType === 'kline') {
    // Kline/candlestick update
    const kline = event.kline;
    console.log(`Kline ${kline.interval}: O=${kline.open} H=${kline.high} L=${kline.low} C=${kline.close}`);
    console.log(`Volume: ${kline.volume}, Closed: ${kline.isFinal}`);
  }
});

// Unsubscribe from topics
// wsClient.unsubscribe(['btcusdt@ticker'], 'main');

// Close a specific connection
// wsClient.close('main');

// Close all connections
// wsClient.closeAll();

```

--------------------------------

### Execute Futures Trading Operations via WebSocket (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Demonstrates Futures market trading operations using the WebsocketAPIClient. This includes fetching futures account balances, submitting and modifying futures orders, and retrieving current futures positions. It utilizes specific methods for futures trading available in the client.

```javascript
// Execute futures trades via WebSocket API
async function futuresExample() {
  try {
    // Get futures account balance
    const balance = await wsApiClient.getFuturesAccountBalanceV2({
      timestamp: Date.now(),
      recvWindow: 5000,
    });
    console.log('Futures balances:', balance);

    // Submit futures order
    const futuresOrder = await wsApiClient.submitNewFuturesOrder('usdm', {
      symbol: 'BTCUSDT',
      side: 'SELL',
      type: 'LIMIT',
      timeInForce: 'GTC',
      price: '45000.00',
      quantity: 0.001,
      positionSide: 'BOTH',
      timestamp: Date.now(),
    });
    console.log('Futures order:', futuresOrder.orderId);

    // Modify existing futures order
    const modifyResult = await wsApiClient.modifyFuturesOrder('usdm', {
      symbol: 'BTCUSDT',
      orderId: futuresOrder.orderId,
      side: 'SELL',
      quantity: '0.002', // New quantity
      price: '45500.00', // New price
      origType: 'LIMIT',
      positionSide: 'BOTH',
      timestamp: Date.now(),
    });
    console.log('Order modified:', modifyResult);

    // Get current positions
    const positions = await wsApiClient.getFuturesPositionV2({
      timestamp: Date.now(),
    });
    positions.forEach(pos => {
      if (parseFloat(pos.positionAmt) !== 0) {
        console.log(`${pos.symbol}: ${pos.positionAmt} @ ${pos.entryPrice}`);
      }
    });

  } catch (error) {
    console.error('Error:', error);
  }
}
```

--------------------------------

### Using WebsocketAPIClient for WebSocket API Calls (TypeScript)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

This snippet demonstrates initializing the WebsocketAPIClient with Ed25519 keys to make REST-like calls to Binance's WebSocket API for futures account balance and order submission. It depends on the 'binance' library and requires a valid API key generated from the public key. Inputs include timestamps and optional recvWindow for timing; outputs are promises resolving to API results like balance data or order confirmations. Limitations: Exclusive to Ed25519 keys, not available on testnet for all features, and requires managing connection health.

```typescript
import { WebsocketAPIClient } from 'binance';

// or, if you prefer `require()`:
// const { WebsocketAPIClient } = require('binance');

/**
 * The WS API only works with an Ed25519 API key.
 *
 * Check the rest-private-ed25519.md in this folder for more guidance
 * on preparing this Ed25519 API key.
 */

const publicKey = `-----BEGIN PUBLIC KEY-----\nMCexampleQTxwLU9o=\n-----END PUBLIC KEY-----\n`;

const privateKey = `-----BEGIN PRIVATE KEY-----\nMC4CAQAexamplewqj5CzUuTy1\n-----END PRIVATE KEY-----\n`;

// API Key returned by binance, generated using the publicKey (above) via Binance's website
const apiKey = 'TQpJexamplerobdG';

// Make an instance of the WS API Client
const wsClient = new WebsocketAPIClient({
  api_key: apiKey,
  api_secret: privateKey,
  beautify: true,

  // Enforce testnet ws connections, regardless of supplied wsKey
  // testnet: true,
});

// Optional, if you see RECV Window errors, you can use this to manage time issues. However, make sure you sync your system clock first!
// https://github.com/tiagosiebler/awesome-crypto-examples/wiki/Timestamp-for-this-request-is-outside-of-the-recvWindow
// wsClient.setTimeOffsetMs(-5000);

// Optional, see above. Can be used to prepare a connection before sending commands
// await wsClient.connectWSAPI(WS_KEY_MAP.mainWSAPI);

// Make WebSocket API calls, very similar to a REST API:

wsClient
  .getFuturesAccountBalanceV2({
    timestamp: Date.now(),
    recvWindow: 5000,
  })
  .then((result) => {
    console.log('getFuturesAccountBalanceV2 result: ', result);
  })
  .catch((err) => {
    console.error('getFuturesAccountBalanceV2 error: ', err);
  });

wsClient
  .submitNewFuturesOrder('usdm', {
    side: 'SELL',
    symbol: 'BTCUSDT',
    type: 'MARKET',
    quantity: 0.001,
    timestamp: Date.now(),
    // recvWindow: 5000,
  })
  .then((result) => {
    console.log('getFuturesAccountBalanceV2 result: ', result);
  })
  .catch((err) => {
    console.error('getFuturesAccountBalanceV2 error: ', err);
  });
```

--------------------------------

### Initialize and operate Binance USD-M Futures client (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Shows how to create aClient with API credentials, test connectivity, fetch account balances, submit a market order, retrieve mark price, list positions, set leverage, and obtain funding rate history. Requires the 'binance' npm package and valid API keys. Outputs are logged to the console; errors are caught and printed.

```JavaScript
import { USDMClient } from 'binance';

const futuresClient = new USDMClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  // Optional: connect to futures testnet
  // testnet: true,
  beautifyResponses: true,
});

// Test connectivity
futuresClient.testConnectivity()
  .then(() => console.log('Connected to futures API'))
  .catch(err => console.error('Connection failed:', err));

// Get futures account balance
futuresClient.getBalance()
  .then(balances => {
    balances.forEach(balance => {
      console.log(`${balance.asset}: ${balance.balance} (Available: ${balance.availableBalance})`);
    });
  })
  .catch(err => console.error('Error:', err));

// Submit a market order to open a short position
futuresClient.submitNewOrder({
  symbol: 'BTCUSDT',
  side: 'SELL',
  type: 'MARKET',
  quantity: 0.001,
})
  .then(result => {
    console.log('Order executed:', result.orderId);
    console.log('Executed Price:', result.avgPrice);
    console.log('Executed Qty:', result.executedQty);
  })
  .catch(err => console.error('Order failed:', err));

// Get mark price (liquidation reference price)
futuresClient.getMarkPrice({ symbol: 'BTCUSDT' })
  .then(markPrice => {
    console('Mark Price:', markPrice.markPrice);
    console.log('Index Price:', markPrice.indexPrice);
    console.log('Funding Rate:', markPrice.lastFundingRate);
  })
  .catch(err => console.error('Error:', err));

// Get current positions
futuresClient.getPositions()
  .then(positions => {
    positions.forEach(pos => {
      if (parseFloat(pos.positionAmt) !== 0) {
        console.log(`${pos.symbol}: ${pos.positionAmt} @ ${pos.entryPrice}`);
        console.log(`  Unrealized PnL: ${pos.unRealizedProfit}`);
      }
    });
  })
  .catch(err => console.error('Error:', err));

// Set leverage for a symbol
futuresClient.setLeverage({
  symbol: 'BTCUSDT',
  leverage: 10,
})
  .then(result => {
    console.log('Leverage set to:', result.leverage);
    console.log('Max notional:', result.maxNotionalValue);
  })
  .catch(err => console.error('Error:', err));

// Get funding rate history
futuresClient.getFundingRateHistory({ symbol: 'BTCUSDT', limit: 10 })
  .then(rates => {
    rates.forEach(rate => {
      console.log(`${new Date(rate.fundingTime)}: ${rate.fundingRate}`);
    });
  })
  .catch(err => console.error('Error:', err));
```

--------------------------------

### Handle WebSocket Events in JavaScript

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Shows how to listen for various WebSocket events such as raw messages, formatted messages, connection status, and errors. These events provide real-time updates and error handling.

```javascript
wsClient.on('message', (data) => {
  console.log('raw message received ', JSON.stringify(data, null, 2));
});

wsClient.on('open', (data) => {
  console.log('connection opened open:', data.wsKey, data.wsUrl);
});

wsClient.on('formattedMessage', (data) => {
  console.log('formattedMessage: ', data);
});

wsClient.on('response', (data) => {
  console.log('log response: ', JSON.stringify(data, null, 2));
});

wsClient.on('reconnecting', (data) => {
  console.log('ws automatically reconnecting.... ', data?.wsKey);
});

wsClient.on('reconnected', (data) => {
  console.log('ws has reconnected ', data?.wsKey);
});

wsClient.on('exception', (data) => {
  console.log('ws saw error ', data?.wsKey);
});
```

--------------------------------

### WebSocket API - Sending Commands

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

The WebSocket API allows sending requests (commands) over an active WebSocket connection. This feature requires Ed25519 keys. Responses can be handled using promises with async/await or an event-driven design.

```APIDOC
## WebSocket API - Sending Commands

Some Binance product groups support sending requests (commands) over an active WebSocket connection. This requires Ed25519 keys.

### Method
`sendWSAPIRequest(wsKey, command, commandParameters)`

### Endpoint
(N/A - Method call on WebsocketClient instance)

### Parameters
#### Path Parameters
(N/A)

#### Query Parameters
(N/A)

#### Request Body
- **wsKey** (string) - Required - Your WebSocket API key.
- **command** (string) - Required - The command to send (e.g., 'ORDER.TRADE').
- **commandParameters** (object) - Optional - Parameters for the command.

### Request Example
```typescript
import { WebsocketClient } from 'binance';

const ws = new WebsocketClient({});

async function sendCommand() {
  try {
    const response = await ws.sendWSAPIRequest('YOUR_WS_KEY', 'ACCOUNT.INFO', {});
    console.log('Command response:', response);
  } catch (error) {
    console.error('Error sending command:', error);
  }
}

sendCommand();
```

### Response
#### Success Response (Promise resolves)
- The resolved value of the promise contains the response from the WebSocket API.

#### Response Example (Success)
```json
{
  "id": "someId",
  "status": 200,
  "result": {
    "someData": "value"
  }
}
```

#### Error Response (Promise rejects)
- The rejected value of the promise contains an error object.

#### Response Example (Error)
```json
{
  "id": "someId",
  "status": 400,
  "error": {
    "code": -1000,
    "message": "An unknown error occurred."
  }
}
```
```

--------------------------------

### Handling Large Integers in WebSocket Messages

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

By default, JSON.parse cannot precisely represent integers larger than Number.MAX_SAFE_INTEGER. This section explains how to provide a custom JSON parser to preserve large integers like order IDs.

```APIDOC
## Preserving Large Integers in WebSocket Messages

By default, messages are parsed using `JSON.parse`, which cannot precisely represent integers larger than `Number.MAX_SAFE_INTEGER`. If you need to preserve large integers (e.g., order IDs), provide a custom parser via `customParseJSONFn`.

### Method
Constructor parameter

### Parameters
#### Request Body
- **customParseJSONFn** (function) - Optional - A function that takes the raw event string and returns the parsed JSON object. This function is used to handle large integers.

### Request Example (using RegEx)
```typescript
import { WebsocketClient } from 'binance';

const ws = new WebsocketClient({
  customParseJSONFn: (rawEvent) => {
    return JSON.parse(
      rawEvent.replace(/"orderId":\s*(\d+)/g, '"orderId":"$1"'),
    );
  }
});

ws.on('message', (msg) => {
  console.log(msg);
});
```

### Request Example (using json-bigint)
```typescript
import { WebsocketClient } from 'binance';
import JSONbig from 'json-bigint';

const ws = new WebsocketClient({
  customParseJSONFn: (rawEvent) => {
    return JSONbig({ storeAsString: true }).parse(rawEvent);
  }
});

ws.on('message', (msg) => {
  console.log(msg);
});
```

### Note on BigInt
If you prefer native BigInt, beware `JSON.stringify` will throw on BigInt values. Use a custom replacer or `JSONbig.stringify` if you need to log/serialize.

```typescript
const replacer = (_k: string, v: unknown) => typeof v === 'bigint' ? v.toString() : v;
console.log(JSON.stringify(msg, replacer));
```
```

--------------------------------

### Initialize and query Binance COIN-M Futures client (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Demonstrates setting up a CoinMClient with API credentials and retrieving exchange information, order book tickers, and 24‑hour price statistics for coin‑margined futures. Requires the 'binance' npm package and valid API keys. Results are printed to the console; any request errors are logged.

```JavaScript
import { CoinMClient } from 'binance';

const coinMClient = new CoinMClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  // Optional: connect to testnet
  // testnet: true,
});

// Get exchange information for coin-margined futures
coinMClient.getExchangeInfo()
 then(info => {
    console.log('Server time:', info.serverTime);
    console.log('Available contracts:', info.symbols.length);
    info.symbols.forEach(symbol => {
      console.log(`${symbol.symbol}: ${symbol.contractType}`);
    });
  })
  .catch(err => console.error('Error:', err));

// Get order book ticker (best bid/ask)
coinMClient.getSymbolOrderBookTicker()
  .then(tickers => {
    tickers.forEach(ticker => {
      console.log(`${ticker.symbol}: Bid ${ticker.bidPrice} / Ask ${ticker.askPrice}`);
    });
  })
  .catch(err => console.error('Error:', err));

// Get 24hr price statistics
coinMClient.get24hrChangeStatistics()
  .then(stats => {
    stats.forEach(stat => {
      console.log(`${stat.symbol}: ${stat.priceChangePercent}% change`);
    });
  })
  .catch(err => console.error('Error:', err));
```

--------------------------------

### Handle WebSocket API requests with TypeScript

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Illustrates the use of the WebSocket API for sending commands over an active WebSocket connection in Binance. Requires Ed25519 keys and demonstrates the event-driven API approach.

```TypeScript
// Example usage of sendWSAPIRequest method
// Note: Actual implementation would require valid wsKey, command, and parameters
ws.sendWSAPIRequest(wsKey, command, commandParameters).then(response => {
  console.log(response);
});
```

--------------------------------

### Preserve large integers in WebSocket messages with TypeScript

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Demonstrates how to handle large integers in WebSocket messages by providing a custom JSON parser. This is useful for preserving order IDs that exceed Number.MAX_SAFE_INTEGER. The example shows using RegEx to pre-process messages, with alternatives like json-bigint mentioned.

```TypeScript
import { WebsocketClient } from 'binance';

const ws = new WebsocketClient({
  customParseJSONFn: (rawEvent) => {
    return JSON.parse(
      rawEvent.replace(/"orderId":\s*(\d+)/g, '"orderId":"$1"'),
    );
  },
});

ws.on('message', (msg) => {
  console.log(msg);
});
```

--------------------------------

### Initialize Binance REST API Client for Spot Trading

Source: https://context7.com/tiagosiebler/binance/llms.txt

Demonstrates how to initialize the MainClient for interacting with Binance Spot trading, margin trading, and wallet management endpoints. It requires API keys and supports optional testnet and response beautification.

```javascript
import { MainClient } from 'binance';

const client = new MainClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  // Optional: connect to testnet
  // testnet: true,
  // Optional: beautify response strings to numbers
  // beautifyResponses: true,
});
```

--------------------------------

### Submit a Spot Trade Order with Binance SDK

Source: https://context7.com/tiagosiebler/binance/llms.txt

Provides an example of placing a limit buy order for BTCUSDT using the `submitNewOrder` method of the Binance SDK. It specifies order parameters such as symbol, side, type, price, and quantity. Error handling for failed orders is included.

```javascript
// Place a spot trade order
client.submitNewOrder({
  symbol: 'BTCUSDT',
  side: 'BUY',
  type: 'LIMIT',
  timeInForce: 'GTC',
  price: '30000.00',
  quantity: '0.001',
})
  .then(order => {
    console.log('Order placed:', order.orderId);
    console.log('Status:', order.status);
    console.log('Executed qty:', order.executedQty);
  })
  .catch(err => console.error('Order failed:', err));
```

--------------------------------

### Large Integer Preservation in Binance WebSocket Messages (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Shows how to handle large order IDs and values in Binance WebSocket messages that might exceed JavaScript's safe integer limit. This is achieved by providing a `customParseJSONFn` to the `WebsocketClient`. Two options are presented: using `String.prototype.replace` with a regular expression or using the `json-bigint` library. Requires API key and secret.

```javascript
import { WebsocketClient } from 'binance';

// Use custom JSON parser to preserve large integers
const wsClient = new WebsocketClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',

  // Option 1: Convert specific fields to strings using RegEx
  customParseJSONFn: (rawEvent) => {
    return JSON.parse(
      rawEvent.replace(/"orderId":\s*(\d+)/g, '"orderId":"$1"')
    );
  },

  // Option 2: Use json-bigint library (npm install json-bigint)
  // customParseJSONFn: (rawEvent) => {
  //   const JSONbig = require('json-bigint');
  //   return JSONbig({ storeAsString: true }).parse(rawEvent);
  // },
});

wsClient.on('message', msg => {
  console.log('Message with large integers preserved:', msg);
  // orderId will be a string instead of potentially corrupted number
  if (msg.orderId) {
    console.log('Order ID (as string):', msg.orderId);
  }
});

wsClient.subscribeUsdFuturesUserDataStream();

```

--------------------------------

### Initialize Binance USDM Futures Client and Interact (JavaScript)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Shows how to initialize the USDMClient for Binance USD-Margined Futures. It covers optional API key setup for private endpoints and provides examples for retrieving account balances and submitting market orders. Error handling is demonstrated.

```javascript
import { USDMClient } from 'binance';

// or, if you prefer `require()`:
// const { USDMClient } = require('binance');

const API_KEY = 'xxx';
const API_SECRET = 'yyy';

const client = new USDMClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  // Connect to testnet environment
  // testnet: true,
});

client
  .getBalance()
  .then((result) => {
    console.log('getBalance result: ', result);
  })
  .catch((err) => {
    console.error('getBalance error: ', err);
  });

client
  .submitNewOrder({
    side: 'SELL',
    symbol: 'BTCUSDT',
    type: 'MARKET',
    quantity: 0.001,
  })
  .then((result) => {
    console.log('submitNewOrder result: ', result);
  })
  .catch((err) => {
    console.error('submitNewOrder error: ', err);
  });
```

--------------------------------

### Handle API Errors and Sync Time in JavaScript

Source: https://context7.com/tiagosiebler/binance/llms.txt

This JavaScript code snippet demonstrates how to synchronize system time with Binance server time and handle API errors when placing orders. It depends on the binance npm package and uses the MainClient for authentication and trading. The function outputs server time offset and order details on success, or specific error messages for issues like timestamp mismatches, insufficient balance, or rate limits.

```javascript
import { MainClient } from 'binance';

const client = new MainClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  // Automatically beautify responses
  beautifyResponses: true,
  // Set custom receive window (default 5000ms)
  recvWindow: 10000,
});

// Handle timestamp sync issues
async function syncTimeAndTrade() {
  try {
    // Get server time first
    const serverTime = await client.getServerTime();
    const localTime = Date.now();
    const timeOffset = serverTime.serverTime - localTime;

    console.log(`Time offset: ${timeOffset}ms`);

    // If you have consistent time sync issues, you can use:
    // client.setTimeOffset(timeOffset);

    // Place order with proper error handling
    const order = await client.submitNewOrder({
      symbol: 'BTCUSDT',
      side: 'BUY',
      type: 'LIMIT',
      timeInForce: 'GTC',
      price: '30000.00',
      quantity: '0.001',
    });

    console.log('Order successful:', order.orderId);

  } catch (error) {
    if (error.response) {
      // Binance API error
      console.error('API Error:', error.response.data);
      console.error('Status:', error.response.status);

      // Handle specific error codes
      if (error.response.data.code === -1021) {
        console.error('Timestamp out of recvWindow - sync your system clock');
      } else if (error.response.data.code === -2010) {
        console.error('Insufficient balance');
      } else if (error.response.data.code === -1003) {
        console.error('Rate limit exceeded');
      }
    } else if (error.request) {
      // Network error
      console.error('Network error:', error.message);
    } else {
      // Other error
      console.error('Error:', error.message);
    }
  }
}

syncTimeAndTrade();
```

--------------------------------

### getFuturesAccountBalanceV2 (WebSocket API)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Retrieves the futures account balance in a promise-based manner using the WebSocket API client. This endpoint mirrors REST API functionality but operates over a persisted WebSocket connection. It requires an Ed25519 API key for authentication and includes parameters like timestamp and optional recvWindow for request validation.

```APIDOC
## GET Futures Account Balance V2 (WebSocket API)

### Description
Retrieves the current account balance for futures trading, similar to the REST API endpoint but accessed via the WebSocket API client for promise-based execution without manual WebSocket management.

### Method
WebSocket API Call (promise-based)

### Endpoint
getFuturesAccountBalanceV2()

### Parameters
#### Query Parameters
- **timestamp** (number) - Required - The timestamp of the request in milliseconds.
- **recvWindow** (number) - Optional - The receive window in milliseconds (default and limits apply).

#### Request Body
None

### Request Example
{
  "timestamp": Date.now(),
  "recvWindow": 5000
}

### Response
#### Success Response
- **balances** (array) - Array of account balance objects, each containing asset, balance, etc.

#### Response Example
{
  "result": "array of balance objects"
}
```

--------------------------------

### Create USD-M Futures Clients with Market Maker Support

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Instantiate separate USDMClient instances for market maker and regular endpoints. Requires API key and secret. Useful when algorithms need access to both MM and standard futures endpoints.

```javascript
import { USDMClient } from 'binance';

// MM client for USD-M futures
const futuresMMClient = new USDMClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  useMMEndpoints: true, // Use MM endpoints for futures
});

// Regular client for USD-M futures
const futuresRegularClient = new USDMClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  useMMEndpoints: false, // Use regular endpoints for futures
});
```

--------------------------------

### Market Maker Endpoints for Binance Futures (JavaScript)

Source: https://context7.com/tiagosiebler/binance/llms.txt

Demonstrates how to use specialized low-latency market maker endpoints for USD-M and Coin-M Futures, as well as WebSocket clients. Requires API key and secret. Enables market maker routing via `useMMSubdomain: true`. Orders submitted with market maker endpoints should use `timeInForce: 'GTX'` for post-only behavior.

```javascript
import { USDMClient, CoinMClient, WebsocketClient } from 'binance';

// USD-M Futures with market maker endpoints
const usdmMMClient = new USDMClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  useMMSubdomain: true, // Enable market maker routing
});

// COIN-M Futures with market maker endpoints
const coinmMMClient = new CoinMClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  useMMSubdomain: true, // Enable market maker routing
});

// WebSocket with market maker endpoints
const wsMMClient = new WebsocketClient({
  api_key: 'YOUR_API_KEY',
  api_secret: 'YOUR_API_SECRET',
  useMMSubdomain: true, // Enable market maker routing
  beautify: true,
});

// Use clients normally - routing is automatic
usdmMMClient.submitNewOrder({
  symbol: 'BTCUSDT',
  side: 'BUY',
  type: 'LIMIT',
  timeInForce: 'GTX', // Post-only for market makers
  price: '30000.00',
  quantity: 0.1,
})
  .then(order => console.log('MM order placed:', order.orderId))
  .catch(err => console.error('Error:', err));

// WebSocket subscriptions automatically use MM endpoints
wsMMClient.subscribe(['btcusdt@depth@100ms'], 'usdm');

```

--------------------------------

### submitNewFuturesOrder (WebSocket API)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Submits a new futures order using the WebSocket API client for promise-based order placement. Supports various order types and parameters for futures trading on USD-M or COIN-M markets. Authentication via Ed25519 API key is required, and the call includes order details like side, symbol, type, and quantity.

```APIDOC
## POST Submit New Futures Order (WebSocket API)

### Description
Places a new futures order via the WebSocket API client, providing a REST-like interface for order submission. This endpoint automatically handles authentication and connection persistence.

### Method
WebSocket API Call (promise-based)

### Endpoint
submitNewFuturesOrder(string: futuresType, object: options)

### Parameters
#### Path Parameters
- **futuresType** (string) - Required - Type of futures, e.g., 'usdm' or 'coinm'.

#### Request Body
- **side** (string) - Required - Order side: 'BUY' or 'SELL'.
- **symbol** (string) - Required - Trading pair symbol, e.g., 'BTCUSDT'.
- **type** (string) - Required - Order type, e.g., 'MARKET'.
- **quantity** (number) - Required - Order quantity.
- **timestamp** (number) - Required - Timestamp in milliseconds.
- **recvWindow** (number) - Optional - Receive window in milliseconds.

### Request Example
{
  "side": "SELL",
  "symbol": "BTCUSDT",
  "type": "MARKET",
  "quantity": 0.001,
  "timestamp": Date.now()
}

### Response
#### Success Response
- **orderId** (string) - The ID of the submitted order.
- **status** (string) - Order status.
- **symbol** (string) - Trading symbol.
- **side** (string) - Order side.
- **type** (string) - Order type.

#### Response Example
{
  "result": "order object with details"
}
```

--------------------------------

### Initialize Binance WebSocket Client in JavaScript

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Demonstrates how to initialize the WebSocketClient with API credentials and optional settings like beautification and testnet. The client manages connections and subscriptions automatically.

```javascript
import { WebsocketClient } from 'binance';

const API_KEY = 'xxx';
const API_SECRET = 'yyy';

const wsClient = new WebsocketClient({
  api_key: key,
  api_secret: secret,
  beautify: true,
  disableHeartbeat: true,
  testnet: true
});
```

--------------------------------

### Enabling Market Maker Endpoints in REST API Clients (JavaScript)

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

This code shows how to initialize USDMClient and CoinMClient with the useMMSubdomain option for accessing optimized market maker endpoints in USD-M and COIN-M futures. It requires the 'binance' library and valid API credentials. Inputs are API key and secret; no specific method calls here, but enables routing for all client methods. Outputs: Standard API responses via optimized paths. Limitations: Only for qualified market makers enrolled in Binance programs, unavailable on testnet and for non-futures products like spot or margin.

```javascript
import { USDMClient, CoinMClient } from 'binance';

// USD-M Futures with MM endpoints
const usdmClient = new USDMClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  useMMSubdomain: true, // Enable market maker endpoints
});

// COIN-M Futures with MM endpoints
const coinmClient = new CoinMClient({
  api_key: API_KEY,
  api_secret: API_SECRET,
  useMMSubdomain: true, // Enable market maker endpoints
});
```

--------------------------------

### Install Browser Dependencies for Frontend Usage

Source: https://github.com/tiagosiebler/binance/blob/master/README.md

Setup dependencies and configuration for using the Binance SDK in browser environments. Requires installing crypto-browserify and stream-browserify packages.

```shell
npm install crypto-browserify stream-browserify
```