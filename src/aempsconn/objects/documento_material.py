"""Module for the 'Documento Material' object."""

from datetime import datetime

from pydantic import BaseModel, HttpUrl


class DocumentoMaterialModel(BaseModel):
    nombre: str
    url: HttpUrl
    fecha: datetime
