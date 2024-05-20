"""Module for the 'Nota' object."""

from datetime import datetime

from pydantic import HttpUrl, field_validator
from pydantic.dataclasses import dataclass


@dataclass
class NotaModel:
    tipo: int
    num: str
    ref: str
    asunto: str
    fecha: datetime
    url: HttpUrl

    @field_validator("tipo")
    def check_tipo_range(cls, tipo: int) -> int:
        if tipo != 1:
            raise ValueError("'Tipo' field must be set to 1")

        return tipo
