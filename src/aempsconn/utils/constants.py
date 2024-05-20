"""Module for the constants of the AEMPSconn."""

from enum import StrEnum
from typing import cast

from pydantic import ConfigDict, HttpUrl


class HttpMethods(StrEnum):
    """Http Methods allowed in the library."""

    GET = "GET"
    POST = "POST"


CONFIG_DICT = ConfigDict(
    use_enum_values=True,
    from_attributes=True,
    validate_assignment=True,
    arbitrary_types_allowed=True,
)  # Configuration Dict for the Pydantic's Validate Calls.


CIMA_URL: HttpUrl = cast(
    HttpUrl, "https://cima.aemps.es/cima/rest"
)  # CIMA Rest API endpoint for the requests.


# Constant values for the Retry Http Adapter.
TOTAL_RETRIES: int = 3
BACKOFF_FACTOR: float = 0.1
BACKOFF_MAX: int = 180

# Constant values for the Request
TOTAL_VALUES = "totalFilas"
PAGE_SIZE = "tamanioPagina"
RESULTS = "resultados"
PAGE = "pagina"
