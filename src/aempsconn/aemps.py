"""Module for orchestrate all the modules of the AEMPSconn."""

from typing import Collection

from pydantic import HttpUrl

from .modules import Medicamento, Medicamentos, Presentaciones, Vmpp
from .utils.request_handler import ReqHandler


class AempsConn:

    def __init__(
        self,
        url: HttpUrl | None = None,
        retry: bool = True,
        status_force_list: Collection[int] | None = None,
        proxies: dict[str, str] | None = None,
    ) -> None:
        self.__url: HttpUrl | None = url
        self.__retry: bool = retry
        self.__status_force_list: Collection[int] | None = status_force_list
        self.__proxies: dict[str, str] | None = proxies

    @property
    def __req_handler(self) -> ReqHandler:
        return ReqHandler(
            url=self.__url,
            retry=self.__retry,
            status_force_list=self.__status_force_list,
            proxies=self.__proxies,
        )

    @property
    def medicamento(self) -> Medicamento:
        return Medicamento(req_handler=self.__req_handler)

    @property
    def medicamentos(self) -> Medicamentos:
        return Medicamentos(req_handler=self.__req_handler)

    @property
    def presentaciones(self) -> Presentaciones:
        return Presentaciones(req_handler=self.__req_handler)

    @property
    def vmpp(self) -> Vmpp:
        return Vmpp(req_handler=self.__req_handler)
