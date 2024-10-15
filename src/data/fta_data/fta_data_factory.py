from src.data.fta_data.fta_data import FTAData
from src.data.fta_data.fta_data_factory_interface import IFTADataFactory


class FTADataFactory(IFTADataFactory):
    def create_fta_data(self) -> FTAData:
        return super().create_fta_data()
