import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("SALES DATA ANALYSIS")
print("=" * 40)
print(f"Total revenue: ${df['Revenue'].sum():,.2f}")
print(f"Units sold: {df['Units_Sold'].sum():,}")
print(f"Average order-line revenue: ${df['Revenue'].mean():,.2f}")

print("\nRevenue by product:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

monthly = df.groupby("Month")["Revenue"].sum()
print("\nRevenue by month:")
print(monthly)

monthly.plot(kind="bar", title="Monthly Sales Revenue", ylabel="Revenue ($)", xlabel="Month")
plt.tight_layout()
plt.savefig("monthly_sales_revenue.png")
print("\nSaved chart as monthly_sales_revenue.png")
