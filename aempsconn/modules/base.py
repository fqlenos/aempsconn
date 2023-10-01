"""
Base module for getting generic methods.
"""

import requests
from requests import Response
import sys

from ..utils import ConfigModel
from ..decorators import http_res_handler


class Base:
    def __init__(self, config: ConfigModel) -> None:
        """
        Initialize the endpoints with the same config.
        """
        self.config: ConfigModel = config
        self.conditions = {}

    @http_res_handler
    def get(self, query: str) -> Response:
        """
        Make request based on generated conditions.

        Arguments:
            query (str): conditions to add to the request.

        Result:
            Response: response of the custom HTTP Request.
        """
        if query == "":
            if self.config.logger is not None:
                self.config.logger.info(f"Creating request for {self.config.url}")
                self.config.logger.warn("Conditions cannot be empty.")
            sys.exit()

        self.endpoint: str = f"{self.config.url}{self.get_specific_endpoint()}{query}"
        if self.config.logger is not None:
            self.config.logger.info(f"URL updated to: {self.endpoint}")

        res = requests.get(
            url=self.endpoint, proxies=self.config.proxies, timeout=self.config.timeout
        )

        return res

    def get_specific_endpoint(self) -> str:
        """
        Get the specific endpoint for the derived class.
        """
        raise NotImplementedError("Subclasses must implement this method.")
