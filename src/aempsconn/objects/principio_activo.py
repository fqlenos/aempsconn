"""Module for the 'Principio Activo' object."""

from pydantic import BaseModel, Field


class PActivoModel(BaseModel):
    pactivo_id: int = Field(alias="id")
    codigo: str
    nombre: str
    cantidad: str
    unidad: str
    orden: int
