from unittest import TestCase
from unittest.mock import Mock

from requests.exceptions import HTTPError, ProxyError, RequestException, Timeout

from aempsconn.decorators import http_res_handler
from aempsconn.errors import (
    HTTPFailure,
    ProxyFailure,
    RequestFailure,
    TimeoutFailure,
    UnhandledError,
)


class TestHTTPResHandler(TestCase):
    def test_http_res_handler_timeout(self):
        """
        Simulates the Timeout error.
        """

        @http_res_handler
        def func(self):
            raise Timeout()

        with self.assertRaises(TimeoutFailure):
            func(Mock())

    def test_http_res_handler_http_error(self):
        """
        Simulates the HTTP error.
        """

        @http_res_handler
        def func(self):
            raise HTTPError()

        with self.assertRaises(HTTPFailure):
            func(Mock())

    def test_http_res_handler_proxy_error(self):
        """
        Simulates the Proxy error.
        """

        @http_res_handler
        def func(self):
            raise ProxyError()

        with self.assertRaises(ProxyFailure):
            func(Mock())

    def test_http_res_handler_request_exc(self):
        """
        Simulates the Python3 Request error.
        """

        @http_res_handler
        def func(self):
            raise RequestException()

        with self.assertRaises(RequestFailure):
            func(Mock())

    def test_http_res_handler_unknown_error(self):
        """
        Simulates the Unhandled error.
        """

        @http_res_handler
        def func(self):
            raise ValueError()

        with self.assertRaises(UnhandledError):
            func(Mock())

    def test_http_res_handler_success(self):
        """
        Simulates succesfull request.
        """

        @http_res_handler
        def func(self):
            return Mock()

        func(Mock())
