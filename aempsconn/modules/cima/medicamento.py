"""
Module for getting information related to Medicamentos.
"""

from logging import Logger

from ..base import Base
from ...utils import Endpoint, Keys


class Medicamento(Base):
    def __init__(self, config) -> None:
        super().__init__(config=config)

    def add_condition(self, key: Keys.MEDICAMENTO.value, value) -> None:
        """
        Add a value for each necessary key condition.

        Arguments:
            key: key to assign as condition
            value: value to assign to the previous key condition
        """
        self.conditions.update({key: value})
        if isinstance(self.config.logger, Logger):
            self.config.logger.info(
                f"'{key}' with value: '{value}' successfully added to conditions."
            )

    def get_specific_endpoint(self) -> str:
        """
        Get the specific endpoint for the derived class.
        """
        return Endpoint.MEDICAMENTO.value
