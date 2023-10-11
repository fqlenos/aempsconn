"""
Data type for 'ATC'.
"""

from pydantic import BaseModel


class ATCModel(BaseModel):
    """
    Pydantic model for data type: ATC.

    :param codigo: Código ATC.
    :type codigo: str
    :param str nombre: Nombre descriptivo.
    :param int nivel: Nivel del código ATC.
    """

    codigo: str
    nombre: str
    nivel: int
