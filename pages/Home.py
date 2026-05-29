import streamlit as st
import pandas as pd

st.title("🏠 NeuralRetail Dashboard")

df = pd.read_csv("data/customer_segments.csv")

total_customers = len(df)

vip_customers = len(
    df[df["Cluster"] == 0]
)

regular_customers = len(
    df[df["Cluster"] == 1]
)

atrisk_customers = len(
    df[df["Cluster"] == 2]
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        total_customers
    )

with col2:
    st.metric(
        "VIP Customers",
        vip_customers
    )

with col3:
    st.metric(
        "Regular Customers",
        regular_customers
    )

with col4:
    st.metric(
        "At Risk",
        atrisk_customers
    )

st.success(
    "NeuralRetail AI Platform Running Successfully"
)