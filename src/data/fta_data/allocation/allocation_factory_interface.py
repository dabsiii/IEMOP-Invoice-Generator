from abc import ABC, abstractmethod

from src.data.fta_data.allocation.allocation_interface import IAllocation


class IAllocationFactory(ABC):
    @abstractmethod
    def create_allocation_from_series(self) -> IAllocation: ...

    @abstractmethod
    def create_allocation_from_dataframe(self) -> IAllocation: ...
