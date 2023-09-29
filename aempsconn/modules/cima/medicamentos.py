"""
Module for getting information related to Medicamentos.
"""

from logging import Logger
from requests.exceptions import JSONDecodeError

from ..base import Base
from ...utils import Endpoint, Keys
from ...datatypes import ListMedicamentoModel
from ...decorators import json_res_handler


class Medicamentos(Base):
    def __init__(self, config) -> None:
        super().__init__(config=config)

    def add_condition(self, key: Keys.MEDICAMENTOS.value, value) -> None:
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

    def get_specific_endpoint(self) -> str:
        """
        Get the specific endpoint for the derived class.

        Result:
            str: Endpoint value
        """
        return Endpoint.MEDICAMENTOS.value

    @json_res_handler
    def get(self) -> list[ListMedicamentoModel] | None:
        """
        Create specific response with the cororect data type

        Result:
            list[ListMedicamentoModel]: List of Medicamento object
        """
        medicamentos: list[ListMedicamentoModel] = []
        results: list = super().get().json()["resultados"]
        if len(results) > 0:
            for medicamento in results:
                medicamentos.append(ListMedicamentoModel(**medicamento))
            return medicamentos

        if isinstance(self.config.logger, Logger):
            self.config.logger.info("The respose seems to be empty.")
