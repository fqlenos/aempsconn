"""Module for retrieving information from 'Materiales' endpoint."""

from typing import Any

from ..filter.material import MaterialFilter
from ..objects.material import MaterialModel
from ..utils.module import BaseModule
from ..utils.request_handler import ReqHandler


class Material(BaseModule[MaterialFilter, MaterialModel]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__(req_handler)

    @property
    def endpoint(self) -> str:
        return "materiales"

    def parse_result(self, data: dict[str, Any]) -> MaterialModel:
        return MaterialModel(**data)
