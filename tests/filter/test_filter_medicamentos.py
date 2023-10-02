from unittest import TestCase
from unittest.mock import patch, Mock
from aempsconn.filter import (
    FilterMedicamentos,
    NombreFilter,
    LabFilter,
    PactivoOneFilter,
    PactivoTwoFilter,
    IDPactivoOneFilter,
    IDPactivoTwoFilter,
    CodNacionalFilter,
    ATCFilter,
    NumRegistroFilter,
    NumeroPactivoFilter,
    TrianguloFilter,
    HuerfanoFilter,
    BiosimilarFilter,
    SustFilter,
    VMPFilter,
    ComercFilter,
    AutorizadosFilter,
    RecetaFilter,
    EstupefacienteFilter,
    PsicotropoFilter,
    EstuopsicoFilter,
)


class TestFilterMedicamentos(TestCase):
    def test_nombre_filter(self):
        self._test_filter_class(NombreFilter, "nombre", "Medicamento A")

    def test_lab_filter(self):
        self._test_filter_class(LabFilter, "laboratorio", "Laboratorio A")

    def test_pactivo_one_filter(self):
        self._test_filter_class(PactivoOneFilter, "practiv1", "Principio Activo A")

    def test_pactivo_two_filter(self):
        self._test_filter_class(PactivoTwoFilter, "practiv2", "Principio Activo B")

    def test_id_pactivo_one_filter(self):
        self._test_filter_class(IDPactivoOneFilter, "idpractiv1", 1)

    def test_id_pactivo_two_filter(self):
        self._test_filter_class(IDPactivoTwoFilter, "idpractiv2", 2)

    def test_cod_nacional_filter(self):
        self._test_filter_class(CodNacionalFilter, "cn", "12345")

    def test_atc_filter(self):
        self._test_filter_class(ATCFilter, "atc", "A01AA01")

    def test_num_registro_filter(self):
        self._test_filter_class(NumRegistroFilter, "nregistro", "67890")

    def test_numero_pactivo_filter(self):
        self._test_filter_class(NumeroPactivoFilter, "npactiv", 3)

    def test_triangulo_filter(self):
        self._test_filter_class(TrianguloFilter, "triangulo", True)

    def test_huerfano_filter(self):
        self._test_filter_class(HuerfanoFilter, "huerfano", False)

    def test_biosimilar_filter(self):
        self._test_filter_class(BiosimilarFilter, "biosimilar", True)

    def test_sust_filter(self):
        self._test_filter_class(SustFilter, "sust", 2)

    def test_vmp_filter(self):
        self._test_filter_class(VMPFilter, "vmp", "VMP001")

    def test_comerc_filter(self):
        self._test_filter_class(ComercFilter, "comerc", False)

    def test_autorizados_filter(self):
        self._test_filter_class(AutorizadosFilter, "autorizados", True)

    def test_receta_filter(self):
        self._test_filter_class(RecetaFilter, "receta", False)

    def test_estupefaciente_filter(self):
        self._test_filter_class(EstupefacienteFilter, "estupefaciente", True)

    def test_psicotropo_filter(self):
        self._test_filter_class(PsicotropoFilter, "psicotropo", False)

    def test_estuopsico_filter(self):
        self._test_filter_class(EstuopsicoFilter, "estuopsico", True)

    def _test_filter_class(self, filter_class, key, value):
        # Creates the FilterMedicamento object with the ConfigModel Mock
        mock_config = Mock()
        filter_medicamentos = FilterMedicamentos(config=mock_config)

        # Calls the method of the selected filter (CodNacionalFilter or NumRegistroFilter)
        filter_instance = filter_class(filter_medicamentos)

        # Check if the object is successfully created
        self.assertIsInstance(filter_instance, filter_class)
        self.assertEqual(filter_instance.med, filter_medicamentos)
        self.assertEqual(filter_instance.key, key)

        # Checks if the filter has been updated with the correct value types
        result_filter = filter_instance.equals(value)
        self.assertIsInstance(result_filter, FilterMedicamentos)
        self.assertEqual(result_filter.conditions, {key: value})
