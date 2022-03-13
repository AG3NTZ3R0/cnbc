# CNBC

A Python package that wraps CNBC API endpoints and returns financial data in JSON format. The API queries business news and live market data to streamline the development of financial applications.
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

### Default

Get metadata that supports other endpoints.
```python
json_resp = cnbc.get_metadata(api_key='YOUR_API_KEY')
```

Get auto complete suggestions by term or phrase.
```python
json_resp = cnbc.auto_complete(query='tesla',
                               api_key='YOUR_API_KEY')
```

### Symbol

Generate image of earnings chart of specific stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_earnings_chart(issue_id='36276',
                                    num_of_years='3',
                                    api_key='YOUR_API_KEY')
```

Get summary information of stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_profile(issue_id='36276',
                             api_key='YOUR_API_KEY')
```

Get raw data to draw price chart of stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_chart(issue_id='36276',
                           interval='1d',
                           api_key='YOUR_API_KEY')
```

Get issue_id from specific symbol.
```python
json_resp = cnbc.translate(symbol='TSLA',
                           api_key='YOUR_API_KEY')
```

Get summary information of stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_summary(issue_ids='36276,24812378',
                             api_key='YOUR_API_KEY')
```

Get fundamental information of stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_fundamentals(issue_ids='36276,24812378',
                                  api_key='YOUR_API_KEY')
```

Generate image of price line chart of specific stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_priceline_chart(issue_id='24812378',
                                     num_of_days='1',
                                     api_key='YOUR_API_KEY')
```

Get peers relating to stock quote, index, exchange, etc.
```python
json_resp = cnbc.get_peers(symbol='36276',
                           api_key='YOUR_API_KEY')
```

### Market

List all available indices.
```python
json_resp = cnbc.list_indices(api_key='YOUR_API_KEY')
```

### News

List trending news.
```python
json_resp = cnbc.list_trending_news(count='25',
                                    api_key='YOUR_API_KEY')
```

List special reports.
```python
json_resp = cnbc.list_special_reports(api_key='YOUR_API_KEY')
```

List latest news by symbol name.
```python
json_resp = cnbc.list_symbol_news(symbol='AAPL',
                                  api_key='YOUR_API_KEY')
```
