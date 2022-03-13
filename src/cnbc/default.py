import requests


def get_meta_data(api_key: str):
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

