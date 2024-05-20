"""Module for the filtering."""

from typing import Any

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Filter:
    key: str
    value: Any

    @property
    def payload(self) -> tuple[str, str]:
        if isinstance(self.value, bool):
            self.value = int(self.value)
        return (self.key, str(object=self.value))


@dataclass
class Filterable:
    query: list[Filter] = Field(default_factory=list)

    @property
    def payload(self) -> list[tuple[str, str]]:
        return [filter.payload for filter in self.query]
