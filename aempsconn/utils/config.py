"""
Defines the configuration needed for activate AEMPSconn.
"""

from logging import Logger

from pydantic import BaseModel, ConfigDict, HttpUrl


class ModelConfig(BaseModel):
    """
    BaseModel generic class ready for inheritance.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ConfigModel(ModelConfig):
    """
    Basic configuration model.
    Needed for orchestrate and normalize all the requests, responses and logs.

    Arguments:
        url (HttpUrl):
        timeout (int): set timeout to requests
        proxies (dict): add proxies to requests
        logger (Logger | None): add custom logging
    """

    url: HttpUrl
    timeout: int
    proxies: dict
    logger: Logger | None = None
