from unittest import TestCase
from unittest.mock import Mock

from aempsconn.filter import CodNacionalFilter, FilterMedicamento, NumRegistroFilter


class TestFilterMedicamento(TestCase):
    def test_cod_nacional_filter(self):
        self._test_filter_class(CodNacionalFilter, "cn", "12345")

    def test_num_registro_filter(self):
        self._test_filter_class(NumRegistroFilter, "nregistro", "67890")

    def _test_filter_class(self, filter_class, key, value):
        # Creates the FilterMedicamento object with the ConfigModel Mock
        mock_config = Mock()
        filter_medicamentos = FilterMedicamento(config=mock_config)

        # Calls the method of the selected filter (CodNacionalFilter or NumRegistroFilter)
        filter_instance = filter_class(filter_medicamentos)

        # Check if the object is successfully created
        self.assertIsInstance(filter_instance, filter_class)
        self.assertEqual(filter_instance.med, filter_medicamentos)
        self.assertEqual(filter_instance.key, key)

        # Checks if the filter has been updated with the correct value types
        result_filter = filter_instance.equals(value)
        self.assertIsInstance(result_filter, FilterMedicamento)
        self.assertEqual(result_filter.conditions, {key: value})
