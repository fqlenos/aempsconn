"""Module for the 'Foto' object."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, HttpUrl


class FotoModel(BaseModel):
    tipo: Literal["materialas", "formafarmac"]
    url: HttpUrl
    fecha: datetime
