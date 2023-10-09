"""
Custom errors for aempsconn
"""


class CustomException(Exception):
    """
    Custom Exception for raising and handling errors

    Arguments:
        message (str): Error to be printed in the Exception
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class TimeoutFailure(CustomException):
    """
    Custom exception related to the timeout
    """

    def __init__(
        self,
        message: str = "Timeout Error. Make sure that you do not set a very low value as default timeout.",
    ) -> None:
        super().__init__(message)


class HTTPFailure(CustomException):
    """
    Custom exception related to the HTTP requests
    """

    def __init__(
        self, message: str = "HTTP Error has been detected. Check internet connection."
    ) -> None:
        super().__init__(message)


class ProxyFailure(CustomException):
    """
    Custom exception related to the proxy configuration
    """

    def __init__(self, message: str = "Check the Proxy.") -> None:
        super().__init__(message)


class RequestFailure(CustomException):
    """
    Custom exception related to the python3 request module
    """

    def __init__(
        self,
        message: str = "Python3 request has failed. Check internet connection.",
    ) -> None:
        super().__init__(message)


class JSONKeyFailure(CustomException):
    """
    Custom exception related to JSON Keys
    """

    def __init__(
        self,
        message: str = "The request you made may be wrong. 'Resultados' should be in the response. You may want to open an issue on 'https://github.com/fqlenos/aempsconn'.",
    ) -> None:
        super().__init__(message)


class JSONDecodeFailure(CustomException):
    """
    Custom exception related to JSON decode
    """

    def __init__(
        self,
        message: str = "HTTP response seems to be empty. You may want to open an issue on 'https://github.com/fqlenos/aempsconn'.",
    ) -> None:
        super().__init__(message)


class UnhandledError(CustomException):
    """
    Custom exception related to unhandled exceptions
    """

    def __init__(
        self,
        message: str = "Unhandled error. You may want to open an issue on 'https://github.com/fqlenos/aempsconn'.",
    ) -> None:
        super().__init__(message)
