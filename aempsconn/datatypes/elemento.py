"""
Data type for 'Elemento'.
"""

from pydantic import BaseModel


class ElementoModel(BaseModel):
    """
    Pydantic model for data type: Elemento.

    Arguments:
        id (int): id del Elemento
        codigo (str): código alfanumérico del Elemento
        nombre (str): nombre descriptivo del Elemento
    """

    id: int
    codigo: str | None = None
    nombre: str
