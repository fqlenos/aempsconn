"""Module for filtering the 'Maestras'."""

from ..utils.filter import Bool, Filterable, Integer, Text


class Maestra(Integer["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key = "maestra"
        super().__init__(key=key, instance=instance)


class Nombre(Text["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key = "nombre"
        super().__init__(key=key, instance=instance)


class Id(Integer["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key = "id"
        super().__init__(key=key, instance=instance)


class Codigo(Text["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key = "codigo"
        super().__init__(key=key, instance=instance)


class Estupefaciente(Bool["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key: str = "estupefaciente"
        super().__init__(key=key, instance=instance)


class Psicotropo(Bool["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key: str = "psicotropo"
        super().__init__(key=key, instance=instance)


class Estuopsico(Bool["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key: str = "estuopsico"
        super().__init__(key=key, instance=instance)


class EnUso(Bool["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key: str = "enuso"
        super().__init__(key=key, instance=instance)


class Pagina(Integer["MaestrasFilter"]):
    def __init__(self, instance: "MaestrasFilter") -> None:
        key: str = "pagina"
        super().__init__(key=key, instance=instance)


class MaestrasFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def maestra(self) -> "Maestra":
        return Maestra(instance=self)

    @property
    def nombre(self) -> "Nombre":
        return Nombre(instance=self)

    @property
    def id(self) -> "Id":
        return Id(instance=self)

    @property
    def codigo(self) -> "Codigo":
        return Codigo(instance=self)

    @property
    def estupefaciente(self) -> "Estupefaciente":
        return Estupefaciente(instance=self)

    @property
    def psicotropo(self) -> "Psicotropo":
        return Psicotropo(instance=self)

    @property
    def estuopsico(self) -> "Estuopsico":
        return Estuopsico(instance=self)

    @property
    def en_uso(self) -> "EnUso":
        return EnUso(instance=self)

    @property
    def pagina(self) -> "Pagina":
        return Pagina(instance=self)
