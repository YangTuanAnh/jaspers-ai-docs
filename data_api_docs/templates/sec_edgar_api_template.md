# SEC EDGAR API Template - Data Scraping Layer

## Service Overview
**Provider:** SEC EDGAR (via sec-api.io)  
**Purpose:** SEC filings, company data, insider trading, ownership data  
**JavaScript Package:** `npm install sec-api`  
**Documentation:** https://sec-api.io/docs

The `sec-api` package is a comprehensive Node.js wrapper for accessing SEC EDGAR filings through a powerful query, search, and streaming API. It provides programmatic access to over 18 million SEC filings dating back to 1993, covering more than 10,000 publicly listed companies, ETFs, hedge funds, mutual funds, and investors.

## Authentication
- **Type:** API Key
- **Setup:** `secApi.setApiKey('YOUR_API_KEY')` or per-module configuration
- **Note:** Requires free or paid API key from sec-api.io

## Rate Limits
- **Limit:** Varies by subscription tier
- **Window:** Per minute
- **Note:** Free tier has strict limits; paid tiers have higher limits

## JavaScript Client Setup

```javascript
const secApi = require('sec-api');

// Set API key globally for all modules
secApi.setApiKey('YOUR_API_KEY');

// Or set per module
const { queryApi, streamApi, xbrlApi, extractorApi, renderApi, fullTextSearchApi } = secApi;
queryApi.setApiKey('YOUR_API_KEY');
```

## Key APIs

### 1. Query API - Search and Filter Filings

**Purpose:** Search and filter across all 18 million SEC filings using Elasticsearch query syntax. Supports pagination, sorting, and complex queries.

**JavaScript Example:**
```javascript
const { queryApi } = require('sec-api');

queryApi.setApiKey('YOUR_API_KEY');

// Search for recent 10-Q filings
const query = {
  query: { query_string: { query: 'formType:"10-Q"' } },
  from: '0',
  size: '10',
  sort: [{ filedAt: { order: 'desc' } }]
};

const filings = await queryApi.getFilings(query);
console.log(`Found ${filings.total.value} filings`);

// Search by ticker and form type
const teslaQuery = {
  query: {
    query_string: {
      query: 'ticker:TSLA AND formType:"10-K"'
    }
  },
  from: '0',
  size: '5',
  sort: [{ filedAt: { order: 'desc' } }]
};

const teslaFilings = await queryApi.getFilings(teslaQuery);
console.log(teslaFilings.filings[0].accessionNo);
console.log(teslaFilings.filings[0].linkToFilingDetails);
```

**Query Syntax Examples:**
- `ticker:TSLA AND filedAt:[2020-01-01 TO 2020-12-31] AND formType:"10-Q"`
- `ticker:AAPL AND formType:"8-K"`
- `formType:"13-F" AND filedAt:[2023-01-01 TO 2023-12-31]`

**Response Structure:**
```typescript
{
  total: {
    value: number;
    relation: string;
  };
  filings: Array<{
    id: string;
    accessionNo: string;
    cik: string;
    ticker: string;
    companyName: string;
    formType: string;
    description: string;
    filedAt: string;
    periodOfReport?: string;
    linkToFilingDetails: string;
    linkToTxt: string;
    linkToHtml: string;
    linkToXbrl?: string;
    entities: Array<{
      companyName: string;
      cik: string;
      sic?: string;
    }>;
    documentFormatFiles: Array<{
      sequence: string;
      description: string;
      documentUrl: string;
      type: string;
      size: string;
    }>;
  }>;
}
```

**Use Case:** Search for specific filings by company, date range, or form type

---

### 2. Full-Text Search API - Search Filing Contents

**Purpose:** Search the complete text of all EDGAR filings and their attachments submitted since 2001. Enables searching for specific phrases, keywords, or terms within filing documents and exhibits.

**JavaScript Example:**
```javascript
const { fullTextSearchApi } = require('sec-api');

fullTextSearchApi.setApiKey('YOUR_API_KEY');

// Search for exact phrase in filings
const query = {
  query: '"LPCN 1154"',
  formTypes: ['8-K', '10-Q'],
  startDate: '2021-01-01',
  endDate: '2021-06-14'
};

const results = await fullTextSearchApi.getFilings(query);

// Search multiple terms
const multiTermQuery = {
  query: 'artificial intelligence OR machine learning',
  formTypes: ['10-K'],
  startDate: '2023-01-01',
  endDate: '2023-12-31'
};

const aiFilings = await fullTextSearchApi.getFilings(multiTermQuery);
console.log(`Found ${aiFilings.total.value} filings`);
results.filings.forEach(filing => {
  console.log(`${filing.ticker}: ${filing.companyName}`);
});
```

**Use Case:** Search filing contents for specific terms, phrases, or keywords

---

### 3. Stream API - Real-Time Filing Notifications

**Purpose:** WebSocket-based live stream of newly published filings on SEC EDGAR. Filings are delivered immediately upon publication, enabling real-time monitoring and alerts.

**JavaScript Example:**
```javascript
const { streamApi } = require('sec-api');

// Connect to real-time stream
streamApi.connect('YOUR_API_KEY');

// Handle individual filing events
streamApi.on('filing', (filing) => {
  console.log(`New ${filing.formType} from ${filing.companyName}`);
  console.log(`Ticker: ${filing.ticker}`);
  console.log(`Filed at: ${filing.filedAt}`);
  console.log(`URL: ${filing.linkToFilingDetails}`);

  // Filter for specific form types
  if (filing.formType === '8-K') {
    console.log('Important 8-K filing detected!');
    // Trigger notification or processing logic
  }
});

// Handle batch filing events
streamApi.on('filings', (filings) => {
  console.log(`Received batch of ${filings.length} filings`);
});

// Close connection when done
streamApi.close();
```

**Command Line Usage:**
```bash
# Install globally
npm install sec-api -g

# Connect to real-time stream
sec-api YOUR_API_KEY
```

**Use Case:** Real-time filing alerts and monitoring

---

### 4. XBRL-to-JSON API - Extract Financial Statements

**Purpose:** Converts XBRL financial data from 10-K and 10-Q filings into structured JSON format. Automatically standardizes all financial statements including income statements, balance sheets, and cash flow statements.

**JavaScript Example:**
```javascript
const { xbrlApi } = require('sec-api');

xbrlApi.setApiKey('YOUR_API_KEY');

// Convert using filing HTM URL
const xbrlFromHtm = await xbrlApi.xbrlToJson({
  htmUrl: 'https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm'
});

// Convert using XBRL file URL
const xbrlFromXml = await xbrlApi.xbrlToJson({
  xbrlUrl: 'https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926_htm.xml'
});

// Convert using accession number
const xbrlFromAccession = await xbrlApi.xbrlToJson({
  accessionNo: '0000320193-20-000096'
});

// Access financial data
const revenue = xbrlFromHtm.StatementsOfIncome.RevenueFromContractWithCustomerExcludingAssessedTax;
console.log(`Revenue for period: $${revenue[0].value}`);
console.log(`Period: ${revenue[0].period.startDate} to ${revenue[0].period.endDate}`);

const cash = xbrlFromHtm.BalanceSheets.CashAndCashEquivalentsAtCarryingValue;
console.log(`Cash on hand: $${cash[0].value}`);
```

**Response Structure:**
```typescript
{
  StatementsOfIncome: {
    RevenueFromContractWithCustomerExcludingAssessedTax: Array<{
      value: number;
      period: {
        startDate: string;
        endDate: string;
      };
      unit: string;
    }>;
    // ... other income statement items
  };
  BalanceSheets: {
    CashAndCashEquivalentsAtCarryingValue: Array<{
      value: number;
      period: {
        instant: string;
      };
      unit: string;
    }>;
    // ... other balance sheet items
  };
  StatementsOfCashFlows: {
    // ... cash flow statement items
  };
}
```

**Use Case:** Extract standardized financial statements for quantitative analysis

---

### 5. Extractor API - Parse 10-K/10-Q Sections

**Purpose:** Extracts individual sections from 10-K and 10-Q filings, returning cleaned and standardized content in either plain text or HTML format. All standard sections (1, 1A, 1B, 2, 3, 4, 5, 6, 7, 7A, 8, 9, 9A, 9B, 10, 11, 12, 13, 14) are supported.

**JavaScript Example:**
```javascript
const { extractorApi } = require('sec-api');

extractorApi.setApiKey('YOUR_API_KEY');

const filingUrl = 'https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm';

// Extract Risk Factors section as text
const riskFactorsText = await extractorApi.getSection(filingUrl, '1A', 'text');
console.log(riskFactorsText);

// Extract Risk Factors as HTML
const riskFactorsHtml = await extractorApi.getSection(filingUrl, '1A', 'html');

// Extract MD&A section
const mdaText = await extractorApi.getSection(filingUrl, '7', 'text');
console.log('Management Discussion and Analysis:', mdaText);

// Extract Business section
const businessSection = await extractorApi.getSection(filingUrl, '1', 'text');

// Extract multiple sections
const sections = ['1A', '7', '7A'];
const extractedSections = await Promise.all(
  sections.map(section => extractorApi.getSection(filingUrl, section, 'text'))
);
```

**Supported Sections:**
- **1:** Business
- **1A:** Risk Factors
- **1B:** Unresolved Staff Comments
- **2:** Properties
- **3:** Legal Proceedings
- **4:** Mine Safety Disclosures
- **5:** Market for Registrant's Common Equity
- **6:** Selected Financial Data
- **7:** Management's Discussion and Analysis
- **7A:** Quantitative and Qualitative Disclosures About Market Risk
- **8:** Financial Statements and Supplementary Data
- **9:** Changes in and Disagreements with Accountants
- **9A:** Controls and Procedures
- **9B:** Other Information
- **10:** Directors, Executive Officers and Corporate Governance
- **11:** Executive Compensation
- **12:** Security Ownership of Certain Beneficial Owners
- **13:** Certain Relationships and Related Transactions
- **14:** Principal Accountant Fees and Services

**Use Case:** Extract specific sections for NLP, sentiment analysis, or compliance monitoring

---

### 6. Render API - Download Filing Content

**Purpose:** Downloads and renders filing content, exhibits, and attachments at high speed (up to 40 filings per second). Provides access to over 650,000 gigabytes of filing data.

**JavaScript Example:**
```javascript
const { renderApi } = require('sec-api');

renderApi.setApiKey('YOUR_API_KEY');

// Download filing content as HTML
const filingUrl = 'https://www.sec.gov/Archives/edgar/data/1841925/000121390021032758/ea142795-8k_indiesemic.htm';
const htmlContent = await renderApi.getFilingContent(filingUrl);

console.log('Filing content length:', htmlContent.length);

// Download as PDF
const pdfContent = await renderApi.getFilingContent(filingUrl, 'pdf');

// Download multiple filings in parallel
const urls = [
  'https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm',
  'https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm'
];

const contents = await Promise.all(
  urls.map(url => renderApi.getFilingContent(url))
);

contents.forEach((content, index) => {
  console.log(`Filing ${index + 1} size: ${content.length} bytes`);
});
```

**Use Case:** Download filing content for processing, storage, or analysis

---

## Error Handling

**Common Error Scenarios:**
- Invalid API key
- Rate limit exceeded
- Invalid query syntax
- Filing not found
- Network errors

**Error Handling Pattern:**
```javascript
try {
  const filings = await queryApi.getFilings(query);
} catch (error) {
  if (error.statusCode === 401) {
    console.error('Invalid API key');
  } else if (error.statusCode === 429) {
    console.error('Rate limit exceeded');
    // Implement exponential backoff
  } else {
    console.error('Error:', error.message);
  }
}
```

## Integration Notes

1. **Global vs Per-Module Configuration:**
   ```javascript
   // Global configuration
   const secApi = require('sec-api');
   secApi.setApiKey('YOUR_API_KEY');
   
   // Per-module configuration
   queryApi.setApiKey('YOUR_API_KEY');
   streamApi.setApiKey('YOUR_API_KEY');
   ```

2. **Query Syntax:**
   - Uses Elasticsearch query syntax
   - Supports boolean operators (AND, OR, NOT)
   - Supports date ranges: `filedAt:[2020-01-01 TO 2020-12-31]`
   - Supports field queries: `ticker:TSLA`, `formType:"10-K"`

3. **Form Types:**
   - Common forms: `10-K`, `10-Q`, `8-K`, `13-F`, `13-D`, `13-G`, `4`, `3`, `5`
   - Over 150 form types supported

4. **Rate Limiting:**
   - Implement exponential backoff
   - Monitor rate limit headers
   - Use job queue with concurrency limits
   - Cache results aggressively

5. **Data Formats:**
   - All APIs return JSON
   - XBRL automatically converted to JSON
   - Extractor supports 'text' or 'html' output
   - Render supports 'html' or 'pdf' output

## Scraping Implementation

```typescript
// Example: SEC Filing Scraper
class SECFilingScraper {
  private queryApi: any;
  private streamApi: any;
  private xbrlApi: any;
  private extractorApi: any;

  constructor(apiKey: string) {
    const secApi = require('sec-api');
    secApi.setApiKey(apiKey);
    this.queryApi = secApi.queryApi;
    this.streamApi = secApi.streamApi;
    this.xbrlApi = secApi.xbrlApi;
    this.extractorApi = secApi.extractorApi;
  }

  async searchFilings(ticker: string, formType: string, startDate: string, endDate: string) {
    const query = {
      query: {
        query_string: {
          query: `ticker:${ticker} AND formType:"${formType}" AND filedAt:[${startDate} TO ${endDate}]`
        }
      },
      from: '0',
      size: '100',
      sort: [{ filedAt: { order: 'desc' } }]
    };

    return await this.queryApi.getFilings(query);
  }

  async extractFinancials(filingUrl: string) {
    return await this.xbrlApi.xbrlToJson({ htmUrl: filingUrl });
  }

  async extractSection(filingUrl: string, section: string) {
    return await this.extractorApi.getSection(filingUrl, section, 'text');
  }

  setupStreaming(callback: (filing: any) => void) {
    this.streamApi.connect(process.env.SEC_API_KEY);
    this.streamApi.on('filing', callback);
  }
}
```

## Cache Strategy

- **TTL:**
  - Filing metadata: 24 hours
  - Financial statements: 7 days (quarterly/annual data)
  - Section extracts: 7 days
  - Full filing content: 30 days

- **Key Format:**
  - `sec_edgar:filing:{accessionNo}`
  - `sec_edgar:xbrl:{accessionNo}`
  - `sec_edgar:section:{accessionNo}:{section}`
  - `sec_edgar:query:{hash}`

## Data Mapping

### Mapping to Database Entities

```typescript
interface SECFiling {
  id: string;
  accessionNo: string;
  cik: string;
  ticker: string;
  companyName: string;
  formType: string;
  filedAt: Date;
  periodOfReport?: Date;
  linkToFilingDetails: string;
  linkToHtml: string;
  linkToXbrl?: string;
  source: 'sec_edgar';
}

interface FinancialStatement {
  filingId: string;
  statementType: 'income' | 'balance' | 'cashflow';
  period: {
    startDate?: Date;
    endDate?: Date;
    instant?: Date;
  };
  metrics: Record<string, number>;
  source: 'sec_edgar';
}
```

## Use Cases in SOPHIA

1. **Filing Monitoring:**
   - Real-time 8-K alerts for material events
   - 10-K/10-Q filing notifications
   - Insider trading tracking (Form 4)

2. **Financial Analysis:**
   - Extract standardized financial statements
   - Build historical financial databases
   - Calculate financial ratios and metrics

3. **Compliance Monitoring:**
   - Track regulatory disclosures
   - Monitor executive compensation (Form DEF 14A)
   - Track institutional ownership (Form 13-F)

4. **Research & Due Diligence:**
   - Search filing contents for specific terms
   - Extract risk factors and MD&A sections
   - Analyze company disclosures

5. **Portfolio Analytics:**
   - Track holdings via 13-F filings
   - Monitor activist positions (13-D)
   - Analyze fund holdings

## Notes

- The `sec-api` package eliminates the need to parse XBRL/XML directly
- All APIs return clean JSON responses
- Works with React, Angular, Vue, and other JavaScript frameworks
- Can be deployed in Node.js servers, serverless functions, or client applications
- Requires API key from sec-api.io (free tier available)
- Supports over 18 million filings dating back to 1993
- Covers 10,000+ publicly listed companies, ETFs, hedge funds, and mutual funds
