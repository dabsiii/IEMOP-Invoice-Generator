from src.data.fta_data.allocation.allocation_interface import IAllocation


class Allocation(IAllocation):

    def stl_id(self):
        return super().stl_id()

    def transaction_reference(self):
        return super().transaction_reference()

    def vatabale_sales(self):
        return super().vatabale_sales()

    def zero_rated_sales(self):
        return super().zero_rated_sales()

    def zero_rate_ecozone_sales(self):
        return super().zero_rate_ecozone_sales()

    def vat_on_sales(self):
        return super().vat_on_sales()

    def ewt(self):
        return super().ewt()
