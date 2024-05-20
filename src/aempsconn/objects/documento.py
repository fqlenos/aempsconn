"""Module for the 'Documento' object."""

from datetime import datetime

from pydantic import HttpUrl, field_validator
from pydantic.dataclasses import dataclass


@dataclass
class DocumentoModel:
    tipo: int
    secc: bool
    url: HttpUrl | None = None
    urlHtml: HttpUrl | None = None
    fecha: datetime | None = None

    @field_validator("tipo")
    @classmethod
    def check_tipo_range(cls, tipo: int) -> int:
        if tipo not in range(1, 5):
            raise ValueError("'Tipo' field must be between 1-4 (both included)")

        return tipo
