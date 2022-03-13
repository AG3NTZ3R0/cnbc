import requests


def list_indices():
    """
    List all available indices.

    :return: API response in JSON.
    """
    url = "https://cnbc.p.rapidapi.com/market/list-indices"
    headers = {
        'x-rapidapi-host': "cnbc.p.rapidapi.com",
        'x-rapidapi-key': "d73bb60f82mshbe3e55c57b941abp1abe67jsn7d7492f26dee"
    }

    response = requests.request("GET", url, headers=headers).json()

    return response
