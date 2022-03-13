import requests


def get_metadata(api_key: str):
    """
    Get metadata that supports other endpoints.

    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/get-meta-data"
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers).json()

    return response


def auto_complete(query: str, api_key: str):
    """
    Get auto complete suggestions by term or phrase.

    :param query: Any familiar term or phrase to get auto complete suggestions.
    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/v2/auto-complete"
    querystring = {
        "q": query
    }
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
