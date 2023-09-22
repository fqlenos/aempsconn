from .formatter import Formatter

import logging


def logger() -> logging.Logger:
    """
    Define the logging with specific format and specific level.

        Returns:
            logging (logging.Logger): logging module

    """
    logger = logging.getLogger("aempsconn")
    logger.setLevel(logging.INFO)
    stdout = logging.StreamHandler()
    stdout.setLevel(0)
    stdout.setFormatter(Formatter())
    logger.addHandler(stdout)

    return logger
