"""Module for the 'Item' object."""

from pydantic.dataclasses import dataclass


@dataclass
class ItemModel:
    id: int
    nombre: str
    codigo: str | None = None
