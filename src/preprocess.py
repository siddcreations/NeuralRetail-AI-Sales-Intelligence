import pandas as pd


def load_data(path):
    df = pd.read_excel(path)

    print("Original Shape:", df.shape)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove null values
    df.dropna(inplace=True)

    print("After Cleaning:", df.shape)

    return df


def create_rfm(df):

    # Convert date column
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Create total price column
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Latest date in dataset
    latest_date = df["InvoiceDate"].max()

    # RFM Calculation
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (latest_date - x.max()).days,
        "InvoiceNo": "count",
        "TotalPrice": "sum"
    })

    rfm.columns = [
        "Recency",
        "Frequency",
        "Monetary"
    ]

    return rfm


if __name__ == "__main__":

    # Load Excel Dataset
    df = load_data("data/Online_Retail.xlsx")

    # Create RFM Table
    rfm = create_rfm(df)

    print("\n===== RFM Dataset =====")
    print(rfm.head())

    # Save RFM Dataset
    rfm.to_csv("data/rfm.csv")

    print("\nrfm.csv saved successfully!")