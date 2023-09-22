"""
Module for getting information related to Medicamentos.
"""

import requests
from requests import Response
from typing import Literal
from logging import Logger
import sys

from ...utils import ConfigModel, Endpoint
from ...decorators import http_res_handler


class Medicamentos:
    literal_keys = Literal[
        "pagina",
        "nombre",
        "laboratorio",
        "practivo1",
        "practivo2",
        "idpractiv1",
        "idpractiv2",
        "cn",
        "atc",
        "nregistro",
        "npactiv",
        "triangulo",
        "huerfano",
        "biosimilar",
        "sust",
        "vmp",
        "comerc",
        "autorizados",
        "receta",
        "estupefaciente",
        "psicotropo",
        "estuopsico",
    ]

    def __init__(self, config: ConfigModel) -> None:
        """
        Initialize the endpoints related to Medicamentos.
        """

        self.config: ConfigModel = config
        self.conditions = {}

    def add_condition(self, key: literal_keys, value) -> None:
        """
        Add a value for each necessary key condition.

        Arguments:
            key: key to assign as condition
            value: value to assign to the previous key condition
        """
        self.conditions.update({key: value})
        if isinstance(self.config.logger, Logger):
            self.config.logger.info(
                f"'{key}' with value: '{value}' successfully added to conditions."
            )

    @http_res_handler
    def get(self) -> Response | None:
        """
        Get one Medicamento based on previous generated the conditions.
        """
        if not self.conditions:
            if isinstance(self.config.logger, Logger):
                self.config.logger.warn("Conditions cannot be {}")
            sys.exit()

        query = "?"
        for key, value in self.conditions.items():
            query += f"{key}={value}&"
        query = query[:-1]  # so it removes the last "&"

        self.endpoint: str = f"{self.config.url}{Endpoint.MEDICAMENTOS.value}{query}"

        res = requests.get(
            url=self.endpoint, proxies=self.config.proxies, timeout=self.config.timeout
        )

        return res
