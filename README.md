# CNBC

A Python package that wraps CNBC API endpoints and returns financial data in JSON. The API queries business news and live market data to streamline the development of financial applications.
<table><tr><td>

#### IMPORTANT LEGAL DISCLAIMER

---

cnbc is **not** affiliated, endorsed, or vetted by CNBC, Inc. It is
an open-source tool that uses a publicly available API and is
intended for research and educational purposes.
</td></tr></table>

## Installation

```shell
pip install cnbc
```

## [Subscribe to CNBC API](https://rapidapi.com/apidojo/api/cnbc/ 'CNBC API')

## Utilization

### APIWrapper
The `APIWrapper` class is used to make requests to the CNBC API. <br>
Note: A majority of the CNBC API endpoints require parameters. These must be set by an additional instruction.

```python
from cnbc import APIWrapper, Endpoints

api_wrapper = APIWrapper(
    api_key='YOUR_API_KEY',
    endpoint=Endpoints.TRANSLATE
)
# The APIWrapper class will supply the required parameters for the configured CNBC API endpoint.
api_wrapper_params = api_wrapper.params
api_wrapper_params['symbol'] = 'AAPL'
# The APIWrapper class will make a request to the CNBC API and return the response in JSON.
json_response = api_wrapper.request()

# The APIWrapper class can be repurposed to make multiple requests to the CNBC API.
api_wrapper.endpoint = Endpoints.GET_SUMMARY
api_wrapper_params = api_wrapper.params
api_wrapper_params['issueIds'] = json_response['issueId']
json_response = api_wrapper.request()
```

#### Translate Endpoint
A majority of the CNBC API endpoints require an `issueId` or `issueIds` parameter. The translate endpoint is used to convert a symbol to an `issueId`. <br>
Note: The `APIWrapper` class contains a translation table which can be loaded and saved to a file to reduce the number of requests to the CNBC API.