"""Module for the 'Videos' object."""

from datetime import datetime

from pydantic import BaseModel, HttpUrl


class VideoModel(BaseModel):
    titulo: str
    url: HttpUrl
    video: HttpUrl
    fecha: datetime
