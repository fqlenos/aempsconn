"""Module for the 'Registro Cambios' object."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class RegistroCambiosModel(BaseModel):
    nregistro: str
    fecha: datetime
    cambio: list[
        Literal[
            "estado",
            "comerc",
            "prosp",
            "ft",
            "psum",
            "notasSeguridad",
            "matinf",
            "otros",
            "fotos",
        ]
    ]
    tipoCambio: int = Field(ge=1, le=4)
