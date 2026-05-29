import pandas as pd
from prophet import Prophet
import joblib

# Load Dataset
df = pd.read_excel("data/Online_Retail.xlsx")

# Convert Date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Total Sales
df["Sales"] = df["Quantity"] * df["UnitPrice"]

# Daily Sales
daily_sales = (
    df.groupby(df["InvoiceDate"].dt.date)["Sales"]
    .sum()
    .reset_index()
)

daily_sales.columns = ["ds", "y"]

# Prophet Model
model = Prophet()

model.fit(daily_sales)

# Future Dates
future = model.make_future_dataframe(
    periods=30
)

forecast = model.predict(future)

# Save Forecast
forecast[
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
].to_csv(
    "data/forecast.csv",
    index=False
)

# Save Model
joblib.dump(
    model,
    "models/forecast_model.pkl"
)

print("Forecast Model Saved Successfully!")
print("forecast.csv generated!")