"""
Test medicamento module
"""

from unittest import TestCase

from pydantic import HttpUrl

from aempsconn.modules.cima import Medicamento
from aempsconn.utils import ConfigModel


class TestMedicamento(TestCase):
    def test_constructor(self):
        med = Medicamento(
            config=ConfigModel(url=HttpUrl("https://test.com"), timeout=180, proxies={})
        )
        assert med.get_specific_endpoint() == "/medicamento"
