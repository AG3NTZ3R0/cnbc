import requests

from constants.urls import Urls


def list_indices(api_key: str):
    """
    List all available indices.

    :return: API response in JSON.
    """
    url = Urls.LIST_INDICES.value
    headers = {
        'x-rapidapi-host': Urls.HOST.value,
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, timeout=10).json()

    return response
