"""Module for the 'Registro Cambios' object."""

from datetime import datetime
from typing import Literal

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class RegistroCambiosModel:
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
