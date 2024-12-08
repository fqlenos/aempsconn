"""Module for the 'Excipiente' object."""

from pydantic import BaseModel, Field


class ExcipienteModel(BaseModel):
    excipiente_id: int = Field(alias="id")
    nombre: str
    cantidad: str
    unidad: str
    orden: int
