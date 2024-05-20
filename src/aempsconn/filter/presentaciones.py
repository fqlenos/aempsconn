"""Module for filtering the 'Presentaciones'."""

from ..utils.filter import Bool, Filterable, Integer, Text


class CodNacional(Text["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "cn"
        super().__init__(key=key, instance=instance)


class NumRegistro(Text["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "nregistro"
        super().__init__(key=key, instance=instance)


class Vmp(Text["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "vmp"
        super().__init__(key=key, instance=instance)


class Vmpp(Text["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "vmpp"
        super().__init__(key=key, instance=instance)


class IdPActivo1(Text["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key = "idpractiv1"
        super().__init__(key=key, instance=instance)


class Comerc(Bool["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "comerc"
        super().__init__(key=key, instance=instance)


class Estupefaciente(Bool["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "estupefaciente"
        super().__init__(key=key, instance=instance)


class Psicotropo(Bool["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "psicotropo"
        super().__init__(key=key, instance=instance)


class Estuopsico(Bool["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "estuopsico"
        super().__init__(key=key, instance=instance)


class Pagina(Integer["PresentacionesFilter"]):
    def __init__(self, instance: "PresentacionesFilter") -> None:
        key: str = "pagina"
        super().__init__(key=key, instance=instance)


class PresentacionesFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def cn(self) -> "CodNacional":
        return CodNacional(instance=self)

    @property
    def nregistro(self) -> "NumRegistro":
        return NumRegistro(instance=self)

    @property
    def vmp(self) -> "Vmp":
        return Vmp(instance=self)

    @property
    def vmpp(self) -> "Vmpp":
        return Vmpp(instance=self)

    @property
    def id_pactivo1(self) -> "IdPActivo1":
        return IdPActivo1(instance=self)

    @property
    def comercializado(self) -> "Comerc":
        return Comerc(instance=self)

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
    def pagina(self) -> "Pagina":
        return Pagina(instance=self)
