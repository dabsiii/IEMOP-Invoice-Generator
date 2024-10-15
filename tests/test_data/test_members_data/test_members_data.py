from pathlib import Path

from src.data.members_data.members_data import MembersData


def test_members_data():
    file_path = Path(
        "C:\\Users\\energy.trading\\Desktop\\IEMOP-Invoice-Generator\\tests\\samples\\members database\\WESM Participants Database.xlsx"
    )
    mem = MembersData(members_file_path=file_path)
