### GET /coins/{id}/contract/{contract_address}/market_chart

Source: https://docs.coingecko.com/reference/contract-address-market-chart

Fetches historical market data for a cryptocurrency contract. You can specify the target currency, the number of days for which to retrieve data, the data interval, and the precision for currency prices.

```APIDOC
## GET /coins/{id}/contract/{contract_address}/market_chart

### Description
Retrieves historical market data (prices, market caps, total volumes) for a specific cryptocurrency contract address. This endpoint is useful for analyzing price trends, trading volumes, and market capitalization over time.

### Method
GET

### Endpoint
/coins/{id}/contract/{contract_address}/market_chart

### Parameters
#### Path Parameters
- **id** (string) - Required - Asset platform ID. Refers to `/asset_platforms`.
- **contract_address** (string) - Required - The contract address of the token.

#### Query Parameters
- **vs_currency** (string) - Required - Target currency of market data. Refers to `/simple/supported_vs_currencies`.
- **days** (string) - Required - Data up to number of days ago. Accepts any integer or `max`.
- **interval** (enum<string>) - Optional - Data interval. Options: `5m`, `hourly`, `daily`. Leave empty for auto granularity.
- **precision** (enum<string>) - Optional - Decimal place for currency price value. Accepts values from '0' to '18' or `full`.

### Request Example
(No request body for this endpoint)

### Response
#### Success Response (200)
- **prices** (array) - An array of timestamp-price pairs.
- **market_caps** (array) - An array of timestamp-market cap pairs.
- **total_volumes** (array) - An array of timestamp-total volume pairs.

#### Response Example
```json
{
  "prices": [
    [1711843200000, 69702.3087473573],
    [1711929600000, 71246.9514406015],
    [1711983682000, 68887.7495158568]
  ],
  "market_caps": [
    [1711843200000, 1370247487960.09],
    [1711929600000, 1401370211582.37],
    [1711983682000, 1355701979725.16]
  ],
  "total_volumes": [
    [1711843200000, 16408802301.8374],
    [1711929600000, 19723005998.215],
    [1711983682000, 30137418199.6431]
  ]
}
```
```

--------------------------------

### GET /coins/{id}/market_chart

Source: https://docs.coingecko.com/v3.0.1/reference/coins-id-market-chart

Fetches historical market data for a given coin ID, including prices, market caps, and 24-hour trading volumes. You can specify the target currency, the number of past days to retrieve data for, and the data interval.

```APIDOC
## GET /coins/{id}/market_chart

### Description
Get historical market data including price, market cap, and 24hr volume for a specified coin.

### Method
GET

### Endpoint
https://api.coingecko.com/api/v3/coins/{id}/market_chart

### Parameters
#### Path Parameters
- **id** (string) - Required - Coin ID. Refers to `/coins/list`.

#### Query Parameters
- **vs_currency** (string) - Required - Target currency of market data. Refers to `/simple/supported_vs_currencies`.
- **days** (string) - Required - Data up to the number of days ago. You may use any integer.
- **interval** (enum<string>) - Optional - Data interval. Possible value: `daily`. If empty, uses auto granularity.
- **precision** (enum<string>) - Optional - Decimal place for currency price value. Possible values: `full`, `0` to `18`.

#### Request Body
None

### Request Example
```json
{
  "example": "GET https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily"
}
```

### Response
#### Success Response (200)
- **prices** (array) - An array of arrays, where each inner array contains a timestamp and the corresponding price.
- **market_caps** (array) - An array of arrays, where each inner array contains a timestamp and the corresponding market cap.
- **total_volumes** (array) - An array of arrays, where each inner array contains a timestamp and the corresponding 24-hour trading volume.

#### Response Example
```json
{
  "prices": [
    [1711843200000, 69702.3087473573],
    [1711929600000, 71246.9514406015],
    [1711983682000, 68887.7495158568]
  ],
  "market_caps": [
    [1711843200000, 1370247487960.09],
    [1711929600000, 1401370211582.37],
    [1711983682000, 1355701979725.16]
  ],
  "total_volumes": [
    [1711843200000, 16408802301.8374],
    [1711929600000, 19723005998.215],
    [1711983682000, 30137418199.6431]
  ]
}
```
```

--------------------------------

### GET /coins/markets

Source: https://docs.coingecko.com/v3.0.1/reference/coins-markets

Fetches market data for a specified list of coins. You can filter and sort the results by various parameters such as currency, IDs, names, symbols, category, order, and more. It also supports including sparkline data and price change percentages.

```APIDOC
## GET /coins/markets

### Description
Fetches market data for a specified list of coins. You can filter and sort the results by various parameters such as currency, IDs, names, symbols, category, order, and more. It also supports including sparkline data and price change percentages.

### Method
GET

### Endpoint
https://api.coingecko.com/api/v3/coins/markets

### Parameters
#### Query Parameters
- **vs_currency** (string) - Required - Target currency of coins and market data. Example: usd. Refers to `/simple/supported_vs_currencies`.
- **ids** (string) - Optional - Coins' IDs, comma-separated if querying more than 1 coin. Refers to `/coins/list`. Default: bitcoin
- **names** (string) - Optional - Coins' names, comma-separated if querying more than 1 coin. Default: Bitcoin
- **symbols** (string) - Optional - Coins' symbols, comma-separated if querying more than 1 coin. Default: btc
- **include_tokens** (enum<string>) - Optional - For `symbols` lookups, specify `all` to include all matching tokens. Default `top` returns top-ranked tokens (by market cap or volume).
- **category** (string) - Optional - Filter based on coins' category. Refers to `/coins/categories/list`. Example: layer-1
- **order** (enum<string>) - Optional - Sort result by field. Default: market_cap_desc. Possible values: market_cap_asc, market_cap_desc, volume_asc, volume_desc, id_asc, id_desc.
- **per_page** (integer) - Optional - Total results per page. Default: 100. Valid values: 1...250.
- **page** (integer) - Optional - Page through results. Default: 1.
- **sparkline** (boolean) - Optional - Include sparkline 7 days data. Default: false.
- **price_change_percentage** (string) - Optional - Include price change percentage timeframe, comma-separated if query more than 1 timeframe. Default: 1h. Valid values: 1h, 24h, 7d, 14d, 30d, 200d, 1y.
- **locale** (enum<string>) - Optional - Language background. Default: en. Possible values: ar, bg, cs, da, de, el, en, es, fi, fr, he, hi, hr, hu, id, it, ja, ko, lt, nl, no, pl, pt, ro, ru, sk, sl, sv, th, tr, uk, vi, zh, zh-tw.
- **precision** (enum<string>) - Optional - Price precision. Default: full. Possible values: full, '0' through '16'.

### Request Example
```json
{
  "example": "GET /coins/markets?vs_currency=usd&ids=bitcoin,ethereum&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=24h"
}
```

### Response
#### Success Response (200)
- **id** (string) - The ID of the coin.
- **symbol** (string) - The symbol of the coin.
- **name** (string) - The name of the coin.
- **image** (string) - URL of the coin's image.
- **current_price** (number) - The current price of the coin.
- **market_cap** (number) - The market capitalization of the coin.
- **market_cap_rank** (integer) - The market cap rank of the coin.
- **fully_diluted_valuation** (number) - The fully diluted valuation of the coin.
- **total_volume** (number) - The total trading volume of the coin.
- **high_24h** (number) - The highest price of the coin in the last 24 hours.
- **low_24h** (number) - The lowest price of the coin in the last 24 hours.
- **price_change_24h** (number) - The price change of the coin in the last 24 hours.
- **price_change_percentage_24h** (number) - The percentage price change of the coin in the last 24 hours.
- **market_cap_change_24h** (number) - The market cap change of the coin in the last 24 hours.
- **market_cap_change_percentage_24h** (number) - The percentage market cap change of the coin in the last 24 hours.
- **circulating_supply** (number) - The circulating supply of the coin.
- **total_supply** (number) - The total supply of the coin.
- **max_supply** (number) - The maximum supply of the coin.
- **all_time_high** (object) - All-time high price and date.
- **all_time_low** (object) - All-time low price and date.
- **sparkline_in_7d** (object) - Sparkline data for the last 7 days.
- **price_change_percentage_14d_in_currency** (number) - Price change percentage for 14 days in the specified currency.
- **price_change_percentage_24h_in_currency** (number) - Price change percentage for 24 hours in the specified currency.
- **price_change_percentage_30d_in_currency** (number) - Price change percentage for 30 days in the specified currency.
- **price_change_percentage_7d_in_currency** (number) - Price change percentage for 7 days in the specified currency.
- **price_change_percentage_1y_in_currency** (number) - Price change percentage for 1 year in the specified currency.

#### Response Example
```json
{
  "example": [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
      "current_price": 65000.00,
      "market_cap": 1200000000000,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1300000000000,
      "total_volume": 50000000000,
      "high_24h": 66000.00,
      "low_24h": 64000.00,
      "price_change_24h": 500.00,
      "price_change_percentage_24h": 0.77,
      "market_cap_change_24h": 10000000000,
      "market_cap_change_percentage_24h": 0.83,
      "circulating_supply": 19000000,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "all_time_high": {
        "at": "2021-11-10T14:24:19.000Z",
        "value": 69000.00
      },
      "all_time_low": {
        "at": "2013-04-21T00:00:00.000Z",
        "value": 0.04650000
      },
      "sparkline_in_7d": {
        "price": [
          65100.00, 65200.00, 65300.00, 65400.00, 65500.00, 65600.00, 65700.00
        ]
      },
      "price_change_percentage_14d_in_currency": 2.5,
      "price_change_percentage_24h_in_currency": 0.77,
      "price_change_percentage_30d_in_currency": 5.0,
      "price_change_percentage_7d_in_currency": 1.5,
      "price_change_percentage_1y_in_currency": 100.0
    }
  ]
}
```
```

--------------------------------

### Derivatives Exchange Data by ID

Source: https://docs.coingecko.com/reference/derivatives-exchanges-id

Fetches comprehensive data for a derivatives exchange using its ID. This endpoint is useful for obtaining specific details like the exchange's name, current open interest, and trading volume.

```APIDOC
## GET /derivatives/exchanges/{id}

### Description

This endpoint allows you to query the derivatives exchange's related data (ID, name, open interest, ...) based on the exchange's ID.

### Method

GET

### Endpoint

/derivatives/exchanges/{id}

### Parameters

#### Path Parameters

- **id** (string) - Required - The ID of the derivatives exchange to query.

### Request Example

```bash
GET https://api.coingecko.com/api/v3/derivatives/exchanges/binance_futures
```

### Response

#### Success Response (200)

- **name** (string) - The name of the derivatives exchange.
- **open_interest** (number) - The current open interest for the exchange.
- **url** (string) - The URL of the derivatives exchange.
- **country** (string) - The country where the exchange is based.
- **image** (string) - URL of the exchange's logo.
- **trading_volume_24h_btc** (number) - The 24-hour trading volume in BTC.

#### Response Example

```json
{
  "name": "Binance Futures",
  "open_interest": 123456789.12,
  "url": "https://www.binance.com/en/futures/BTCUSD",
  "country": "Cayman Islands",
  "image": "https://static.coingecko.com/s/coingecko-logo-100x100-9a97f8551e540f97f5d3192a4d39f5509b52f085065f64a1c4b533e20a4f0568.png",
  "trading_volume_24h_btc": 56789.12345
}
```
```

--------------------------------

### GET /coins/{id}/market_chart

Source: https://docs.coingecko.com/reference/coins-id-market-chart

Fetches historical market data for a specific cryptocurrency, including prices, market caps, and 24-hour trading volumes. The granularity of the data is determined automatically.

```APIDOC
## GET /coins/{id}/market_chart

### Description
Retrieves historical market data for a specified coin, including price, market cap, and 24-hour volume with auto-determined granularity.

### Method
GET

### Endpoint
/coins/{id}/market_chart

### Parameters
#### Path Parameters
- **id** (string) - Required - Coin ID. Refers to `/coins/list`.

#### Query Parameters
- **vs_currency** (string) - Required - Target currency of market data. Refers to `/simple/supported_vs_currencies`.
- **days** (string) - Required - Data up to the number of days ago. Accepts any integer or `max`.
- **interval** (enum<string>) - Optional - Data interval. Possible values: `5m`, `hourly`, `daily`. Leave empty for auto granularity.
- **precision** (enum<string>) - Optional - Decimal place for currency price value. Possible values: `full`, `0` through `18`.

#### Request Body
This endpoint does not accept a request body.

### Request Example
```json
{
  "example": "Request body is empty for this endpoint."
}
```

### Response
#### Success Response (200)
- **prices** (array) - An array of price data points, where each point is an array containing a timestamp and price.
- **market_caps** (array) - An array of market cap data points, where each point is an array containing a timestamp and market cap.
- **total_volumes** (array) - An array of total volume data points, where each point is an array containing a timestamp and volume.

#### Response Example
```json
{
  "prices": [
    [1711843200000, 69702.3087473573],
    [1711929600000, 71246.9514406015],
    [1711983682000, 68887.7495158568]
  ],
  "market_caps": [
    [1711843200000, 1370247487960.09],
    [1711929600000, 1401370211582.37],
    [1711983682000, 1355701979725.16]
  ],
  "total_volumes": [
    [1711843200000, 16408802301.8374],
    [1711929600000, 19723005998.215],
    [1711983682000, 30137418199.6431]
  ]
}
```
```

--------------------------------

### GET /coins/{id}/market_chart/range

Source: https://docs.coingecko.com/reference/coins-id-market-chart-range

Fetches historical market data for a coin within a specified date range.

```APIDOC
## GET /coins/{id}/market_chart/range

### Description
This endpoint retrieves historical market data (prices, market caps, total volumes) for a specific cryptocurrency within a given date range. You can specify the target currency, date range, data interval, and precision for the price.

### Method
GET

### Endpoint
`https://pro-api.coingecko.com/api/v3/coins/{id}/market_chart/range`

### Parameters
#### Path Parameters
- **id** (string) - Required - The unique identifier of the coin (e.g., 'bitcoin'). Refer to `/coins/list` for a list of available coin IDs.

#### Query Parameters
- **vs_currency** (string) - Required - The target currency of the market data (e.g., 'usd'). Refer to `/simple/supported_vs_currencies` for supported currencies.
- **from** (string) - Required - The starting date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. ISO date string is recommended.
- **to** (string) - Required - The ending date in ISO date string (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM`) or UNIX timestamp. ISO date string is recommended.
- **interval** (enum<string>) - Optional - The data interval. Possible values: `5m`, `hourly`, `daily`. If not specified, the granularity is auto-detected.
- **precision** (enum<string>) - Optional - The number of decimal places for the currency price value. Possible values: `full`, '0' through '18'.

#### Request Body
This endpoint does not accept a request body.

### Request Example
```bash
curl -X GET \
  'https://pro-api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1704067200&to=1704070800&interval=hourly' \
  -H 'accept: application/json' \
  -H 'x-cg-pro-api-key: YOUR_API_KEY'
```

### Response
#### Success Response (200)
- **prices** (array) - An array of [timestamp, price] pairs representing the price history.
- **market_caps** (array) - An array of [timestamp, market_cap] pairs representing the market cap history.
- **total_volumes** (array) - An array of [timestamp, total_volume] pairs representing the total volume history.

#### Response Example
```json
{
  "prices": [
    [1704067241331, 42261.0406175669],
    [1704070847420, 42493.2764087546],
    [1704074443652, 42654.0731066594]
  ],
  "market_caps": [
    [1704067241331, 827596236151.196],
    [1704070847420, 831531023621.411],
    [1704074443652, 835499399014.932]
  ],
  "total_volumes": [
    [1704067241331, 14305769170.9498],
    [1704070847420, 14130205376.1709],
    [1704074443652, 13697382902.2424]
  ]
}
```

### Error Handling
- **400 Bad Request**: Invalid parameters provided.
- **401 Unauthorized**: Invalid API key or insufficient permissions.
- **404 Not Found**: Coin ID not found or resource not available.
```

--------------------------------

### GET /coins/{id}/circulating_supply_chart

Source: https://docs.coingecko.com/reference/coins-id-circulating-supply-chart

Retrieves the historical circulating supply chart for a given coin ID. You can specify the number of past days to fetch data for and the data interval.

```APIDOC
## GET /coins/{id}/circulating_supply_chart

### Description
This endpoint allows you to query historical circulating supply of a coin by number of days away from now based on provided coin ID.

### Method
GET

### Endpoint
`/coins/{id}/circulating_supply_chart`

### Parameters
#### Path Parameters
- **id** (string) - Required - coin ID. Refers to `/coins/list`.

#### Query Parameters
- **days** (string) - Required - Data up to the number of days ago. Valid values: any integer or `max`.
- **interval** (enum<string>) - Optional - Data interval. Possible values: `5m`, `hourly`, `daily`.

#### Request Body
None

### Request Example
```
GET https://pro-api.coingecko.com/api/v3/coins/bitcoin/circulating_supply_chart?days=1&interval=daily

# Header Authentication (choose one)
X-CG-PRO-API-KEY: YOUR_API_KEY
# OR
x_cg_pro_api_key: YOUR_API_KEY
```

### Response
#### Success Response (200)
- **circulating_supply** (array) - An array of arrays, where each inner array contains a timestamp and the corresponding circulating supply.

#### Response Example
```json
{
  "circulating_supply": [
    [1712448000000, "19675268.0"],
    [1712534400000, "19675268.0"],
    [1712586776000, "19675268.0"]
  ]
}
```
```

--------------------------------

### NFT Collection Data

Source: https://docs.coingecko.com/reference/nfts-id

Fetches detailed data for a specific NFT collection, including its name, symbol, images, description, market cap, floor price, volume, and historical performance metrics. It also includes links to external resources and all-time high information.

```APIDOC
## GET /api/v3/nft/{id}

### Description
Retrieves detailed information about a specific NFT collection.

### Method
GET

### Endpoint
/api/v3/nft/{id}

### Parameters
#### Path Parameters
- **id** (string) - Required - The unique identifier of the NFT collection (e.g., 'pudgy-penguins').

#### Query Parameters
None

### Request Example
None

### Response
#### Success Response (200)
- **id** (string) - The unique identifier of the NFT collection.
- **contract_address** (string) - The contract address of the NFT collection.
- **asset_platform_id** (string) - The platform ID the NFT collection belongs to (e.g., 'ethereum').
- **name** (string) - The name of the NFT collection.
- **symbol** (string) - The symbol of the NFT collection.
- **image** (object) - Contains URLs for the small and small_2x versions of the collection's image.
- **banner_image** (string) - URL for the collection's banner image.
- **description** (string) - A description of the NFT collection.
- **native_currency** (string) - The native currency of the blockchain the NFT is on.
- **native_currency_symbol** (string) - The symbol of the native currency.
- **market_cap_rank** (number) - The market cap rank of the collection.
- **floor_price** (object) - Contains the floor price in native currency and USD.
- **market_cap** (object) - Contains the market cap in native currency and USD.
- **volume_24h** (object) - Contains the trading volume in the last 24 hours in native currency and USD.
- **floor_price_in_usd_24h_percentage_change** (number) - The percentage change in floor price (USD) over the last 24 hours.
- **floor_price_24h_percentage_change** (object) - Contains the percentage change in floor price (native currency and USD) over the last 24 hours.
- **market_cap_24h_percentage_change** (object) - Contains the percentage change in market cap (native currency and USD) over the last 24 hours.
- **volume_24h_percentage_change** (object) - Contains the percentage change in volume (native currency and USD) over the last 24 hours.
- **number_of_unique_addresses** (number) - The number of unique addresses holding the NFT.
- **number_of_unique_addresses_24h_percentage_change** (number) - The percentage change in unique addresses over the last 24 hours.
- **volume_in_usd_24h_percentage_change** (number) - The percentage change in volume (USD) over the last 24 hours.
- **total_supply** (number) - The total supply of the NFT collection.
- **one_day_sales** (number) - The number of sales in the last day.
- **one_day_sales_24h_percentage_change** (number) - The percentage change in one-day sales over the last 24 hours.
- **one_day_average_sale_price** (number) - The average sale price in the last day.
- **one_day_average_sale_price_24h_percentage_change** (number) - The percentage change in the one-day average sale price over the last 24 hours.
- **links** (object) - Contains links to the collection's homepage, Twitter, and Discord.
- **floor_price_7d_percentage_change** (object) - Percentage change in floor price (native currency and USD) over 7 days.
- **floor_price_14d_percentage_change** (object) - Percentage change in floor price (native currency and USD) over 14 days.
- **floor_price_30d_percentage_change** (object) - Percentage change in floor price (native currency and USD) over 30 days.
- **floor_price_60d_percentage_change** (object) - Percentage change in floor price (native currency and USD) over 60 days.
- **floor_price_1y_percentage_change** (object) - Percentage change in floor price (native currency and USD) over 1 year.
- **explorers** (array) - List of explorers with their names and links.
- **user_favorites_count** (number) - Number of users who favorited the collection.
- **ath** (object) - Contains the all-time high price in native currency and USD.
- **ath_change_percentage** (object) - Contains the percentage change from the all-time high in native currency and USD.
- **ath_date** (object) - Contains the date of the all-time high in native currency and USD.

#### Response Example
```json
{
  "id": "pudgy-penguins",
  "contract_address": "0xBd3531dA5CF5857e7CfAA92426877b022e612cf8",
  "asset_platform_id": "ethereum",
  "name": "Pudgy Penguins",
  "symbol": "PPG",
  "image": {
    "small": "https://coin-images.coingecko.com/nft_contracts/images/38/small/pudgy.jpg?1730778323",
    "small_2x": "https://coin-images.coingecko.com/nft_contracts/images/38/small_2x/pudgy.jpg?1730778323"
  },
  "banner_image": "https://coin-images.coingecko.com/nft_contracts/images/20/bored-ape-yacht-club-banner.png?1708416120",
  "description": "Pudgy Penguins is a collection of 8,888 unique NFTs featuring cute cartoon penguins, which are generated from a collection of 150 different hand-drawn traits.",
  "native_currency": "ethereum",
  "native_currency_symbol": "ETH",
  "market_cap_rank": 3,
  "floor_price": {
    "native_currency": 12.5,
    "usd": 42317
  },
  "market_cap": {
    "native_currency": 111100,
    "usd": 376114941
  },
  "volume_24h": {
    "native_currency": 429.88,
    "usd": 1455314
  },
  "floor_price_in_usd_24h_percentage_change": 1.07067,
  "floor_price_24h_percentage_change": {
    "usd": 1.07067060717791,
    "native_currency": 1.21457489878543
  },
  "market_cap_24h_percentage_change": {
    "usd": 1.07067060717767,
    "native_currency": -0.404858299595142
  },
  "volume_24h_percentage_change": {
    "usd": -3.19833776698741,
    "native_currency": -1.80185531390094
  },
  "number_of_unique_addresses": 4752,
  "number_of_unique_addresses_24h_percentage_change": 0.08425,
  "volume_in_usd_24h_percentage_change": -3.19834,
  "total_supply": 8888,
  "one_day_sales": 36,
  "one_day_sales_24h_percentage_change": -2.7027027027027,
  "one_day_average_sale_price": 11.9411943888889,
  "one_day_average_sale_price_24h_percentage_change": 0.925870927379588,
  "links": {
    "homepage": "https://www.pudgypenguins.com/",
    "twitter": "https://twitter.com/pudgypenguins",
    "discord": "https://discord.gg/pudgypenguins"
  },
  "floor_price_7d_percentage_change": {
    "usd": -18.0014948262365,
    "native_currency": -13.7931034482759
  },
  "floor_price_14d_percentage_change": {
    "usd": -8.63235339431041,
    "native_currency": -8.61905110022663
  },
  "floor_price_30d_percentage_change": {
    "usd": -14.3765649314409,
    "native_currency": -0.777901254167328
  },
  "floor_price_60d_percentage_change": {
    "usd": 15.2779758703282,
    "native_currency": -18.0327868852459
  },
  "floor_price_1y_percentage_change": {
    "usd": 429.5685372855,
    "native_currency": 196.208530805687
  },
  "explorers": [
    {
      "name": "Etherscan",
      "link": "https://etherscan.io/token/0xBd3531dA5CF5857e7CfAA92426877b022e612cf8"
    },
    {
      "name": "Ethplorer",
      "link": "https://ethplorer.io/address/0xBd3531dA5CF5857e7CfAA92426877b022e612cf8"
    }
  ],
  "user_favorites_count": 3660,
  "ath": {
    "native_currency": 22.9,
    "usd": 67535
  },
  "ath_change_percentage": {
    "native_currency": -59.825327510917,
    "usd": -64.3396788440525
  },
  "ath_date": {
    "native_currency": "2024-02-17T09:25:05.056Z",
    "usd": "2024-02-29T11:45:08.150Z"
  }
}
```
```

--------------------------------

### Get Latest NFT Data

Source: https://docs.coingecko.com/docs/3-get-exchanges-nft-data

Fetch the latest market data for a specific NFT collection using its ID. This includes metrics relevant to NFT performance.

```APIDOC
## GET /nfts/{id}

### Description
Retrieves the latest market data for a specific NFT collection.

### Method
GET

### Endpoint
/nfts/{id}

### Parameters
#### Path Parameters
- **id** (string) - Required - The ID of the NFT collection (e.g., `cryptopunks`).

### Request Example
None

### Response
#### Success Response (200)
- **name** (string) - The name of the NFT collection.
- **asset_platform_id** (string) - The ID of the blockchain platform.
- **floor_price** (object) - The current floor price of the NFT collection.
  - **native_currency** (string) - The native currency symbol.
  - **decimal_place** (integer) - The number of decimal places for the currency.
  - **value** (number) - The floor price value.

#### Response Example
```json
{
  "name": "CryptoPunks",
  "asset_platform_id": "ethereum",
  "floor_price": {
    "native_currency": "ETH",
    "decimal_place": 18,
    "value": 50.75
  }
}
```
```

--------------------------------

### GET /networks/{network}/tokens/multi/{addresses}

Source: https://docs.coingecko.com/v3.0.1/reference/tokens-data-contract-addresses

Fetches on-chain data for one or more token contract addresses on a specified network. You can include details about top liquidity pools and their composition.

```APIDOC
## GET /networks/{network}/tokens/multi/{addresses}

### Description
Retrieves on-chain data for specified token contract addresses on a given network. This endpoint supports fetching multiple tokens by providing a comma-separated list of addresses. Optional parameters allow for the inclusion of detailed information about top liquidity pools and their composition.

### Method
GET

### Endpoint
`/networks/{network}/tokens/multi/{addresses}`

### Parameters
#### Path Parameters
- **network** (string) - Required - The ID of the blockchain network (e.g., 'solana'). Refers to [/networks](/reference/networks-list).
- **addresses** (string) - Required - A comma-separated string of token contract addresses.

#### Query Parameters
- **include** (enum<string>) - Optional - Attributes to include. Supported values: 'top_pools'.
- **include_composition** (boolean) - Optional - Whether to include pool composition details. Defaults to `false`.

#### Request Body
This endpoint does not accept a request body.

### Request Example
```bash
GET https://api.coingecko.com/api/v3/onchain/networks/solana/tokens/multi/6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN,2g4LS3y2myPe6vj9wTvoBE1wKqxvhnZPoZA9QU9upump?include=top_pools&include_composition=true
```

### Response
#### Success Response (200)
- **data** (array) - An array of token objects, each containing detailed on-chain attributes such as address, name, symbol, price, market cap, and liquidity pool information.
  - **id** (string) - The unique identifier for the token.
  - **type** (string) - The type of the resource.
  - **attributes** (object) - Contains core on-chain attributes of the token.
    - **address** (string) - The contract address of the token.
    - **name** (string) - The name of the token.
    - **symbol** (string) - The symbol of the token.
    - **decimals** (integer) - The number of decimal places for the token.
    - **image_url** (string) - URL for the token's image.
    - **coingecko_coin_id** (string) - CoinGecko's internal ID for the coin.
    - **total_supply** (string) - The total supply of the token.
    - **normalized_total_supply** (string) - Normalized total supply.
    - **price_usd** (string) - The current price of the token in USD.
    - **fdv_usd** (string) - The fully diluted valuation in USD.
    - **total_reserve_in_usd** (string) - Total liquidity reserve in USD.
    - **volume_usd** (object) - Trading volume information.
      - **h24** (string) - 24-hour trading volume in USD.
    - **market_cap_usd** (string) - Market capitalization in USD.
    - **launchpad_details** (object) - Details related to token launchpad events.
      - **graduation_percentage** (number) - Percentage completion of the launchpad event.
      - **completed** (boolean) - Whether the launchpad event is completed.
      - **completed_at** (string, nullable) - Timestamp when the launchpad event was completed.
      - **migrated_destination_pool_address** (string, nullable) - Address of the migrated destination pool.
  - **relationships** (object) - Relationships to other resources.
    - **top_pools** (object) - Information about top liquidity pools associated with the token.
      - **data** (array) - Array of top pool data.
        - **id** (string) - The ID of the pool.
        - **type** (string) - The type of the resource.
- **included** (array) - Additional included resources, if requested.
  - **id** (string) - The unique identifier for the included resource.

#### Response Example
```json
{
  "data": [
    {
      "id": "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN",
      "type": "token",
      "attributes": {
        "address": "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN",
        "name": "Bonk",
        "symbol": "BONK",
        "decimals": 5,
        "image_url": "https://static.coingecko.com/s/coingecko-logo-d13d65c170e7099b3418a7663f6376e756e01f263d6f6c0394c6a2277b071f97.png",
        "coingecko_coin_id": "bonk",
        "total_supply": "49990053151795.26",
        "normalized_total_supply": "49990053151795.26",
        "price_usd": "0.00002456",
        "fdv_usd": "1228034525.36",
        "total_reserve_in_usd": "1228034525.36",
        "volume_usd": {
          "h24": "1228034525.36"
        },
        "market_cap_usd": "1228034525.36",
        "launchpad_details": null
      },
      "relationships": {
        "top_pools": {
          "data": [
            {
              "id": "pool123",
              "type": "liquidity_pool"
            }
          ]
        }
      }
    }
  ],
  "included": []
}
```
```