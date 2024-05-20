"""Module for the 'Foto' object."""

from datetime import datetime
from typing import Literal

from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


@dataclass
class FotoModel:
    tipo: Literal["materialas", "formafarmac"]
    url: HttpUrl
    fecha: datetime
