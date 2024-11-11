import pathlib
import pandas as pd
from pathlib import Path
if __name__ == '__main__':
    csv_file = Path(__file__).parent.parent.joinpath('tutorialpkg/data','paralympics_events_raw.csv')
    excel_file = Path(__file__).parent.parent.joinpath('tutorialpkg/data','paralympics_all_raw.xlsx')

    csv_df = pd.read_csv(csv_file)
    excel_df = pd.read_excel(excel_file)
    pd.read_csv(excel_df, sheetname = "medal_standings")
    #csv_df_2 = pd.read_csv(csv_file, sheetname = "medal_standings")