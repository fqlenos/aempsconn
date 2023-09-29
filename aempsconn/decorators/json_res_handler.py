"""
Decorator to handle JSON responses.
"""

from functools import wraps
from requests.exceptions import JSONDecodeError
from logging import Logger
import traceback


def json_res_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
            if isinstance(self.config.logger, Logger):
                self.config.logger.info(
                    f"JSON-decoding responses from: '{self.endpoint}'."
                )

            return res

        except KeyError as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error(
                    "The request may be wrong. 'Resultados' should be in the response."
                )
                self.config.logger.error(e)

        except JSONDecodeError as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error("HTTP Response seems to be empty.")
                self.config.logger.error(e)

        except Exception as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.critical(f"Unhandled error: {e}")
                self.config.logger.critical(traceback.format_exc())

    return wrapper
