
import matplotlib.pyplot as plt
import seaborn as sns

def counts_of_patients(file):
    brca_cancer_subtypes = file['BRCA_Subtype_PAM50']

    plt.bar(brca_cancer_subtypes.value_counts().index, brca_cancer_subtypes.value_counts().values)
    plt.xlabel('BRCA Subtypes')
    plt.ylabel('Patient Count')
    plt.title('Counts of Patients with certain BRCA Subtypes')
    plt.show()

def plot_hist_genes(brca_genes):
    palette = {
    "LumA": "blue",
    "LumB": "green",
    "Basal": "red",
    "Her2": "orange"
    }
    for col in brca_genes.drop(columns=["BRCA_Subtype_PAM50"]).columns:
        plt.figure(figsize=(6,4))
        sns.histplot(data=brca_genes, x=col, hue="BRCA_Subtype_PAM50", element="step", kde=False,palette=palette)
        plt.title(f"Histogram of {col} by BRCA Subtype")
        plt.ylabel("Density")
        plt.tight_layout()
        plt.show()

def scree_plot(pca):
    pve = pca.explained_variance_ratio_
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(pve) + 1), pve, 'bo-', linewidth=2, markersize=8)  # Plot PVE vs PC number
    plt.xlabel('Principal Component')
    plt.ylabel('Proportion of Variance Explained')
    plt.title('Scree Plot - Variance Explained by Each PC')
    plt.grid(True, alpha=0.3)
    plt.show()

def elbow_plot(k_values,inertias):
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, inertias, 'ro-', linewidth=2, markersize=8)
    plt.xlabel('Number of clusters K')
    plt.ylabel('Total within-clusters sum of squares')
    plt.title('Elbow Method for PCA Clustering (using 4 PCs)')

    for i, (k, inertia) in enumerate(zip(k_values, inertias)):
        plt.annotate(f'k={k}\n{inertia:.0f}', (k, inertia),
                    textcoords="offset points", xytext=(0,15), ha='center', fontsize=8)

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_clusters(pcs):

    sns.scatterplot(
        data=pcs,
        x="PC1",
        y="PC2",
        hue="BRCA_Subtype_PAM50",
        style="cluster",
        s=100,
        alpha=0.7
    )

def plot_clusters_centroids(pcs, kmeans, new_point=None):
    plot_clusters(pcs)

    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=200, marker='o', label='Centroids')

    if new_point is not None:
        plt.scatter(new_point[0], new_point[1], c='black', s=150, marker='X', label='New Patient')

    plt.legend()
    plt.show()