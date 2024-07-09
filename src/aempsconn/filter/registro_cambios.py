"""Module for filtering the 'Registro Cambios'."""

from ..utils.filter import Date, Filterable, Integer, Text


class Fecha(Date["RegistroCambiosFilter"]):
    def __init__(self, instance: "RegistroCambiosFilter") -> None:
        key: str = "fecha"
        super().__init__(key=key, instance=instance)


class NumRegistro(Text["RegistroCambiosFilter"]):
    def __init__(self, instance: "RegistroCambiosFilter") -> None:
        key: str = "nregistro"
        super().__init__(key=key, instance=instance)


class Pagina(Integer["RegistroCambiosFilter"]):
    def __init__(self, instance: "RegistroCambiosFilter") -> None:
        key: str = "pagina"
        super().__init__(key=key, instance=instance)


class RegistroCambiosFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def fecha(self) -> "Fecha":
        return Fecha(instance=self)

    @property
    def nregistro(self) -> "NumRegistro":
        return NumRegistro(instance=self)

    @property
    def pagina(self) -> "Pagina":
        return Pagina(instance=self)
