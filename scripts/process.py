import pandas as pd

def load_data(path: str = "data/sample.csv") -> pd.DataFrame:
    return pd.read_csv(path)

def add_feature(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["z"] = df["value"] * df["x"]
    return df
