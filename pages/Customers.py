import streamlit as st
import pandas as pd

st.title("👥 Customer Segmentation")

df = pd.read_csv("data/customer_segments.csv")

cluster_names = {
    0: "VIP",
    1: "Regular",
    2: "At Risk"
}

df["Segment"] = df["Cluster"].map(cluster_names)

st.dataframe(
    df[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "Segment"
        ]
    ].head(20)
)

st.subheader("Customer Segments")

st.bar_chart(
    df["Segment"].value_counts()
)