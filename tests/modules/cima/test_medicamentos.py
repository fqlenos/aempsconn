"""
Test medicamentos module
"""

from unittest import TestCase

from pydantic import HttpUrl

from aempsconn.modules.cima import Medicamentos
from aempsconn.utils import ConfigModel


class TestMedicamento(TestCase):
    def test_constructor(self):
        med = Medicamentos(
            config=ConfigModel(url=HttpUrl("https://test.com"), timeout=180, proxies={})
        )
        assert med.get_specific_endpoint() == "/medicamentos"
