"""Module for filtering the 'Medicamentos'."""

from ..utils.filter import Bool, Filterable, Integer, Text


class Nombre(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key = "nombre"
        super().__init__(key=key, instance=instance)


class Lab(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key = "laboratorio"
        super().__init__(key=key, instance=instance)


class PActivo1(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key = "practiv1"
        super().__init__(key=key, instance=instance)


class PActivo2(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key = "practiv2"
        super().__init__(key=key, instance=instance)


class IdPActivo1(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key = "idpractiv1"
        super().__init__(key=key, instance=instance)


class IdPActivo2(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key = "idpractiv2"
        super().__init__(key=key, instance=instance)


class CodNacional(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "cn"
        super().__init__(key=key, instance=instance)


class Atc(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "atc"
        super().__init__(key=key, instance=instance)


class NumRegistro(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "nregistro"
        super().__init__(key=key, instance=instance)


class NumPActivos(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "npactiv"
        super().__init__(key=key, instance=instance)


class Triangulo(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "triangulo"
        super().__init__(key=key, instance=instance)


class Huerfano(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "huerfano"
        super().__init__(key=key, instance=instance)


class Biosimilar(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "biosimilar"
        super().__init__(key=key, instance=instance)


class Sust(Integer["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "sust"
        super().__init__(key=key, instance=instance)


class Vmp(Text["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "vmp"
        super().__init__(key=key, instance=instance)


class Comerc(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "comerc"
        super().__init__(key=key, instance=instance)


class Autorizados(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "autorizados"
        super().__init__(key=key, instance=instance)


class Receta(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "receta"
        super().__init__(key=key, instance=instance)


class Estupefaciente(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "estupefaciente"
        super().__init__(key=key, instance=instance)


class Psicotropo(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "psicotropo"
        super().__init__(key=key, instance=instance)


class Estuopsico(Bool["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "estuopsico"
        super().__init__(key=key, instance=instance)


class Pagina(Integer["MedicamentosFilter"]):
    def __init__(self, instance: "MedicamentosFilter") -> None:
        key: str = "pagina"
        super().__init__(key=key, instance=instance)


class MedicamentosFilter(Filterable):

    def __init__(self) -> None:
        super().__init__()

    @property
    def nombre(self) -> "Nombre":
        return Nombre(instance=self)

    @property
    def laboratorio(self) -> "Lab":
        return Lab(instance=self)

    @property
    def pactivo1(self) -> "PActivo1":
        return PActivo1(instance=self)

    @property
    def pactivo2(self) -> "PActivo2":
        return PActivo2(instance=self)

    @property
    def id_pactivo1(self) -> "IdPActivo1":
        return IdPActivo1(instance=self)

    @property
    def id_pactivo2(self) -> "IdPActivo2":
        return IdPActivo2(instance=self)

    @property
    def cod_nacional(self) -> "CodNacional":
        return CodNacional(self)

    @property
    def atc(self) -> "Atc":
        return Atc(instance=self)

    @property
    def num_registro(self) -> "NumRegistro":
        return NumRegistro(instance=self)

    @property
    def num_pactivo(self) -> "NumPActivos":
        return NumPActivos(instance=self)

    @property
    def triangulo(self) -> "Triangulo":
        return Triangulo(instance=self)

    @property
    def huerfano(self) -> "Huerfano":
        return Huerfano(instance=self)

    @property
    def biosimilar(self) -> "Biosimilar":
        return Biosimilar(self)

    @property
    def sust(self) -> "Sust":
        return Sust(instance=self)

    @property
    def vmp(self) -> "Vmp":
        return Vmp(instance=self)

    @property
    def comercializado(self) -> "Comerc":
        return Comerc(instance=self)

    @property
    def autorizado(self) -> "Autorizados":
        return Autorizados(instance=self)

    @property
    def receta(self) -> "Receta":
        return Receta(instance=self)

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
