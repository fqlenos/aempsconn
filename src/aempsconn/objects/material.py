"""Module for the 'Material' object."""

from pydantic import HttpUrl
from pydantic.dataclasses import dataclass

from .documento_material import DocumentoMaterialModel


@dataclass
class MaterialModel:
    titulo: str
    listaDocsPaciente: list[DocumentoMaterialModel]
    listaDocsProfesional: list[DocumentoMaterialModel]
    video: HttpUrl
