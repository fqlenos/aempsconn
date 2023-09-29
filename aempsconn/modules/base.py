"""
Base module for getting generic methods.
"""

import requests
from requests import Response
from logging import Logger
import sys
from multiprocessing.pool import ThreadPool

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
    def get(self, all_pages: bool = True) -> Response:
        """
        Make request based on generated conditions.

        Arguments:
            all_pages (bool): Indicates if all the pages are going to be downloaded at once or not.
        """
        if not self.conditions:
            if isinstance(self.config.logger, Logger):
                self.config.logger.info(f"Creating request for {self.config.url}")
                self.config.logger.warn("Conditions cannot be {}")
            sys.exit()

        if "pagina" in list(self.conditions.keys()) and all_pages:
            """
            Checks if "pagina" condition exists in the conditions and if the all_pages argument is chosen.
            If "pagina" exists the all_pages condition will be turned off.
            """
            all_pages = False
            if isinstance(self.config.logger, Logger):
                self.config.logger.warn("Option 'all_pages' is disabled.")

        query = "?"
        for key, value in self.conditions.items():
            query += f"{key}={value}&"
        query = query[:-1]  # so it removes the last "&"

        self.endpoint: str = f"{self.config.url}{self.get_specific_endpoint()}{query}"
        if isinstance(self.config.logger, Logger):
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