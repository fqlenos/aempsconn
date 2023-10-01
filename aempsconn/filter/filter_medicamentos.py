"""
Filters for "medicamento" requests 
"""

from typing import TypeVar, Generic

from .filter import Filter
from ..utils import ConfigModel

T = TypeVar("T")


class Equals(Generic[T]):
    """
    Adds new condition to the conditions dict
    """

    def equals(self, value: T) -> "FilterMedicamentos":
        """
        "equals" because the condition should be equal to the value added.
        """
        self.med: FilterMedicamentos
        self.key: str
        self.med.conditions.update({self.key: value})

        return self.med


class NombreFilter(Equals[str]):
    """
    Condition related to "nombre"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "nombre"


class LabFilter(Equals[str]):
    """
    Condition related to "laboratorio"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "laboratorio"


class PactivoOneFilter(Equals[str]):
    """
    Condition related to "practiv1"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "practiv1"


class PactivoTwoFilter(Equals[str]):
    """
    Condition related to "practiv2"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "practiv2"


class IDPactivoOneFilter(Equals[int]):
    """
    Condition related to "idpractiv1"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "idpractiv1"


class IDPactivoTwoFilter(Equals[int]):
    """
    Condition related to "idpractiv2"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "idpractiv2"


class CodNacionalFilter(Equals[str]):
    """
    Condition related to "cn"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "cn"


class ATCFilter(Equals[str]):
    """
    Condition related to "atc"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "atc"


class NumRegistroFilter(Equals[str]):
    """
    Condition related to "nregistro"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "nregistro"


class NumeroPactivoFilter(Equals[int]):
    """
    Condition related to "npactiv". Number of "principios activos".
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "npactiv"


class TrianguloFilter(Equals[bool]):
    """
    Condition related to "triangulo"
    True: it has "triangulo"
    False: it does not have "triangulo"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "triangulo"


class HuerfanoFilter(Equals[bool]):
    """
    Condition related to "huerfano"
    True: it is "huerfano"
    False: it is not "huerfano"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "huerfano"


class BiosimilarFilter(Equals[bool]):
    """
    Condition related to "biosimilar"
    True: It is "biosimilar"
    False: It is not "biosimilar"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "biosimilar"


class SustFilter(Equals[int]):
    """
    Condition related to "sust"
    1: Biológicos,
    2: Medicamentos con principios activos de estrecho margen terapéutico,
    3: Medicamentos de especial control médico o con medidas especiales de seguridad,
    4: Medicamentos para el aparato respiratorio administrados por vía inhalatoria,
    5: Medicamentos de estrecho margen terapéutico
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "sust"


class VMPFilter(Equals[str]):
    """
    Condition related to "vmp"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "vmp"


class ComercFilter(Equals[bool]):
    """
    Condition related to "comerc"
    1: it is "comercializado"
    0: it is not "comercializado"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "comerc"


class AutorizadosFilter(Equals[bool]):
    """
    Condition related to "autorizados"
    1: only "autorizados"
    0: only not "autorizados"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "autorizados"


class RecetaFilter(Equals[bool]):
    """
    Condition related to "receta"
    1: with "receta"
    0: without "receta"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "receta"


class EstupefacienteFilter(Equals[bool]):
    """
    Condition related to "estupefaciente"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "estupefaciente"


class PsicotropoFilter(Equals[bool]):
    """
    Condition related to "psicotropo"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "psicotropo"


class EstuopsicoFilter(Equals[bool]):
    """
    Condition related to "estuopsico"
    """

    def __init__(self, med: "FilterMedicamentos") -> None:
        super().__init__()
        self.med = med
        self.key = "estuopsico"


class FilterMedicamentos(Filter):
    """
    "Medicamentos" accepts one or more condition.
    """

    def __init__(self, config: ConfigModel) -> None:
        super().__init__(config)
        self.conditions: dict = {}

    @property
    def nombre(self):
        """
        "Nombre" of the "medicamento".
        """
        return NombreFilter(self)

    @property
    def laboratorio(self):
        """
        "Laboratorio" of the "medicamento".
        """
        return LabFilter(self)

    @property
    def pactivo1(self):
        """
        First "principio activo" of the "medicamento".
        """
        return PactivoOneFilter(self)

    @property
    def pactivo2(self):
        """
        Second "principio activo" of the "medicamento".
        """
        return PactivoTwoFilter(self)

    @property
    def id_pactivo1(self):
        """
        First ID of the "principio activo" of the "medicamento".
        """
        return IDPactivoOneFilter(self)

    @property
    def id_pactivo2(self):
        """
        Second ID of the "principio activo" of the "medicamento".
        """
        return IDPactivoTwoFilter(self)

    @property
    def cod_nacional(self):
        """
        "Código nacional" of the "medicamento".
        """
        return CodNacionalFilter(self)

    @property
    def atc(self):
        """
        "ATC" of the "medicamento".
        """
        return ATCFilter(self)

    @property
    def num_registro(self):
        """
        Add condition to "nregistro"
        """
        return NumRegistroFilter(self)

    @property
    def num_pactivo(self):
        """
        Add condition to "npactiv"
        """
        return NumeroPactivoFilter(self)

    @property
    def triangulo(self):
        """
        Add condition to "triangulo"
        """
        return TrianguloFilter(self)

    @property
    def huerfano(self):
        """
        Add condition to "huerfano"
        """
        return HuerfanoFilter(self)

    @property
    def biosimilar(self):
        """
        Add condition to "biosimilar"
        """
        return BiosimilarFilter(self)

    @property
    def sust(self):
        """
        Add condition to "sust", where:
        1: Biológicos,
        2: Medicamentos con principios activos de estrecho margen terapéutico,
        3: Medicamentos de especial control médico o con medidas especiales de seguridad,
        4: Medicamentos para el aparato respiratorio administrados por vía inhalatoria,
        5: Medicamentos de estrecho margen terapéutico
        """
        return SustFilter(self)

    @property
    def vmp(self):
        """
        Add condition to "vmp"
        """
        return VMPFilter(self)

    @property
    def comercializado(self):
        """
        Add condition to "comerc"
        """
        return ComercFilter(self)

    @property
    def autorizado(self):
        """
        Add condition to "autorizados"
        """
        return AutorizadosFilter(self)

    @property
    def receta(self):
        """
        Add condition to "receta"
        """
        return RecetaFilter(self)

    @property
    def estupefaciente(self):
        """
        Add condition to "estupefaciente"
        """
        return EstupefacienteFilter(self)

    @property
    def psicotropo(self):
        """
        Add condition to "psicotropo"
        """
        return PsicotropoFilter(self)

    @property
    def estupsico(self):
        """
        Add condition to "estupsico"
        """
        return EstuopsicoFilter(self)
