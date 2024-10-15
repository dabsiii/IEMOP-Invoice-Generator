from abc import ABC, abstractmethod
from pathlib import Path

from src.data.members_data.member.member_interface import IMember


class IMembersData(ABC):

    @abstractmethod
    def get_member_info(self, stl_id: str) -> IMember: ...
