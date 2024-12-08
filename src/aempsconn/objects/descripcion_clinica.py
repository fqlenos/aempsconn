"""Module for the 'Descripción Clínica' object."""

from pydantic import BaseModel


class DescripcionClinicaModel(BaseModel):
    vmp: str
    vmpDesc: str
    vmpp: str
    vmppDesc: str
    presComerc: int
