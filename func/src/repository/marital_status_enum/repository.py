from abc import ABC
from typing import List, Tuple

from func.src.core.interfaces.repository.marital_status_enum.interface import IMaritalStatusEnumRepository
from func.src.repository.enum_marital_status_cache.repository import EnumMaritalStatusCacheRepository
from func.src.repository.base_repository.oracle.repository import OracleBaseRepository


class MaritalStatusEnumRepository(IMaritalStatusEnumRepository, ABC):

    enum_query = """
            SELECT DESC_EST_CIVIL as marital_status
            FROM CORRWIN.TSCDXEST_CIVIL
        """

    @classmethod
    def get_marital_status_enum(cls) -> List[Tuple]:
        sql = cls.enum_query
        result = cls._get_marital_status_cached_enum(sql)
        return result

    @classmethod
    def _get_marital_status_cached_enum(cls, query: str) -> List[Tuple]:
        if cached_enum := EnumMaritalStatusCacheRepository.get_enum_marital_status():
            return cached_enum

        enum_values = OracleBaseRepository.query(sql=query)
        EnumMaritalStatusCacheRepository.save_enum_marital_status(enum_values)
        return enum_values
