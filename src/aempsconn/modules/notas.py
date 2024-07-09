"""Module for retrieving information from 'Notas' endpoint."""

from typing import Any

from ..filter.nota import NotaFilter
from ..objects.nota import NotaModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class Notas(BaseModule[NotaFilter, NotaModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "notas"

    def parse_result(self, data: list[dict[str, Any]]) -> list[NotaModel]:
        return [NotaModel(**d) for d in data]
