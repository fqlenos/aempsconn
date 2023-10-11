"""
Filters for "medicamento" requests 
"""

from typing import Generic, TypeVar

from aempsconn.utils import ConfigModel

from ..utils import ConfigModel
from .filter import Filter

T = TypeVar("T")


class Equals(Generic[T]):
    """
    Adds new condition to the conditions dict
    """

    med: "FilterMedicamento"
    key: str

    def equals(self, value: T) -> "FilterMedicamento":
        """
        "equals" because the condition should be equal to the value added.
        """
        new_meds = FilterMedicamento(config=self.med.config)
        new_meds.conditions.update({self.key: value})

        return new_meds


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
    def cod_nacional(self) -> CodNacionalFilter:
        """
        Add condition to "cn"
        """
        return CodNacionalFilter(self)

    @property
    def num_registro(self) -> NumRegistroFilter:
        """
        Add condition to "nregistro"
        """
        return NumRegistroFilter(self)
