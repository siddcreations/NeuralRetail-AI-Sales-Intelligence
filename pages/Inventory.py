import streamlit as st

st.title("📦 Inventory Optimization")

current_stock = st.number_input(
    "Current Stock",
    value=100
)

predicted_demand = st.number_input(
    "Predicted Demand",
    value=150
)

reorder = max(
    predicted_demand - current_stock,
    0
)

st.metric(
    "Recommended Reorder Quantity",
    reorder
)