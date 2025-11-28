# SEC EDGAR Filings API

The sec-api package is a comprehensive Node.js wrapper for accessing SEC EDGAR filings through a powerful query, search, and streaming API. It provides programmatic access to over 18 million SEC filings dating back to 1993, covering more than 10,000 publicly listed companies, ETFs, hedge funds, mutual funds, and investors. All filings are mapped to CIK and ticker symbols, supporting over 150 form types including 10-K, 10-Q, 8-K, 13-F, and many others.

The library offers six primary APIs: Query API for searching and filtering filings, Full-Text Search API for searching filing contents, Stream API for real-time filing notifications, XBRL-to-JSON API for extracting standardized financial statements, Extractor API for parsing specific sections from 10-K/10-Q filings, and Render API for downloading filing content. All APIs return JSON-formatted data, eliminating the need to work with XBRL/XML directly. The library supports both client-side and server-side JavaScript environments.

## Query API - Search and Filter Filings

The Query API enables searching and filtering across all 18 million SEC filings using Elasticsearch query syntax. It supports pagination, sorting, and complex queries to find specific filings by form type, company, date range, and other attributes.

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

## Full-Text Search API - Search Filing Contents

The Full-Text Search API searches the complete text of all EDGAR filings and their attachments submitted since 2001. It enables searching for specific phrases, keywords, or terms within filing documents and exhibits.

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

## Stream API - Real-Time Filing Notifications

The Stream API provides a WebSocket-based live stream of newly published filings on SEC EDGAR. Filings are delivered to connected clients immediately upon publication, enabling real-time monitoring and alerts.

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

## XBRL-to-JSON API - Extract Financial Statements

The XBRL-to-JSON API converts XBRL financial data from 10-K and 10-Q filings into structured JSON format. It automatically standardizes all financial statements including income statements, balance sheets, and cash flow statements, mapping XBRL facts to their respective contexts with period instants and date ranges.

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

## Extractor API - Parse 10-K/10-Q Sections

The Extractor API extracts individual sections from 10-K and 10-Q filings, returning cleaned and standardized content in either plain text or HTML format. All standard sections (1, 1A, 1B, 2, 3, 4, 5, 6, 7, 7A, 8, 9, 9A, 9B, 10, 11, 12, 13, 14) are supported.

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

## Render API - Download Filing Content

The Render API downloads and renders filing content, exhibits, and attachments at high speed (up to 40 filings per second). It provides access to over 650,000 gigabytes of filing data for processing in memory or saving to disk.

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

## Global API Key Configuration

Set the API key globally for all API modules or individually per module. The global configuration simplifies code when using multiple APIs together.

```javascript
const secApi = require('sec-api');

// Set API key globally for all modules
secApi.setApiKey('YOUR_API_KEY');

// Now all APIs can be used without individual key configuration
const { queryApi, streamApi, xbrlApi, extractorApi } = secApi;

const filings = await queryApi.getFilings({
  query: { query_string: { query: 'ticker:AAPL' } },
  from: '0',
  size: '5'
});

// Or set API key per module
queryApi.setApiKey('YOUR_API_KEY');
streamApi.setApiKey('YOUR_API_KEY');
xbrlApi.setApiKey('YOUR_API_KEY');
```

## Command Line Usage - Real-Time Filing Stream

Run the Stream API directly from the command line to monitor new SEC filings in real-time without writing code. Useful for quick monitoring, testing, and piping data to other command-line tools.

```bash
# Install globally
npm install sec-api -g

# Connect to real-time stream
sec-api YOUR_API_KEY

# Output: JSON objects streamed to console as filings are published
# {
#  "accessionNo": "0001213900-21-032169",
#  "ticker": "JOFF",
#  "companyName": "JOFF Fintech Acquisition Corp.",
#  "formType": "10-Q",
#  "filedAt": "2021-06-11T17:25:44-04:00",
#  ...
# }
```

## Summary

The sec-api library serves as a comprehensive solution for accessing SEC EDGAR data programmatically, catering to financial analysis, compliance monitoring, research, and trading applications. Common use cases include building real-time filing alert systems, extracting financial statement data for quantitative analysis, monitoring institutional ownership changes through 13-F filings, performing due diligence by searching filing contents, and creating dashboards that track regulatory disclosures. The library eliminates the complexity of parsing XBRL and navigating the SEC EDGAR website structure, providing clean JSON responses for all data.

Integration patterns typically combine multiple APIs for complete workflows: using the Stream API to detect new filings, the Query API to retrieve historical data, the XBRL API to extract financial metrics, and the Extractor API to parse specific sections for natural language processing or sentiment analysis. The library works seamlessly with React, Angular, Vue, and other JavaScript frameworks, and can be deployed in Node.js servers, serverless functions, or client applications. Error handling should implement retry logic with exponential backoff, and rate limits should be respected according to the API tier. The library requires a free or paid API key from sec-api.io, with different tiers supporting varying request volumes and feature access.
