"""
Base URL and usable endpoints for the wrapper.
"""

from enum import Enum

BASEURL = "https://cima.aemps.es/cima/rest"


class Endpoint(Enum):
    MEDICAMENTOS = "/medicamentos"
    MEDICAMENTO = "/medicamento"
    PRESENTACIONES = "/presentaciones"
    PRESENTACION = "/presentacion"
    PSUMINISTRO = "/psuministro"
