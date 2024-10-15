from pathlib import Path
from typing import List

from pandas import read_csv, read_excel

from src.data.fta_data.allocation.allocation_factory_interface import IAllocationFactory
from src.data.fta_data.allocation.allocation_interface import IAllocation
from src.data.fta_data.fta_data_interface import IFTAData


class FTAData(IFTAData):

    def __init__(self, fta_file_path: Path) -> None:
        self._fta_file_path = fta_file_path
        self._dataframe = read_csv(fta_file_path, header=1)

    def _set_allocation_factory(self, allocation_factory: IAllocationFactory) -> None:
        self._allocation_factory = allocation_factory

    def get_stl_ids(self) -> List[str]:
        return self._dataframe["STL_ID"].to_list()

    def get_allocation_info(self, stl_id: str) -> IAllocation:
        pass
