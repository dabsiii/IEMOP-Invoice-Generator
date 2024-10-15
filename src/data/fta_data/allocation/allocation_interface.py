from abc import ABC, abstractmethod
from decimal import Decimal


class IAllocation(ABC):

    @abstractmethod
    def stl_id(self) -> str: ...

    @abstractmethod
    def transaction_reference(self) -> str: ...

    @abstractmethod
    def vatabale_sales(self) -> Decimal: ...

    @abstractmethod
    def zero_rated_sales(self) -> Decimal: ...

    @abstractmethod
    def zero_rate_ecozone_sales(self) -> Decimal: ...

    @abstractmethod
    def vat_on_sales(self) -> Decimal: ...

    @abstractmethod
    def ewt(self) -> Decimal: ...
