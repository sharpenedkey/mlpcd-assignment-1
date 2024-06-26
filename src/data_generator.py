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

    # Initialize the data array
    data = np.zeros((k * n_per_cluster + n_noise, dim))

    # Generate the clusters
    for i in range(k):
        # Generate the cluster center
        relevant_dimensions = np.random.choice(range(dim), cluster_dim, replace=False)
        center = np.random.rand(cluster_dim) * 100

        # Generate the cluster
        for j in range(n_per_cluster):
            # Generate the data point within the cluster
            point = center + np.random.randn(cluster_dim) * radius
            point = np.clip(point, 0, 100)  # Clip point values to [0, 100]

            # Assign the point to relevant dimensions
            data[i * n_per_cluster + j, relevant_dimensions] = point

            # Generate random values for non-relevant dimensions
            non_relevant_dimensions = [d for d in range(dim) if d not in relevant_dimensions]
            data[i * n_per_cluster + j, non_relevant_dimensions] = np.random.rand(len(non_relevant_dimensions)) * 100

    # Generate the noise
    if has_noise:
        data[-n_noise:, :] = np.random.rand(n_noise, dim) * 100

    return data