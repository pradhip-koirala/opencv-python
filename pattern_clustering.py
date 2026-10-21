from sklearn.datasets import load_digits
from sklearn.cluster import KMeans

x, y = load_digits(return_X_y= True)

kmeans = KMeans(n_clusters=10)
kmeans.fit(x)

print(kmeans.labels_)