import pandas as pd
import numpy as np


def load_path(filepath: str):
    brca_cancer = pd.read_csv(filepath)
    return brca_cancer



def filter_genes(df: pd.DataFrame, n=5, seed=None):
    if seed is not None:
        np.random.seed(seed)
    genes = np.random.choice(df.columns[1:-1], size=n, replace=False)
    cols = list(genes) + ["BRCA_Subtype_PAM50"]
    return df[cols]


def filter_transform_genes(df: pd.DataFrame):
    brca_numeric = df.select_dtypes(include='number')

    #Finding columns with non-zero sum and variance
    keep_cols = (brca_numeric.abs().sum() != 0) & (brca_numeric.var() != 0)
    sel_cols = brca_numeric.columns[keep_cols]
    out = df[list(sel_cols) + ["BRCA_Subtype_PAM50"]].copy()
    out[sel_cols] =  np.log1p(df[sel_cols])

    return out,list(sel_cols)

def new_patient(df: pd.DataFrame, cols_to_use: list):
    new_patient_data = df[cols_to_use].copy()
    new_patient_data = np.log1p(new_patient_data)

    new_patient_mean = new_patient_data.iloc[0, :].mean()

    new_patient_data = new_patient_data - new_patient_mean 

    return new_patient_data
