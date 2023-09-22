"""
Data type for 'Problemas de Suministro'.
"""

from pydantic import BaseModel


class SuministroModel(BaseModel):
    """
    Pydantic model for data type: Problemas de Suministro.

    Arguments:
        cn (str): código nacional
        nombre (str): nombre de la presentación
        fini (int): fecha de inicio del problema de suministro
        ffin (int): fecha de fin del problema de suministro
        observ (str): observaciones asociadas
        activo (bool): si el problema sigue activo
    """

    cn: str
    nombre: str
    fini: int
    ffin: int
    observ: str
    activo: bool
