import pandas as pd

def import_data(filepath):
    df = pd.read_csv(filepath)
    print(df.describe())
    return df