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

