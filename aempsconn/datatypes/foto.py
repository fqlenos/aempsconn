"""
Data type for 'Foto'.
"""

from pydantic import BaseModel, HttpUrl
from typing import Literal


class FotoModel(BaseModel):
    """
    Pydantic model for data type: Foto.

    Arguments:
        tipo (str):  tipo de Imagen
        url (HttpURL): URL para acceder a las Imágenes
        fecha (int): fecha de actualización de la Imagen
    """

    tipo: Literal["materialas", "formafarmac"]
    url: HttpUrl
    fecha: int
