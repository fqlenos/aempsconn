"""Module for the set of operators that each type could have."""

from typing import Generic

from .base_operator import Contains, Equals, R, StartsWith


class Text(
    Equals[str, R],
    Contains[str, R],
    StartsWith[str, R],
    Generic[R],
):
    pass


class Bool(
    Equals[bool, R],
    Generic[R],
):
    pass


class Integer(
    Equals[int, R],
    Generic[R],
):
    pass
