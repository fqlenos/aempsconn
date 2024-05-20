"""Module for the 'Descripción Clínica' object."""

from pydantic.dataclasses import dataclass


@dataclass
class DescripcionClinicaModel:
    vmp: str
    vmpDesc: str
    vmpp: str
    vmppDesc: str
    presComerc: int
