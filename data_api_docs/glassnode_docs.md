### Fetch NUPL Data using JavaScript

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet demonstrates how to make an HTTP GET request to the Glassnode API to fetch Net Unrealized Profit/Loss (NUPL) data. It uses the `fetch` API and requires your API key and the desired asset ID.

```JavaScript
const apiKey = 'YOUR_API_KEY';
const assetId = 'YOUR_ASSET_ID'; // e.g., 'btc'
const url = `https://api.glassnode.com/v1/metrics/indicators/net_unrealized_profit_loss?a=${assetId}&api_keystring=${apiKey}`;

fetch(url, {
  method: 'GET',
  headers: {
    'Accept': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching NUPL data:', error);
});

```

--------------------------------

### Fetch LTH-NUPL Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet uses the `fetch` API to retrieve LTH-NUPL data. It constructs the API URL with the asset and API key, then parses the JSON response. Ensure you replace 'YOUR_API_KEY' and 'BTC' with your specific values.

```JavaScript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // e.g., BTC, ETH
const url = `https://api.glassnode.com/v1/metrics/indicators/nupl_more_155?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    // Process the LTH-NUPL data here
  })
  .catch(error => {
    console.error('Error fetching LTH-NUPL data:', error);
  });

```

--------------------------------

### Fetch Realized Profit Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates how to call the Glassnode API to get Realized Profit data. It uses the `fetch` API to make a GET request, including the API key and asset parameter in the URL. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'text'; // Replace with desired asset

fetch(`https://api.glassnode.com/v1/metrics/indicators/realized_profit?a=${asset}&api_keystring=${apiKey}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
```

--------------------------------

### Fetch Price OHLC Data (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript code snippet shows how to fetch OHLC price data from the Glassnode API using the `fetch` API. It constructs the URL with necessary parameters and handles the JSON response.

```javascript
fetch('https://api.glassnode.com/v1/metrics/market/price_usd_ohlc?a=BTC&api_keystring=YOUR_API_KEY')
  .then(response => response.json())
  .then(data => console.log(data));
```

--------------------------------

### Get NVT Signal Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

Demonstrates how to fetch NVT Signal data using JavaScript's Fetch API. This example shows how to construct the request URL with parameters and handle the JSON response.

```javascript
fetch("https://api.glassnode.com/v1/metrics/indicators/nvts?a=text", {
  "method": "GET",
  "headers": {
    "accept": "application/json"
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.error(err));
```

--------------------------------

### Get Investor Capitalization Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

Shows how to retrieve Investor Capitalization data using JavaScript's fetch API. This example includes setting up the request with necessary headers and query parameters for the Glassnode API.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // e.g., BTC, ETH

fetch(`https://api.glassnode.com/v1/metrics/indicators/investor_capitalization?a=${asset}&api_key=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

```

--------------------------------

### Retrieve Average Dormancy (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates fetching the average dormancy data using the `fetch` API. It requires your Glassnode API key and the asset symbol. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'text'; // Replace with the desired asset

fetch(`https://api.glassnode.com/v1/metrics/indicators/average_dormancy?a=${asset}&api_keystring=${apiKey}`,
  {
    method: 'GET',
    headers: {
      'Accept': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

--------------------------------

### Fetch Options Combo Premiums Sellers (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/options

This JavaScript code snippet illustrates how to fetch 'Options Combo Premiums Sellers' data using the `fetch` API. It constructs the URL with query parameters and includes the necessary `Authorization` header with your API key. The response is parsed as JSON.

```JavaScript
async function getComboPremiumsSellers(assetId) {
  const apiKey = 'YOUR_API_KEY';
  const url = `https://api.glassnode.com/v1/metrics/options/combo_premiums_sellers?a=${assetId}`;

  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Example usage:
// getComboPremiumsSellers('BTC');
```

--------------------------------

### Retrieve Pi Cycle Top Indicator Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates how to fetch the Pi Cycle Top Indicator using the fetch API. It constructs the URL with required parameters and handles the JSON response.

```javascript
const apiKey = "YOUR_API_KEY";
const asset = "text"; // e.g., BTC, ETH, LTC

fetch(`https://api.glassnode.com/v1/metrics/indicators/pi_cycle_top?a=${asset}&api_key=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("Error fetching data:", error);
  });

```

--------------------------------

### Fetch Spot ADL Data (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript snippet illustrates how to fetch the Spot Accumulation/Distribution Line (ADL) metric using the `fetch` API. It requires your API key and allows customization of asset and date range parameters.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'YOUR_ASSET_ID'; // e.g., 'btc'
const apiUrl = `https://api.glassnode.com/v1/metrics/market/spot_accumulation_distribution_line?a=${asset}&api_key=${apiKey}`;

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log('Spot ADL Data:', data);
  })
  .catch(error => {
    console.error('Error fetching Spot ADL data:', error);
  });

```

--------------------------------

### JavaScript Fetch Example - Get Time Series Data

Source: https://docs.glassnode.com/basic-api/endpoints/breakdowns

This JavaScript code illustrates how to use the `fetch` API to make a GET request to the Glassnode API. It demonstrates setting the `X-Api-Key` header and handling the JSON response.

```javascript
const apiKey = "YOUR_API_KEY";
const asset = "BTC";
const metric = "market_price_usd";
const interval = "daily";
const startTimestamp = 1640995200;
const endTimestamp = 1672531200;

const url = `https://api.glassnode.com/v1/metrics/asset/price_usd?a=${asset}&m=${metric}&i=${interval}&s=${startTimestamp}&u=${endTimestamp}`;

fetch(url, {
  method: 'GET',
  headers: {
    'X-Api-Key': apiKey
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching data:', error);
});
```

--------------------------------

### Fetch Net Realized Profit/Loss (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code demonstrates how to fetch Net Realized Profit/Loss data using the Glassnode API. It uses the fetch API and requires a valid API key and asset identifier. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'btc'; // Example asset

fetch(`https://api.glassnode.com/v1/metrics/indicators/net_realized_profit_loss?a=${asset}`, {
  headers: {
    'x-api-key': apiKey
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));

```

--------------------------------

### Fetch Options Net Premium Strike Heatmap (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/options

JavaScript code to fetch the Options Net Premium Strike Heatmap data from the Glassnode API. This example uses the `fetch` API to make a GET request, including necessary headers for authentication and specifying query parameters for asset and period.

```javascript
async function getOptionsNetPremiumStrikeHeatmap(asset, period, apiKey) {
    const url = `https://api.glassnode.com/v1/metrics/options/premiums_strike_heatmap?a=${asset}&period=${period}`;
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'x-api-key': apiKey
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

// Example usage:
// const apiKey = 'YOUR_API_KEY';
// getOptionsNetPremiumStrikeHeatmap('BTC', '1y', apiKey).then(data => console.log(data));
```

--------------------------------

### Fetch Realized Volatility (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript code uses the `fetch` API to retrieve realized volatility data from Glassnode. It requires a valid asset ID and your API key. The response is parsed as JSON.

```javascript
const assetId = 'text'; // Replace with a valid asset ID
const apiKey = 'YOUR_API_KEY'; // Replace with your Glassnode API key

fetch(`https://api.glassnode.com/v1/metrics/market/realized_volatility_all?a=${assetId}&api_key=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching realized volatility:', error);
  });

```

--------------------------------

### GET Spot Buying Volume (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript code snippet illustrates how to fetch spot buying volume data using the Fetch API. It constructs the request URL with query parameters and includes the API key in the headers. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // Example asset

fetch(`https://api.glassnode.com/v1/metrics/market/spot_buying_volume_sum?a=${asset}`, {
  method: 'GET',
  headers: {
    'x-api-key': apiKey,
    'Accept': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});
```

--------------------------------

### JavaScript Fetch: Get SOPD (ATH-Partitioned)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet shows how to fetch the ATH-partitioned Spent Output Price Distribution data from the Glassnode API using the `fetch` function. It includes setting up the necessary headers with the API key and constructing the URL with the asset parameter.

```javascript
fetch('https://api.glassnode.com/v1/metrics/indicators/spent_output_price_distribution_ath?a=text', {
  method: 'GET',
  headers: {
    'Authorization': 'YOUR_API_KEY'
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching data:', error);
});

```

--------------------------------

### Fetch STH Relative Unrealized Profit (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript example fetches the STH Relative Unrealized Profit metric using the 'fetch' API. It includes necessary headers for authentication and specifies the asset and format. The response is parsed as JSON.

```javascript
async function getSTHUnrealizedProfit(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/unrealized_profit_less_155?a=${assetId}&api_key=${apiKey}&f=json`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json'
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Example usage:
// getSTHUnrealizedProfit('btc', 'YOUR_API_KEY');
```

--------------------------------

### Fetch Cost Basis Distribution Heatmap Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript snippet illustrates how to use the 'fetch' API to get the Cost Basis Distribution Heatmap data from Glassnode. It constructs the URL with asset and period parameters and handles the JSON response. Ensure you replace 'YOUR_API_KEY' with your actual key.

```JavaScript
const apiKey = "YOUR_API_KEY";
const asset = "text"; // e.g., "btc"
const period = "text"; // e.g., "1month"

fetch(`https://api.glassnode.com/v1/metrics/indicators/cost_basis_distribution_heatmap?a=${asset}&period=${period}&api_key=${apiKey}`,
  {
    method: "GET",
    headers: {
      "Accept": "application/json"
    }
  }
)
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error("Error fetching data:", error);
});

```

--------------------------------

### Fetch Net Premium by Strike (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/options

This JavaScript code demonstrates how to fetch net premium data by strike price using the Glassnode API. It constructs the request URL with the asset and frequency parameters and handles the JSON response.

```javascript
const asset = 'BTC'; // Example asset
const frequency = '10m'; // Example frequency

fetch(`https://api.glassnode.com/v1/metrics/options/options_net_premium_breakdown_by_strike_price?a=${asset}&i=${frequency}`, {
  headers: {
    'Authorization': 'YOUR_API_KEY' // Replace with your actual API key
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Process the data here
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

```

--------------------------------

### Fetch Short-Term Holder CDD (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript example shows how to retrieve Short-Term Holder Coin Days Destroyed data using the fetch API. It constructs the URL with necessary parameters and includes authentication via an API key. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'ETH'; // Replace with desired asset
const url = `https://api.glassnode.com/v1/metrics/indicators/cdd_sth?a=${asset}`;

fetch(url, {
  headers: {
    'Authorization': `Bearer ${apiKey}`
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching data:', error);
});
```

--------------------------------

### Get NVT Ratio Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet fetches the NVT Ratio using the 'fetch' API. It requires a valid asset ID and your Glassnode API key. The function returns a Promise that resolves to the JSON response containing the NVT ratio data.

```javascript
async function getNvtRatio(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/nvt?a=${assetId}`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'api_key': apiKey
    }
  });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return await response.json();
}

// Example usage:
// const apiKey = 'YOUR_API_KEY';
// const asset = 'BTC';
// getNvtRatio(asset, apiKey).then(data => console.log(data)).catch(error => console.error('Error fetching NVT Ratio:', error));
```

--------------------------------

### Get LTH-MVRV Data (JavaScript)

Source: https://docs.glassnode.com/api/market

Example of fetching Long Term Holder MVRV data using JavaScript's fetch API. This snippet demonstrates how to make a GET request and handle the JSON response.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC';
const url = `https://api.glassnode.com/v1/metrics/market/mvrv_more_155?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

```

--------------------------------

### JavaScript Fetch API for Spot Volume

Source: https://docs.glassnode.com/api/market

This JavaScript code uses the Fetch API to make a GET request to the Glassnode API for daily spot volume data. It shows how to construct the URL with query parameters and handle the JSON response.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // Example asset

fetch(`https://api.glassnode.com/v1/metrics/market/spot_volume_daily_sum_all?a=${asset}`, {
  headers: {
    'x-api-key': apiKey
  }
})
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching spot volume:', error);
  });

```

--------------------------------

### Fetch Velocity Metric (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates how to use the `fetch` API to retrieve the Velocity metric from Glassnode. It constructs the URL with parameters and handles the JSON response.

```javascript
const asset = "text";
const url = `https://api.glassnode.com/v1/metrics/indicators/velocity?a=${asset}`;

fetch(url, {
  method: "GET",
  headers: {
    "Accept": "application/json"
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

--------------------------------

### Fetch HODL Cave Metric Data (JavaScript)

Source: https://docs.glassnode.com/api/market

This snippet demonstrates how to retrieve HODL Cave metric data using JavaScript. It outlines the necessary parameters and the expected JSON response structure.

```javascript
fetch('https://api.glassnode.com/v1/metrics/market/hodl_cave?a=your_asset_id&i=1w&api_key=your_api_key')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

```

--------------------------------

### Get Hash Ribbon Indicator Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet shows how to make a request to the Glassnode API to get the Hash Ribbon indicator data. It uses the `fetch` API and includes the necessary API key. The response is parsed as JSON.

```JavaScript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC';

fetch(`https://api.glassnode.com/v1/metrics/indicators/hash_ribbon?a=${asset}&api_key=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching Hash Ribbon data:', error);
  });

```

--------------------------------

### Get Spot Volume Intraday (JavaScript)

Source: https://docs.glassnode.com/api/market

JavaScript example using the fetch API to retrieve intraday spot volume data. Includes placeholders for API key and asset ID. Error handling for network requests is recommended.

```JavaScript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // e.g., BTC, ETH

fetch(`https://api.glassnode.com/v1/metrics/market/spot_volume_sum_intraday?a=${asset}&api_key=${apiKey}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching spot volume:', error);
  });

```

--------------------------------

### Get Spot Volume Delta Sum (JavaScript)

Source: https://docs.glassnode.com/api/market

Fetches Spot Volume Delta sum data using JavaScript's `fetch` API. This code snippet shows how to construct the request URL with necessary query parameters and handle the JSON response.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // Example asset

fetch(`https://api.glassnode.com/v1/metrics/market/spot_vd_sum?a=${asset}&api_key=${apiKey}`)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

--------------------------------

### Fetch Leverage Position Openings (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript example illustrates fetching leverage position openings using the `fetch` API. It includes setting up the API key and parameters for the request.

```JavaScript
const apiKey = "YOUR_API_KEY";
const asset = "text"; // Replace with desired asset, e.g., "BTC"

fetch(`https://api.glassnode.com/v1/metrics/indicators/leverage_position_openings?a=${asset}`, {
  method: 'GET',
  headers: {
    'Authorization': `ApiKey ${apiKey}`
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

--------------------------------

### Fetch STH-NUPL using JavaScript

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript snippet shows how to retrieve the Short Term Holder NUPL (STH-NUPL) metric using the `fetch` API. It constructs the URL with the asset and API key, handling the JSON response.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // Replace with the desired asset

fetch(`https://api.glassnode.com/v1/metrics/indicators/nupl_less_155?a=${asset}&api_keystring=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching STH-NUPL data:', error);
  });
```

--------------------------------

### Fetch Relative LTH/STH Realized Profit/Loss to Exchanges (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet demonstrates how to fetch the relative realized profit/loss of LTH/STH to exchanges using the Glassnode API. It utilizes the `fetch` API to make a GET request, including the asset parameter. The response is parsed as JSON, providing timestamps and profit/loss data.

```javascript
fetch('/v1/metrics/indicators/realized_profit_loss_lth_sth_to_exchanges_relative?a=text', {
  method: 'GET',
  headers: {
    'Accept': '*/*'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

--------------------------------

### Retrieve MVRV Z-Score Data (JavaScript)

Source: https://docs.glassnode.com/api/market

A JavaScript example using the fetch API to retrieve MVRV Z-Score data. This code demonstrates how to make the API call, handle the response, and parse the JSON output. Remember to include your API key and specify the asset.

```JavaScript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // e.g., 'BTC', 'ETH'
const url = `https://api.glassnode.com/v1/metrics/market/mvrv_z_score?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    // Process the data, e.g., display the MVRV Z-Score
  })
  .catch(error => {
    console.error('Error fetching MVRV Z-Score data:', error);
  });

```

--------------------------------

### Fetch Realized Loss (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates how to fetch the Realized Loss metric using the `fetch` API. It constructs the URL with required parameters like asset ID and API key, and handles the JSON response.

```javascript
const apiKey = "YOUR_API_KEY";
const assetId = "YOUR_ASSET_ID"; // e.g., "BTC"
const url = `https://api.glassnode.com/v1/metrics/indicators/realized_loss?a=${assetId}&api_key=${apiKey}`;

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

```

--------------------------------

### Fetch Relative LTH/STH Realized Profit/Loss (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet shows how to make a GET request to the Glassnode API to retrieve the relative LTH/STH realized profit/loss metric. It uses the `fetch` API and expects a JSON response.

```JavaScript
async function getRelativeLTHSTHRealizedProfitLoss(assetId, since, until, frequency, format, timestampFormat) {
  const apiKey = 'YOUR_API_KEY'; // Replace with your actual API key
  let url = `https://api.glassnode.com/v1/metrics/indicators/realized_profit_loss_lth_sth_relative?a=${assetId}`;
  if (since) url += `&s=${since}`;
  if (until) url += `&u=${until}`;
  if (frequency) url += `&i=${frequency}`;
  if (format) url += `&f=${format}`;
  if (timestampFormat) url += `&timestamp_format=${timestampFormat}`;

  try {
    const response = await fetch(url, {
      headers: {
        'Authorization': `ApiKey ${apiKey}`
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}

// Example usage:
// getRelativeLTHSTHRealizedProfitLoss('BTC', 1678886400, 1678972800, '24h', 'json', 'unix').then(data => console.log(data));
```

--------------------------------

### Fetch Hodled or Lost Coins (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code uses the `fetch` API to get the Hodled or Lost Coins metric. It includes setting the API key and asset as query parameters. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'YOUR_ASSET'; // e.g., 'btc'

fetch(`https://api.glassnode.com/v1/metrics/indicators/hodled_lost_coins?a=${asset}&api_key=${apiKey}`)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

--------------------------------

### Fetch Spot Volume 24h (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript code snippet demonstrates how to fetch the 24-hour spot volume using the Fetch API. It requires your Glassnode API key and the asset symbol. The response is parsed as JSON.

```javascript
const apiKey = "YOUR_API_KEY";
const asset = "BTC"; // Example asset

fetch(`https://api.glassnode.com/v1/metrics/market/spot_volume_daily_sum?a=${asset}&api_key=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

```

--------------------------------

### Get Leverage Position Closures (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

JavaScript code snippet using the 'fetch' API to retrieve leverage position closures data. It includes setting the 'api_key' in the headers and specifying the asset ID in the URL. Handles JSON response parsing.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'YOUR_ASSET_ID'; // e.g., 'btc'

fetch(`https://api.glassnode.com/v1/metrics/indicators/leverage_position_closures?a=${asset}`, {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'api_key': apiKey
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching data:', error);
});

```

--------------------------------

### Fetch Dormancy Flow Metric (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates how to asynchronously fetch the Dormancy Flow metric using the `fetch` API. It constructs the URL with required parameters and includes the API key in the headers for authentication. Error handling for network issues or bad responses is included.

```JavaScript
async function getDormancyFlow(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/dormancy_flow?a=${assetId}`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Accept': 'application/json'
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching Dormancy Flow:', error);
    return null;
  }
}

// Example usage:
// getDormancyFlow('BTC', 'YOUR_API_KEY').then(data => console.log(data));

```

--------------------------------

### GET Relative Outputs by Date Bands (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet illustrates how to make a GET request to the Glassnode API for relative spent transaction outputs by date bands using the `fetch` API. It constructs the URL with parameters and handles the JSON response.

```javascript
async function getRelativeOutputsByDateBands(asset = 'BTC', apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/spent_outputs_by_date_bands_relative?a=${asset}`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `ApiKeyAuth ${apiKey}`,
        'Accept': 'application/json'
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}

// Example usage:
// const apiKey = 'YOUR_API_KEY';
// getRelativeOutputsByDateBands('BTC', apiKey).then(data => console.log(data));
```

--------------------------------

### Fetch Realized Volatility (1 Year) - JavaScript

Source: https://docs.glassnode.com/api/market

This JavaScript example shows how to make a GET request to the Glassnode API to retrieve 1-year realized volatility data. It uses the `fetch` API and requires your API key for authorization.

```javascript
const apiKey = 'YOUR_API_KEY'; // Replace with your actual API key
const assetId = 'BTC'; // Replace with the desired asset ID
const apiUrl = `https://api.glassnode.com/v1/metrics/market/realized_volatility_1_year?a=${assetId}`;

fetch(apiUrl, {
  method: 'GET',
  headers: {
    'Authorization': `ApiKeyAuth ${apiKey}`
  }
})
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

```

--------------------------------

### Fetch Relative Unrealized Loss (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript snippet shows how to retrieve the Relative Unrealized Loss metric using the Fetch API. It constructs the URL with required parameters like asset, API key, and date range, and handles the JSON response.

```javascript
const apiKey = "YOUR_API_KEY";
const asset = "text"; // Replace with desired asset
const url = `https://api.glassnode.com/v1/metrics/indicators/unrealized_loss?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("Error fetching data:", error);
  });

```

--------------------------------

### Get LTH-SOPR Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet shows how to retrieve Long Term Holder SOPR (LTH-SOPR) data from the Glassnode API using the `fetch` API. It includes a placeholder for your API key and the asset ID.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC'; // Example asset

fetch(`https://api.glassnode.com/v1/metrics/indicators/sopr_more_155?a=${asset}&api_key=${apiKey}`)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Error fetching LTH-SOPR data:', error));

```

--------------------------------

### Fetch Spot CVD Sum (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript code snippet illustrates how to fetch the Spot Cumulative Volume Delta (CVD) sum using the `fetch` API. It constructs the URL with parameters and handles the JSON response.

```javascript
const apiKey = 'YOUR_API_KEY';
const assetId = 'YOUR_ASSET_ID'; // e.g., 'btc'
const url = `https://api.glassnode.com/v1/metrics/market/spot_cvd_sum?a=${assetId}&api_key=${apiKey}`;

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    // Process the CVD data here
  })
  .catch(error => {
    console.error('Error fetching Spot CVD sum:', error);
  });

```

--------------------------------

### Fetch LTH-NUPL Data (Python)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This Python script utilizes the `requests` library to fetch LTH-NUPL data from the Glassnode API. It includes error handling for the HTTP request and prints the JSON response. Remember to replace 'YOUR_API_KEY' and 'BTC' with your credentials and desired asset.

```Python
import requests

api_key = 'YOUR_API_KEY'
asset = 'BTC'  # e.g., BTC, ETH
url = f'https://api.glassnode.com/v1/metrics/indicators/nupl_more_155?a={asset}&api_key={api_key}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    print(data)
    # Process the LTH-NUPL data here
except requests.exceptions.RequestException as e:
    print(f"Error fetching LTH-NUPL data: {e}")

```

--------------------------------

### Get ASOL Metric (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code demonstrates fetching the ASOL metric using the `fetch` API. It constructs the URL with query parameters and includes the API key in the request headers for authentication. The response is parsed as JSON.

```JavaScript
async function getASOL(asset, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/asol?a=${asset}`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'x-api-key': apiKey
    }
  });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return await response.json();
}

// Example usage:
// const apiKey = 'YOUR_API_KEY';
// getASOL('BTC', apiKey).then(data => console.log(data));

```

--------------------------------

### Get Liveliness Metric (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript example illustrates fetching the Liveliness metric using the `fetch` API. It constructs the URL with required parameters like asset and API key, and handles the JSON response. Error handling for network issues or invalid responses is included.

```javascript
const apiKey = "YOUR_API_KEY";
const asset = "BTC";
```

--------------------------------

### Get Miner Revenue (Total) - JavaScript

Source: https://docs.glassnode.com/api/mining

JavaScript code to make a request to the Miner Revenue API. It constructs the URL with parameters and fetches the data. Ensure you replace 'YOUR_API_KEY' and 'text' appropriately.

```javascript
const apiKey = 'YOUR_API_KEY';
const asset = 'text'; // e.g., 'BTC', 'ETH'
const url = `https://api.glassnode.com/v1/metrics/mining/revenue_sum?a=${asset}&api_key=${apiKey}`;

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

--------------------------------

### Retrieve Cost Basis Distribution Quantiles Data (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code example shows how to make an API request to retrieve the Cost Basis Distribution Quantiles metric. It utilizes the `fetch` API to send a GET request to the specified Glassnode endpoint.

```javascript
fetch('https://api.glassnode.com/v1/metrics/indicators/cost_basis_distribution_quantiles?a=text', {
  method: 'GET',
  headers: {
    'Accept': '*/*',
    'api_key': 'YOUR_API_KEY' // Replace with your actual API key
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching data:', error);
});

```

--------------------------------

### Fetch Premium Weighted Median Strike (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/options

This JavaScript code demonstrates how to fetch premium-weighted median strike prices using the Glassnode API. It utilizes the `fetch` API and requires your API key and the desired asset ID. The response is parsed as JSON.

```JavaScript
async function getPremiumWeightedMedianStrike(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/options/premium_weighted_median_strike?a=${assetId}&api_key=${apiKey}`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}

// Example usage:
const apiKey = 'YOUR_API_KEY';
const asset = 'BTC';
getPremiumWeightedMedianStrike(asset, apiKey).then(data => console.log(data));

```

--------------------------------

### Get Market Cap (JavaScript)

Source: https://docs.glassnode.com/api/market

JavaScript code using `fetch` to get market capitalization data. It includes authorization with an API key and specifies the asset and desired format. Error handling for the request is also included.

```javascript
async function getMarketCap(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/market/marketcap_usd?api_key=${apiKey}&a=${assetId}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Error fetching market cap:', error);
  }
}

// Example usage:
// const apiKey = 'YOUR_API_KEY';
// const asset = 'BTC';
// getMarketCap(asset, apiKey);
```

--------------------------------

### Fetch Spot OBV Metric (JavaScript)

Source: https://docs.glassnode.com/api/market

This JavaScript code snippet illustrates how to retrieve the Spot On-Balance Volume (OBV) metric using the `fetch` API. It demonstrates setting the API endpoint, required query parameters, and authorization headers. The response is parsed as JSON.

```JavaScript
async function getSpotOBV(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/market/spot_on_balance_volume?a=${assetId}`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `ApiKey ${apiKey}`
      }
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching Spot OBV:', error);
    return null;
  }
}

// Example Usage:
// const apiKey = 'YOUR_API_KEY';
// getSpotOBV('BTC', apiKey).then(data => console.log(data));
```

--------------------------------

### Get Realized Volatility (1 Week) - JavaScript

Source: https://docs.glassnode.com/api/market

Demonstrates how to retrieve 1-week realized volatility data using JavaScript and the Fetch API. The code constructs the API request URL with the asset parameter and handles the JSON response, logging the retrieved data.

```javascript
fetch('https://api.glassnode.com/v1/metrics/market/realized_volatility_1_week?a=your_asset_id', {
  method: 'GET',
  headers: {
    'Authorization': 'YOUR_API_KEY'
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching data:', error);
});

```

--------------------------------

### Fetch Short-Term Holder ASOL (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code fetches the Short-Term Holder ASOL metric using the fetch API. It includes error handling for network requests and parses the JSON response. Replace 'ASSET_ID' and 'YOUR_API_KEY' accordingly.

```javascript
async function getShortTermHolderASOL(assetId, apiKey) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/asol_sth?a=${assetId}&api_key=${apiKey}`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error("Error fetching Short-Term Holder ASOL:", error);
  }
}

// Example usage:
// getShortTermHolderASOL('ETH', 'YOUR_API_KEY');
```

--------------------------------

### Fetch URPD (ATH-Partitioned) Metric - JavaScript

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript code snippet retrieves the ATH-partitioned URPD metric using the fetch API. It requires your Glassnode API key and a valid asset ID. The response is parsed as JSON.

```javascript
const apiKey = 'YOUR_API_KEY';
const assetId = 'YOUR_ASSET_ID'; // e.g., 'BTC'

fetch(`https://api.glassnode.com/v1/metrics/indicators/utxo_realized_price_distribution_ath?a=${assetId}`, {
  method: 'GET',
  headers: {
    'x-api-key': apiKey,
    'Accept': 'application/json'
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error fetching URPD data:', error);
});

```

--------------------------------

### Get Hodler Net Position Change (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript example demonstrates how to retrieve Hodler Net Position Change data using the fetch API. It requires an API key and an asset ID, and it handles the JSON response.

```javascript
async function getHodlerNetPositionChange(apiKey, assetId) {
  const url = `https://api.glassnode.com/v1/metrics/indicators/hodler_net_position_change?a=${assetId}`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'x-api-key': apiKey
    }
  });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data = await response.json();
  return data;
}

// Example usage:
// const apiKey = 'YOUR_API_KEY';
// const assetId = 'BTC';
// getHodlerNetPositionChange(apiKey, assetId).then(data => console.log(data)).catch(error => console.error('Error:', error));

```

--------------------------------

### Fetch Long-Term Holder ASOL (JavaScript)

Source: https://docs.glassnode.com/basic-api/endpoints/indicators

This JavaScript snippet demonstrates how to fetch the Long-Term Holder ASOL metric using the fetch API. It constructs the URL with the asset parameter and includes necessary headers for authorization and content type.

```javascript
fetch('https://api.glassnode.com/v1/metrics/indicators/asol_lth?a=ETH', {
  headers: {
    'Authorization': 'YOUR_API_KEY'
  }
})
  .then(response => response.json())
  .then(data => console.log(data));
```

--------------------------------

### Get Realized Volatility (3 Months) using JavaScript

Source: https://docs.glassnode.com/api/market

This JavaScript example shows how to make a request to the Glassnode API to retrieve realized volatility data. It utilizes the `fetch` API and expects a JSON response.

```javascript
fetch('https://api.glassnode.com/v1/metrics/market/realized_volatility_3_months?a=BTC&api_key=YOUR_API_KEY')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

```