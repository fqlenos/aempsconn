"""
Data type for 'Presentación'.
"""

from pydantic import BaseModel
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    """
    'if' blocks that are never True on runtime (running your code) but they are used by code analysis (IDEs) to highlight the types.
    """
    from .estado import EstadoModel


class PresentacionModel(BaseModel):
    """
    Pydantic model for data type: Presentación.

    Arguments:
        cn (str): código nacional - número de reigstro del medicamento
        nombre (str): nombre del medicamento
        estado (EstadoModel): estado de registro de la Presentación
        comerc (bool): indica si está comercializada o no
        psum (bool): inidica si el medicamento tiene problemas de suministro abiertos
    """

    cn: str
    nombre: str
    estado: "EstadoModel"
    comerc: bool
    psum: bool
