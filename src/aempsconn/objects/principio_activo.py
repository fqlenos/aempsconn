"""Module for the 'Principio Activo' object."""

from pydantic.dataclasses import dataclass


@dataclass
class PActivoModel:
    id: int
    codigo: str
    nombre: str
    cantidad: str
    unidad: str
    orden: int
