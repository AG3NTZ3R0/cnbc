"""
Endpoints for CNBC API.
"""
from enum import Enum

from .exceptions import InvalidParameterConfiguration


class Endpoints(Enum):
    """
    Endpoints for CNBC API.
    """
    class Parameters(dict):
        """
        Parameters for the endpoint.
        """
        def __init__(self, *args, **kwargs):
            """
            Initialize the parameters.

            :param args: The arguments.
            :param kwargs: The keyword arguments.
            """
            super().__init__(*args, **kwargs)
            self._init_keys = set(self.keys())

        def __setitem__(self, key: str, value: str):
            """
            Set the item.

            :param key: The key.
            :param value: The value.
            """
            if key not in self._init_keys:
                raise InvalidParameterConfiguration()
            super().__setitem__(key, value)

    HOST: str = "cnbc.p.rapidapi.com"
    BASE_URL: str = f"https://{HOST}"
    # Default
    GET_METADATA: tuple[str, Parameters] = (f"{BASE_URL}/get-meta-data", Parameters())
    AUTO_COMPLETE: tuple[str, Parameters] = (f"{BASE_URL}/v2/auto-complete", Parameters({"q": None}))
    # Market
    LIST_INDICES: tuple[str, Parameters] = (f"{BASE_URL}/market/list-indices", Parameters())
    # News
    LIST_TRENDING_NEWS: tuple[str, Parameters] = (f"{BASE_URL}/news/v2/list-trending", Parameters({"tag": "Articles", "count": None}))
    LIST_SPECIAL_REPORTS: tuple[str, Parameters] = (f"{BASE_URL}/news/v2/list-special-reports", Parameters({"pageSize": None, "page": None}))
    LIST_SYMBOL_NEWS: tuple[str, Parameters] = (f"{BASE_URL}/news/v2/list-by-symbol", Parameters({"symbol": None, "page": None, "pageSize": None}))
    # Symbol
    GET_EARNINGS_CHART: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-earnings-chart", Parameters({"issueId": None, "numberOfYears": None}))
    GET_PROFILE: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-profile", Parameters({"issueId": None}))
    GET_CHART: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-chart", Parameters({"symbol": None, "interval": None}))
    TRANSLATE: tuple[str, Parameters] = (f"{BASE_URL}/symbols/translate", Parameters({"symbol": None}))
    GET_SUMMARY: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-summary", Parameters({"issueIds": None}))
    GET_FUNDAMENTALS: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-fundamentals", Parameters({"issueIds": None}))
    GET_PRICELINE_CHART: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-priceline-chart", Parameters({"issueId": None, "numberOfDays": None}))
    GET_PEERS: tuple[str, Parameters] = (f"{BASE_URL}/symbols/get-peers", Parameters({"symbol": None}))

    def get_endpoint(self) -> str | None:
        """
        Get the endpoint of the API request.
        :return: The endpoint of the API request.
        """
        if self in [Endpoints.HOST, Endpoints.BASE_URL]:
            return None
        return self.value[0]

    def get_parameters(self) -> Parameters | None:
        """
        Get the parameters of the endpoint.
        :return: The parameters of the endpoint.
        """
        if self in [Endpoints.HOST, Endpoints.BASE_URL]:
            return None
        return self.value[1]
