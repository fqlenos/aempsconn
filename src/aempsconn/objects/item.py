"""Module for the 'Item' object."""

from pydantic import BaseModel, Field


class ItemModel(BaseModel):
    item_id: int = Field(alias="id")
    nombre: str
    codigo: str | None = None
