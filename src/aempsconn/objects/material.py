"""Module for the 'Material' object."""

from pydantic.dataclasses import dataclass

from .documento_material import DocumentoMaterialModel
from .videos import VideoModel


@dataclass
class MaterialModel:
    titulo: str | None = None
    listaDocsPaciente: list[DocumentoMaterialModel] | None = None
    listaDocsProfesional: list[DocumentoMaterialModel] | None = None
    videos: list[VideoModel] | None = None
