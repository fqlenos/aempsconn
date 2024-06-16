"""Module for filtering the 'Materiales'."""

from ..utils.filter import Filterable, Text


class NumRegistro(Text["MaterialFilter"]):
    def __init__(self, instance: "MaterialFilter") -> None:
        key: str = "nregistro"
        super().__init__(key=key, instance=instance)


class MaterialFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def nregistro(self) -> "NumRegistro":
        return NumRegistro(instance=self)
