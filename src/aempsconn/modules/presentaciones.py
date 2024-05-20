"""Module for retrieving information from 'Presentaciones' endpoint."""

from typing import Any

from ..filter.presentaciones import PresentacionesFilter
from ..objects.presentacion import PresentacionesModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class Presentaciones(BaseModule[PresentacionesFilter, PresentacionesModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "presentaciones"

    def parse_result(self, data: dict[str, Any]) -> PresentacionesModel:
        return PresentacionesModel(**data)
