import requests


def list_indices(api_key: str):
    """
    List all available indices.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/market/list-indices"
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers).json()

    return response
