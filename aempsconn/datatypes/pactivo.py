"""
Data type for 'Principio Activo'.
"""

from pydantic import BaseModel


class PActivoModel(BaseModel):
    """
    Pydantic model for data type: Principio Activo.

    Arguments:
        id (int): id del Principio Activo
        codigo (str): código del Principio Activo
        nombre (str): nombre del Principio Activo
        cantidad (str): cantidad del Principio Activo
        unidad (str): unidad para la cantidad
        orden (int): orden en la lista de principios activos de un medicamento
    """

    id: int
    codigo: str
    nombre: str
    cantidad: str
    unidad: str
    orden: int
