import pandas as pd

def clean_data(df):
    # Rename columns
    df.columns = df.columns.str.strip()

    # Remove cancelled orders (Invoice starting with C)
    df = df[~df["Invoice"].astype(str).str.startswith("C")]

    # Drop missing CustomerID
    df = df.dropna(subset=["Customer ID"])

    # Convert datatypes
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Quantity"] = df["Quantity"].astype(int)
    df["Price"] = df["Price"].astype(float)

    # Remove negative or zero values
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

    # Revenue calculation
    df["Revenue"] = df["Quantity"] * df["Price"]

    # Date features
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day

    return df
