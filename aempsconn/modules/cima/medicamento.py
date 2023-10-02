"""
Module for getting information related to Medicamentos.
"""

import sys

from ..base import Base
from ...utils import Endpoint, ConfigModel
from ...datatypes import MedicamentoModel
from ...decorators import json_res_handler
from ...filter import FilterMedicamento


class Medicamento(Base):
    def __init__(self, config: ConfigModel) -> None:
        super().__init__(config=config)

    def get_specific_endpoint(self) -> str:
        """
        Get the specific endpoint for the derived class.

        Result:
            str: Endpoint value
        """
        return Endpoint.MEDICAMENTO.value

    @json_res_handler
    def get(self, filter: FilterMedicamento) -> MedicamentoModel | None:
        """
        Create specific response with the cororect data type

        Arguments:
            filter (FilterMedicamento): the conditions needed for running the request.

        Result:
            MedicamentoModel: Medicamento object
        """

        if not isinstance(filter, FilterMedicamento):
            if self.config.logger is not None:
                self.config.logger.error("Filter is needed for running the query.")
                sys.exit()

        medicamento: MedicamentoModel = MedicamentoModel(
            **super().get(filter.query()).json()
        )
        return medicamento
