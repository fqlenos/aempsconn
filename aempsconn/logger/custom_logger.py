from logging import Logger, StreamHandler
from .formatter import Formatter


class CustomLogger(Logger):
    """
    Custom logger for aempsconn
    """

    def __init__(self, name: str = "aempsconn", level: int = 0) -> None:
        super().__init__(name, level)
        stdout = StreamHandler()
        stdout.setLevel(0)
        stdout.setFormatter(Formatter())
        super().addHandler(stdout)
