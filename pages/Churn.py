import streamlit as st
import pandas as pd

st.title("⚠️ Churn Analysis")

df = pd.read_csv(
    "data/customer_segments.csv"
)

median_recency = df["Recency"].median()

df["Churn"] = (
    df["Recency"] > median_recency
).astype(int)

st.write(
    "Churn Distribution"
)

st.bar_chart(
    df["Churn"].value_counts()
)