"""Module for the 'Seccion' object."""

from pydantic.dataclasses import dataclass


@dataclass
class SeccionModel:
    seccion: str
    titulo: str
    orden: int
    contenido: str
