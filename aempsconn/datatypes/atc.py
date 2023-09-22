"""
Data type for 'ATC'.
"""

from pydantic import BaseModel


class ATCModel(BaseModel):
    """
    Pydantic model for data type: ATC.

    Arguments:
        codigo (str): código ATC
        nombre (str): nombre descriptivo
        nivel (str): nivel del código ATC
    """

    codigo: str
    nombre: str
    nivel: str
