"""
Custom exceptions for the API client.
"""


class APIRequestException(Exception):
    """
    Custom exception for API request errors.
    """
    def __init__(self, status_code, message):
        super().__init__(f"Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message


class NetworkError(Exception):
    """
    Custom exception for network errors.
    """
    def __init__(self):
        super().__init__("Failed to connect to the server")


class InvalidParameterConfiguration(Exception):
    """
    Custom exception for invalid parameter configuration.
    """
    def __init__(self):
        super().__init__("The supplied parameters are incompatible with the required parameters")
