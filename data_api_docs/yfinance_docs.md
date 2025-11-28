### Install and Search Yahoo Finance Data

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/README.md

Installs the yahoo-finance2 package globally and demonstrates how to perform a search for a stock symbol with options.

```bash
$ npm install -g yahoo-finance2
$ yahoo-finance search MSFT '{ "someOption": true }'
```

--------------------------------

### Update Yahoo Finance Initialization (v2 to v3)

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/UPGRADING.md

This snippet demonstrates the change in how to initialize the yahoo-finance2 library when upgrading from v2 to v3. It shows the difference in import statements and the instantiation of the library with configuration options.

```diff
- import yahooFinance from "yahoo-finance2";
- yahooFinance.setGlobalConfig(options); // optional
- yahooFinance.suppressNotices["yahooSurvey"]; // optional

+ import YahooFinance from "yahoo-finance2";
+ const yahooFinance = new YahooFinance({
+   ...options, // optional
+   suppressNotices: ["yahooSurvey"], // optional
+ });
```

--------------------------------

### Clone yahoo-finance2 Project

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/CONTRIBUTING.md

Commands to clone the yahoo-finance2 repository and navigate into the project directory. Assumes Git is installed. The default branch for development is 'dev'.

```bash
git clone https://github.com/gadicc/node-yahoo-finance2.git
cd node-yahoo-finance2
```

--------------------------------

### Common Query and Module Options

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/README.md

Defines query options specific to a module and general module options like development mode, fetch options, and result validation. The example shows how to pass these options when calling a module.

```javascript
const queryOpts = {}; // query options specific to the module

const moduleOpts = {
  devel: boolean | string, // see the main README
  fetchOptions: {}, // options to pass to fetch
  validateResult: boolean, // READ SUPER NB VALIDATION DOC BEFORE TURNING THIS OFF
};

const result = await yahooFinance.module(query, queryOpts, moduleOpts);
```

--------------------------------

### CLI: Get help and search for stock symbols with yahoo-finance2

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/README.md

Demonstrates how to use the yahoo-finance2 command-line interface (CLI) to display help information and search for stock symbols like AMZN. This is useful for quickly checking available commands or finding ticker symbols.

```bash
npx yahoo-finance2 --help
npx yahoo-finance2 search AMZN
```

--------------------------------

### Quote Data Retrieval: v1 vs v2

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/UPGRADING.md

Compares the 'quote' functionality between v1 and v2 of the yahoo-finance library. V1 used quote() with an options object, while v2 uses quoteSummary() with the symbol as the first argument.

```javascript
import yahooFinanceV1 from 'yahoo-finance-v1';
// V1 took a single OPTIONS object as the only paramater
// The API was called "quote" (in v2, it's "quoteSummary")
yahooFinanceV1.quote({ symbol, modules });
{
  // Depends on modules argument:
  price: { /* ... */ },
  summaryDetail: { /* ... */ },
}
```

```javascript
import yahooFinanceV2 from 'yahoo-finance-v2';
// V2 takes SYMBOL as 1st parameter, OPTIONS as 2nd.
// The API is called "quoteSummary" (in v1, it's "quote")
yahooFinanceV2.quoteSummary(symbol, { modules });
{
  // The output should otherwise be identical.
  // Please open an issue if you find any edge-cases.
}
```

--------------------------------

### Fetch IEX Trading Stock News

Source: https://github.com/gadicc/yahoo-finance2/wiki/Alternative-Sources

This example shows how to retrieve news articles for a specific stock symbol (e.g., AAPL) from the IEX Trading API. It supports fetching the latest news or a specified number of recent articles.

```bash
https://api.iextrading.com/1.0/stock/aapl/news
```

```bash
https://api.iextrading.com/1.0/stock/aapl/news/last/2
```

--------------------------------

### Historical Data Retrieval: v1 vs v2

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/UPGRADING.md

Compares the 'historical' data retrieval between v1 and v2 of the yahoo-finance library. V1 used historical() with an options object, while v2 uses historical() with the symbol as the first argument and different date parameters.

```javascript
import yahooFinanceV1 from 'yahoo-finance-v1';
// V1 took a single OPTIONS object as the only paramater
yahooFinanceV1.historical({ symbol, from, to });
[
  {
    date,
    open,
    high,
    low,
    close,
    adjClose,
    volume,
    symbol, // was included
  },
  // ...
];
```

```javascript
import yahooFinanceV2 from 'yahoo-finance-v2';
// V2 takes SYMBOL as 1st parameter, OPTIONS as 2nd.
yahooFinanceV2.historical(symbol, { period1 });
[
  {
    date,
    open,
    high,
    low,
    close,
    adjClose,
    volume,
    // symbol NOT included
  },
  // ...
];
```

--------------------------------

### Example Validation Error Structure

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Illustrates the structure of a typical validation error received from the API, showing instancePath, schemaPath, keyword, params, message, and the erroneous data. This helps in identifying the cause of validation failures.

```javascript
[
  {
    instancePath: "/topHoldings",
    schemaPath: "#/required",
    keyword: "required",
    params: { missingProperty: "stockPosition" },
    message: "must have required property 'stockPosition'",
    data: {
      maxAge: 1,
      holdings: [],
      equityHoldings: {
        priceToEarnings: 0,
        priceToBook: 0,
        priceToSales: 0,
        priceToCashflow: 0,
      },
      bondHoldings: {},
      bondRatings: [],
      sectorWeightings: [],
    },
  },
];
```

--------------------------------

### Fetch Real-Time Webull Ticker Data

Source: https://github.com/gadicc/yahoo-finance2/wiki/Alternative-Sources

This example demonstrates how to fetch real-time ticker data from the Webull API using cURL. It targets specific ticker IDs and retrieves full details. This method requires knowledge of Webull's API endpoints and ticker ID format.

```bash
curl 'https://quoteapi.webull.com/api/quote/tickerRealTimes/full?tickerIds=925334567,925353501,913255891'
```

--------------------------------

### Update Git Remote URL and Branches

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/UPGRADING.md

These bash commands are used to update the local git repository's remote URL and rename branches to reflect changes in the project's repository structure. This is necessary when migrating from older repository configurations.

```bash
# or for HTTPS: git remote set-url origin https://github.com/gadicc/yahoo-finance2.git
git remote set-url origin git@github.com:gadicc/yahoo-finance2.git
# or for forks: git remote set-url upstream git@github.com:gadicc/yahoo-finance2.git

git branch -m devel dev
git branch -m master main
git fetch origin
git branch -u origin/dev dev
git branch -u origin/main main
git remote set-head origin -a
```

--------------------------------

### Run Tests with Deno

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/CONTRIBUTING.md

Executes all tests in the project. HTTP requests are cached by default using 'fetch-mock-cache' for faster, consistent runs. Environment variables can control cache behavior.

```bash
deno task test
# To force network tests without cache:
FETCH_DEVEL=nocache deno task test
# To force network tests and rewrite cache for failing tests:
FETCH_DEVEL=recache deno task test
```

--------------------------------

### Generate and Manage Documentation with Deno

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/CONTRIBUTING.md

Commands for generating API documentation locally. The 'docs:gen' command builds docs into the 'jsdocs' directory, 'docs:watch' rebuilds on file changes, and 'docs:open' opens the generated docs in a browser.

```bash
deno task docs:gen
deno task docs:watch
deno task docs:open
```

--------------------------------

### Lint and Format Code with Deno

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/CONTRIBUTING.md

Ensures code quality and consistent formatting. These commands are typically handled automatically by the Deno extension in VS Code.

```bash
deno lint
deno fmt
```

--------------------------------

### Error Handling with Try-Catch

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/README.md

Demonstrates how to wrap calls to yahooFinance modules in a try...catch block to handle potential errors such as network issues, HTTP errors, missing resources, or validation failures. It shows how to inspect the error and take appropriate action.

```javascript
let result;
try {
  result = await yahooFinance.quote(symbol);
} catch (error) {
  // Inspect error and decide what to do; often, you may want to just abort:
  console.warn(
    `Skipping yf.quote("${symbol}"): [${error.name}] ${error.message}`,
  );
  return;
}

doSomethingWith(result); // safe to use in the way you expect
```

--------------------------------

### Import and Use Yahoo Finance in TypeScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/README.md

Shows how to import and instantiate the Yahoo Finance client in TypeScript, and perform basic operations like searching for a company and fetching quote data.

```typescript
import YahooFinance from "yahoo-finance2";

const yahooFinance = new YahooFinance();

const results = await yahooFinance.search("Apple");

const quote = await yahooFinance.quote('AAPL');
const { regularMarketPrice as price, currency } = quote;
```

--------------------------------

### CLI: Fetch quote summary for GOOGL and NVDA with yahoo-finance2

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/README.md

Shows how to retrieve a quote summary for specific stock symbols (GOOGL and NVDA) using the yahoo-finance2 CLI. It also illustrates how to pass a JSON string to request specific modules like 'assetProfile' and 'secFilings' for NVDA.

```bash
npx yahoo-finance2 quoteSummary GOOGL
npx yahoo-finance2 quoteSummary NVDA '{"modules":["assetProfile", "secFilings"]}'
```

--------------------------------

### Specific Error Handling for yahoo-finance2

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/README.md

Illustrates how to handle specific error types thrown by the yahoo-finance2 library, such as `FailedYahooValidationError` and `HTTPError`, within a try...catch block. It also shows how to handle generic `Error` objects.

```javascript
import YahooFinance from "yahoo-finance2";
const yahooFinance = new YahooFinance();

let result;
try {
  result = await yahooFinance.quote(symbol);
} catch (error) {
  if (error instanceof yahooFinance.errors.FailedYahooValidationError) {
    // See the validation docs for examples of how to handle this
    // error.result will be a partially validated / coerced result.
  } else if (error instanceof yahooFinance.errors.HTTPError) {
    // Probably you just want to log and skip these
    console.warn(
      `Skipping yf.quote("${symbol}"): [${error.name}] ${error.message}`,
    );
    return;
  } else {
    // Same here
    console.warn(
      `Skipping yf.quote("${symbol}"): [${error.name}] ${error.message}`,
    );
    return;
  }
}

doSomethingWith(result); // safe to use in the way you expect
```

--------------------------------

### Run Yahoo Finance Requests in Series and Parallel

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/concurrency.md

Demonstrates how to fetch quote summary data for multiple stock symbols using both sequential (series) and concurrent (parallel) execution with Promises. The parallel execution respects the library's internal concurrency limit.

```javascript
const symbols = ["TSLA", "MSFT", "AAPL"];

// Series: perform one request at a time, one after the other
const data = [];
for (const symbol of symbols) {
  data.push(await yahooFinance.quoteSummary(symbol));
}

// Parallel: perform all requests simultaneously (within concurrency limit)
const data = Promise.all(
  symbols.map((symbol) => yahooFinance.quoteSummary(symbol)),
);
```

```javascript
// Will run in parallel, but without exceeding the concurrency limit
databaseResults.forEach(async (row) => {
  const result = await yahooFinance.quoteCombine(row.symbol);
  // do something
});
```

--------------------------------

### Fetch IEX Trading Symbols

Source: https://github.com/gadicc/yahoo-finance2/wiki/Alternative-Sources

This cURL command retrieves a list of all supported stock symbols from the IEX Trading API. The response is a JSON array of symbol objects, which can be used to query specific stock data.

```bash
https://api.iextrading.com/1.0/ref-data/symbols
```

--------------------------------

### Yahoo Interface CSS Styling

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This extensive CSS code defines the styling for various elements of the Yahoo interface. It includes rules for fonts, layout, themes (e.g., 'crunch', 'fuji2'), responsiveness across different screen sizes, and specific component styling.

```css
/*\n * Copyright 2017 Yahoo Holdings, Inc. All rights reserved. */
template { display: none }
._yb_1asdu {
  font-family: 'Helvetica Neue', Helvetica, Tahoma, Geneva, Arial, sans-serif;
  font-weight: 400;
  font-stretch: normal;
  direction: ltr;
  display: block;
  box-sizing: border-box;
  text-align: start;
  -webkit-font-smoothing: antialiased;
  z-index: 1000;
  overflow-anchor: none;
}

.ybar-ytheme-crunch.ybar-property-homepage._yb_1asdu {
  font-family: 'Poppins', 'YahooSans VF', YahooSans, 'Yahoo Sans', 'Verdana', sans-serif;
}

.ybar-ytheme-crunch._yb_1asdu, .ybar-ytheme-fuji2._yb_1asdu {
  font-family: 'YahooSans VF', YahooSans, 'Yahoo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

#ybar._yb_1rdrh {
  margin: 0 auto;
}

._yb_1asdu ._yb_san39 {
  display: flex;
  flex-direction: column;
}

html[data-color-theme-enabled][data-color-scheme=dark] #ybar-inner-wrap {
  background: #1d2228;
}

@media (prefers-color-scheme: dark) {
  html[data-color-theme-enabled] #ybar-inner-wrap {
    background: #1d2228;
  }
}

._yb_156ds {
  display: flex;
  justify-content: center;
}

._yb_kwqpl {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  min-width: 0;
  max-width: 1920px;
  box-sizing: border-box;
  transition: margin .2s ease-out, opacity .15s linear .2s;
  opacity: 1;
}

._yb_1c376 ._yb_kwqpl, ._yb_1ky9q ._yb_kwqpl {
  min-width: 0;
  max-width: 1301px;
}

.ybar-ytheme-crunch ._yb_kwqpl {
  max-width: 1440px;
}

.ybar-ytheme-fuji2 ._yb_kwqpl {
  max-width: 1340px;
  padding: 0 20px;
  transition: margin .2s ease-out, opacity .15s linear .2s, padding .4s;
}

.ybar-property-sports._yb_14tdx #ybar-navigation {
  max-width: 100%;
  padding: 0;
}

.ybar-sticky #ybar._yb_14tdx #ybar-inner-wrap {
  left: 0;
}

.ybar-ytheme-fuji2._yb_1ky9q ._yb_kwqpl, .ybar-ytheme-fuji2._yb_1ky9q ._yb_pycvd ._yb_kwqpl {
  padding: 0;
  margin: 0;
}

.ybar-ytheme-fuji2._yb_1ky9q ._yb_156ds._yb_17y4j, .ybar-ytheme-fuji2._yb_1ky9q ._yb_156ds._yb_pycvd {
  padding: 0 20px;
  transition: padding .4s;
}

@media screen and (min-width: 1020px) {
  .ybar-ytheme-fuji2 ._yb_kwqpl {
    padding: 0 40px;
  }
  .ybar-ytheme-fuji2._yb_1ky9q ._yb_156ds._yb_17y4j, .ybar-ytheme-fuji2._yb_1ky9q ._yb_156ds._yb_pycvd {
    padding: 0 40px;
  }
}

.ybar-ytheme-fuji2._yb_wzzje ._yb_kwqpl {
  padding: 0;
  max-width: 100%;
}

.ybar-ytheme-fuji2._yb_1vi8b._yb_1ky9q ._yb_kwqpl {
  max-width: 1264px;
  min-width: 0;
}

._yb_18zef ._yb_kwqpl, .ybar-ytheme-fuji2._yb_1c376 ._yb_18zef ._yb_kwqpl, .ybar-ytheme-fuji2._yb_1ky9q ._yb_18zef ._yb_kwqpl {
  padding: 0;
  position: relative;
  display: none;
}

.ybar-ytheme-fuji2 ._yb_18zef ._yb_kwqpl {
  display: flex;
}

.ybar-ytheme-fuji2.ybar-property-mail.fuji2-dialpad ._yb_18zef {
  display: none;
}

._yb_17yd1 {
  background: #232a31;
  flex: 1;
}

.ybar-dark ._yb_17yd1 {
  background: #464e56;
}

.ybar-dark ._yb_t7qjt ._yb_17yd1 {
  background-color: #7e1fff;
}

html[data-color-theme-enabled][data-color-scheme=dark] ._yb_17yd1 {
  background-color: #7759ff;
}

@media (prefers-color-scheme: dark) {
  html[data-color-theme-enabled] ._yb_17yd1 {
    background-color: #7759ff;
  }
}

.ybar-ytheme-fuji2 ._yb_18zef {
  overflow: hidden;
}

@media screen and (max-width: 1340px) {
  .ybar-ytheme-fuji2 ._yb_18zef {
    width: 100%;
    min-width: 1032px;
  }
  .ybar-ytheme-fuji2 ._yb_17yd1 {
    display: none;
  }
}

._yb_18b0r {
  min-width: 0;
  padding: 0;
  height: 84px;
}

._yb_1ucqa ._yb_18b0r, ._yb_1xdma ._yb_18b0r, ._yb_1rdrh ._yb_18b0r, ._yb_dcnd7 ._yb_18b0r, ._yb_1udgu ._yb_18b0r, ._yb_8we47 ._yb_18b0r, ._yb_7fmm1 ._yb_18b0r {
  padding: 0 64px 0 50px;
}

._yb_15bdk._yb_156ds._yb_fhy2y {
  padding: 0 16px;
  margin-bottom: 8px;
  justify-content: center;
  width: auto;
}

._yb_1c376 ._yb_15bdk._yb_156ds._yb_fhy2y, .ybar-property-generic ._yb_15bdk._yb_156ds._yb_fhy2y, .ybar-property-homepage ._yb_15bdk._yb_156ds._yb_fhy2y {
  margin-bottom: 16px;
}

._yb_pycvd ._yb_kwqpl {
  height: 34px;
  padding-left: 24px;
}

ybar-y
```

--------------------------------

### Generate JSON Schemas with Deno

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/CONTRIBUTING.md

Generates JSON schemas from TypeScript interfaces marked with '@yf-schema'. This ensures input validation. It can be run on demand or in watch mode.

```bash
deno task schema
deno task schema --watch
```

--------------------------------

### Safely fetch and use search results with error handling - JavaScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Shows how to use a try-catch block to handle potential errors during data fetching with yahooFinance.search, ensuring subsequent code execution is safe.

```javascript
let result;
try {
  result = await yahooFinance.search("gold");
} catch (e) {
  // i.e. do nothing with invalid result
  return;
}
// Everything below here will be safe and won't throw unexpected errors
$("input").value(result.Result[0].name);
```

--------------------------------

### Configure Yahoo Finance Concurrency Limit

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/concurrency.md

Shows how to instantiate the YahooFinance client with a custom concurrency limit, allowing control over the maximum number of simultaneous requests.

```javascript
import YahooFinance from "yahoo-finance2";
const yahooFinance = new YahooFinance({ queue: { concurrency: 1 } }); // or 8, Infinity, etc.
```

--------------------------------

### Basic Button Styling

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This CSS defines basic styling for buttons, including padding and font size. It also includes a 'primary' class for styling primary action buttons with a specific background color, text color, and cursor.

```css
.btn { padding: 15px; font-size:20px;min-width: 30%; }\n.btn.primary{background-color: #0f69ff;color: #fff;cursor: pointer;}
```

--------------------------------

### Configure Yahoo Finance to Allow Additional Properties

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Demonstrates how to instantiate the YahooFinance class with the 'allowAdditionalProps' option set to false to revert to the old behavior of throwing errors on unknown keys. This is useful for development and testing.

```javascript
const yahooFinance = new YahooFinance({
  validation: { allowAdditionalProps: false },
});
```

--------------------------------

### Yahoo API Response Headers

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This snippet details the response headers received from a Yahoo API call. It includes information about caching, content security, server details, and security policies like XSS protection and referrer policy.

```json
{
  "response": {
    "ok": true,
    "status": 200,
    "statusText": "OK",
    "headers": {
      "content-encoding": [
        "gzip"
      ],
      "expires": [
        "0"
      ],
      "cache-control": [
        "no-cache, no-store, must-revalidate"
      ],
      "content-security-policy-report-only": [
        "default-src 'none'; block-all-mixed-content; connect-src 'self'; frame-ancestors 'none'; img-src 'self' https://s.yimg.com; media-src 'none'; script-src 'self' 'nonce-nwyhMAH+t7jn7Pz79Kab3iWjWDy1neqa' https://s.yimg.com; style-src 'self' 'nonce-nwyhMAH+t7jn7Pz79Kab3iWjWDy1neqa' https://s.yimg.com; font-src 'self'; object-src 'none'; frame-src 'none'; report-uri https://csp.yahoo.com/beacon/csp?src=guce"
      ],
      "server": [
        "guce"
      ],
      "x-xss-protection": [
        "1; mode=block"
      ],
      "pragma": [
        "no-cache"
      ],
      "x-frame-options": [
        "DENY"
      ],
      "referrer-policy": [
        "strict-origin-when-cross-origin"
      ],
      "date": [
        "Mon, 08 May 2023 15:12:38 GMT"
      ],
      "connection": [
        "close"
      ],
      "strict-transport-security": [
        "max-age=31536000; includeSubDomains"
      ],
      "x-content-type-options": [
        "nosniff"
      ],
      "content-type": [
        "text/html;charset=UTF-8"
      ],
      "content-length": [
        "8374"
      ]
    },
    "body": "\n\n\n Yahoo is part of the Yahoo family of brands\n\n \n \n \n \n /*! Copyright 2017 Yahoo Holdings, Inc. All rights reserved. */\ntemplate{display:none}.\_yb\_1asdu{font-family:'Helvetica Neue',Helvetica,Tahoma,Geneva,Arial,sans-serif;font-weight:400;font-stretch:normal;direction:ltr;display:block;box-sizing:border-box;text-align:start;-webkit-font-smoothing:antialiased;z-index:1000;overflow-anchor:none}.ybar-ytheme-crunch.ybar-property-homepage.\_yb\_1asdu{font-family:'Poppins','YahooSans VF',YahooSans,'Yahoo Sans','Verdana',sans-serif}.ybar-ytheme-crunch.\_yb\_1asdu,.ybar-ytheme-fuji2.\_yb\_1asdu{font-family:'YahooSans VF',YahooSans,'Yahoo Sans','Helvetica Neue',Helvetica,Arial,sans-serif}#ybar.\_yb\_1rdrh{margin:0 auto}.\_yb\_1asdu .\_yb\_san39{display:flex;flex-direction:column}html[data-color-theme-enabled][data-color-scheme=dark] #ybar-inner-wrap{background:#1d2228}@media (prefers-color-scheme:dark){html[data-color-theme-enabled] #ybar-inner-wrap{background:#1d2228}}.\_yb\_156ds{display:flex;justify-content:center}.\_yb\_kwqpl{display:flex;justify-content:flex-start;align-items:center;width:100%;min-width:0;max-width:1920px;box-sizing:border-box;transition:margin .2s ease-out,opacity .15s linear .2s;opacity:1}.\_yb\_1c376 .\_yb\_kwqpl,.\_yb\_1ky9q .\_yb\_kwqpl{min-width:0;max-width:1301px}.ybar-ytheme-crunch .\_yb\_kwqpl{max-width:1440px}.ybar-ytheme-fuji2 .\_yb\_kwqpl{max-width:1340px;padding:0 20px;transition:margin .2s ease-out,opacity .15s linear .2s,padding .4s}.ybar-property-sports.\_yb\_14tdx #ybar-navigation{max-width:100%;padding:0}.ybar-sticky #ybar.\_yb\_14tdx #ybar-inner-wrap{left:0}.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_kwqpl,.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_pycvd .\_yb\_kwqpl{padding:0;margin:0}.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_156ds.\_yb\_17y4j,.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_156ds.\_yb\_pycvd{padding:0 20px;transition:padding .4s}@media screen and (min-width:1020px){.ybar-ytheme-fuji2 .\_yb\_kwqpl{padding:0 40px}.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_156ds.\_yb\_17y4j,.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_156ds.\_yb\_pycvd{padding:0 40px}}.ybar-ytheme-fuji2.\_yb\_wzzje .\_yb\_kwqpl{padding:0;max-width:100%}.ybar-ytheme-fuji2.\_yb\_1vi8b.\_yb\_1ky9q .\_yb\_kwqpl{max-width:1264px;min-width:0}.\_yb\_18zef .\_yb\_kwqpl,.ybar-ytheme-fuji2.\_yb\_1c376 .\_yb\_18zef .\_yb\_kwqpl,.ybar-ytheme-fuji2.\_yb\_1ky9q .\_yb\_18zef .\_yb\_kwqpl{padding:0;position:relative;display:none}.ybar-ytheme-fuji2 .\_yb\_18zef .\_yb\_kwqpl{display:flex}.ybar-ytheme-fuji2.ybar-property-mail.fuji2-dialpad .\_yb\_18zef{display:none}.\_yb\_17yd1{background:#232a31;flex:1}.ybar-dark .\_yb\_17yd1{background:#464e56}.ybar-dark .\_yb\_t7qjt .\_yb\_17yd1{background-color:#7e1fff}html[data-color-theme-enabled][data-color-scheme=dark] .\_yb\_17yd1{background-color:#7759ff}@media (prefers-color-scheme:dark){html[data-color-theme-enabled] .\_yb\_17yd1{background-color:#7759ff}}.ybar-ytheme-fuji2 .\_yb\_18zef{overflow:hidden}@media screen and (max-width:1340px){.ybar-ytheme-fuji2 .\_yb\_18zef{width:100%;min-width:1032px}.ybar-ytheme-fuji2 .\_yb\_17yd1{display:none}}.\_yb\_18b0r{min-width:0;padding:0;height:84px}.\_yb\_1ucqa .\_yb\_18b0r,.\_yb\_1xdma .\_yb\_18b0r,.\_yb\_1rdrh .\_yb\_18b0r,.\_yb\_dcnd7 .\_yb\_18b0r,.\_yb\_1udgu .\_yb\_18b0r,.\_yb\_8we47 .\_yb\_18b0r,.\_yb\_7fmm1 .\_yb\_18b0r{padding:0 64px 0 50px}.\_yb\_15bdk.\_yb\_156ds.\_yb\_fhy2y{padding:0 16px;margin-bottom:8px;justify-content:center;width:auto}.\_yb\_1c376 .\_yb\_15bdk.\_yb\_156ds.\_yb\_fhy2y,.ybar-property-generic .\_yb\_15bdk.\_yb\_156ds.\_yb\_fhy2y,.ybar-property-homepage .\_yb\_15bdk.\_yb\_156ds.\_yb\_fhy2y{margin-bottom:16px}.\_yb\_pycvd .\_yb\_kwqpl{height:34px;padding-left:24px}.ybar-y"
        }
      }
    }
  }
}
```

--------------------------------

### Handle errors and use fallback data with validation - JavaScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Demonstrates how to catch errors during data fetching and use a fallback result, followed by custom validation to ensure the data's integrity before use.

```javascript
let result;
try {
  result = await yahooFinance.search("gold");
} catch (error) {
  // i'll take responsibility for this
  result = error.result;
}
// and will do my own validation
if (
  result &&
  isArray(result.Result) &&
  result.Result[0] &&
  typeof result.Result[0].name === "string"
) {
  $("input").value(result.Result[0].name);
}
```

--------------------------------

### Yahoo Finance CSS Styling

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This block contains various CSS rules for styling elements within the Yahoo Finance interface. It includes rules for element sizing, alignment, object fitting, and responsive design adjustments based on screen width and color themes.

```css
max-height:56px}}.ybar-ytheme-fuji2 ._yb_ckub7._yb_t9ofo{width:auto;max-height:40px}.{_yb_t9ofo:focus{outline-offset:2px}.{_yb_1gfiu{align-self:flex-start;max-height:100%;max-width:100%}@media screen and (min-width:768px){._yb_1gfiu{max-height:40px}}._yb_17mog ._yb_1gfiu{height:100%;max-height:100%}.ybar-ytheme-fuji2 ._yb_1gfiu{height:auto;width:auto;max-height:100%;max-width:100%;flex-shrink:0;-o-object-fit:contain;object-fit:contain;-o-object-position:left;object-position:left}.ybar-ytheme-fuji2._yb_ckub7 ._yb_1gfiu{-o-object-position:center;object-position:center}html[data-color-theme-enabled][data-color-scheme=dark] .{_yb_167t3,.ybar-dark .{_yb_167t3,.ybar-light .{_yb_t9l1i{display:none}html[data-color-theme-enabled][data-color-scheme=dark] .{_yb_t9l1i{display:block}@media (prefers-color-scheme:dark){html[data-color-theme-enabled] .{_yb_167t3{display:none}html[data-color-theme-enabled] .{_yb_t9l1i{display:block}}}}.ybar-amp .{_yb_t9ofo{display:block;margin:auto;padding:10px 0;text-align:center}@media screen and (max-width:768px){._yb_1uc3p .{_yb_1gfiu,.{_yb_oga1u .{_yb_1gfiu{height:100%;max-height:32px}}._yb_xsy4s{-o-object-fit:fill;object-fit:fill;height:50px;width:50px}._yb_11q4t{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden}.ybar-dark .ybar-ytheme-crunch .{_yb_t9ofo path{fill:#fff}
```

--------------------------------

### Yahoo Consent Collection API Request

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This snippet shows a sample API request to the Yahoo consent collection endpoint. It includes the URL for collecting user consent, which is a common step in web application data handling.

```json
{
  "request": {
    "url": "https://consent.yahoo.com/v2/collectConsent?sessionId=3_cc-session_bd7a0720-7115-4809-82ad-97ac2fc34194"
  }
}
```

--------------------------------

### Consent Page Background Styling

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This CSS targets the 'ybar' div within the '#consent-page' ID. It sets the background color to white and applies left padding, likely for the consent management overlay.

```css
#consent-page #ybar div{background: #fff;padding-left: 0}
```

--------------------------------

### Turn off options validation for experimental API usage - TypeScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Demonstrates how to disable validation for API options using `{ validateOptions: false }`. This allows sending experimental or unknown options directly to Yahoo's API.

```typescript
const quote = await yahooFinance.quote("AAPL", undefined, {
  validateOptions: false,
});
```

--------------------------------

### Skip validation entirely using module option - JavaScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Shows how to disable result validation by passing `{ validateResult: false }` as a module option. This requires manual validation of the returned data.

```javascript
const result = await yahooFinance.search("gold", {}, { validateResult: false });

if (
  result &&
  isArray(result.Result) &&
  result.Result[0] &&
  typeof result.Result[0].name === "string"
) {
  $("input").value(result.Result[0].name);
}
```

--------------------------------

### Disable verbose error logging for validation failures - JavaScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Provides instructions on how to disable the detailed error logging that occurs when data validation fails by setting `{ validation: { logErrors: false } }` during YahooFinance initialization.

```javascript
import YahooFinance from "yahoo-finance2";
const yahooFinance = new YahooFinance{ validation: { logErrors: false } });
```

--------------------------------

### Calculate Stock Holding Value with potential undefined price - JavaScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Demonstrates a common scenario where stock price data might be undefined, leading to NaN results and potential app crashes. This highlights the need for validation.

```javascript
function calculateStockHoldingValue(symbol) {
  const { qty } = await db.holdings.findOne({ symbol });
  const { price } = await yahooFinance.quoteSummary(symbol, {
    modules: "price",
  });

  return qty * price.regularMarketPrice;
}
```

--------------------------------

### Handle undefined or non-Date market time - JavaScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Illustrates issues with date objects returned from Yahoo Finance, specifically when the market time is undefined or not a proper Date object, which can lead to type errors or incorrect comparisons.

```javascript
const { price: { regularMarketTime } } = await yahooFinance.quoteSummary(
  "AAPL",
);

// Uncaught TypeError: Cannot read property 'getTime' of undefined
regularMarketTime.getTime(); //  "But it worked fine in development!!"

// Even worse is it IS defined, but is not a Date.  That *won't* throw an error in my code,
instead, I'll be making a comparison that will be true when it should be false, etc.
const goodTimeToTrade = regularMarketTime > anotherDateObject;
```

--------------------------------

### Fixing Validation Error: Making a Property Optional

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Shows a code modification using 'git diff' format to make the 'stockPosition' property optional in the 'TopHoldings' interface within the quoteSummary module. This is a common fix for validation errors where a property might be missing.

```diff
export interface TopHoldings {
  [key: string]: any;
  maxAge: number;
-  stockPosition: number;
+  stockPosition?: number;
  holdings: TopHoldingsHolding[];
  equityHoldings: TopHoldingsEquityHoldings;
  bondHoldings: object;

```

--------------------------------

### Dark Theme SVG Path Styling

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This CSS rule specifically targets SVG paths within the '.ybar-ytheme-crunch' class in a dark theme. It sets the fill color of the paths to white, likely to ensure visibility against a dark background.

```css
.ybar-dark .ybar-ytheme-crunch ._yb_t9ofo path{fill:#fff}
```

--------------------------------

### TypeScript unknown type after validation failure - TypeScript

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/docs/validation.md

Explains TypeScript behavior when validation fails. The return type becomes 'unknown', forcing explicit type checking to maintain code safety.

```typescript
let result;
try {
  result = await yahooFinance.search("gold"); // result is a SearchResult
} catch (error) {
  result = error.result; // result is an unknown
}
```

--------------------------------

### Add 'js' class to body element

Source: https://github.com/gadicc/yahoo-finance2/blob/dev/tests/http/getCrumb-quote-AAPL-collectConsent.html

This JavaScript snippet checks if the 'classList' property is available on the document body. If it is, it adds the 'js' class and removes the 'no-js' class. This is a common technique for progressive enhancement, allowing CSS to target browsers with JavaScript enabled.

```javascript
if ('classList' in document.body) {
 document.body.classList.add('js');
 document.body.classList.remove('no-js');
 }
```

=== COMPLETE CONTENT === This response contains all available snippets from this library. No additional content exists. Do not make further requests.