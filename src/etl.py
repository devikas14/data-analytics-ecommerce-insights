import os
import pandas as pd

def main():
    print("ETL started")

    # Base project path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    raw_path = os.path.join(BASE_DIR, "data", "raw", "online_retail_II.xlsx")
    clean_path = os.path.join(BASE_DIR, "data", "clean", "clean_sales_data.csv")

    # Load data
    df = pd.read_excel(raw_path)

    # Rename columns
    df = df.rename(columns={
        "Invoice": "InvoiceNo",
        "Price": "UnitPrice",
        "Customer ID": "CustomerID"
    })

    # Basic cleaning
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Datetime fix
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    df.to_csv(clean_path, index=False)

    print("ETL completed successfully")
    print("Final columns:")
    print(df.columns)

if __name__ == "__main__":
    main()

