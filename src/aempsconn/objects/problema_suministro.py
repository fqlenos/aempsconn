"""Module for the 'Problema Suministro' object."""

from datetime import datetime

from pydantic import BaseModel


class ProblemaSuministroModel(BaseModel):
    cn: str
    nombre: str
    fini: datetime
    ffin: datetime
    observ: str
    activo: bool
