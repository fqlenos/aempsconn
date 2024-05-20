"""Module for the 'Documento Material' object."""

from datetime import datetime

from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


@dataclass
class DocumentoMaterialModel:
    nombre: str
    url: HttpUrl
    fecha: datetime
