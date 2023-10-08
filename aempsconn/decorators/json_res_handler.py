"""
Decorator to handle JSON responses.
"""

from functools import wraps

from requests.exceptions import JSONDecodeError

from ..errors import JSONDecodeFailure, JSONKeyFailure, UnhandledError


def json_res_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
            if self.config.logger is not None:
                self.config.logger.info(
                    f"JSON-decoding responses from: '{self.endpoint}'."
                )

            return res

        except KeyError as e:
            if self.config.logger is not None:
                self.config.logger.error(e)

            raise JSONKeyFailure()

        except JSONDecodeError as e:
            if self.config.logger is not None:
                self.config.logger.error(e)

            raise JSONDecodeFailure()

    return wrapper
