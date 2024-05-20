"""Module for filtering the 'Medicamento'."""

from ..utils.filter import Filterable, Integer, Text


class CodNacional(Text["MedicamentoFilter"]):
    def __init__(self, instance: "MedicamentoFilter") -> None:
        key: str = "cn"
        super().__init__(key=key, instance=instance)


class NumRegistro(Text["MedicamentoFilter"]):
    def __init__(self, instance: "MedicamentoFilter") -> None:
        key: str = "nregistro"
        super().__init__(key=key, instance=instance)


class Pagina(Integer["MedicamentoFilter"]):
    def __init__(self, instance: "MedicamentoFilter") -> None:
        key: str = "pagina"
        super().__init__(key=key, instance=instance)


class MedicamentoFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def cn(self) -> "CodNacional":
        return CodNacional(instance=self)

    @property
    def nregistro(self) -> "NumRegistro":
        return NumRegistro(instance=self)

    @property
    def pagina(self) -> "Pagina":
        return Pagina(instance=self)
