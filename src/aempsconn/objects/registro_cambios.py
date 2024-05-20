"""Module for the 'Registro Cambios' object."""

from datetime import datetime
from typing import Literal

from pydantic import field_validator
from pydantic.dataclasses import dataclass


@dataclass
class RegistroCambiosModel:
    nregistro: str
    fecha: datetime
    tipoCambio: int
    cambios: list[
        Literal[
            "estado",
            "comerc",
            "prosp",
            "ft",
            "psum",
            "notasSeguridad",
            "matinf",
            "otros",
        ]
    ]

    @field_validator("tipoCambio")
    @classmethod
    def check_tipo_cambio_range(cls, tipo_cambio: int) -> int:
        if tipo_cambio not in range(1, 4):
            raise ValueError("'TipoCambio' field must be between 1-4 (both included)")

        return tipo_cambio
