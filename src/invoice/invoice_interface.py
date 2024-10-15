from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal


class IInvoice(ABC):
    @abstractmethod
    def cash_sales(self) -> Decimal: ...

    @abstractmethod
    def charge_sales(self) -> Decimal: ...

    @abstractmethod
    def date(self) -> datetime: ...

    @abstractmethod
    def registered_name(self) -> str: ...

    @abstractmethod
    def tin_number(self) -> str: ...

    @abstractmethod
    def business_address(self) -> str: ...
