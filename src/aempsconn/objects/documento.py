"""Module for the 'Documento' object."""

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class DocumentoModel(BaseModel):
    secc: bool
    tipo: int = Field(ge=1, le=4)
    url: HttpUrl | None = None
    url_html: HttpUrl | None = Field(alias="urlHtml", default=None)
    fecha: datetime | None = None
