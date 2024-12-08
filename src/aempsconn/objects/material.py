"""Module for the 'Material' object."""

from pydantic import BaseModel

from .documento_material import DocumentoMaterialModel
from .videos import VideoModel


class MaterialModel(BaseModel):
    titulo: str | None = None
    listaDocsPaciente: list[DocumentoMaterialModel] | None = None
    listaDocsProfesional: list[DocumentoMaterialModel] | None = None
    videos: list[VideoModel] | None = None
