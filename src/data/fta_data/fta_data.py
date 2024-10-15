from src.data.fta_data.fta_data_interface import IFTAData


class FTAData(IFTAData):

    def get_stl_ids(self):
        return super().get_stl_ids()

    def get_allocation_info(self, stl_id):
        return super().get_allocation_info(stl_id)
