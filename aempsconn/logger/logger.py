from .formatter import Formatter

import logging


def logger(level: int = logging.INFO) -> logging.Logger:
    """
    Define the logging with specific format and specific level.

        Returns:
            logging (logging.Logger): logging module

    """
    logger = logging.getLogger("aempsconn")
    logger.setLevel(level=level)
    stdout = logging.StreamHandler()
    stdout.setLevel(0)
    stdout.setFormatter(Formatter())
    logger.addHandler(stdout)

    return logger
