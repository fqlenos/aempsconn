"""Module for the base operators of the filtering."""

from typing import Generic, TypeVar

from .filter import Filter, Filterable

T = TypeVar("T")
R = TypeVar("R", bound=Filterable)


class BaseOperator(Generic[T, R]):
    def __init__(
        self,
        key: str,
        instance: R,
    ) -> None:
        super().__init__()
        self.key: str = key
        self.instance: R = instance


class Equals(BaseOperator[T, R], Generic[T, R]):
    def equals(self, value: T) -> R:
        self.instance.query.append(Filter(key=self.key, value=value))
        return self.instance


class Contains(BaseOperator[T, R], Generic[T, R]):
    def contains(self, value: T) -> R:
        self.instance.query.append(Filter(key=self.key, value=f"*{value}*"))
        return self.instance


class StartsWith(BaseOperator[T, R], Generic[T, R]):
    def startswith(self, value: T) -> R:
        self.instance.query.append(Filter(key=self.key, value=f"{value}*"))
        return self.instance
