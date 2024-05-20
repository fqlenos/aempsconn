"""Module for the 'Excipiente' object."""

from pydantic.dataclasses import dataclass


@dataclass
class ExcipienteModel:
    id: int
    nombre: str
    cantidad: str
    unidad: str
    orden: int
