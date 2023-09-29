"""
Data type for 'Estado'.
"""

from pydantic import BaseModel


class EstadoModel(BaseModel):
    """
    Pydantic model for data type: Estado.

    Arguments:
        aut (int): fecha de autorización
        sup (int): fecha de suspensión
        rev (int): fecha de revocación
    """

    aut: int | None = None
    sup: int | None = None
    rev: int | None = None
