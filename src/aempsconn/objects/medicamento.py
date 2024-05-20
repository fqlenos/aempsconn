"""Module for the 'Medicamento' object."""

from pydantic.dataclasses import dataclass

from .atc import ATCModel
from .documento import DocumentoModel
from .estado import EstadoModel
from .excipiente import ExcipienteModel
from .foto import FotoModel
from .item import ItemModel
from .presentacion import PresentacionModel
from .principio_activo import PActivoModel


@dataclass
class MedicamentoBase:
    nregistro: str
    nombre: str
    labtitular: str
    estado: "EstadoModel"
    cpresc: str
    comerc: bool
    receta: bool
    conduc: bool
    triangulo: bool
    huerfano: bool
    biosimilar: bool
    nosustituible: "ItemModel"
    psum: bool
    ema: bool
    notas: bool
    materialesInf: bool
    docs: list["DocumentoModel"]
    viasAdministracion: list["ItemModel"]
    formaFarmaceutica: "ItemModel"
    formaFarmaceuticaSimplificada: "ItemModel"
    dosis: str
    fotos: list["FotoModel"] | None = None


@dataclass(kw_only=True)
class MedicamentoModel(MedicamentoBase):
    pactivos: str
    atcs: list["ATCModel"]
    principiosActivos: list["PActivoModel"]
    presentaciones: list["PresentacionModel"]
    excipientes: list["ExcipienteModel"] | None = None


@dataclass
class MedicamentosModel(MedicamentoBase):
    pass
