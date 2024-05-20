"""Module for the Request Handler of the AEMPSconn."""

import concurrent.futures
from concurrent.futures import Future
from typing import Any, Collection, Generator

from pydantic import HttpUrl, validate_call
from requests import Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from .constants import (
    BACKOFF_FACTOR,
    BACKOFF_MAX,
    CIMA_URL,
    CONFIG_DICT,
    PAGE,
    PAGE_SIZE,
    RESULTS,
    TOTAL_RETRIES,
    TOTAL_VALUES,
    HttpMethods,
)
from .hof import http_res_handler


class ReqHandler(Session):
    """Custom Request Handler for the AEMPSconn requests.

    Args:
        url (HttpUrl | None) AEMPS URL to make the requests to. Defaults to: None.
        retry (bool). Whether to automatic retry the requests or not. Defaults to: True.
        status_force_list (Collection[int] | None) Status codes to retry if `retry=True`. Defaults to: None.
        proxies (dict[str, str] | None) Custom proxies to add to the request. Defaults to: None.
    """

    @validate_call(config=CONFIG_DICT)
    def __init__(
        self,
        url: HttpUrl | None = None,
        retry: bool = True,
        status_force_list: Collection[int] | None = None,
        proxies: dict[str, str] | None = None,
    ) -> None:
        super().__init__()
        self.__url: HttpUrl | None = url
        self.__retry: bool = retry
        self.__status_force_list: Collection[int] | None = status_force_list
        self.__proxies: dict[str, str] | None = proxies

    @property
    def url(self) -> str:
        if self.__url is None:
            return str(object=CIMA_URL)
        return str(object=self.__url)

    @property
    def status_force_list(self) -> Collection[int]:
        if self.__status_force_list is None:
            return range(500, 600)

        return self.__status_force_list

    @property
    def retries(self) -> Retry | int:
        if self.__retry is True:
            return Retry(
                total=TOTAL_RETRIES,
                backoff_factor=BACKOFF_FACTOR,
                backoff_max=BACKOFF_MAX,
                status_forcelist=self.status_force_list,
            )
        return 0

    def _prepare_session(self):
        self.mount("http://", HTTPAdapter(max_retries=self.retries))
        self.mount("https://", HTTPAdapter(max_retries=self.retries))
        self.headers.update(
            {
                "Accept": "application/json",
                "Content_Type": "application/json",
            }
        )

    @http_res_handler
    @validate_call(config=CONFIG_DICT)
    def _raw_request(
        self,
        method: HttpMethods,
        endpoint: str,
        params: list[tuple[str, str]] | None,
        **kwargs,
    ) -> dict[str, Any]:
        response: Response = self.request(
            url=f"{str(object=self.url)}/{endpoint}",
            method=method,
            proxies=self.__proxies,
            params=params,
            **kwargs,
        )

        return response.json()

    @validate_call(config=CONFIG_DICT)
    def _request(
        self,
        method: HttpMethods,
        endpoint: str,
        max_workers: int,
        params: list[tuple[str, str]] | None,
        **kwargs,
    ) -> Generator[dict[str, Any], None, None]:
        self._prepare_session()

        initial_response: dict[str, Any] = self._raw_request(
            method=method, endpoint=endpoint, params=params, **kwargs
        )
        if initial_response.get(RESULTS, None) is None:
            yield initial_response

        else:
            for result in initial_response[RESULTS]:
                yield result

        total_values: int | None = initial_response.get(TOTAL_VALUES)
        page_size: int | None = initial_response.get(PAGE_SIZE)

        if total_values is None or page_size is None:
            return

        total_pages: int = (total_values // page_size) + 1

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures: list[Future[dict]] = [
                executor.submit(
                    self._raw_request,
                    method,
                    endpoint,
                    (
                        params + [(PAGE, str(page))]
                        if isinstance(params, list)
                        else [(PAGE, str(page))]
                    ),
                    **kwargs,
                )
                for page in range(2, total_pages + 1)
            ]

            for future in concurrent.futures.as_completed(fs=futures):
                page_response: dict = future.result()
                for result in page_response.get(RESULTS, {}):
                    yield result

    @validate_call(config=CONFIG_DICT)
    def get(
        self,
        endpoint: str,
        params: list[tuple[str, str]],
        max_workers: int = 10,
        **kwargs,
    ) -> Generator[dict[str, Any], None, None]:
        for result in self._request(
            method=HttpMethods.GET,
            endpoint=endpoint,
            params=params,
            max_workers=max_workers,
            **kwargs,
        ):
            yield result
