"""
Data type for 'Medicamento'.
"""

from pydantic import BaseModel
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    """
    'if' blocks that are never True on runtime (running your code) but they are used by code analysis (IDEs) to highlight the types.
    """
    from .atc import ATCModel
    from .elemento import ElementoModel
    from .estado import EstadoModel
    from .excipiente import ExcipienteModel
    from .foto import FotoModel
    from .documento import DocumentoModel
    from .pactivo import PActivoModel
    from .presentacion import PresentacionModel


class MedicamentoBaseModel(BaseModel):
    """
    Pydantic model for the base data type: Medicamento.

    Arguments:
        nregistro (str): número de registro del Medicamento
        nombre (str): nombre del Medicamento
        labtitular (str): laboratorio titular del Medicamento
        estado (EstadoModel): estado del Medicamento
        cpresc (str): condiciones de prescripción del Medicamento
        comerc (bool): indica si tiene alguna presentación comercializada
        receta (bool): indica si el Medicamento necesita una receta médica
        conduc (bool): indica si el Medicamento afecta o no a la conducción
        triangulo (bool): indica si el Medicamento tiene asociado el triángulo negro
        huerfano (bool): indica si el Medicamento está considerado como medicamento huérfano
        biosimilar (bool): indica si el Medicamento está considerado como biosimilar
        nosustituible (ElementoModel): TBD
        psum (bool): indica si el Medicamento tiene problemas de suministro
        ema (bool): indica si el Medicamento se ha registrado por procedimiento centralizado (EMA) o no
        notas (bool): indica si existen notas asociadas al Medicamento
        materialesInf (bool): indica si existen materiales informáticos de seguridad asociados al Medicamento
        docs (list[DocumentoModel]): lista de documentos asociados al Medicamento
        fotos (list[FotoModel]): lista de imágenes asociadas al Medicamento
        viasAdministracion (list[ElementoModel]): lista de las vías de administración para las que esté autorizado el Medicamento
        formaFarmaceutica (ElementoModel): forma farmacéutica
        formaFarmaceuticaSimplificada (ElementoModel): forma farmacéutica simplificada
        dosis (str): dosis del principio activo. En el caso de que haya más de un principio activo, aparecerán separados por “/” y en el mismo orden que los principios activos
    """

    nregistro: str
    nombre: str
    labtitular: str
    estado: "EstadoModel"
    cpresc: str
    comerc: bool
    receta: bool
    conduc: bool
    triangulo: bool
    huerfano: bool
    biosimilar: bool
    nosustituible: "ElementoModel"
    psum: bool
    ema: bool
    notas: bool
    materialesInf: bool
    docs: list["DocumentoModel"]
    fotos: list["FotoModel"] | None = None
    viasAdministracion: list["ElementoModel"]
    formaFarmaceutica: "ElementoModel"
    formaFarmaceuticaSimplificada: "ElementoModel"
    dosis: str


class MedicamentoModel(MedicamentoBaseModel):
    """
    Pydantic model for data type: Medicamento.

        Arguments:
            nregistro (str): número de registro del Medicamento
            nombre (str): nombre del Medicamento
            labtitular (str): laboratorio titular del Medicamento
            estado (EstadoModel): estado del Medicamento
            cpresc (str): condiciones de prescripción del Medicamento
            comerc (bool): indica si tiene alguna presentación comercializada
            receta (bool): indica si el Medicamento necesita una receta médica
            conduc (bool): indica si el Medicamento afecta o no a la conducción
            triangulo (bool): indica si el Medicamento tiene asociado el triángulo negro
            huerfano (bool): indica si el Medicamento está considerado como medicamento huérfano
            biosimilar (bool): indica si el Medicamento está considerado como biosimilar
            nosustituible (ElementoModel): TBD
            psum (bool): indica si el Medicamento tiene problemas de suministro
            ema (bool): indica si el Medicamento se ha registrado por procedimiento centralizado (EMA) o no
            notas (bool): indica si existen notas asociadas al Medicamento
            materialesInf (bool): indica si existen materiales informáticos de seguridad asociados al Medicamento
            docs (list[DocumentoModel]): lista de documentos asociados al Medicamento
            fotos (list[FotoModel]): lista de imágenes asociadas al Medicamento
            viasAdministracion (list[ElementoModel]): lista de las vías de administración para las que esté autorizado el Medicamento
            formaFarmaceutica (ElementoModel): forma farmacéutica
            formaFarmaceuticaSimplificada (ElementoModel): forma farmacéutica simplificada
            dosis (str): dosis del principio activo. En el caso de que haya más de un principio activo, aparecerán separados por “/” y mismo orden que los principios activos
            pactivos (str): lista de principios activos separada por comas. Solo aparece el nombre
            atcs (list[ATCModel]): lista de códigos de ATC asociados al Medicamento
            principiosActivos (list[PActivoModel]): lista de los principios activos del Medicamento
            excipientes (list[ExcipienteModel]): lista de excipientes del Medicamento
            presentaciones (list[PresentacionModel]): lista de presentaciones del Medicamento
    """

    pactivos: str
    atcs: list["ATCModel"]
    principiosActivos: list["PActivoModel"]
    excipientes: list["ExcipienteModel"] | None = None
    presentaciones: list["PresentacionModel"]


class ListMedicamentoModel(MedicamentoBaseModel):
    """
    Pydantic model for data type: List of Medicamento.

        Arguments:
            nregistro (str): número de registro del Medicamento
            nombre (str): nombre del Medicamento
            labtitular (str): laboratorio titular del Medicamento
            estado (EstadoModel): estado del Medicamento
            cpresc (str): condiciones de prescripción del Medicamento
            comerc (bool): indica si tiene alguna presentación comercializada
            receta (bool): indica si el Medicamento necesita una receta médica
            conduc (bool): indica si el Medicamento afecta o no a la conducción
            triangulo (bool): indica si el Medicamento tiene asociado el triángulo negro
            huerfano (bool): indica si el Medicamento está considerado como medicamento huérfano
            biosimilar (bool): indica si el Medicamento está considerado como biosimilar
            nosustituible (ElementoModel): TBD
            psum (bool): indica si el Medicamento tiene problemas de suministro
            ema (bool): indica si el Medicamento se ha registrado por procedimiento centralizado (EMA) o no
            notas (bool): indica si existen notas asociadas al Medicamento
            materialesInf (bool): indica si existen materiales informáticos de seguridad asociados al Medicamento
            docs (list[DocumentoModel]): lista de documentos asociados al Medicamento
            fotos (list[FotoModel]): lista de imágenes asociadas al Medicamento
            viasAdministracion (list[ElementoModel]): lista de las vías de administración para las que esté autorizado el Medicamento
            formaFarmaceutica (ElementoModel): forma farmacéutica
            formaFarmaceuticaSimplificada (ElementoModel): forma farmacéutica simplificada
            dosis (str): dosis del principio activo. En el caso de que haya más de un principio activo, aparecerán separados por “/” y mismo orden que los principios activos
    """

    pass
