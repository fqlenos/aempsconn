"""
Filters for "medicamento" requests 
"""

from typing import TypeVar, Generic

from aempsconn.utils import ConfigModel

from .filter import Filter
from ..utils import ConfigModel

T = TypeVar("T")


class Equals(Generic[T]):
    """
    Adds new condition to the conditions dict
    """

    def equals(self, value: T) -> "FilterMedicamento":
        """
        "equals" because the condition should be equal to the value added.
        """
        self.med: FilterMedicamento
        self.key: str
        self.med.conditions.clear()  # it clears the dict because only one value is valid.
        self.med.conditions.update({self.key: value})

        return self.med


class CodNacionalFilter(Equals[str]):
    """
    Condition related to "cn"
    """

    def __init__(self, med: "FilterMedicamento") -> None:
        super().__init__()
        self.med = med
        self.key = "cn"


class NumRegistroFilter(Equals[str]):
    """
    Condition related to "nregistro"
    """

    def __init__(self, med: "FilterMedicamento") -> None:
        super().__init__()
        self.med = med
        self.key = "nregistro"


class FilterMedicamento(Filter):
    """
    "Medicamento" only accepts one condition so the last one added will be saved.
    """

    def __init__(self, config: ConfigModel) -> None:
        super().__init__(config)
        self.conditions: dict = {}

    @property
    def cod_nacional(self):
        """
        Add condition to "cn"
        """
        return CodNacionalFilter(self)

    @property
    def num_registro(self):
        """
        Add condition to "nregistro"
        """
        return NumRegistroFilter(self)
