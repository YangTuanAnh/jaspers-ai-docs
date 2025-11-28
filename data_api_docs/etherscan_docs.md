### Fetch Daily Network Utilization (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/dailynetutilization

This snippet demonstrates how to call the Etherscan API to get daily network utilization data. It requires an API key and specifies the chain ID, module, action, date range, and sort order.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailynetutilization&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Daily Gas Used Data (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/dailygasused

This code snippet demonstrates how to retrieve the daily total gas used on the Ethereum network using a curl command. It requires an Etherscan API key and specifies the start and end dates for the query. The output is a JSON object containing the gas used for each day.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailygasused&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Daily Block Count and Rewards (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/dailyblkcount

This snippet demonstrates how to call the Etherscan API using cURL to retrieve daily block counts and rewards. It requires an API key and specifies parameters for chain ID, module, action, date range, and sort order. The output is a JSON object containing the requested data.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyblkcount&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Block by Number using curl

Source: https://docs.etherscan.io/api-reference/endpoint/ethgetblockbynumber

This example demonstrates how to fetch block information by its hexadecimal number using the Etherscan API via curl. It requires an API key and specifies the chain ID, module, action, block tag, and transaction detail level.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=proxy&action=eth_getBlockByNumber&tag=0x10d4f&boolean=true&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Daily Transactions (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/dailytx

This snippet demonstrates how to use cURL to request daily transaction counts from the Etherscan API. It requires parameters such as API key, chain ID, date range, and sort order. The output is a JSON object containing transaction data.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailytx&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Daily Uncle Block Count and Rewards (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/dailyuncleblkcount

This snippet demonstrates how to fetch daily uncle block count and rewards using cURL. It requires specifying the chain ID, module, action, start date, end date, sort order, and an Etherscan API key. The output is a JSON object containing the results.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyuncleblkcount&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Ethereum Node Size Data (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/chainsize

This snippet demonstrates how to fetch Ethereum node size data using a curl command. It requires parameters such as chain ID, date range, client type, sync mode, and an API key. The output is a JSON object containing the chain size information.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=chainsize&startdate=2019-02-01&enddate=2019-02-28&clienttype=geth&syncmode=default&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Withdrawal Transactions (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/getwithdrawaltxs

Example using curl to query withdrawal transactions from an address on Optimism or Arbitrum. Requires an API key and specifies pagination and sorting.

```bash
curl "https://api.etherscan.io/v2/api?chainid=10&module=account&action=getwithdrawaltxs&address=0x80f3950a4d371c43360f292a4170624abd9eed03&page=1&offset=10&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### GET /api?module=account&action=tokentx

Source: https://docs.etherscan.io/api-reference/endpoint/tokentx

Fetches ERC20 token transfer records for a specified address. You can filter by contract address, block range, and control pagination and sorting.

```APIDOC
## GET /api?module=account&action=tokentx

### Description
Fetches ERC20 token transfer records for a specified address. You can filter by contract address, block range, and control pagination and sorting.

### Method
GET

### Endpoint
/api?module=account&action=tokentx

### Parameters
#### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Optional - Chain ID to query, eg `1` for Ethereum, `8453` for Base from our [supported chains](/supported-chains).
- **module** (string) - Required - Set to `account` for this endpoint.
- **action** (string) - Required - Set to `tokentx` for this endpoint.
- **contractaddress** (string) - Optional - The ERC20 token contract address to filter transfers by, eg `0xdac17f958d2ee523a2206206994597c13d831ec7` for USDT.
- **address** (string) - Required - The address to query, like `0xfefefefefefefefefefefefefefefefefefefefe`
- **startblock** (integer) - Optional - Starting block number to search from. Defaults to `0`.
- **endblock** (integer) - Optional - Ending block number to search to. Defaults to `9999999999`.
- **page** (integer) - Optional - Page number for pagination. Defaults to `1`.
- **offset** (integer) - Optional - Number of transactions per page. Defaults to `1`.
- **sort** (string) - Optional - Sort order either `desc` for the latest transactions first or `asc` for the oldest transactions first. Defaults to `desc`.

### Request Example
(No request body for GET requests, parameters are in the query string)

### Response
#### Success Response (200)
- **status** (string) - The status of the request ('1' for success, '0' for failure).
- **message** (string) - The message returned by the API.
- **result** (array) - An array of ERC20 transfer objects.
  - **blockNumber** (string) - The block number in which the transaction was included.
  - **timeStamp** (string) - The timestamp of the block (Unix epoch time).
  - **hash** (string) - The transaction hash.
  - **nonce** (string) - The transaction nonce.
  - **blockHash** (string) - The hash of the block.
  - **from** (string) - The address that sent the tokens.
  - **contractAddress** (string) - The contract address of the ERC20 token.
  - **to** (string) - The address that received the tokens.
  - **value** (string) - The amount of tokens transferred (in the smallest unit).
  - **tokenName** (string) - The name of the ERC20 token.
  - **tokenSymbol** (string) - The symbol of the ERC20 token.
  - **tokenDecimal** (string) - The number of decimal places the token uses.
  - **transactionIndex** (string) - The index of the transaction within the block.
  - **gas** (string) - The gas limit set for the transaction.
  - **gasPrice** (string) - The gas price used for the transaction.
  - **gasUsed** (string) - The amount of gas used by the transaction.
  - **cumulativeGasUsed** (string) - The cumulative gas used within the block at the time of this transaction.
  - **input** (string) - Deprecated field.
  - **methodId** (string) - The method ID of the function call.
  - **functionName** (string) - The name of the function called.
  - **confirmations** (string) - The number of confirmations for the transaction.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "blockNumber": "4730207",
      "timeStamp": "1513240363",
      "hash": "0xe8c208398bd5ae8e4c237658580db56a2a94dfa0ca382c99b776fa6e7d31d5b4",
      "nonce": "406",
      "blockHash": "0x022c5e6a3d2487a8ccf8946a2ffb74938bf8e5c8a3f6d91b41c56378a96b5c37",
      "from": "0x642ae78fafbb8032da552d619ad43f1d81e4dd7c",
      "contractAddress": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
      "to": "0x4e83362442b8d1bec281594cea3050c8eb01311c",
      "value": "5901522149285533025181",
      "tokenName": "Maker",
      "tokenSymbol": "MKR",
      "tokenDecimal": "18",
      "transactionIndex": "81",
      "gas": "940000",
      "gasPrice": "32010000000",
      "gasUsed": "77759",
      "cumulativeGasUsed": "2523379",
      "input": "deprecated",
      "methodId": "0xbe040fb0",
      "functionName": "redeem()",
      "confirmations": "18737452"
    }
  ]
}
```
```

--------------------------------

### GET /api/stats/dailyavggaslimit

Source: https://docs.etherscan.io/api-reference/endpoint/dailyavggaslimit

Retrieves historical daily average gas limit data. This is a PRO endpoint.

```APIDOC
## GET /api/stats/dailyavggaslimit

### Description
Retrieves historical daily average gas limit for a given chain and date range.

### Method
GET

### Endpoint
`/api/stats/dailyavggaslimit`

### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Required - Chain ID to query, e.g. `1` for Ethereum, `8453` for Base.
- **module** (string) - Required - Set to `stats` for this endpoint.
- **action** (string) - Required - Set to `dailyavggaslimit` for this endpoint.
- **startdate** (string) - Required - Starting date in `yyyy-MM-dd` format.
- **enddate** (string) - Required - Ending date in `yyyy-MM-dd` format.
- **sort** (string) - Optional - Sort order either `desc` for the latest results first or `asc` for the oldest results first. Defaults to `desc`.

### Request Example
```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyavggaslimit&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the status of the request.
- **message** (string) - Describes the result of the request.
- **result** (array) - An array of objects containing daily gas limit data.
  - **UTCDate** (string) - The date in `yyyy-MM-dd` format.
  - **unixTimeStamp** (string) - The Unix timestamp for the date.
  - **gasLimit** (string) - The average gas limit for the day.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "UTCDate": "2019-02-01",
      "unixTimeStamp": "1548979200",
      "gasLimit": "8001360"
    },
    {
      "UTCDate": "2019-02-02",
      "unixTimeStamp": "1549065600",
      "gasLimit": "8001269"
    }
  ]
}
```
```

--------------------------------

### Get Estimation of Confirmation Time

Source: https://docs.etherscan.io/api-reference/endpoint/gasestimate

Estimate confirmation time based on a provided gas price. This endpoint requires specifying the module and action parameters to retrieve gas estimation data.

```APIDOC
## GET /api

### Description
Estimate confirmation time based on a provided gas price.

### Method
GET

### Endpoint
https://api.etherscan.io/v2/api

### Parameters
#### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Required - Chain ID to query, eg `1` for Ethereum, `8453` for Base.
- **module** (string) - Required - Set to `gastracker` for this endpoint.
- **action** (string) - Required - Set to `gasestimate` for this endpoint.
- **gasprice** (string) - Required - Gas price paid per unit of gas, in wei.

### Request Example
```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=gastracker&action=gasestimate&gasprice=2000000000&apikey=YourApiKeyToken"
```

### Response
#### Success Response (200)
- **status** (string) - The status of the request.
- **message** (string) - The message returned by the API.
- **result** (string) - The estimated confirmation time in seconds.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": "45"
}
```
```

--------------------------------

### Get Gas Oracle Recommendations (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/gasoracle

This snippet demonstrates how to fetch current gas price recommendations using a cURL request to the Etherscan API. It requires an API key and specifies the chain ID, module, and action for the gas oracle endpoint.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=gastracker&action=gasoracle&apikey=YourApiKeyToken"
```

--------------------------------

### Get Current Gas Price using curl

Source: https://docs.etherscan.io/api-reference/endpoint/ethgasprice

This snippet demonstrates how to fetch the current gas price from the Etherscan API using a curl command. It requires your Etherscan API key and specifies the chain ID, module, and action.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=proxy&action=eth_gasPrice&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Latest Block Number (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/ethblocknumber

This snippet demonstrates how to fetch the latest block number using cURL. It requires your Etherscan API key and specifies the chain ID, module, and action parameters.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Ether Daily Price (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/ethdailyprice

This snippet demonstrates how to make a GET request to the Etherscan API to retrieve historical daily Ether prices. It requires an API key and specifies the date range and sorting preference. The response is in JSON format.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=ethdailyprice&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Fetch Daily Average Block Time (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/dailyavgblocktime

This snippet demonstrates how to make a GET request to the Etherscan API to retrieve daily average block times. It requires an API key and specifies the chain ID, module, action, date range, and sorting preference.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyavgblocktime&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Etherscan API Event Log Response Example

Source: https://docs.etherscan.io/api-reference/endpoint/getlogs-topics

This JSON structure represents a successful response from the Etherscan API when fetching event logs. It includes status, message, and a list of log objects, each containing details like address, topics, data, and block information.

```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "address": "0xbd3531da5cf5857e7cfaa92426877b022e612cf8",
      "topics": [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x0000000000000000000000000000000000000000000000000000000000000000",
        "0x000000000000000000000000c45a4b3b698f21f88687548e7f5a80df8b99d93d",
        "0x00000000000000000000000000000000000000000000000000000000000000b5"
      ],
      "data": "0x",
      "blockNumber": "0xc48174",
      "blockHash": "0x837e109ab8b1b40ec7d1032bff82397325d85e719b97d900fa0d9aa9745b2c27",
      "timeStamp": "0x60f9ce56",
      "gasPrice": "0x2e90edd000",
      "gasUsed": "0x247205",
      "logIndex": "0x",
      "transactionHash": "0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",
      "transactionIndex": "0x"
    }
  ]
}
```

--------------------------------

### Get Daily Network Utilization

Source: https://docs.etherscan.io/api-reference/endpoint/dailynetutilization

Retrieves daily network utilization data for a specified chain and date range. This is a PRO endpoint and requires a paid tier subscription.

```APIDOC
## GET /api/v2/api

### Description
Retrieves daily network utilization data for a specified chain and date range. This is a PRO endpoint.

### Method
GET

### Endpoint
https://api.etherscan.io/v2/api

### Parameters
#### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Required - Chain ID to query, e.g., `1` for Ethereum, `8453` for Base.
- **module** (string) - Required - Set to `stats` for this endpoint.
- **action** (string) - Required - Set to `dailynetutilization` for this endpoint.
- **startdate** (string) - Required - Starting date in `yyyy-MM-dd` format.
- **enddate** (string) - Required - Ending date in `yyyy-MM-dd` format.
- **sort** (string) - Optional - Sort order either `desc` for the latest results first or `asc` for the oldest results first. Defaults to `desc`.

### Request Example
```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailynetutilization&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the request ('1' for success).
- **message** (string) - Describes the status of the request ('OK' for success).
- **result** (array) - An array of objects, each containing daily network utilization data.
  - **UTCDate** (string) - The date in `yyyy-MM-dd` format.
  - **unixTimeStamp** (string) - The Unix timestamp for the start of the day.
  - **networkUtilization** (string) - The network utilization value for that day.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "UTCDate": "2019-02-01",
      "unixTimeStamp": "1548979200",
      "networkUtilization": "0.8464"
    },
    {
      "UTCDate": "2019-02-02",
      "unixTimeStamp": "1549065600",
      "networkUtilization": "0.7687"
    }
  ]
}
```
```

--------------------------------

### GET /api

Source: https://docs.etherscan.io/api-reference/endpoint/getlogs

Fetches event logs for a specified address. This is a GET request to the Etherscan API endpoint.

```APIDOC
## GET /api

### Description
Retrieves event logs emitted by a specific address on the Ethereum blockchain. You can filter logs by block number ranges and paginate results.

### Method
GET

### Endpoint
`/api`

### Parameters
#### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Required - Chain ID to query, e.g., `1` for Ethereum, `8453` for Base.
- **module** (string) - Required - Set to `logs` for this endpoint.
- **action** (string) - Required - Set to `getLogs` for this endpoint.
- **address** (string) - Required - Address to check for logs.
- **fromBlock** (integer) - Required - Starting block number to search from.
- **toBlock** (integer) - Required - Ending block number to search to.
- **page** (integer) - Optional - Page number for pagination. Defaults to 1.
- **offset** (integer) - Optional - Number of records per page. Limited to 1000 records per query; use the `page` parameter for subsequent records. Defaults to 1000.

### Request Example
```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=logs&action=getLogs&address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8&fromBlock=12878196&toBlock=12878196&page=1&offset=1000&apikey=YourApiKeyToken"
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the status of the request ('1' for success).
- **message** (string) - A message describing the result of the request ('OK' for success).
- **result** (array) - An array of log objects, each containing details of an emitted event.
  - **address** (string) - The address that emitted the log.
  - **topics** (array) - An array of topics associated with the log.
  - **data** (string) - The data payload of the log.
  - **blockNumber** (string) - The block number in which the log was included.
  - **blockHash** (string) - The hash of the block.
  - **timeStamp** (string) - The timestamp of the block.
  - **gasPrice** (string) - The gas price at the time of the transaction.
  - **gasUsed** (string) - The amount of gas used for the transaction.
  - **logIndex** (string) - The index of the log within the block.
  - **transactionHash** (string) - The hash of the transaction that emitted the log.
  - **transactionIndex** (string) - The index of the transaction within the block.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "address": "0xbd3531da5cf5857e7cfaa92426877b022e612cf8",
      "topics": [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x0000000000000000000000000000000000000000000000000000000000000000",
        "0x000000000000000000000000c45a4b3b698f21f88687548e7f5a80df8b99d93d",
        "0x00000000000000000000000000000000000000000000000000000000000000b5"
      ],
      "data": "0x",
      "blockNumber": "0xc48174",
      "blockHash": "0x837e109ab8b1b40ec7d1032bff82397325d85e719b97d900fa0d9aa9745b2c27",
      "timeStamp": "0x60f9ce56",
      "gasPrice": "0x2e90edd000",
      "gasUsed": "0x247205",
      "logIndex": "0x",
      "transactionHash": "0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",
      "transactionIndex": "0x"
    },
    {
      "address": "0xbd3531da5cf5857e7cfaa92426877b022e612cf8",
      "topics": [
        "0x645f26e653c951cec836533f8fe0616d301c20a17153debc17d7c3dbe4f32b28",
        "0x00000000000000000000000000000000000000000000000000000000000000b5"
      ],
      "data": "0x",
      "blockNumber": "0xc48174",
      "blockHash": "0x837e109ab8b1b40ec7d1032bff82397325d85e719b97d900fa0d9aa9745b2c27",
      "timeStamp": "0x60f9ce56",
      "gasPrice": "0x2e90edd000",
      "gasUsed": "0x247205",
      "logIndex": "0x1",
      "transactionHash": "0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",
      "transactionIndex": "0x"
    }
  ]
}
```
```

--------------------------------

### Get Event Logs using cURL

Source: https://docs.etherscan.io/api-reference/endpoint/getlogs-topics

This snippet demonstrates how to fetch event logs using the cURL command-line tool. It includes essential query parameters such as block range, topic filters, pagination, and API key. The request targets the Etherscan API for log retrieval.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=logs&action=getLogs&fromBlock=12878196&toBlock=12879196&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&topic0_1_opr=and&topic1=0x0000000000000000000000000000000000000000000000000000000000000000&topic1_2_opr=and&topic2=0x000000000000000000000000c45a4b3b698f21f88687548e7f5a80df8b99d93d&topic2_3_opr=and&topic3=0x00000000000000000000000000000000000000000000000000000000000000b5&topic0_2_opr=and&topic0_3_opr=and&topic1_3_opr=and&page=1&offset=1000&apikey=YourApiKeyToken"
```

--------------------------------

### Get Daily Average Gas Limit (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/dailyavggaslimit

This code snippet demonstrates how to retrieve historical daily average gas limit data using a cURL command. It requires an Etherscan API key and specifies the chain ID, date range, and sort order.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyavggaslimit&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### eth_call

Source: https://docs.etherscan.io/api-reference/endpoint/ethcall

Execute a call to a contract without creating a transaction. This is useful for reading data from smart contracts.

```APIDOC
## GET /api

### Description
Execute a call to a contract without creating a transaction. This is useful for reading data from smart contracts.

### Method
GET

### Endpoint
https://api.etherscan.io/v2/api

### Parameters
#### Query Parameters
- **apikey** (string) - Optional - Your Etherscan API key.
- **chainid** (string) - Optional - Chain ID to query, eg `1` for Ethereum, `8453` for Base from our [supported chains](/supported-chains).
- **module** (string) - Optional - Set to `proxy` for this endpoint.
- **action** (string) - Optional - Set to `eth_call` for this endpoint.
- **to** (string) - Required - The address to interact with.
- **data** (string) - Required - Hash of the method signature and encoded parameters.
- **tag** (string) - Optional - Use `latest`, `earliest`, `pending`, or a block number in hex.

### Request Example
```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=proxy&action=eth_call&to=0xAEEF46DB4855E25702F8237E8f403FddcaF931C0&data=0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724&tag=latest&apikey=YourApiKeyToken"
```

### Response
#### Success Response (200)
- **jsonrpc** (string) - The JSON-RPC version.
- **id** (integer) - The request ID.
- **result** (string) - The result of the eth_call, typically a hex-encoded value.

#### Response Example
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x00000000000000000000000000000000000000000000000000601d8888141c00"
}
```
```

--------------------------------

### Fetch ERC20 Token TotalSupply History (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/tokensupplyhistory

This snippet demonstrates how to fetch the historical total supply of an ERC20 token at a specific block number using cURL. It requires the Etherscan API key, chain ID, contract address, and block number as parameters. The response includes the total supply.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=tokensupplyhistory&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&blockno=8000000&apikey=YourApiKeyToken"
```

--------------------------------

### Get Block Reward (Bash)

Source: https://docs.etherscan.io/api-reference/endpoint/getblockreward

This snippet demonstrates how to fetch block and uncle rewards for a given block number using the Etherscan API via a `curl` command. It requires specifying the chain ID, module, action, block number, and an API key.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=block&action=getblockreward&blockno=2165403&apikey=YourApiKeyToken"
```

--------------------------------

### Daily Average Gas Price API Response Structure

Source: https://docs.etherscan.io/api-reference/endpoint/dailyavggasprice

Illustrates the JSON structure of the response when fetching daily average gas price statistics. It includes fields for the date, timestamp, maximum, minimum, and average gas prices in Wei.

```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "UTCDate": "2019-02-01",
      "unixTimeStamp": "1548979200",
      "maxGasPrice_Wei": "60814303896257",
      "minGasPrice_Wei": "432495",
      "avgGasPrice_Wei": "13234562600"
    },
    {
      "UTCDate": "2019-02-02",
      "unixTimeStamp": "1549065600",
      "maxGasPrice_Wei": "20000000000000",
      "minGasPrice_Wei": "2352",
      "avgGasPrice_Wei": "12000569516"
    }
  ]
}
```

--------------------------------

### Get Ether Total Supply using cURL

Source: https://docs.etherscan.io/api-reference/endpoint/ethsupply

This snippet demonstrates how to fetch the total supply of Ether using a cURL command. It requires your Etherscan API key and specifies the chain ID, module, and action parameters.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=ethsupply&apikey=YourApiKeyToken"
```

--------------------------------

### Get Daily Block Rewards with Curl

Source: https://docs.etherscan.io/api-reference/endpoint/dailyblockrewards

This snippet demonstrates how to fetch daily block rewards using a cURL command. It includes parameters for chain ID, module, action, start date, end date, sort order, and your Etherscan API key. Ensure you replace 'YourApiKeyToken' with your actual API key.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyblockrewards&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Get Ether Supply via Curl

Source: https://docs.etherscan.io/api-reference/endpoint/ethsupply2

This snippet demonstrates how to fetch the total Ether supply using a curl command. It requires an API key and specifies the module and action parameters for the 'ethsupply2' endpoint.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=ethsupply2&apikey=YourApiKeyToken"
```

--------------------------------

### GET /api?module=contract&action=getcontractcreation

Source: https://docs.etherscan.io/api-reference/endpoint/getcontractcreation

Fetches the creator address and transaction hash for specified contract addresses.

```APIDOC
## GET /api?module=contract&action=getcontractcreation

### Description
Retrieve a contract's deployer address and creation transaction.

### Method
GET

### Endpoint
/api

### Parameters
#### Query Parameters
- **apikey** (string) - Optional - Your Etherscan API key.
- **chainid** (string) - Optional - Chain ID to query, eg `1` for Ethereum, `8453` for Base from our [supported chains](/supported-chains).
- **module** (string) - Required - Set to `contract` for this endpoint.
- **action** (string) - Required - Set to `getcontractcreation` for this endpoint.
- **contractaddresses** (string) - Required - Up to 5 contract addresses, separated by commas.

### Response
#### Success Response (200)
- **status** (string) - API status message.
- **message** (string) - API response message.
- **result** (array) - An array of objects, where each object contains details about a contract's creation.
  - **contractAddress** (string) - The address of the contract.
  - **contractCreator** (string) - The address of the contract creator.
  - **txHash** (string) - The transaction hash of contract creation.
  - **blockNumber** (string) - The block number where the transaction was included.
  - **timestamp** (string) - The timestamp of the block.
  - **contractFactory** (string) - The factory address if the contract was deployed by a factory.
  - **creationBytecode** (string) - The bytecode of the contract's creation.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": [
    {
      "contractAddress": "0xcbdcd3815b5f975e1a2c944a9b2cd1c985a1cb7f",
      "contractCreator": "0x3d080421c9dd5fb387d6e3124f7e1c241ade9568",
      "txHash": "0xdce495a9261c4a2a5d4e879cfb55c060b4616a846d3425c441a9e31aa34c956f",
      "blockNumber": "10720863",
      "timestamp": "1598242563",
      "contractFactory": "",
      "creationBytecode": "0x602d3d8160093d39f3363d3d373d3d3d363d73c6cf0f044ba8ea402bfedf9e87b88bf1c008d1625af43d82803e903d91602b57fd5bf3"
    }
  ]
}
```
```

--------------------------------

### Fetch Daily Average Network Difficulty (cURL)

Source: https://docs.etherscan.io/api-reference/endpoint/dailyavgnetdifficulty

This snippet demonstrates how to call the Etherscan API to retrieve daily average network difficulty. It requires an API key and specifies the chain ID, date range, and sorting preference. The output is a JSON object containing the network difficulty for each day within the specified period.

```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyavgnetdifficulty&startdate=2019-02-01&enddate=2019-02-28&sort=desc&apikey=YourApiKeyToken"
```

--------------------------------

### Get Contract ABI

Source: https://docs.etherscan.io/api-reference/endpoint/getabi

Fetches the ABI for a specified verified smart contract address.

```APIDOC
## GET /api/v1/contract/getabi

### Description
Retrieve the ABI for a verified smart contract.

### Method
GET

### Endpoint
/api/v1/contract/getabi

### Parameters
#### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Optional - Chain ID to query, eg `1` for Ethereum, `8453` for Base from our [supported chains](/supported-chains).
- **module** (string) - Required - Set to `contract` for this endpoint.
- **action** (string) - Required - Set to `getabi` for this endpoint.
- **address** (string) - Required - The contract address to query.

### Request Example
```json
{
  "apikey": "YourApiKeyToken",
  "chainid": "1",
  "module": "contract",
  "action": "getabi",
  "address": "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
}
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the request ('1' for success, '0' for failure).
- **message** (string) - A message describing the result of the request.
- **result** (string) - The ABI of the contract, returned as a JSON string.

#### Response Example
```json
{
  "status": "1",
  "message": "OK",
  "result": "[{\"constant\":false,\"inputs\":[{\"name\":\"_c\",\"type\":\"string\"}],\"name\":\"enterValue\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"test\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]"
}
```
```

--------------------------------

### eth_blockNumber

Source: https://docs.etherscan.io/api-reference/endpoint/ethblocknumber

Fetches the latest block number on the Ethereum blockchain. This endpoint requires an API key and allows specifying the chain ID.

```APIDOC
## GET /api

### Description
Fetch the latest block number.

### Method
GET

### Endpoint
https://api.etherscan.io/v2/api

### Parameters
#### Query Parameters
- **apikey** (string) - Required - Your Etherscan API key.
- **chainid** (string) - Required - Chain ID to query, eg `1` for Ethereum, `8453` for Base from our [supported chains](/supported-chains).
- **module** (string) - Required - Set to `proxy` for this endpoint.
- **action** (string) - Required - Set to `eth_blockNumber` for this endpoint.

### Request Example
```bash
curl "https://api.etherscan.io/v2/api?chainid=1&module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken"
```

### Response
#### Success Response (200)
- **jsonrpc** (string) - The JSON-RPC protocol version.
- **id** (number) - The request ID.
- **result** (string) - The latest block number as a hexadecimal string.

#### Response Example
```json
{
  "jsonrpc": "2.0",
  "id": 83,
  "result": "0x1661760"
}
```
```