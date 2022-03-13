import requests


def get_earnings_chart(issue_id: str, number_of_years: str, api_key: str):
    """
    Generate image of earnings chart of specific stock quote, index, exchange, etc.

    :param issue_id: The value of the issueId field returned in auto-complete or translate endpoints.
    :param number_of_years: The latest number of years to get an earnings report of (1 to 10).
    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/symbols/get-earnings-chart"
    querystring = {
        "issueId": issue_id,
        "numberOfYears": number_of_years
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_profile(issue_id: str, api_key: str):
    """
    Get summary information of stock quote, index, exchange, etc.

    :param issue_id: The value of the issueId field returned in auto-complete or translate endpoints.
    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/symbols/get-profile"
    querystring = {
        "issueId": "36276"
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': "d73bb60f82mshbe3e55c57b941abp1abe67jsn7d7492f26dee"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_chart(issue_id: str, interval: str, api_key: str):
    """
    Get raw data to draw price chart of stock quote, index, exchange, etc.

    :param issue_id: The value of the issueId field returned in auto-complete or translate endpoints.
    :param interval: One of the following: 1d, 5d, 1m, 3m, 6m, ytd, 1y, 3y, 5y, 10y, all.
    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/symbols/get-chart"
    querystring = {
        "symbol": issue_id,
        "interval": interval
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def translate(symbol: str, api_key: str):
    """
    Get issue_id from specific symbol.

    :param symbol: Symbol of a stock, index, exchange, etc.
    :param api_key: An API key to CNBC API.

    :return: API response in JSON
    """
    url = "https://cnbc.p.rapidapi.com/symbols/translate"
    querystring = {
        "symbol": symbol
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_summary(issue_ids: str, api_key: str):
    """
    Get summary information of stock quote, index, exchange, etc.

    :param issue_ids: The value of the issueId field returned in auto-complete or translate endpoints. Separated by comma for multiple values. Ex : 36276,24812378
    :param api_key: An API key to CNBC API

    :return: API response in JSON
    """
    url = "https://cnbc.p.rapidapi.com/symbols/get-summary"
    querystring = {
        "issueIds": issue_ids
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_fundamentals(issue_ids: str, api_key: str):
    """
    Get fundamental information of stock quote, index, exchange, etc.

    :param issue_ids: The value of the issueId field returned in auto-complete or translate endpoints. Separated by comma for multiple values. Ex : 36276,24812378
    :param api_key: An API key to CNBC API

    :return: API response in JSON
    """
    url = "https://cnbc.p.rapidapi.com/symbols/get-fundamentals"
    querystring = {
        "issueIds": issue_ids
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
