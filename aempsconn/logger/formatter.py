import logging


class Formatter(logging.Formatter):
    """
    Stablish my custom logging format
    """

    grey: str = "\x1b[38;20m"
    cyan: str = "\x1b[36;20m"
    yellow: str = "\x1b[33;20m"
    red: str = "\x1b[31;20m"
    bold_red: str = "\x1b[31;1m"
    reset: str = "\x1b[0m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )  # type: ignore

    FORMATS = {
        logging.DEBUG: grey + format + reset,  # type: ignore
        logging.INFO: cyan + format + reset,  # type: ignore
        logging.WARNING: yellow + format + reset,  # type: ignore
        logging.ERROR: red + format + reset,  # type: ignore
        logging.CRITICAL: bold_red + format + reset,  # type: ignore
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)

        return formatter.format(record)
