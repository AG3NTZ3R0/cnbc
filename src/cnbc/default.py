import requests

from constants.urls import Urls


def get_metadata(api_key: str):
    """
    Get metadata that supports other endpoints.

    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = Urls.GET_METADATA.value
    headers = {
        'x-rapidapi-host': Urls.HOST.value,
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, timeout=10).json()

    return response


def auto_complete(query: str, api_key: str):
    """
    Get auto complete suggestions by term or phrase.

    :param query: Any familiar term or phrase to get auto complete suggestions.
    :param api_key: An API key from CNBC API.

    :return: API response in JSON.
    """
    url = Urls.AUTO_COMPLETE.value
    querystring = {
        "q": query
    }
    headers = {
        'x-rapidapi-host': Urls.HOST.value,
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10).json()

    return response
