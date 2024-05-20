"""Module for higher order functions of the AEMPSconn."""

from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

from requests.exceptions import (
    HTTPError,
    JSONDecodeError,
    ProxyError,
    RequestException,
    Timeout,
)

T = TypeVar("T")
P = ParamSpec("P")


def http_res_handler(func: Callable[P, T]) -> Callable[P, T | dict[str, Any]]:

    @wraps(wrapped=func)
    def wrap(*args: P.args, **kwargs: P.kwargs) -> T | dict[str, Any]:
        try:
            return func(*args, **kwargs)

        except JSONDecodeError as e:
            raise e

        except (HTTPError, ProxyError, RequestException, Timeout) as e:
            raise e

        except Exception as e:
            raise e

    return wrap
