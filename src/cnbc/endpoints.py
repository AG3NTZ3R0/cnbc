"""
Endpoints for CNBC API.
"""
from enum import Enum


class Endpoints(Enum):
    """
    Endpoints for CNBC API.
    """
    HOST: str = "cnbc.p.rapidapi.com"
    BASE_URL: str = f"https://{HOST}"
    # Default
    GET_METADATA: tuple[str, None] = (f"{BASE_URL}/get-meta-data", None)
    AUTO_COMPLETE: tuple[str, dict[str, str]] = (f"{BASE_URL}/v2/auto-complete", {"q": None})
    # Market
    LIST_INDICES: tuple[str, None] = (f"{BASE_URL}/market/list-indices", None)
    # News
    LIST_TRENDING_NEWS: tuple[str, dict[str, str]] = (f"{BASE_URL}/news/v2/list-trending", {"tag": "Articles", "count": None})
    LIST_SPECIAL_REPORTS: tuple[str, dict[str, str]] = (f"{BASE_URL}/news/v2/list-special-reports", {"pageSize": None, "page": None})
    LIST_SYMBOL_NEWS: tuple[str, dict[str, str]] = (f"{BASE_URL}/news/v2/list-by-symbol", {"symbol": None, "page": None, "pageSize": None})
    # Symbol
    GET_EARNINGS_CHART: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-earnings-chart", {"issueId": None, "numberOfYears": None})
    GET_PROFILE: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-profile", {"issueId": None})
    GET_CHART: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-chart", {"symbol": None, "interval": None})
    TRANSLATE: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/translate", {"symbol": None})
    GET_SUMMARY: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-summary", {"issueIds": None})
    GET_FUNDAMENTALS: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-fundamentals", {"issueIds": None})
    GET_PRICELINE_CHART: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-priceline-chart", {"issueId": None, "numberOfDays": None})
    GET_PEERS: tuple[str, dict[str, str]] = (f"{BASE_URL}/symbols/get-peers", {"symbol": None})

    def get_endpoint(self) -> str | None:
        """
        Get the endpoint of the API request.
        :return: The endpoint of the API request.
        """
        if self in [Endpoints.HOST, Endpoints.BASE_URL]:
            return None
        return self.value[0]

    def get_parameters(self) -> dict[str, str] | None:
        """
        Get the parameters of the endpoint.
        :return: The parameters of the endpoint.
        """
        if self in [Endpoints.HOST, Endpoints.BASE_URL]:
            return None
        return self.value[1]
