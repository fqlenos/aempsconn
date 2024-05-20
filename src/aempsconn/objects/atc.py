"""Module for the 'Atc' object."""

from pydantic.dataclasses import dataclass


@dataclass
class ATCModel:
    codigo: str
    nombre: str
    nivel: int
