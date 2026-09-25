
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from scipy.spatial.distance import euclidean

def k_means_inertias(df):
    k_values = range(1, 11)  # Test 1 to 10 clusters
    inertias = []  # Store within-cluster sum of squares

    for k in k_values:
        if k == 1:
            # For k=1, calculate total variance (all points in one cluster)
            total_variance = np.sum(np.var(df, axis=0)) * len(df)
            inertias.append(total_variance)
        else:
            # For k>1, use standard k-means inertia
            kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans_temp.fit(df)  # Use first 3 PCs
            inertias.append(kmeans_temp.inertia_)
    return k_values,inertias

def fit_k_means(df, clusters):
    kmeans = KMeans(n_clusters=clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df)
    return kmeans, labels

def evaluate_k_means(df):
    df_subtype = df['BRCA_Subtype_PAM50']
    ari = adjusted_rand_score(df["cluster"]+1, df_subtype)
    nmi = normalized_mutual_info_score(df["cluster"]+1, df_subtype)
    crosstab = pd.crosstab(df["cluster"]+1, df_subtype)
    return {
        "ARI": ari,
        "NMI": nmi,
        "crosstab": crosstab
    }

def nearest_centroid_patient(scores, k_means_model,n_pcs=2):
    centroids = k_means_model.cluster_centers_[:, :n_pcs]
    point = scores.loc[0, [f"PC{i+1}" for i in range(n_pcs)]].to_numpy()
    distances = {i: euclidean(point, c) for i, c in enumerate(centroids)}
    nearest = min(distances, key=distances.get)
    return distances, nearest