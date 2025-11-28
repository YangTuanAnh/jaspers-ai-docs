### Get Economic Data

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches specific economic data using a given economic code.

```javascript
finnhubClient.economicData("MA-USA-656880", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Fetch Stock Tick Data (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves raw tick-level data for a stock on a specific date. This granular data is useful for high-frequency trading analysis and detailed market microstructure studies.

```javascript
finnhubClient.stockTick("AAPL", "2020-03-25", 500, 0, (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Company Earnings

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches company earnings data, with an optional limit on the number of results.

```javascript
finnhubClient.companyEarnings("AAPL", {'limit': 10}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Visa Application Data (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches visa application data for a company within a specified date range. This can indicate hiring trends, international operations, or workforce expansion.

```javascript
finnhubClient.stockVisaApplication('AAPL', '2021-01-01', '2021-12-31', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Explore Investment Themes (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches data related to specific investment themes, such as financial exchanges data. This helps identify broader market trends and thematic investment opportunities.

```javascript
finnhubClient.investmentThemes('financialExchangesData', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Forex Candles

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches historical forex candlestick data for a given currency pair, resolution, and time range.

```javascript
finnhubClient.forexCandles("OANDA:EUR_USD", "D", 1590988249, 1591852249, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Fetch Insider Transactions (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves data on insider trading activities for a given stock symbol. This provides insights into corporate sentiment and potential future stock movements based on insider actions.

```javascript
finnhubClient.insiderTransactions('AAPL', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Retrieve Stock Dividends (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches historical dividend data for a specified stock within a defined date range. This is useful for analyzing a company's dividend payout history and yield.

```javascript
finnhubClient.stockDividends("KO", "2019-01-01", "2020-06-30", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Filings

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves company filings data for a specified symbol.

```javascript
finnhubClient.filings({"symbol": "AAPL"}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Aggregate Indicator

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches aggregate technical indicator data for a stock symbol and resolution.

```javascript
finnhubClient.aggregateIndicator("AAPL", "D", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Earnings Calendar

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches the earnings calendar for a specified date range.

```javascript
finnhubClient.earningsCalendar({"from": "2020-06-01", "to": "2020-06-30"}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Company Executive

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches information about the executives of a specified company.

```javascript
finnhubClient.companyExecutive("AAPL", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Company Revenue Estimates

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches revenue estimates for a specified company.

```javascript
finnhubClient.companyRevenueEstimates("AAPL", {}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Financials

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches company financial statements (e.g., income statement 'ic') for a specified period (e.g., 'annual').

```javascript
finnhubClient.financials("AAPL", "ic", "annual", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Analyst Upgrade/Downgrade Data (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves historical analyst upgrade and downgrade data for a specified stock. This provides insights into changes in analyst sentiment and recommendations.

```javascript
finnhubClient.upgradeDowngrade({"symbol": "AAPL"}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Company News

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches news articles related to a specific company within a defined date range. Includes error handling for robust operation.

```javascript
finnhubClient.companyNews("AAPL", "2020-01-01", "2020-05-01", (error, data, response) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data)
    }
});
```

--------------------------------

### Get Crypto Candles

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves historical cryptocurrency candlestick data for a given symbol, resolution, and time range.

```javascript
finnhubClient.cryptoCandles("BINANCE:BTCUSDT", "D", 1590988249, 1591852249, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Fetch Recommendation Trends (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves analyst recommendation trends for a given stock symbol. This includes buy, hold, and sell ratings over time, providing insights into analyst sentiment.

```javascript
finnhubClient.recommendationTrends("AAPL", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Covid-19 Data

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches Covid-19 related data from the Finnhub API.

```javascript
finnhubClient.covid19((error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Stock Candles

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves historical stock candlestick data for a given symbol, resolution, and time range. Useful for charting and technical analysis.

```javascript
finnhubClient.stockCandles("AAPL", "D", 1590988249, 1591852249, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Financials Reported

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves reported financial data for a company based on its symbol.

```javascript
finnhubClient.financialsReported({"symbol": "AAPL"}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get USPTO Patent Data (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves patent application data from the United States Patent and Trademark Office (USPTO) for a company within a specified date range. Useful for intellectual property analysis.

```javascript
finnhubClient.stockUsptoPatent('NVDA', '2021-01-01', '2021-12-31', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get EBITDA Estimates

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) estimates for a company, with an option for annual frequency.

```javascript
finnhubClient.companyEbitdaEstimates("AAPL", {"freq": "annual"}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Indices Constituents (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches the current list of constituents for a specified stock index (e.g., S&P 500). This provides insight into the composition of major market indices.

```javascript
finnhubClient.indicesConstituents("^GSPC", (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Company Basic Financials

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves basic financial metrics for a company, such as margin data.

```javascript
finnhubClient.companyBasicFinancials("AAPL", "margin", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Retrieve Cryptocurrency Profile (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches detailed profile information for a cryptocurrency. This includes general information about the crypto asset, its description, and key characteristics.

```javascript
finnhubClient.cryptoProfile('BTC', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Investor Ownership

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves investor ownership data for a company, with an optional limit on the number of results.

```javascript
let optsLimit = {'limit': 10};
finnhubClient.ownership("AAPL", optsLimit, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Forex Rates

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches real-time forex rates, with an option to specify a base currency.

```javascript
finnhub
```

--------------------------------

### Retrieve Mutual Fund Profile (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches detailed profile information for a Mutual Fund. This includes general information about the fund, its investment objectives, and management details.

```javascript
finnhubClient.mutualFundProfile({'symbol': 'VTSAX'}, (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Company Profile

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches detailed company profile information using various identifiers such as symbol, ISIN, or CUSIP.

```javascript
finnhubClient.companyProfile({'symbol': 'AAPL'}, (error, data, response) => {
    console.log(data)
});
```

```javascript
finnhubClient.companyProfile({'isin': 'US0378331005'}, (error, data, response) => {
    console.log(data)
});
```

```javascript
finnhubClient.companyProfile({'cusip': '037833100'}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Historical Indices Constituents (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves historical constituent data for a specified stock index. This is useful for backtesting strategies and analyzing changes in index composition over time.

```javascript
finnhubClient.indicesHistoricalConstituents("^GSPC", (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Crypto Exchanges

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches a list of supported cryptocurrency exchanges.

```javascript
finnhubClient.cryptoExchanges((error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Fetch Company ESG Score (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves Environmental, Social, and Governance (ESG) scores for a company. This provides insights into a company's sustainability, ethical practices, and social impact.

```javascript
finnhubClient.companyEsgScore('AAPL', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Retrieve Earnings Call Transcripts (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches the full transcript of an earnings call using a unique transcript ID. This provides detailed insights into a company's financial performance and management commentary.

```javascript
finnhubClient.transcripts("AAPL_162777", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Company Earnings Quality Score (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches the earnings quality score for a company, indicating the reliability and sustainability of its reported earnings. This can be retrieved on a quarterly or annual basis.

```javascript
finnhubClient.companyEarningsQualityScore('AAPL', 'quarterly', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Retrieve ETF Profile (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches detailed profile information for an Exchange Traded Fund (ETF). This includes general information about the ETF, its investment strategy, and key characteristics.

```javascript
finnhubClient.etfsProfile({'symbol': 'SPY'}, (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Company Revenue Breakdown (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Fetches the revenue breakdown for a company by segment or product. This is useful for detailed financial analysis, understanding revenue streams, and business diversification.

```javascript
finnhubClient.revenueBreakdown({'symbol': 'AAPL'}, (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Analyze Social Sentiment (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves social media sentiment data for a given stock. This provides insights into public perception, trending topics, and potential market reactions.

```javascript
finnhubClient.socialSentiment('GME', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### List Stock Symbols (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves a comprehensive list of all available stock symbols for a specified exchange or market. This endpoint is useful for symbol lookup and market data discovery.

```javascript
finnhubClient.stockSymbols("US", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Stock Splits (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Obtains historical stock split information for a given symbol and date range. This data is essential for adjusting historical stock prices and understanding share count changes.

```javascript
finnhubClient.stockSplits("AAPL", "2000-01-01", "2020-06-15", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Mutual Fund Holdings (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves the current holdings of a specified Mutual Fund. This shows the underlying assets the fund invests in, offering transparency into its portfolio construction.

```javascript
finnhubClient.mutualFundHoldings({'symbol': 'VTSAX'}, (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get ETF Holdings (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves the current holdings of a specified ETF. This shows the underlying assets the ETF invests in, providing transparency into its portfolio.

```javascript
finnhubClient.etfsHoldings({'symbol': 'ARKK'}, (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Supply Chain Relationships (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves information about a company's supply chain relationships. This is useful for understanding business dependencies, risks, and operational structures.

```javascript
finnhubClient.supplyChainRelationships('AAPL', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Get Company Peers

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves a list of peer companies for a given stock symbol.

```javascript
finnhubClient.companyPeers("AAPL", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get EBIT Estimates

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves EBIT (Earnings Before Interest and Taxes) estimates for a company, with an option for annual frequency.

```javascript
finnhubClient.companyEbitEstimates("AAPL", {"freq": "annual"}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Company Profile 2

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves an alternative or updated company profile, typically using a symbol.

```javascript
finnhubClient.companyProfile2({'symbol': 'AAPL'}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Analyze Support and Resistance Levels (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Calculates and returns key support and resistance levels for a stock based on a given timeframe. This helps technical analysts identify potential price reversal points.

```javascript
finnhubClient.supportResistance("AAPL", "D", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### List Earnings Call Transcripts (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Gets a list of available earnings call transcripts for a given stock symbol. This allows users to discover and access historical earnings call records.

```javascript
finnhubClient.transcriptsList("AAPL", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Economic Code

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves economic codes from the Finnhub API.

```javascript
finnhubClient.economicCode((error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Company EPS Estimates

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves earnings per share (EPS) estimates for a company.

```javascript
finnhubClient.companyEpsEstimates("AAPL", {}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Calculate Technical Indicator (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Computes various technical indicators for a stock over a specified period. It requires the stock symbol, resolution (timeframe), from/to timestamps, and the type of indicator (e.g., 'macd').

```javascript
finnhubClient.technicalIndicator("AAPL", "D", 1580988249, 1591852249, "macd", {}, (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Crypto Symbols

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves a list of cryptocurrency symbols available on a specified exchange.

```javascript
finnhubClient.cryptoSymbols("BINANCE", (error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get List of Countries

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves a list of supported countries from the Finnhub API.

```javascript
finnhubClient.country((error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Get Forex Exchanges

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Retrieves a list of supported forex exchanges.

```javascript
finnhubClient.forexExchanges((error, data, response) => {
    console.log(data)
});
```

--------------------------------

### Initialize Finnhub JavaScript Client

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Demonstrates how to import the Finnhub library and initialize the API client with your API key. This setup is required for all subsequent API calls.

```javascript
const finnhub = require('finnhub');

const finnhubClient = new finnhub.DefaultApi("<API_key>") // Replace this
```

--------------------------------

### Analyze Mutual Fund Industry Exposure (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Provides a breakdown of a Mutual Fund's exposure across different industries. This is useful for analyzing portfolio diversification and sector allocation within the fund.

```javascript
finnhubClient.mutualFundSectorExposure('VTSAX', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Analyze Mutual Fund Country Exposure (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Shows a Mutual Fund's exposure to different countries. This is important for understanding geographical diversification and potential geopolitical risks within the fund's investments.

```javascript
finnhubClient.mutualFundCountryExposure('VTSAX', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Analyze ETF Industry Exposure (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Provides a breakdown of an ETF's exposure across different industries. This is useful for analyzing portfolio diversification and sector allocation.

```javascript
finnhubClient.etfsSectorExposure('SPY', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Analyze ETF Country Exposure (JavaScript)

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Shows an ETF's exposure to different countries. This is important for understanding geographical diversification and potential geopolitical risks.

```javascript
finnhubClient.etfsCountryExposure('SPY', (error, data, response) => {
    console.log(data);
});
```

--------------------------------

### Install Finnhub JavaScript Client

Source: https://github.com/finnhub-stock-api/finnhub-js/blob/master/README.md

Installs the Finnhub JavaScript client library using npm, saving it as a dependency in the project's package.json file.

```Shell
npm install finnhub --save
```