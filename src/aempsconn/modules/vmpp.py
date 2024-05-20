"""Module for retrieving information from 'Vmpp' endpoint."""

from typing import Any

from ..filter.vmpp import VmppFilter
from ..objects.descripcion_clinica import DescripcionClinicaModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class Vmpp(BaseModule[VmppFilter, DescripcionClinicaModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "vmpp"

    def parse_result(self, data: dict[str, Any]) -> DescripcionClinicaModel:
        return DescripcionClinicaModel(**data)
