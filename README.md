# CNBC

A Python package that wraps CNBC API endpoints and returns financial data in JSON. The API queries business news and live market data to streamline the development of financial applications.
<table><tr><td>

#### IMPORTANT LEGAL DISCLAIMER

---

cnbc is **not** affiliated, endorsed, or vetted by CNBC, Inc. It is
an open-source tool that uses a publicly available API and is
intended for research and educational purposes.
</td></tr></table>

## Install

```shell
pip install cnbc
```

## [Subscribe to CNBC API](https://rapidapi.com/apidojo/api/cnbc/ 'CNBC API')

## Tutorial

```python
import cnbc
```

## APIWrapper
The APIWrapper class is the main class of the package. It is used to make requests to the CNBC API.

### Initialization
To initialize the APIWrapper, you need to provide your API key and the endpoint you want to use. The available endpoints are defined in the `Endpoints` class.
```python
from cnbc.api_wrapper import APIWrapper
from cnbc.constants.endpoints import Endpoints

api_wrapper = APIWrapper(
    api_key='YOUR_API_KEY',
    endpoint=Endpoints.GET_METADATA
)
```
#### Endpoint Parameters
A majority of the endpoints require parameters. There is an additional step in this scenario.
```python
endpoint_params = api_wrapper.get_params()
# Set the specific parameter(s) for the endpoint
endpoint_params['issueIds'] = '123,459,789'
api_wrapper.set_params(endpoint_params)
```

### Request
To make a request to the CNBC API, use the `request` method. This method returns the JSON response from the API.
```python
json_resp = api_wrapper.request()
```

### Reuse
You can reuse the APIWrapper instance to make multiple requests to the CNBC API. Just set the new endpoint and parameters.
```python
api_wrapper.set_endpoint(Endpoints.GET_SUMMARY)

endpoint_params = api_wrapper.get_params()
endpoint_params['issueIds'] = '987,654,321'
api_wrapper.set_params(endpoint_params)

json_resp = api_wrapper.request()
```

### Endpoints

#### GET_METADATA
Get metadata that supports other endpoints.

#### AUTO_COMPLETE
Get auto complete suggestions by term or phrase.
##### Parameters
- `q`: The term or phrase for which to get auto complete suggestions.

#### LIST_INDICES
List all available indices.

#### LIST_TRENDING_NEWS
List trending news.
##### Parameters
- `count`: The number of trending news to list.
- `tag` (optional): The tag to filter the news.

#### LIST_SPECIAL_REPORTS
List special reports.
##### Parameters
- `pageSize`: The number of items per page.
- `page`: The page number.

#### LIST_SYMBOL_NEWS
List latest news by symbol name.
##### Parameters
- `symbol`: The specific symbol to get news for.
- `pageSize`: The number of items per page.
- `page`: The page number.

#### GET_EARNINGS_CHART
Generate image of earnings chart of specific stock quote, index, exchange, etc.
##### Parameters
- `issueId`: The ID of the specific stock quote, index, exchange, etc.
- `numberOfYears`: The number of years for which to generate the earnings chart.

#### GET_PROFILE
Get summary information of stock quote, index, exchange, etc.
##### Parameters
- `issueId`: The ID of the specific stock quote, index, exchange, etc.

#### GET_CHART
Get raw data to draw price chart of stock quote, index, exchange, etc.
##### Parameters
- `symbol`: The specific symbol to get chart data for.
- `interval`: The interval for the price chart data.

#### TRANSLATE
Get issue ID from specific symbol.
##### Parameters
- `symbol`: The specific symbol to translate into an issue ID.

#### GET_SUMMARY
Get summary information of stock quote, index, exchange, etc.
##### Parameters
- `issueIds`: A comma-separated list of issue IDs to get summary information.

#### GET_FUNDAMENTALS
Get fundamental information of stock quote, index, exchange, etc.
##### Parameters
- `issueIds`: A comma-separated list of issue IDs to get fundamental information.

#### GET_PRICELINE_CHART
Generate image of price line chart of specific stock quote, index, exchange, etc.
##### Parameters
- `issueId`: The ID of the specific stock quote, index, exchange, etc.
- `numberOfDays`: The number of days for which to generate the price line chart.

#### GET_PEERS
Get peers relating to stock quote, index, exchange, etc.
##### Parameters
- `symbol`: The specific symbol to get peers relating to it.
