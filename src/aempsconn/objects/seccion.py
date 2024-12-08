"""Module for the 'Seccion' object."""

from pydantic import BaseModel


class SeccionModel(BaseModel):
    seccion: str
    titulo: str
    orden: int
    contenido: str
