"""
Data type for 'Sección'.
"""

from pydantic import BaseModel


class SeccionModel(BaseModel):
    """
    Pydantic model for data type: Sección.

    Arguments:
        seccion (str): número de sección - puede tener hasta tres niveles separados por '.'
        titulo (str): título de sección
        orden (int): orden de la sección
        contenido (str): texto de la sección en formato HTMl
    """

    seccion: str
    titulo: str
    orden: int
    contenido: str
