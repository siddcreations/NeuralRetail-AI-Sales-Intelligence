import streamlit as st
import pandas as pd

st.title("📈 Demand Forecast")

forecast = pd.read_csv(
    "data/forecast.csv"
)

st.dataframe(
    forecast.tail(30)
)

st.line_chart(
    forecast["yhat"]
)