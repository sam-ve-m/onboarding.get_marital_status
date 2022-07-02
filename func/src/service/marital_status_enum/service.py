from etria_logger import Gladsheim

from src.core.interfaces.service.marital_status_enum.interface import (
    IMaritalStatusEnumService,
)
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.marital_status_enum.repository import MaritalStatusEnumRepository


class MaritalStatusEnumService(IMaritalStatusEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = MaritalStatusEnumRepository.get_marital_status_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response
