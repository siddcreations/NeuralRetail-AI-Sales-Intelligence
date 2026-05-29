import pandas as pd
import joblib

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# Load RFM Data
rfm = pd.read_csv("data/rfm.csv")


# Scaling
scaler = StandardScaler()

scaled_data = scaler.fit_transform(
    rfm[["Recency", "Frequency", "Monetary"]]
)


# KMeans Model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(
    scaled_data
)


# Cluster Summary
print("\nCluster Summary\n")

print(
    rfm.groupby("Cluster")[
        ["Recency", "Frequency", "Monetary"]
    ].mean()
)


# Save Model
joblib.dump(
    kmeans,
    "models/segment_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)


# Save Output
rfm.to_csv(
    "data/customer_segments.csv",
    index=False
)

print(
    "\nCustomer Segmentation Completed!"
)