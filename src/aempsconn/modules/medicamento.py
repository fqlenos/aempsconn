"""Module for retrieving information from 'Medicamento' endpoint."""

from typing import Any

from ..filter.medicamento import MedicamentoFilter
from ..objects.medicamento import MedicamentoModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class Medicamento(BaseModule[MedicamentoFilter, MedicamentoModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "medicamento"

    def parse_result(self, data: dict[str, Any]) -> MedicamentoModel:
        return MedicamentoModel(**data)
