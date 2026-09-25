import pandas as pd
import numpy as np

from BRCASubtype_clustering import fit_k_means, nearest_centroid_patient

def test_nearest_centroid_patient():
    df = np.array([[1, 2], [2, 3], [21, 22], [23,24],  [-10,-11], [-12,-13]])
    kmeans_df, labels_df = fit_k_means(df, clusters=3)

    scores = pd.DataFrame({"PC1": [1.5], "PC2": [2.5]})
    scores_patient, kmeans_patient = nearest_centroid_patient(scores, kmeans_df, n_pcs=2)

    assert len(scores_patient) == 3
    assert k_means_patient in range(3)
    assert scores_patient[k_means_patient] == min(scores_patient.values())
