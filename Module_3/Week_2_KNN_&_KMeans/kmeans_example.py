from kmeans_class import KMeans
import numpy as np


data = np.array([[2.0, 3.0, 1.5],
                 [3.0, 3.5, 2.0],
                 [3.5, 3.0, 2.5],
                 [8.0, 8.0, 7.5],
                 [8.5, 8.5, 8.0],
                 [9.0, 8.0, 8.5],
                 [1.0, 2.0, 1.0],
                 [1.5, 2.5, 1.5]])
kmeans_model = KMeans(k=3)
kmeans_model.fit(data)