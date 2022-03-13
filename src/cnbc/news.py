import requests


def list_trending_news(count: str, api_key: str):
    """
    List trending news.

    :param count: Number of items returned by the endpoint.
    :param api_key: An API key to CNBC API.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/news/v2/list-trending"
    querystring = {
        "tag": "Articles",
        "count": count
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def list_special_reports(api_key: str, page: str = 1, page_size: str = 25, ):
    """
    List special reports.

    :param api_key: An API key to CNBC API.
    :param page: For paging purposes.
    :param page_size: For paging purposes.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/news/v2/list-special-reports"
    querystring = {
        "pageSize": page_size,
        "page": page
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def list_symbol_news(symbol: str, api_key: str, page: str = 1, page_size: str = 25):
    """
    List latest news by symbol name.

    :param symbol: Symbol of a stock, index, exchange, etc.
    :param api_key: An API key to CNBC API.
    :param page: For paging purposes.
    :param page_size: For paging purposes.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/news/v2/list-by-symbol"
    querystring = {
        "symbol": symbol,
        "page": page,
        "pageSize": page_size
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
