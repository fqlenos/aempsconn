"""Module for the base module that will inherit the AEMPSconn modules."""

from abc import ABC, abstractmethod
from typing import Any, Generator, Generic, NoReturn, TypeVar

from ..filter import Filterable
from ..request_handler import ReqHandler

T = TypeVar("T", bound=Filterable)
R = TypeVar("R")


class BaseModule(ABC, Generic[T, R]):

    def __init__(self, req_handler: ReqHandler) -> None:
        super().__init__()
        self._req_handler: ReqHandler = req_handler

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """Get the base endpoint of the module."""
        ...

    @abstractmethod
    def parse_result(self, data: dict[str, Any]) -> R:
        """Parse a single result dict to the desired return type.

        Args:
            data (dict[str, Any]): Data to parse into a specific object.

        Returns:
            R: The data parsed to the specific type object.

        """
        ...

    def get(self, filter: T) -> Generator[R, None, None]:
        """Return the base object.

        Args:
            filter (T): The filter to apply to the query.

        Yields:
            R: The result parsed.
        """
        for result in self._req_handler.get(
            endpoint=self.endpoint,
            params=filter.payload,
        ):
            yield self.parse_result(data=result)

    def post(self) -> NoReturn:
        raise NotImplementedError("The POST method is not implemented yet")
