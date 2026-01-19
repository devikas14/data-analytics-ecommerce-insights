def calculate_kpis(df):
    return {
        "Total Revenue": round(df["Revenue"].sum(), 2),
        "Total Orders": df["Invoice"].nunique(),
        "Total Customers": df["Customer ID"].nunique(),
        "Avg Order Value": round(df["Revenue"].sum() / df["Invoice"].nunique(), 2),
        "Top Country": df.groupby("Country")["Revenue"].sum().idxmax()
    }
