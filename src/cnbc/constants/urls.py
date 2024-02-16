from enum import Enum


class Urls(Enum):
    """
    URLs for CNBC API.
    """
    HOST = "cnbc.p.rapidapi.com"
    BASE_URL = f"https://{HOST.value}"
    # Default
    GET_METADATA = f"{BASE_URL.value}/get-meta-data"
    AUTO_COMPLETE = f"{BASE_URL.value}/v2/auto-complete"
    # Market
    LIST_INDICES = f"{BASE_URL.value}/market/list-indices"
    # News
    LIST_TRENDING_NEWS = f"{BASE_URL.value}/news/v2/list-trending"
    LIST_SPECIAL_REPORTS = f"{BASE_URL.value}/news/v2/list-special-reports"
    LIST_SYMBOL_NEWS = f"{BASE_URL.value}/news/v2/list-by-symbol"
    # Symbol
    GET_EARNINGS_CHART = f"{BASE_URL.value}/symbols/get-earnings-chart"
    GET_PROFILE = f"{BASE_URL.value}/symbols/get-profile"
    GET_CHART = f"{BASE_URL.value}/symbols/get-chart"
    TRANSLATE = f"{BASE_URL.value}/symbols/translate"
    GET_SUMMARY = f"{BASE_URL.value}/symbols/get-summary"
    GET_FUNDAMENTALS = f"{BASE_URL.value}/symbols/get-fundamentals"
    GET_PRICELINE_CHART = f"{BASE_URL.value}/symbols/get-priceline-chart"
    GET_PEERS = f"{BASE_URL.value}/symbols/get-peers"
