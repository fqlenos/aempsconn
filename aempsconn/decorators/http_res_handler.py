"""
Decorator to handle HTTP responses.
"""

from functools import wraps

from requests.exceptions import HTTPError, ProxyError, RequestException, Timeout

from ..errors import (
    HTTPFailure,
    ProxyFailure,
    RequestFailure,
    TimeoutFailure,
    UnhandledError,
)


def http_res_handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
            if self.config.logger is not None:
                self.config.logger.info(f"Request to '{self.endpoint}' successful")
                self.config.logger.info(res.text)

            raise UnhandledError()
            return res

        except Timeout as e:
            if self.config.logger is not None:
                self.config.logger.error(e)

            raise TimeoutFailure()

        except HTTPError as e:
            if self.config.logger is not None:
                self.config.logger.error(e)

            raise HTTPFailure()

        except ProxyError as e:
            if self.config.logger is not None:
                self.config.logger.error(e)

            raise ProxyFailure()

        except RequestException as e:
            if self.config.logger is not None:
                self.config.logger.error(e)

            raise RequestFailure()

        except Exception as e:
            if self.config.logger is not None:
                self.config.logger.critical(f"Unhandled error: {e}")

            raise UnhandledError()

    return wrapper
