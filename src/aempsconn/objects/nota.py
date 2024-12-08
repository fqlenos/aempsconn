"""Module for the 'Nota' object."""

from datetime import datetime

from pydantic import BaseModel, HttpUrl, field_validator


class NotaModel(BaseModel):
    tipo: int
    num: str
    referencia: str
    asunto: str
    fecha: datetime
    url: HttpUrl

    @field_validator("tipo")
    def check_tipo_range(cls, tipo: int) -> int:
        if tipo != 1:
            raise ValueError("'Tipo' field must be set to 1")

        return tipo
