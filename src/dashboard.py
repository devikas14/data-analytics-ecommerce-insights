import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    layout="wide"
)

st.title("E-Commerce Sales Insights")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "clean", "clean_sales_data.csv")

# LOAD DATA
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

if not os.path.exists(DATA_PATH):
    st.error("Clean data not found. Please run ETL first.")
    st.stop()

df = load_data(DATA_PATH)

st.success("Data loaded successfully")

# KPI CALCULATIONS
total_revenue = df["TotalAmount"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()
avg_order_value = total_revenue / total_orders

# KPI DISPLAY
c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Total Revenue", f"₹ {total_revenue:,.2f}")
c2.metric("🧾 Total Orders", f"{total_orders}")
c3.metric("👥 Total Customers", f"{total_customers}")
c4.metric("📦 Avg Order Value", f"₹ {avg_order_value:,.2f}")

# REVENUE BY COUNTRY
st.subheader("🌍 Top 10 Countries by Revenue")

country_sales = (
    df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig1, ax1 = plt.subplots()
country_sales.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Revenue")
ax1.set_xlabel("Country")
st.pyplot(fig1)

# MONTHLY SALES TREND
st.subheader("📈 Monthly Revenue Trend")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["TotalAmount"].sum()

fig2, ax2 = plt.subplots()
monthly_sales.plot(ax=ax2)
ax2.set_ylabel("Revenue")
ax2.set_xlabel("Month")
st.pyplot(fig2)

# FOOTER
st.markdown("---")
st.caption("Built by Devika | Python • Pandas • Streamlit")