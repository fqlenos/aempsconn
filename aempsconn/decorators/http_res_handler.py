"""
Decorator to handle HTTP responses.
"""

from functools import wraps
from requests.exceptions import (
    HTTPError,
    ProxyError,
    ConnectionError,
    RequestException,
    Timeout,
)
from logging import Logger
import traceback


def http_res_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
            if isinstance(self.config.logger, Logger):
                self.config.logger.info(f"Request to '{self.endpoint}' successful")
                self.config.logger.info(res.text)

            return res

        except Timeout as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error(e)

        except HTTPError as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error(e)

        except ProxyError as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error(e)

        except ConnectionError as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error(e)

        except RequestException as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.error(e)

        except Exception as e:
            if isinstance(self.config.logger, Logger):
                self.config.logger.critical(f"Unhandled error: {e}")
                self.config.logger.critical(traceback.format_exc())

    return wrapper
