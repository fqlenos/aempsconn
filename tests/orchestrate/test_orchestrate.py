"""
Test orchestrate
"""

from unittest import TestCase

from aempsconn.orchestrate import Orchestrate


class TestOrchestrate(TestCase):
    def test_constructor(self):
        orch = Orchestrate()
        assert orch.medicamento.conditions == {}
        assert orch.medicamentos.conditions == {}
        assert orch.filter_medicamento.conditions == {}
        assert orch.filter_medicamentos.conditions == {}
