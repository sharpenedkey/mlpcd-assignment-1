import numpy as np


def generate_data(dim, k, n_per_cluster, radius, cluster_dim, has_noise, n_noise):
    """
    Function to generate synthetic clustered data.
    
    The method shall generate a dataset of dimensonality dim,
    where each dimension has the value range [0, 100]. 

    The dataset shall contain k clusters, each with n_per_cluster
    data points. The clusters will either be in full-space or sub-space
    depending on the value of cluster_dim.

    The distance function is the Euclidean distance.

    For each cluster, if cluster_dim < dim, the cluster will be
    recognizable only in the cluster_dim dimensions. The relevant dimensions
    will be randomly selected. In the non-relevant dimensions, the 
    objects are randomly distributed within the range [0, 100].

    Additionally, the dataset may contain noise if has_noise is True.
    The noise will be generated as n_noise data points randomly distributed
    in the full space.

    Inputs:
    - dim: int, number of dimensions of the dataset
    - k: int, number of clusters
    - n_per_cluster: int, number of data points per cluster
    - radius: float, radius of the clusters
    - cluster_dim: int, number of dimensions in which the clusters are recognizable
    - has_noise: bool, whether the dataset contains noise
    - n_noise: int, number of noise data points

    Returns:
    - data: np.array, shape (n, dim), the synthetic dataset
    """
    # Test of a force push
    data = np.random.rand(100, 2)
    return data