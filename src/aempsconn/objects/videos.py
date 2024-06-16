"""Module for the 'Videos' object."""

from datetime import datetime

from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


@dataclass
class VideoModel:
    titulo: str
    url: HttpUrl
    video: HttpUrl
    fecha: datetime
