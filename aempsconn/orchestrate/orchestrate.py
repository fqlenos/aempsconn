"""
Module in charge of orchestrating all existing modules in the project.
"""

from logging import Logger
from pydantic import ValidationError
import sys
from pydantic import HttpUrl

from ..utils import ConfigModel, BASEURL
from ..modules import cima, Base


class Orchestrate:
    def __init__(
        self,
        url: HttpUrl = HttpUrl(BASEURL),
        timeout: int = 180,
        proxies: dict = {},
        logger: Logger | None = None,
    ) -> None:
        """
        Module in charge of orchestrating existing modules.

        Arguments:
            url (HttpUrl): base URL for the CIMA Rest API
            timeout (int): set timeout for the API requests
            proxies (dict): add proxies to the API requests
            logger (Logger | None): select your logging format if wanted
        """

        try:
            config = ConfigModel(
                logger=logger,
                proxies=proxies,
                timeout=timeout,
                url=url,
            )

        except ValidationError as e:
            print(str(e) + "\n")
            print("Check wether the variables are correctly typed.")
            sys.exit()

        # Initialize existing modules with current configuration.
        # Related to CIMA
        self.base = Base(config=config)
        self.medicamento = cima.Medicamento(config=config)
        self.medicamentos = cima.Medicamentos(config=config)
        self.presentacion = cima.Presentacion(config=config)
        self.presentaciones = cima.Presentaciones(config=config)

        # Related to CIMA Vet

        # Related to REEC
