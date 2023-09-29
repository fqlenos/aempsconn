"""
Usable Literal keys for the wrapper conditions.
"""

from enum import Enum
from typing import Literal


class Keys(Enum):
    MEDICAMENTO = Literal["cn", "nregistro"]
    MEDICAMENTOS = Literal[
        "pagina",
        "nombre",
        "laboratorio",
        "practivo1",
        "practivo2",
        "idpractiv1",
        "idpractiv2",
        "cn",
        "atc",
        "nregistro",
        "npactiv",
        "triangulo",
        "huerfano",
        "biosimilar",
        "sust",
        "vmp",
        "comerc",
        "autorizados",
        "receta",
        "estupefaciente",
        "psicotropo",
        "estuopsico",
    ]
    PRESENTACION = Literal["codNacional"]
    PRESENTACIONES = Literal[
        "pagina",
        "cn",
        "nregistro",
        "vmp",
        "vmpp",
        "idpractiv1",
        "comerc",
        "estupefaciente",
        "psicotropo",
        "estuopsico",
    ]
