"""Module for the 'Estado' object."""

from datetime import datetime

from pydantic import field_validator
from pydantic.dataclasses import dataclass


@dataclass
class EstadoModel:
    aut: datetime | None = None
    susp: datetime | None = None
    rev: datetime | None = None

    @field_validator("aut", "susp", "rev", mode="before")
    @classmethod
    def validate_datetime(cls, v: datetime | None) -> datetime | None:
        """Validate the datetime format or None format.

        Args:
            v (datetime | None): The input value.

        Returns:
            datetime | None: Valid return data-type.
        """
        if v is None:
            return None

        try:
            if isinstance(v, int):
                try:
                    return datetime.fromtimestamp(v)

                except (OSError, ValueError):
                    return None

            elif isinstance(v, str):
                try:
                    return datetime.fromisoformat(v)

                except ValueError:
                    return None

            elif isinstance(v, datetime):
                return v

            else:
                return None

        except (ValueError, TypeError):
            return None
