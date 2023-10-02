"""
Module for getting information related to Medicamentos.
"""

import sys

from ..base import Base
from ...utils import Endpoint, ConfigModel
from ...datatypes import ListMedicamentoModel
from ...decorators import json_res_handler
from ...filter import FilterMedicamentos


class Medicamentos(Base):
    def __init__(self, config: ConfigModel) -> None:
        super().__init__(config=config)

    def get_specific_endpoint(self) -> str:
        """
        Get the specific endpoint for the derived class.

        Result:
            str: Endpoint value
        """
        return Endpoint.MEDICAMENTOS.value

    @json_res_handler
    def get(self, filter: FilterMedicamentos) -> list[ListMedicamentoModel] | None:
        """
        Create specific response with the cororect data type

        Arguments:
            filter (FilterMedicamentos): the conditions needed for running the request.

        Result:
            list[ListMedicamentoModel]: List of Medicamento object
        """

        if not isinstance(filter, FilterMedicamentos):
            if self.config.logger is not None:
                self.config.logger.error("Filter is needed for running the query.")
                sys.exit()

        medicamentos: list[ListMedicamentoModel] = []
        results: list = super().get(filter.query()).json()["resultados"]
        if len(results) > 0:
            for medicamento in results:
                medicamentos.append(ListMedicamentoModel(**medicamento))
            return medicamentos

        if self.config.logger is not None:
            self.config.logger.info("The respose seems to be empty.")
