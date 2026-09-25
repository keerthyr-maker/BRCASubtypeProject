# Breast Cancer Subtyping

Data Availability: The initial data with all the genes/subjects can be found at this link: 
https://bioconductor.posit.co/packages/release/bioc/vignettes/TCGAbiolinks/inst/doc/subtypes.html?utm_source=chatgpt.com

The specific patient data is in the data folder in this repository.

## Goals of this Project:
1. To discover a method to find the subtype of breast cancer based on gene expression data
2. To test this method on specific patient gene expression data

## Methodology

1. Preprocess the dataset by filtering out genes with zero expression and no variance
2. Perform a log-transform on the gene expression values
3. Perform PCA on the preprocessed dataset (centered but not scaled — scaling was found to obscure cluster separation) to reduce dimensionality
4. Do K-means clustering on the PCs
5. Evaluate the clustering with ARI and NMI scores
6. Perform all the steps on the new patient to find its cluster/subtype


## Results

### ARI Score: 0.2890294318204527
### NMI Score: 0.36744816410771963

### Cross Table
| Cluster | Basal | Her2 | LumA | LumB |
|--------:|------:|-----:|-----:|-----:|
| 0       | 190   | 14   | 0    | 1    |
| 1       | 1     | 46   | 356  | 52   |
| 2       | 0     | 22   | 201  | 158  |
| 3       | 17    | 9    | 71   | 22   |


<img width="583" height="432" alt="ClusterScatterplot" src="https://github.com/user-attachments/assets/454a3495-01d1-4f71-bc85-9038ad45d900" />

### Figure 1: Clusters created from K-means (based on shape)

<img width="583" height="432" alt="NewPatientCluster" src="https://github.com/user-attachments/assets/07811e3a-964c-4e63-bc40-897d5046a4c1" />

### Figure 2: The cluster the new patient would belong to, represented by a point overlayed on the initial clustering

The new patient's expression profile projected closest to the Her2 cluster and the cluster 0 shaped points However, it is also close to the Basal subtype, which
represents cluster 0 most, based on the cross table. So the new patient could be more projected towards the Basal subtype. 



### How to run this project: pip install -r requirements.txt, clone the notebook
- When cloning repo, run the CompilationofCode.ipynb to run all the python files

### How to test the project: pip install -r requirements-dev.txt && pytest

## Next Steps
1. Utilizing more than 2 PCs to improve clustering method
2. Testing on more patients
3. Compare against a true spectral clustering implementation and a supervised baseline (e.g. KNN)
