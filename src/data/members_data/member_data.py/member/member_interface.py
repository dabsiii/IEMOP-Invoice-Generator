from abc import ABC, abstractmethod


class IMember(ABC):

    @abstractmethod
    def name_shortname(self) -> str: ...

    @abstractmethod
    def stl_id(self) -> str: ...
