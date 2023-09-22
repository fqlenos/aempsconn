"""
Data type for 'Excipiente'.
"""

from pydantic import BaseModel


class ExcipienteModel(BaseModel):
    """
    Pydantic model for data type: Excipiente.

    Arguments:
        id (int): id del excipiente
        nombre (str): nombre del excipiente
        cantidad (str): cantidad de excipiente
        unidad (str): unidad para la cantidad
        orden (int): orden en la lista de excipiente de un medicamento
    """

    id: int
    nombre: str
    cantidad: str
    unidad: str
    orden: int
