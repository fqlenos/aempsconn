"""
Data type for 'Documento'.
"""

from pydantic import BaseModel, HttpUrl
from typing import Literal


class DocumentoModel(BaseModel):
    """
    Pydantic model for data type: Documento.

    Arguments:
        tipo (int): tipo de documento: 1. "Ficha técnica", 2. "Prospecto", 3. "Informe público evaluación", 4. "Plan de gestión de riesgos"
        url (HttpUrl): URL para acceder al documento
        secc (bool): indica si el documento está disponible en HTML por secciones
        urlHtml (HttpUrl | None): URL en formato HTML (sólo si secc = true)
        fecha (int): fecha de modificación del documento
    """

    tipo: int
    url: HttpUrl | None = None
    secc: bool
    urlHtml: HttpUrl | None = None
    fecha: int | None = None
