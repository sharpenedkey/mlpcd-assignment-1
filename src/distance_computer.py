from sklearn.metrics import pairwise_distances
import numpy as np

def farthest_neighbor_distance(dataset, metric):
    distances = pairwise_distances(dataset, metric=metric)
    max_distances = np.max(distances, axis=1)
    return np.mean(max_distances)

def nearest_neighbor_distance(dataset, metric):
    distances = pairwise_distances(dataset, metric=metric)
    np.fill_diagonal(distances, np.inf)
    min_distances = np.min(distances, axis=1)
    return np.mean(min_distances)

def fnd_nnd_ratio(dataset, metric):
    return farthest_neighbor_distance(dataset, metric) / nearest_neighbor_distance(dataset, metric)