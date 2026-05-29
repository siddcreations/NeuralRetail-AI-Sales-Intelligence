import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load Customer Segments Data
df = pd.read_csv("data/customer_segments.csv")


# Create Churn Label
# Customers with high Recency are assumed churned

median_recency = df["Recency"].median()

df["Churn"] = (
    df["Recency"] > median_recency
).astype(int)


# Features
X = df[
    ["Recency", "Frequency", "Monetary"]
]

# Target
y = df["Churn"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)


# Prediction
y_pred = model.predict(X_test)


# Accuracy
acc = accuracy_score(
    y_test,
    y_pred
)

print(f"\nAccuracy: {acc:.4f}")


# Save Model
joblib.dump(
    model,
    "models/churn_model.pkl"
)

print(
    "\nChurn Model Saved Successfully!"
)