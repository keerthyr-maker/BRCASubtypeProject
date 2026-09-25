
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.preprocessing import StandardScaler

def pca_fit(df, scale, n_svd_components=50, n_pca_components=10, random_state=42):
    X = df.drop(columns=["BRCA_Subtype_PAM50"])
    scaler = None
    if scale:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

    svd = TruncatedSVD(n_components=n_svd_components, random_state=random_state)
    X_svd = svd.fit_transform(X)

    pca = PCA(n_components=n_pca_components)
    pca_scores = pca.fit_transform(X_svd)
    return scaler, svd, pca, pca_scores
    

def project_new_sample(df: pd.DataFrame, scaler, svd, pca):
    if scaler is not None:
        df = scaler.transform(df)
    # Project into the same SVD space
    x_patient_svd = svd.transform(df)
    # Project into the same PCA space
    x_patient_pca = np.dot(x_patient_svd, pca.components_.T)  # shape: (1, n_components)
    return x_patient_pca
 