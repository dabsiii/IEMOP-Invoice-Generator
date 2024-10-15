from abc import ABC, abstractmethod

from src.data.fta_data.fta_data_interface import IFTAData


class IFTADataFactory(ABC):
    @abstractmethod
    def create_fta_data(self) -> IFTAData: ...
