from abc import ABC, abstractmethod
from typing import List

from src.data.fta_data.allocation.allocation_interface import IAllocation


class IFTAData(ABC):
    @abstractmethod
    def get_stl_ids(self) -> List[str]: ...

    @abstractmethod
    def get_allocation_info(self, stl_id: str) -> IAllocation: ...
