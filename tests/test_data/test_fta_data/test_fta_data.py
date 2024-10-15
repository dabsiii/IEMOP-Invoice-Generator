from pathlib import Path

from src.data.fta_data.fta_data import FTAData


def test_fta_data():
    fta_file = Path(
        "C:\\Users\\energy.trading\\Desktop\\IEMOP-Invoice-Generator\\tests\samples\\final transaction reports\\PPEI_TS-WF-211F-0019908.csv"
    )
    fta = FTAData(fta_file_path=fta_file)
    print(fta._dataframe.columns)
    print(fta.get_stl_ids())

    for i in fta.get_stl_ids():
        print(i)
