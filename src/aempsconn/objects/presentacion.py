"""Module for the 'Presentacion' object."""

from pydantic import BaseModel

from .documento import DocumentoModel
from .estado import EstadoModel


class PresentacionModel(BaseModel):
    cn: str
    nombre: str
    estado: "EstadoModel"
    comerc: bool
    psum: bool


class PresentacionesModel:
    nregistro: str
    cn: str
    nombre: str
    pactivos: str
    labtitular: str
    estado: "EstadoModel"
    cpresc: str
    comerc: bool
    conduc: bool
    triangulo: bool
    huerfano: bool
    ema: bool
    psum: bool
    docs: list["DocumentoModel"]
    notas: bool
