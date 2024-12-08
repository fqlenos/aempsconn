"""Module for the 'Atc' object."""

from pydantic import BaseModel


class ATCModel(BaseModel):
    codigo: str
    nombre: str
    nivel: int
