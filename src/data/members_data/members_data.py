from pathlib import Path

from pandas import read_csv, read_excel

from src.data.members_data.member.member_interface import IMember
from src.data.members_data.members_data_interface import IMembersData


class MembersData(IMembersData):
    def __init__(self, members_file_path: Path) -> None:
        self._members_file_path = members_file_path

    def get_member_info(self, stl_id: str) -> IMember:
        return super().get_member_info(stl_id)
