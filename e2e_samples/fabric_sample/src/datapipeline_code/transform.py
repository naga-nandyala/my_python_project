import os

import pandas as pd

data_folder_path = os.path.join(os.path.dirname(__file__), "../data")
file_name = f"{data_folder_path}/employee.csv"


def read_csv(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["salary"] = df["salary"] * 1.1
    return df
