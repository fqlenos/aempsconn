"""Module for the 'Documento' object."""

from datetime import datetime

from pydantic import Field, HttpUrl
from pydantic.dataclasses import dataclass


@dataclass
class DocumentoModel:
    secc: bool
    tipo: int = Field(ge=1, le=4)
    url: HttpUrl | None = None
    urlHtml: HttpUrl | None = None
    fecha: datetime | None = None
