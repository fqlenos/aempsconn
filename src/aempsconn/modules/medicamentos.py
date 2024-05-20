"""Module for retrieving information from 'Medicamentos' endpoint."""

from typing import Any

from ..filter.medicamentos import MedicamentosFilter
from ..objects.medicamento import MedicamentosModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class Medicamentos(BaseModule[MedicamentosFilter, MedicamentosModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "medicamentos"

    def parse_result(self, data: dict[str, Any]) -> MedicamentosModel:
        return MedicamentosModel(**data)
