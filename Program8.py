import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture 

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
print(X.head())

X_norm = preprocessing.normalize(X)

y = pd.DataFrame(iris.target)
y.columns = ['Targets']

# K-Means Clustering
model = KMeans(n_clusters = 3)
model.fit(X_norm)

# EM Model
gmm = GaussianMixture(n_components = 3)
gmm.fit(X_norm)
gmm_y = gmm.predict(X_norm)

plt.figure(figsize = (14, 14))
colormap = np.array(['red', 'blue', 'green'])

#Plotting all data

# Real Clusters
plt.subplot(2, 2, 1)
plt.scatter(X.Petal_Length, X.Petal_Width, c = colormap[y.Targets], s = 40)
plt.title('Real Clusters')
plt.xlabel('Petal Lenght')
plt.ylabel('Petal Width')

# K-Means Output
plt.subplot(2, 2, 2)
plt.scatter(X.Petal_Length, X.Petal_Width, c = colormap[model.labels_], s = 40)
plt.title('K-Means Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# EM Output
plt.subplot(2, 2, 3)
plt.scatter(X.Petal_Length, X.Petal_Width, c = colormap[gmm_y], s = 40)
plt.title('GMM Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.show()