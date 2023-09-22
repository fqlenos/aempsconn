from .atc import ATCModel
from .documento import DocumentoModel
from .elemento import ElementoModel
from .estado import EstadoModel
from .excipiente import ExcipienteModel
from .pactivo import PActivoModel
from .foto import FotoModel
from .medicamento import MedicamentoModel, ListMedicamentoModel
from .presentacion import PresentacionModel
from .seccion import SeccionModel
from .suministro import SuministroModel

"""
Avoiding circular imports
"""
MedicamentoModel.model_rebuild()
ListMedicamentoModel.model_rebuild()
PresentacionModel.model_rebuild()
