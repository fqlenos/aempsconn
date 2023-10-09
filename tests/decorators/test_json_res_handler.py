from unittest import TestCase
from unittest.mock import Mock

from requests.exceptions import JSONDecodeError

from aempsconn.decorators import json_res_handler
from aempsconn.errors import JSONDecodeFailure, JSONKeyFailure


class TestJSONResHandler(TestCase):
    def test_json_res_handler_key_error(self):
        """
        Simulates the Key error.
        """

        @json_res_handler
        def func(self):
            raise KeyError("Key error - not found.")

        with self.assertRaises(JSONKeyFailure):
            func(Mock())

    def test_json_res_handler_json_decode_error(self):
        """
        Simulates the JSON Decode error.
        """

        @json_res_handler
        def func(self):
            json_content = '{"key": "value"}'
            raise JSONDecodeError("JSON Decode error", json_content, 0)

        with self.assertRaises(JSONDecodeFailure):
            func(Mock())

    def test_json_res_handler_success(self):
        """
        Simulates succesfull request.
        """

        @json_res_handler
        def func(self):
            return Mock()

        func(Mock())
