### Fetch Crypto Bars in JavaScript

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Fetches cryptocurrency bars for a given symbol using the Alpaca JavaScript SDK. The data is then displayed in a table format in the console. This is an asynchronous operation.

```javascript
(async () => {
  const bars = await alpaca.getCryptoBars(["BTC/USD"], options);

  console.table(bars.get("BTC/USD"));
})();
```

--------------------------------

### Display Crypto Bars in JavaScript (Console Table)

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Shows how cryptocurrency bar data is presented when using the `console.table()` method in JavaScript after fetching it via the Alpaca SDK. This provides a clear, tabular view of the OHLCV data directly in the browser's developer console or Node.js environment.

```text
┌─────────┬──────────┬──────────┬──────────┬────────────┬──────────┬────────────────────────┬──────────────┬──────────────────┐
│ (index) │ Close    │ High     │ Low      │ TradeCount │ Open     │ Timestamp              │ Volume       │ VWAP             │
├─────────┼──────────┼──────────┼──────────┼────────────┼──────────┼────────────────────────┼──────────────┼──────────────────┤
│ 0       │ 20156.76 │ 20292    │ 19564.86 │ 110122     │ 20055.79 │ '2022-09-01T05:00:00Z' │ 7141.975485  │ 19934.1678446199 │
│ 1       │ 19919.47 │ 20444    │ 19757.72 │ 96231      │ 20156.76 │ '2022-09-02T05:00:00Z' │ 7165.911879  │ 20075.2008677126 │
│ 2       │ 19806.11 │ 19968.2  │ 19658.04 │ 51551      │ 19924.83 │ '2022-09-03T05:00:00Z' │ 2677.652012  │ 19800.1854803241 │
│ 3       │ 19888.67 │ 20058    │ 19587.86 │ 62082      │ 19805.39 │ '2022-09-04T05:00:00Z' │ 4325.67879   │ 19834.4514137038 │
│ 4       │ 19760.56 │ 20180.5  │ 19635.96 │ 84784      │ 19888.67 │ '2022-09-05T05:00:00Z' │ 6274.552824  │ 19812.0959815687 │
│ 5       │ 18724.59 │ 20026.91 │ 18534.06 │ 128106     │ 19761.39 │ '2022-09-06T05:00:00Z' │ 11217.789784 │ 19266.8355201911 │
└─────────┴──────────┴──────────┴──────────┴────────────┴──────────┴────────────────────────┴──────────────┴──────────────────┘
```

--------------------------------

### Fetch Crypto Bars in Go

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Retrieves cryptocurrency bars (OHLCV data) for a specified symbol and time range using the Alpaca Go SDK. It iterates through the returned bars and prints each one. Error handling is included for the API call.

```go
bars, err := client.GetCryptoBars("BTC/USD", request)
	if err != nil {
		panic(err)
	}
	for _, bar := range bars {
		fmt.Printf("%+v\n", bar)
	}
```

--------------------------------

### Fetch AAPL Daily Bars (IEX Feed)

Source: https://docs.alpaca.markets/docs/market-data-faq

Retrieves the historical daily bar data for AAPL using the IEX data feed. Requires API key and secret. Specifies the timeframe, start date, and limit for the query. The output includes bar details such as open, high, low, close prices, volume, and trade counts. This feed typically offers more granular trade data.

```bash
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/bars?feed=iex&timeframe=1Day&start=2023-09-29&limit=1" | jq .

```

--------------------------------

### Fetch Latest AAPL Trade

Source: https://docs.alpaca.markets/docs/market-data-faq

Retrieves the latest trade data for the AAPL symbol. By default, it uses the IEX feed if no subscription for SIP data is present. Requires API key and secret. The response includes the trade timestamp, exchange, price, size, and conditions.

```bash
$  curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/trades/latest" | jq .

```

--------------------------------

### Fetch Latest Crypto Order Book Data via REST API

Source: https://docs.alpaca.markets/docs/crypto-pricing-data

Requests the latest order book data (bid and asks) for specified crypto trading pairs using the Alpaca Data API. Requires API key and secret for authentication. Returns a JSON object containing order book details for each symbol.

```curl
curl --request GET 'https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD,SOL/USDT' \
--header 'Apca-Api-Key-Id: <KEY>' \
--header 'Apca-Api-Secret-Key: <SECRET>'
```

--------------------------------

### Fetch AAPL Daily Bars (SIP Feed)

Source: https://docs.alpaca.markets/docs/market-data-faq

Retrieves the historical daily bar data for AAPL using the SIP data feed. Requires API key and secret. Specifies the timeframe, start date, and limit for the query. The output includes bar details such as open, high, low, close prices, volume, and trade counts.

```bash
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "https://data.alpaca.markets/v2/stocks/AAPL/bars?feed=sip&timeframe=1Day&start=2023-09-29&limit=1" | jq .

```

--------------------------------

### Get List of Assets - Python, JavaScript, C#, Go

Source: https://docs.alpaca.markets/docs/working-with-assets

Retrieves a list of all active assets from the Alpaca API. The code examples demonstrate how to fetch this data using respective language SDKs and optionally filter results by asset class or exchange. Dependencies include the respective Alpaca SDKs for each language.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

trading_client = TradingClient('api-key', 'secret-key')

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)
```

```javascript
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get a list of all active assets.
const activeAssets = alpaca
  .getAssets({
    status: "active",
  })
  .then((activeAssets) => {
    // Filter the assets down to just those on NASDAQ.
    const nasdaqAssets = activeAssets.filter(
      (asset) => asset.exchange == "NASDAQ"
    );
    console.log(nasdaqAssets);
  });
```

```csharp
using Alpaca.Markets;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace CodeExamples
{
    internal static class Example
    {
        private static string API_KEY = "your_api_key";

        private static string API_SECRET = "your_secret_key";

        public static async Task Main(string[] args)
        {
            // First, open the API connection
            var client = Alpaca.Markets.Environments.Paper
                .GetAlpacaTradingClient(new SecretKey(API_KEY, API_SECRET));

            // Get a list of all active assets.
            var assets = await client.ListAssetsAsync(
                new AssetsRequest { AssetStatus = AssetStatus.Active });

            // Filter the assets down to just those on NASDAQ.
            var nasdaqAssets = assets.Where(asset => asset.Exchange == Exchange.NyseMkt);

            Console.Read();
        }
    }
}
```

```go
package main

import (
	"github.com/alpacahq/alpaca-trade-api-go/alpaca"
)

func init() {
	alpaca.SetBaseUrl("https://paper-api.alpaca.markets")
}

func main() {
	// Get a list of all active assets.
	status := "active"
	assets, err := alpaca.ListAssets(&status)
	if err != nil {
		panic(err)
	}

	// Filter the assets down to just those on NASDAQ.
	nasdaq_assets := []alpaca.Asset{}
	for _, asset := range assets {
		if asset.Exchange == "NASDAQ" {
			nasdaq_assets = append(nasdaq_assets, asset)
		}
	}
}
```

--------------------------------

### Fetch Latest Stock Trades (Shell)

Source: https://docs.alpaca.markets/docs/market-data-faq

Retrieves the latest stock trades for a given symbol using a cURL command. It requires API key and secret headers and specifies the data URL. The output is in JSON format, which is then pretty-printed using jq.

```shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" "${APCA_API_DATA_URL}/v2/stocks/trades/latest?symbols=FB" | jq .
{
  "trades": {
    "FB": {
      "c": [
        "@",
        "T"
      ],
      "i": 31118,
      "p": 196.29,
      "s": 121,
      "t": "2022-06-08T23:59:55.103033856Z",
      "x": "P",
      "z": "C"
    }
  }
}
```

--------------------------------

### Display Crypto Bars in Python (Pandas DataFrame)

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Demonstrates the output of fetching cryptocurrency bars in Python, typically represented as a Pandas DataFrame. The example shows the columns and a few rows of the data, including timestamp, open, high, low, close, volume, trade count, and VWAP.

```text
                                       open      high       low     close        volume  trade_count          vwap
symbol  timestamp
BTC/USD 2022-09-01 05:00:00+00:00  20055.79  20292.00  19564.86  20156.76   7141.975485     110122.0  19934.167845
        2022-09-02 05:00:00+00:00  20156.76  20444.00  19757.72  19919.47   7165.911879      96231.0  20075.200868
        2022-09-03 05:00:00+00:00  19924.83  19968.20  19658.04  19806.11   2677.652012      51551.0  19800.185480
        2022-09-04 05:00:00+00:00  19805.39  20058.00  19587.86  19888.67   4325.678790      62082.0  19834.451414
        2022-09-05 05:00:00+00:00  19888.67  20180.50  19635.96  19760.56   6274.552824      84784.0  19812.095982
        2022-09-06 05:00:00+00:00  19761.39  20026.91  18534.06  18724.59  11217.789784     128106.0  19266.835520
```

--------------------------------

### Fetch Historical Daily Bars with 'asof' Enabled (Shell)

Source: https://docs.alpaca.markets/docs/market-data-faq

Fetches historical daily stock bars for a specified symbol and date range using cURL. The 'asof' parameter is enabled by default, allowing retrieval of data even if the symbol has changed. The output is formatted as tab-separated values (TSV) using jq.

```shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=META&start=2022-06-06&end=2022-06-11" | \
  jq -r '.bars.META[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-06T04:00:00Z    193.99  196.92  188.4   194.25
2022-06-07T04:00:00Z    191.93  196.53  191.49  195.65
2022-06-08T04:00:00Z    194.67  202.03  194.41  196.64
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
```

--------------------------------

### Fetch Historical Daily Bars with 'asof' Set to Past Date (Shell)

Source: https://docs.alpaca.markets/docs/market-data-faq

Fetches historical daily stock bars using an old ticker symbol by specifying an 'asof' date prior to the symbol change. This demonstrates how to access historical data associated with the original symbol name. The output is formatted as TSV.

```shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=FB&start=2022-06-06&end=2022-06-11&asof=2022-06-06" | \
  jq -r '.bars.FB[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-06T04:00:00Z    193.99  196.92  188.4   194.25
2022-06-07T04:00:00Z    191.93  196.53  191.49  195.65
2022-06-08T04:00:00Z    194.67  202.03  194.41  196.64
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
```

--------------------------------

### Get Crypto Bars

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Retrieves historical cryptocurrency bar data for a given symbol and options. Examples provided in Go and JavaScript.

```APIDOC
## GET /v2/crypto/{symbol}/bars

### Description
Retrieves historical cryptocurrency bar data for a given symbol.

### Method
GET

### Endpoint
/v2/crypto/{symbol}/bars

### Parameters
#### Path Parameters
- **symbol** (string) - Required - The cryptocurrency symbol (e.g., BTC/USD).

#### Query Parameters
- **start** (string) - Optional - The start date for the bars (YYYY-MM-DD).
- **end** (string) - Optional - The end date for the bars (YYYY-MM-DD).
- **timeframe** (string) - Optional - The timeframe for the bars (e.g., '1Min', '1Hour', '1Day').

### Request Example
```go
request := &api.GetCryptoBarsRequest{
	Start: "2022-09-01",
	End:   "2022-09-06",
	TimeFrame: "1Day",
}
bars, err := client.GetCryptoBars("BTC/USD", request)
```
```javascript
const options = {
  start: '2022-09-01',
  end: '2022-09-06',
  timeframe: '1Day',
};
alpaca.getCryptoBars(['BTC/USD'], options);
```

### Response
#### Success Response (200)
- **bars** (map[string]interface{}) - A map where keys are symbols and values are arrays of bar data.

#### Response Example
```json
{
  "BTC/USD": [
    {
      "t": 1661971200000,
      "o": 20055.79,
      "h": 20292.00,
      "l": 19564.86,
      "c": 20156.76,
      "v": 7141.975485,
      "n": 110122,
      "vw": 19934.167845
    }
  ]
}
```
```

--------------------------------

### Example: Fetch Account Info with Curl

Source: https://docs.alpaca.markets/docs/getting-started-with-trading-api

This example demonstrates how to fetch account information using curl, a command-line tool. It highlights the request headers and the 'X-Request-ID' present in the response, which is crucial for support.

```shell
$ curl -v https://paper-api.alpaca.markets/v2/account
...
> GET /v2/account HTTP/1.1
> Host: paper-api.alpaca.markets
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 403 Forbidden
< Date: Fri, 25 Aug 2023 09:34:40 GMT
< Content-Type: application/json
< Content-Length: 26
< Connection: keep-alive
< X-Request-ID: 649c5a79da1ab9cb20742ffdada0a7bb
< 
...
```

--------------------------------

### Fetch Latest Crypto Order Book Data (cURL)

Source: https://docs.alpaca.markets/docs/crypto-trading

This snippet demonstrates how to request the latest order book data (bids and asks) for multiple cryptocurrency pairs using cURL. It requires specifying the desired symbols in the query parameters. The output is a JSON object containing order book details for each symbol.

```curl
curl 'https://data.alpaca.markets/v1beta3/crypto/us/latest/orderbooks?symbols=BTC/USD,ETH/BTC,ETH/USD'
```

--------------------------------

### Calculate Daily Portfolio Gain/Loss using Account Data

Source: https://docs.alpaca.markets/docs/working-with-account

Utilize account information, such as buying power and current positions, to calculate the daily profit or loss of your trading portfolio. This involves fetching account details first.

```Python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# Get our account information.
account = trading_client.get_account()
```

--------------------------------

### Fetching Options Positions

Source: https://docs.alpaca.markets/docs/options-trading

The existing Positions API can be used to fetch options positions. Future enhancements aim to support filtering positions by asset class.

```APIDOC
## GET /v1.1/positions

### Description
Fetches all open positions, including options contracts. The existing model supports options.

### Method
GET

### Endpoint
/v1.1/positions

### Parameters
*No specific parameters mentioned for options filtering in the provided text. Refer to general Positions API documentation.*

### Response
#### Success Response (200)
- **positions** (array) - An array of position objects.

#### Response Example
```json
[
  {
    "symbol": "SPY230616C00400000",
    "qty": 1,
    "side": "long",
    "market_value": 150.00,
    "cost_basis": 120.00,
    "unrealized_pl": 30.00,
    "realized_pl": 0.00,
    "current_price": 150.00,
    "last_day_trades": 0,
    "asset_class": "option"
  }
]
```
```

--------------------------------

### Subscribe to Real-time Stock Data Channels

Source: https://docs.alpaca.markets/docs/real-time-stock-pricing-data

This JSON object demonstrates how to subscribe to various real-time stock data channels. You can specify actions like 'subscribe' and list symbols for trades and quotes, or use '*' to subscribe to all bars. Ensure your subscription aligns with your account's data feed.

```json
{
  "action": "subscribe",
  "trades": ["AAPL"],
  "quotes": ["AMD", "CLDR"],
  "bars": ["*"]
}
```

--------------------------------

### Define Crypto Bars Request Parameters

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Define the parameters for requesting historical cryptocurrency bar data. This includes specifying symbols, timeframe, and the start and end dates for the data.

```python
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

# Creating request object
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Day,
  start=datetime(2022, 9, 1),
  end=datetime(2022, 9, 7)
)
```

```go
request := marketdata.GetCryptoBarsRequest{
  TimeFrame: marketdata.OneDay,
  Start:     time.Date(2022, 9, 1, 0, 0, 0, 0, time.UTC),
  End:       time.Date(2022, 9, 7, 0, 0, 0, 0, time.UTC),
}
```

```javascript
let options = {
  start: "2022-09-01",
  end: "2022-09-07",
  timeframe: alpaca.newTimeframe(1, alpaca.timeframeUnit.DAY),
};

```

--------------------------------

### Fetch Historical Daily Bars with 'asof' Disabled (Shell)

Source: https://docs.alpaca.markets/docs/market-data-faq

Retrieves historical daily stock bars for a given symbol and date range, but with the 'asof' parameter explicitly disabled ('asof=-'). This ensures that only data associated with the current symbol is returned, excluding data from before a potential symbol change. Output is formatted as TSV.

```shell
$ curl -s -H "APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H "APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
  "${APCA_API_DATA_URL}/v2/stocks/bars?timeframe=1Day&symbols=META&start=2022-06-06&end=2022-06-11&asof=-" | \
  jq -r '.bars.META[] | [.t, .o, .h, .l, .c] | @tsv'
2022-06-09T04:00:00Z    194.28  199.45  183.68  184
2022-06-10T04:00:00Z    183.04  183.1   175.02  175.57
```

--------------------------------

### Get Trading Account Buying Power (JSON)

Source: https://docs.alpaca.markets/docs/draft-instant-funding

Fetches a user's trading account details, including their current buying power. This is useful after an instant funding transfer is completed to confirm the available funds for trading. The response is in JSON format.

```json
{
    "id": "{ACCOUNT_ID}",
    "admin_configurations": {
        "allow_instant_ach": true,
        "disable_shorting": true,
        "max_margin_multiplier": "1"
    },
    "user_configurations": null,
    "account_number": "{ACCOUNT_NO}",
    "status": "ACTIVE",
    "crypto_status": "INACTIVE",
    "currency": "USD",
    "buying_power": "100",
    "regt_buying_power": "100",
    "daytrading_buying_power": "0",
    "effective_buying_power": "100",
    "non_marginable_buying_power": "0",
    "bod_dtbp": "0",
    "cash": "100",
    "cash_withdrawable": "0",
    "cash_transferable": "0",
    "accrued_fees": "0",
    "pending_transfer_out": "0",
    "pending_transfer_in": "0",
    "portfolio_value": "0",
    "pattern_day_trader": false,
    "trading_blocked": false,
    "transfers_blocked": false,
    "account_blocked": false,
    "created_at": "2024-07-10T17:23:51.655324Z",
    "trade_suspended_by_user": false,
    "multiplier": "1",
    "shorting_enabled": false,
    "equity": "0",
    "last_equity": "0",
    "long_market_value": "0",
    "short_market_value": "0",
    "position_market_value": "0",
    "initial_margin": "0",
    "maintenance_margin": "0",
    "last_maintenance_margin": "0",
    "sma": "0",
    "daytrade_count": 0,
    "balance_asof": "2024-07-09",
    "previous_close": "2024-07-09T20:00:00-04:00",
    "last_long_market_value": "0",
    "last_short_market_value": "0",
    "last_cash": "0",
    "last_initial_margin": "0",
    "last_regt_buying_power": "0",
    "last_daytrading_buying_power": "0",
    "last_buying_power": "0",
    "last_daytrade_count": 0,
    "clearing_broker": "ALPACA_APCA",
    "memoposts": "100",
    "intraday_adjustments": "0",
    "pending_reg_taf_fees": "0"
}
```

--------------------------------

### Fetch Option Contracts

Source: https://docs.alpaca.markets/docs/options-trading

Retrieve details for option contracts. This endpoint allows fetching a list of contracts based on various parameters, including underlying symbols and expiration dates.

```APIDOC
## GET /v2/options/contracts

### Description
Retrieves a list of option contracts. Supports filtering by underlying symbols and other parameters. The default parameters include expiration date up to the next weekend and a limit of 100 contracts.

### Method
GET

### Endpoint
/v2/options/contracts

### Query Parameters
- **underlying_symbols** (string) - Optional - Comma-separated list of underlying symbols to filter contracts.
- **expiration_date_lte** (string) - Optional - Filter contracts by expiration date less than or equal to the provided date (YYYY-MM-DD).
- **expiration_date_gte** (string) - Optional - Filter contracts by expiration date greater than or equal to the provided date (YYYY-MM-DD).
- **limit** (integer) - Optional - The maximum number of contracts to return. Defaults to 100.
- **page_token** (string) - Optional - Token for pagination.

### Request Example
```bash
GET /v2/options/contracts?underlying_symbols=AAPL,MSFT&expiration_date_lte=2024-01-19
```

### Response
#### Success Response (200)
- **option_contracts** (array) - An array of option contract objects.
  - **id** (string) - Unique identifier for the option contract.
  - **symbol** (string) - The option symbol.
  - **name** (string) - The full name of the option contract.
  - **status** (string) - The status of the option contract (e.g., 'active').
  - **tradable** (boolean) - Indicates if the contract is currently tradable.
  - **expiration_date** (string) - The expiration date of the contract (YYYY-MM-DD).
  - **root_symbol** (string) - The root symbol of the underlying asset.
  - **underlying_symbol** (string) - The symbol of the underlying asset.
  - **underlying_asset_id** (string) - The asset ID of the underlying asset.
  - **type** (string) - The type of option ('call' or 'put').
  - **style** (string) - The style of the option ('american' or 'european').
  - **strike_price** (string) - The strike price of the option.
  - **size** (string) - The contract size.
  - **open_interest** (string) - The current open interest for the contract.
  - **open_interest_date** (string) - The date for which open interest was recorded.
  - **close_price** (string) - The closing price of the option contract on a given date.
  - **close_price_date** (string) - The date for which the closing price is reported.
- **page_token** (string) - Token for the next page of results.
- **limit** (integer) - The limit used for the request.

#### Response Example
```json
{
    "option_contracts": [
        {
            "id": "6e58f870-fe73-4583-81e4-b9a37892c36f",
            "symbol": "AAPL240119C00100000",
            "name": "AAPL Jan 19 2024 100 Call",
            "status": "active",
            "tradable": true,
            "expiration_date": "2024-01-19",
            "root_symbol": "AAPL",
            "underlying_symbol": "AAPL",
            "underlying_asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
            "type": "call",
            "style": "american",
            "strike_price": "100",
            "size": "100",
            "open_interest": "6168",
            "open_interest_date": "2024-01-12",
            "close_price": "85.81",
            "close_price_date": "2024-01-12"
        }
    ],
   "page_token": "MTAw",
   "limit": 100
}
```
```

--------------------------------

### Place Various Order Types in JavaScript

Source: https://docs.alpaca.markets/docs/working-with-orders

This JavaScript code uses the Alpaca Trade API to fetch bar data and then place different types of orders: bracket orders with stop-loss and take-profit, OTO orders with stop-loss, and OCO orders with stop-loss and take-profit. It assumes the Alpaca API is initialized.

```javascript
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

const symbol = "AAPL";
alpaca
  .getBars("minute", symbol, {
    limit: 5,
  })
  .then((barset) => {
    const currentPrice = barset[symbol].slice(-1)[0].closePrice;

    // We could buy a position and add a stop-loss and a take-profit of 5 %
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

    // We could buy a position and just add a stop loss of 5 % (OTO Orders)
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

    // We could split it to 2 orders. first buy a stock,
    // and then add the stop/profit prices (OCO Orders)
    alpaca.createOrder({
      symbol: symbol,
      qty: 1,
      side: "buy",
      type: "limit",
      time_in_force: "gtc",
      limit_price: currentPrice,
    });

    // wait for it to buy position and then
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

--------------------------------

### Instantiate Crypto Historical Data Client

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Initialize the client for requesting historical cryptocurrency data using the Alpaca SDK. For crypto data, API keys and a paper URL are not strictly required for client instantiation.

```python
from alpaca.data.historical import CryptoHistoricalDataClient

# No keys required for crypto data
client = CryptoHistoricalDataClient()
```

```go
package main

import "github.com/alpacahq/alpaca-trade-api-go/v3/marketdata"

func main() {
	// No keys required for crypto data
	client := marketdata.NewClient(marketdata.ClientOpts{})
}
```

```javascript
import Alpaca from "@alpacahq/alpaca-trade-api";

// Alpaca() requires the API key and sectret to be set, even for crypto
const alpaca = new Alpaca({
  keyId: "YOUR_API_KEY",
  secretKey: "YOUR_API_SECRET",
});
```

--------------------------------

### Display Crypto Bars in Go (Struct Output)

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Illustrates the raw output format of cryptocurrency bars when fetched using the Go SDK. Each bar is represented as a struct, showing its timestamp and OHLCV values. This format is useful for direct processing within Go applications.

```text
{Timestamp:2022-09-01 05:00:00 +0000 UTC Open:20055.79 High:20292 Low:19564.86 Close:20156.76 Volume:7141.975485 TradeCount:110122 VWAP:19934.1678446199}
{Timestamp:2022-09-02 05:00:00 +0000 UTC Open:20156.76 High:20444 Low:19757.72 Close:19919.47 Volume:7165.911879 TradeCount:96231 VWAP:20075.2008677126}
{Timestamp:2022-09-03 05:00:00 +0000 UTC Open:19924.83 High:19968.2 Low:19658.04 Close:19806.11 Volume:2677.652012 TradeCount:51551 VWAP:19800.1854803241}
{Timestamp:2022-09-04 05:00:00 +0000 UTC Open:19805.39 High:20058 Low:19587.86 Close:19888.67 Volume:4325.67879 TradeCount:62082 VWAP:19834.4514137038}
{Timestamp:2022-09-05 05:00:00 +0000 UTC Open:19888.67 High:20180.5 Low:19635.96 Close:19760.56 Volume:6274.552824 TradeCount:84784 VWAP:19812.0959815687}
{Timestamp:2022-09-06 05:00:00 +0000 UTC Open:19761.39 High:20026.91 Low:18534.06 Close:18724.59 Volume:11217.789784 TradeCount:128106 VWAP:19266.8355201911}
```

--------------------------------

### Get Stock Positions - JavaScript

Source: https://docs.alpaca.markets/docs/working-with-positions

Fetches stock positions from the Alpaca Markets API. This snippet demonstrates how to get a specific stock's position or all open positions in a portfolio. It utilizes the '@alpacahq/alpaca-trade-api' library.

```javascript
const Alpaca = require("@alpacahq/alpaca-trade-api");
const alpaca = new Alpaca();

// Get our position in AAPL.
aaplPosition = alpaca.getPosition("AAPL");

// Get a list of all of our positions.
alpaca.getPositions().then((portfolio) => {
  // Print the quantity of shares for each position.
  portfolio.forEach(function (position) {
    console.log(`${position.qty} shares of ${position.symbol}`);
  });
});
```

--------------------------------

### Retrieve Historical Crypto Bars

Source: https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data

Retrieve historical daily bar data for Bitcoin using the previously defined request parameters. The result can be accessed as a pandas DataFrame via the .df property.

```python
# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = client.get_crypto_bars(request_params)
```

--------------------------------

### View Account Level Instant Funding Limits (JSON)

Source: https://docs.alpaca.markets/docs/draft-instant-funding

Fetches the instant funding limit available for a specific account or multiple accounts. This allows monitoring the limit per end user. The response is a JSON array containing details for each account requested.

```json
[
    {
        "account_no": "{ACCOUNT_NO}",
        "amount_available": "900",
        "amount_in_use": "100",
        "amount_limit": "1000"
    }
]
```

--------------------------------

### GET /v1/instant_funding/:instant_funding_id

Source: https://docs.alpaca.markets/docs/draft-instant-funding

Fetches a specific instant funding transfer by its ID to check its current status.

```APIDOC
## GET /v1/instant_funding/:instant_funding_id

### Description
Fetches a specific instant funding transfer using its unique identifier to retrieve its current status and details.

### Method
GET

### Endpoint
/v1/instant_funding/:instant_funding_id

### Parameters
#### Path Parameters
- **instant_funding_id** (string) - Required - The unique identifier of the instant funding transfer.

### Response
#### Success Response (200)
- **account_no** (string) - The account number that was credited.
- **amount** (string) - The amount transferred.
- **created_at** (string) - The timestamp when the transfer was created.
- **deadline** (string) - The deadline for the transfer settlement.
- **fees** (array) - An array of fees associated with the transfer.
- **id** (string) - The unique identifier for the instant funding transfer.
- **interests** (array) - An array of interest details associated with the transfer.
- **remaining_payable** (string) - The amount still payable for the transfer.
- **source_account_no** (string) - The source account number from which funds were borrowed.
- **status** (string) - The current status of the transfer (e.g., EXECUTED).
- **system_date** (string) - The system date.
- **total_interest** (string) - The total interest accrued on the transfer.

#### Response Example
```json
{
  "account_no": "{ACCOUNT_NO}",
  "amount": "20",
  "created_at": "2024-09-10T09:12:36.88272Z",
  "deadline": "2024-09-11",
  "fees": [],
  "id": "d96bdc91-6d1c-49b5-a3c3-03f16c70321b",
  "interests": [],
  "remaining_payable": "20",
  "source_account_no": "{ACCOUNT_NO}",
  "status": "EXECUTED",
  "system_date": "2024-09-10",
  "total_interest": "0"
}
```
```

--------------------------------

### Fetch Option Contracts - JSON Example

Source: https://docs.alpaca.markets/docs/options-trading

Example JSON response structure for fetching option contracts. This response includes details like contract ID, symbol, expiration date, strike price, and open interest. It's part of the API for retrieving option contract information.

```json
{
    "option_contracts": [
        {
            "id": "6e58f870-fe73-4583-81e4-b9a37892c36f",
            "symbol": "AAPL240119C00100000",
            "name": "AAPL Jan 19 2024 100 Call",
            "status": "active",
            "tradable": true,
            "expiration_date": "2024-01-19",
            "root_symbol": "AAPL",
            "underlying_symbol": "AAPL",
            "underlying_asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
            "type": "call",
            "style": "american",
            "strike_price": "100",
            "size": "100",
            "open_interest": "6168",
            "open_interest_date": "2024-01-12",
            "close_price": "85.81",
            "close_price_date": "2024-01-12"
        }
	],
   "page_token": "MTAw",
   "limit": 100
}
```

--------------------------------

### Connect to Alpaca Option Data WebSocket Stream

Source: https://docs.alpaca.markets/docs/real-time-option-data

Establishes a WebSocket connection to the Alpaca Markets real-time option data stream. Requires specifying the feed ('indicative' or 'opra') and uses msgpack for data.

```python
import websocket
import json

# Replace with your actual feed (indicative or opra)
FEED = "indicative"

URL = f"wss://stream.data.alpaca.markets/v1beta1/{FEED}"
# Sandbox URL: wss://stream.data.sandbox.alpaca.markets/v1beta1/{FEED}

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")

def on_open(ws):
    print("Connection opened")
    # Authentication: Replace with your actual API key and secret
    auth_message = {
        "action": "auth",
        "key": "YOUR_API_KEY",
        "secret": "YOUR_API_SECRET"
    }
    ws.send(json.dumps(auth_message))

    # Subscribe to channels (e.g., trades and quotes for a specific symbol)
    # Note: The actual subscription message format might differ for options.
    # Refer to Alpaca documentation for the correct subscription structure for options.
    subscribe_message = {
        "action": "subscribe",
        "quotes": ["AAPL240315C00172500"], # Example option symbol
        "trades": ["AAPL240315C00172500"]
    }
    ws.send(json.dumps(subscribe_message))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(URL, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever()

```