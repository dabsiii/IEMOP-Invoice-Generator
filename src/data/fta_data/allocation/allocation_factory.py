from src.data.fta_data.allocation.allocation import Allocation
from src.data.fta_data.allocation.allocation_factory_interface import IAllocationFactory


class AllocationFactory(IAllocationFactory):
    def create_allocation_from_dataframe(self) -> Allocation:
        return super().create_allocation_from_dataframe()

    def create_allocation_from_series(self) -> Allocation:
        return super().create_allocation_from_series()
