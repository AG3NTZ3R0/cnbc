"""
A module to make API requests.
"""
import requests

from src.cnbc.constants.endpoints import Endpoints
from src.cnbc.exceptions import APIRequestException, NetworkError, InvalidParameterConfiguration


class APIWrapper:
    """
    A class to make API requests.
    """

    def __init__(self, api_key: str, endpoint: Endpoints, timeout: int = 10):
        """
        Initialize the APIWrapper.

        :param api_key: The API key.
        :param endpoint: The endpoint of the API request.
        :param timeout: The timeout of the API request.
        """
        self._endpoint: str
        self._params: dict[str, str]
        self._headers: dict[str, str]
        self.timeout: int

        self._endpoint, self._params = endpoint
        self._headers = {'x-rapidapi-host': Endpoints.HOST, 'x-rapidapi-key': api_key}
        self._timeout = timeout

    def _safe_delete(self):
        """
        Safely delete the attributes.
        """
        del self._endpoint
        del self._params

    @property
    def endpoint(self):
        """
        Get the endpoint of the API request.
        :return: The endpoint of the API request.
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: Endpoints):
        self._endpoint, self._params = endpoint

    @endpoint.deleter
    def endpoint(self):
        self._safe_delete()

    @property
    def params(self):
        """
        Get the parameters of the API request.
        :return: The parameters of the API request.
        """
        return self._params

    @params.setter
    def params(self, params: dict[str, str]):
        if set(self._params.keys()) == set(params.keys()):
            self._params.update(params)
        else:
            raise InvalidParameterConfiguration()

    @params.deleter
    def params(self):
        self._safe_delete()

    @property
    def headers(self):
        """
        Get the headers of the API request.
        :return: The headers of the API request.
        """
        return self._headers

    @headers.setter
    def headers(self, headers: dict):
        self._headers = headers

    @headers.deleter
    def headers(self):
        del self._headers

    @property
    def timeout(self):
        """
        Get the timeout of the API request.
        :return: The timeout of the API request.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout: int):
        self._timeout = timeout

    @timeout.deleter
    def timeout(self):
        del self._timeout

    def request(self) -> dict:
        """
        Make an API request.
        :return: API response in JSON.
        """
        with requests.request("GET", self._endpoint,
                              headers=self._headers, params=self._params, timeout=self._timeout) as response:
            try:
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                raise APIRequestException(response.status_code, response.text) from e
            except requests.exceptions.RequestException as e:
                raise NetworkError() from e
