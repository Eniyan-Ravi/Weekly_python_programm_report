#sales report using pandas
import pandas as pd

sales = {
    "Product":["Laptop","Phone","Laptop","Tablet","Phone","Laptop","Tablet"],
    "Quantity":[2,5,1,3,4,2,5],
    "Price":[60000,25000,60000,30000,25000,60000,30000]
}

df = pd.DataFrame(sales)

print("Sales Report")
print(df)

print("\nProduct Count")
print(df["Product"].value_counts())

print("\nAverage Price")
print(df.groupby("Product")["Price"].mean())

print("\nTotal Quantity")
print(df.groupby("Product")["Quantity"].sum())

df.to_csv("sales.csv",index=False)

print("\nCSV File Saved Successfully")

new_df = pd.read_csv("sales.csv")

print("\nReading CSV")
print(new_df)