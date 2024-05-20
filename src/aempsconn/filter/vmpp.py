"""Module for filtering the 'Vmpp'."""

from ..utils.filter import Bool, Filterable, Integer, Text


class PActivo1(Text["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "practiv1"
        super().__init__(key=key, instance=instance)


class IdPActivo1(Text["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "idpractiv1"
        super().__init__(key=key, instance=instance)


class Dosis(Text["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "dosis"
        super().__init__(key=key, instance=instance)


class Forma(Text["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "forma"
        super().__init__(key=key, instance=instance)


class Atc(Text["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "atc"
        super().__init__(key=key, instance=instance)


class Nombre(Text["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "nombre"
        super().__init__(key=key, instance=instance)


class ModoArbol(Bool["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key = "modoArbol"
        super().__init__(key=key, instance=instance)


class Pagina(Integer["VmppFilter"]):
    def __init__(self, instance: "VmppFilter") -> None:
        key: str = "pagina"
        super().__init__(key=key, instance=instance)


class VmppFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def pactivo1(self) -> "PActivo1":
        return PActivo1(instance=self)

    @property
    def id_pactivo1(self) -> "IdPActivo1":
        return IdPActivo1(instance=self)

    @property
    def dosis(self) -> "Dosis":
        return Dosis(instance=self)

    @property
    def forma(self) -> "Forma":
        return Forma(instance=self)

    @property
    def atc(self) -> "Atc":
        return Atc(instance=self)

    @property
    def nombre(self) -> "Nombre":
        return Nombre(instance=self)

    @property
    def modo_arbol(self) -> "ModoArbol":
        return ModoArbol(instance=self)

    @property
    def pagina(self) -> "Pagina":
        return Pagina(instance=self)
