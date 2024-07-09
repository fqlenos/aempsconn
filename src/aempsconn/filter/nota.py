"""Module for filtering the 'Notas'."""

from ..utils.filter import Filterable, Text


class NumRegistro(Text["NotaFilter"]):
    def __init__(self, instance: "NotaFilter") -> None:
        key: str = "nregistro"
        super().__init__(key=key, instance=instance)


class NotaFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def nregistro(self) -> "NumRegistro":
        return NumRegistro(instance=self)
