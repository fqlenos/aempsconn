"""Module for retrieving information from 'Registro Cambios' endpoint."""

from typing import Any

from ..filter.registro_cambios import RegistroCambiosFilter
from ..objects.registro_cambios import RegistroCambiosModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class RegistroCambios(BaseModule[RegistroCambiosFilter, RegistroCambiosModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "registroCambios"

    def parse_result(self, data: dict[str, Any]) -> RegistroCambiosModel:
        if "Es necesario indicar la fecha" in data.values():
            raise KeyError("You must filter, at least, by `fecha`")
        return RegistroCambiosModel(**data)
