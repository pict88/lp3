import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, preprocessing, decomposition

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
df.head()


features = ['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'MSRP']
#X = df[features].fillna(df[features].median())
X=df[features]


# Select numeric features
scaler = preprocessing.StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)


# 3. Elbow Method to find optimal K
wcss = []
for k in range(1, 11):
    km = cluster.KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()


# 4. Fit K-Means (K=3)
km = cluster.KMeans(n_clusters=3, random_state=42, n_init=10)

km.fit(X_scaled)          # find cluster centers
df['Cluster'] = km.predict(X_scaled)   # assign cluster number


# 5. PCA for 2D visualization (4D -> 2D)
pca = decomposition.PCA(2)
pca = pca.fit_transform(X_scaled)

plt.scatter(pca[:, 0], pca[:, 1], c=df['Cluster'])
plt.title("K-Means Clusters (PCA Reduced)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Cluster")
plt.show()


# 6. Display cluster counts
print("Cluster Counts:\n", df['Cluster'].value_counts())
