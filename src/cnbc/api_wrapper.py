"""
A module to make API requests.
"""
import json
import requests

from .endpoints import Endpoints
from .exceptions import APIRequestException, NetworkError, InvalidParameterConfiguration


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
        self._timeout: int

        self._translate_table: dict[str, str]

        self._endpoint, self._params = endpoint.value
        self._headers = {'x-rapidapi-host': Endpoints.HOST.value, 'x-rapidapi-key': api_key}
        self._timeout = timeout

        self._translation_table = {}

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
        self._endpoint, self._params = endpoint.value

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
        try:
            # Update the parameters if the input parameters match the endpoint parameters.
            if set(self._params.keys()) == set(params.keys()):
                self._params.update(params)
            else:
                raise InvalidParameterConfiguration()
        except AttributeError:
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

    @property
    def translation_table(self):
        """
        Get the translation table of the API request.
        :return: The translation table of the API request.
        """
        return self._translation_table

    @translation_table.setter
    def translation_table(self, translation_table: dict):
        self._translation_table = translation_table

    @translation_table.deleter
    def translation_table(self):
        del self._translation_table

    def translation_table_load(self, file_path: str):
        """
        Load the translation table from a file.
        :param file_path: The file path of the translation table.
        :return: None
        """
        with open(file_path, "r") as file:
            self._translation_table = json.load(file)

    def translation_table_save(self, file_path: str):
        """
        Save the translation table to a file.
        :param file_path: The file path of the translation table.
        :return: None
        """
        with open(file_path, "w") as file:
            json.dump(self._translation_table, file)

    def request(self) -> dict:
        """
        Make an API request.
        :return: API response in JSON.
        """
        # If the endpoint is the translate endpoint, then check if the symbol is in the translation table.
        if self._endpoint == Endpoints.TRANSLATE.get_endpoint():
            # If the symbol is in the translation table, then return a faux JSON response.
            if issueId := self._translation_table.get(self._params['symbol']):
                return {'issueId': issueId, 'errorMessage': '', 'errorCode': ''}

        with requests.request("GET", self._endpoint,
                              headers=self._headers, params=self._params, timeout=self._timeout) as response:
            try:
                response.raise_for_status()
                response_json = response.json()
                # If the endpoint is the translate endpoint, then update the translation table.
                if self._endpoint == Endpoints.TRANSLATE.get_endpoint():
                    self._translation_table[self._params['symbol']] = response_json['issueId']
                return response_json
            except requests.exceptions.HTTPError as e:
                raise APIRequestException(response.status_code, response.text) from e
            except requests.exceptions.RequestException as e:
                raise NetworkError() from e
