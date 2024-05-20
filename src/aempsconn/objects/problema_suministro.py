"""Module for the 'Problema Suministro' object."""

from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class ProblemaSuministroModel:
    cn: str
    nombre: str
    fini: datetime
    ffin: datetime
    observ: str
    activo: bool
