"""
Data type for 'Documento'.
"""

from pydantic import BaseModel, HttpUrl
from typing import Literal


class DocumentoModel(BaseModel):
    """
    Pydantic model for data type: Documento.

    Arguments:
        tipo (str): tipo de documento
        url (HttpUrl): URL para acceder al documento
        secc (bool): indica si el documento está disponible en HTML por secciones
        urlHtml (HttpUrl | None): URL en formato HTML (sólo si secc = true)
        fecha (int): fecha de modificación del documento
    """

    tipo: Literal[
        "Ficha técnica",
        "Prospecto",
        "Informe público evaluación",
        "Plan de gestión de riesgos",
    ]
    url: HttpUrl
    secc: bool
    urlHtml: HttpUrl | None = None
    fecha: int
