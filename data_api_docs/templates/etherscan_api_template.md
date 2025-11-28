# Etherscan API Template - Data Scraping Layer

## Service Overview
**Provider:** Etherscan  
**Purpose:** Ethereum blockchain data, on-chain metrics, token data  
**Base URL:** `https://api.etherscan.io/v2/api`

## Authentication
- **Type:** API Key
- **Parameter:** `apikey` (query parameter)
- **Note:** Free tier available with rate limits; paid tiers have higher limits

## Rate Limits
- **Free Tier:** 5 requests per second
- **Paid Tier:** Higher limits (varies by plan)
- **Window:** Per second
- **Note:** Implement rate limiting with exponential backoff

## Key Endpoints

### 1. Token Transfers (ERC-20)
**Endpoint:** `GET /api?module=account&action=tokentx`

**Purpose:** Get ERC-20 token transfer records for an address

**Parameters:**
- `apikey` (required): API key
- `chainid` (optional): Chain ID (1 for Ethereum, 8453 for Base, etc.)
- `module` (required): `account`
- `action` (required): `tokentx`
- `contractaddress` (optional): Filter by token contract address
- `address` (required): Address to query
- `startblock` (optional): Starting block (default: 0)
- `endblock` (optional): Ending block (default: 9999999999)
- `page` (optional): Page number (default: 1)
- `offset` (optional): Results per page (default: 1)
- `sort` (optional): `asc` or `desc` (default: `desc`)

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: Array<{
    blockNumber: string;
    timeStamp: string;
    hash: string;
    nonce: string;
    blockHash: string;
    from: string;
    contractAddress: string;
    to: string;
    value: string;              // Token amount (in smallest unit)
    tokenName: string;
    tokenSymbol: string;
    tokenDecimal: string;
    transactionIndex: string;
    gas: string;
    gasPrice: string;
    gasUsed: string;
    cumulativeGasUsed: string;
    methodId: string;
    functionName: string;
    confirmations: string;
  }>;
}
```

**Use Case:** Track token transfers for wallet addresses

---

### 2. Event Logs
**Endpoint:** `GET /api?module=logs&action=getLogs`

**Purpose:** Get event logs emitted by a contract

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `logs`
- `action` (required): `getLogs`
- `address` (required): Contract address
- `fromBlock` (required): Starting block number
- `toBlock` (required): Ending block number
- `page` (optional): Page number
- `offset` (optional): Results per page (max: 1000)

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: Array<{
    address: string;
    topics: string[];
    data: string;
    blockNumber: string;
    blockHash: string;
    timeStamp: string;
    gasPrice: string;
    gasUsed: string;
    logIndex: string;
    transactionHash: string;
    transactionIndex: string;
  }>;
}
```

**Use Case:** Monitor smart contract events (transfers, approvals, etc.)

---

### 3. Block Information
**Endpoint:** `GET /api?module=proxy&action=eth_getBlockByNumber`

**Purpose:** Get block details by block number

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `proxy`
- `action` (required): `eth_getBlockByNumber`
- `tag` (required): Block number (hex) or 'latest', 'earliest', 'pending'
- `boolean` (optional): Include full transaction objects (true/false)

**Response Structure:**
```typescript
{
  jsonrpc: "2.0";
  id: number;
  result: {
    number: string;
    hash: string;
    parentHash: string;
    timestamp: string;
    gasLimit: string;
    gasUsed: string;
    transactions: Array<string | TransactionObject>;
    miner: string;
    difficulty: string;
    totalDifficulty: string;
    size: string;
  };
}
```

**Use Case:** Block-level analytics

---

### 4. Gas Oracle
**Endpoint:** `GET /api?module=gastracker&action=gasoracle`

**Purpose:** Get current gas price recommendations

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `gastracker`
- `action` (required): `gasoracle`

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: {
    LastBlock: string;
    SafeGasPrice: string;      // Recommended for standard transactions
    ProposeGasPrice: string;   // Recommended for fast transactions
    FastGasPrice: string;      // Recommended for fastest transactions
    suggestBaseFee: string;
    gasUsedRatio: string;
  };
}
```

**Use Case:** Gas price estimation for transactions

---

### 5. Daily Network Statistics
**Endpoint:** `GET /api?module=stats&action=dailytx`

**Purpose:** Get daily transaction count

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `stats`
- `action` (required): `dailytx`
- `startdate` (required): Start date (YYYY-MM-DD)
- `enddate` (required): End date (YYYY-MM-DD)
- `sort` (optional): `asc` or `desc` (default: `desc`)

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: Array<{
    UTCDate: string;
    unixTimeStamp: string;
    transactionCount: string;
  }>;
}
```

**Use Case:** Network activity metrics

---

### 6. Daily Gas Used
**Endpoint:** `GET /api?module=stats&action=dailygasused`

**Purpose:** Get daily total gas used

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `stats`
- `action` (required): `dailygasused`
- `startdate` (required): Start date (YYYY-MM-DD)
- `enddate` (required): End date (YYYY-MM-DD)
- `sort` (optional): `asc` or `desc`

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: Array<{
    UTCDate: string;
    unixTimeStamp: string;
    gasUsed: string;
  }>;
}
```

**Use Case:** Network utilization metrics

---

### 7. Daily Network Utilization (PRO)
**Endpoint:** `GET /api?module=stats&action=dailynetutilization`

**Purpose:** Get daily network utilization percentage

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `stats`
- `action` (required): `dailynetutilization`
- `startdate` (required): Start date (YYYY-MM-DD)
- `enddate` (required): End date (YYYY-MM-DD)
- `sort` (optional): `asc` or `desc`

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: Array<{
    UTCDate: string;
    unixTimeStamp: string;
    networkUtilization: string;  // Percentage (0-1)
  }>;
}
```

**Use Case:** Network congestion metrics

---

### 8. Contract ABI
**Endpoint:** `GET /api/v1/contract/getabi`

**Purpose:** Get ABI for verified contracts

**Parameters:**
- `apikey` (required): API key
- `chainid` (optional): Chain ID
- `module` (required): `contract`
- `action` (required): `getabi`
- `address` (required): Contract address

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: string;  // JSON string of ABI array
}
```

**Use Case:** Contract interaction and analysis

---

### 9. Contract Creation Info
**Endpoint:** `GET /api?module=contract&action=getcontractcreation`

**Purpose:** Get contract creator and creation transaction

**Parameters:**
- `apikey` (optional): API key
- `chainid` (optional): Chain ID
- `module` (required): `contract`
- `action` (required): `getcontractcreation`
- `contractaddresses` (required): Up to 5 addresses, comma-separated

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: Array<{
    contractAddress: string;
    contractCreator: string;
    txHash: string;
    blockNumber: string;
    timestamp: string;
    contractFactory?: string;
    creationBytecode: string;
  }>;
}
```

**Use Case:** Contract origin tracking

---

### 10. Latest Block Number
**Endpoint:** `GET /api?module=proxy&action=eth_blockNumber`

**Purpose:** Get latest block number

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `proxy`
- `action` (required): `eth_blockNumber`

**Response Structure:**
```typescript
{
  jsonrpc: "2.0";
  id: number;
  result: string;  // Hex block number
}
```

**Use Case:** Sync status and block tracking

---

### 11. ETH Call (Read Contract)
**Endpoint:** `GET /api?module=proxy&action=eth_call`

**Purpose:** Execute read-only contract call

**Parameters:**
- `apikey` (optional): API key
- `chainid` (optional): Chain ID
- `module` (optional): `proxy`
- `action` (optional): `eth_call`
- `to` (required): Contract address
- `data` (required): Encoded function call (method signature + params)
- `tag` (optional): Block tag ('latest', 'earliest', 'pending', or hex block number)

**Response Structure:**
```typescript
{
  jsonrpc: "2.0";
  id: number;
  result: string;  // Hex-encoded return value
}
```

**Use Case:** Read contract state (token balances, contract data)

---

### 12. Token Supply History
**Endpoint:** `GET /api?module=stats&action=tokensupplyhistory`

**Purpose:** Get historical token total supply at specific block

**Parameters:**
- `apikey` (required): API key
- `chainid` (required): Chain ID
- `module` (required): `stats`
- `action` (required): `tokensupplyhistory`
- `contractaddress` (required): Token contract address
- `blockno` (required): Block number

**Response Structure:**
```typescript
{
  status: "1" | "0";
  message: string;
  result: string;  // Token supply at block
}
```

**Use Case:** Token supply tracking over time

---

## Error Handling

**Common Error Codes:**
- `0`: No transactions found (not necessarily an error)
- `1`: Success
- `Invalid API Key`: Authentication failed
- `Rate limit exceeded`: Too many requests

**Error Response:**
```typescript
{
  status: "0";
  message: string;  // Error description
  result: string;   // Usually empty or error details
}
```

## Integration Notes

1. **Chain IDs:**
   - `1`: Ethereum Mainnet
   - `10`: Optimism
   - `56`: BSC
   - `137`: Polygon
   - `8453`: Base
   - `42161`: Arbitrum

2. **Block Numbers:**
   - Use hex format: `0x10d4f`
   - Or use tags: `latest`, `earliest`, `pending`

3. **Address Format:**
   - Must be valid Ethereum address (0x prefix, 42 chars)
   - Case-insensitive

4. **Pagination:**
   - Use `page` and `offset` parameters
   - Max `offset`: 10000 for some endpoints
   - Default `offset`: 1 (very small!)

5. **Rate Limiting:**
   - Free tier: 5 requests/second
   - Implement exponential backoff
   - Use job queue with concurrency: 3-5 workers
   - Cache aggressively (on-chain data is immutable)

6. **Data Types:**
   - All numbers returned as strings
   - Timestamps in Unix epoch (seconds)
   - Values in wei (smallest unit) - need to divide by decimals

## Scraping Implementation

```typescript
// Example: Etherscan On-Chain Scraper
class EtherscanScraper {
  async getTokenTransfers(address: string, contractAddress?: string, startBlock?: number, endBlock?: number) {
    // Fetch ERC-20 transfers
    // Parse and normalize data
    // Cache results
  }
  
  async getEventLogs(contractAddress: string, fromBlock: number, toBlock: number, topics?: string[]) {
    // Fetch contract event logs
    // Decode if ABI available
  }
  
  async getGasOracle() {
    // Get current gas prices
    // Update cache
  }
  
  async getNetworkStats(startDate: string, endDate: string) {
    // Fetch daily network statistics
    // Aggregate for on-chain metrics
  }
  
  async getContractABI(contractAddress: string) {
    // Get contract ABI for decoding
    // Cache ABI
  }
}
```

## Cache Strategy
- **TTL:** 
  - Token transfers: 5 minutes (for recent blocks)
  - Historical data: 24 hours (immutable)
  - Gas prices: 30 seconds
  - Network stats: 1 hour
- **Key Format:** 
  - `etherscan:transfers:{address}:{contract}:{blockRange}`
  - `etherscan:logs:{contract}:{blockRange}`
  - `etherscan:gas:latest`
  - `etherscan:stats:{date}`

## On-Chain Metrics Mapping

For the `crypto_onchain_cache` table:

```typescript
// Map Etherscan data to on-chain metrics
const onChainMetrics = {
  symbol: tokenSymbol,
  chain: 'ethereum',
  contract_address: contractAddress,
  active_addresses_24h: calculateFromTransfers(transfers24h),
  transaction_count_24h: transfers24h.length,
  transaction_volume_24h: sumTransferAmounts(transfers24h),
  avg_transaction_fee: averageGasUsed * averageGasPrice,
  total_holders: getHolderCount(contractAddress),
  exchange_inflow_24h: calculateExchangeInflow(transfers24h, exchangeAddresses),
  exchange_outflow_24h: calculateExchangeOutflow(transfers24h, exchangeAddresses),
  exchange_netflow_24h: inflow - outflow,
  whale_transactions_24h: countLargeTransfers(transfers24h, threshold),
  data_source: 'etherscan',
  timestamp: new Date()
};
```

