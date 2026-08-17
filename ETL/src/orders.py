import pandas as pd

orders_df = "ETL/data/raw/orders.csv"

df = pd.read_csv(orders_df)
print(df.head())
print("")
df["order_id"] = df["order_id"].str.strip()
df = df.drop_duplicates(subset=["order_id"],keep="first")

print(df.tail())