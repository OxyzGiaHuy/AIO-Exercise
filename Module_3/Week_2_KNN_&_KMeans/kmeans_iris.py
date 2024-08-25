from kmeans_class import KMeans
from sklearn.datasets import load_iris


iris_dataset = load_iris()
data = iris_dataset.data[:, :2]
kmeans_model = KMeans(k=5)
kmeans_model.fit(data)
