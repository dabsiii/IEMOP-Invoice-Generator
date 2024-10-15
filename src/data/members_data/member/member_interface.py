from abc import ABC, abstractmethod


class IMember(ABC):

    @abstractmethod
    def name_shortname(self) -> str: ...

    @abstractmethod
    def stl_id(self) -> str: ...

    @abstractmethod
    def billing_id(self) -> str: ...

    @abstractmethod
    def bussiness_style(self) -> str: ...

    @abstractmethod
    def tin_number(self) -> str: ...

    @abstractmethod
    def bir_address(self) -> str: ...
