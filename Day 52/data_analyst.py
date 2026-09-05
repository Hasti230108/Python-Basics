import pandas as pd

data = {
    "Customer": ["Aarav", "Himanshi", "Kabir", "Kajal", "Dev", "Anaya", "Krish", "Sara"],
    "City": ["Mumbai", "Mumbai", "Thane", "Mumbai", "Thane", "Navi Mumbai", "Thane", "Navi Mumbai"],
    "Item": ["Coffee", "Tea", "Pizza", "Coffee", "Pizza", "Tea", "Coffee", "Pizza"],
    "Amount": [180, 120, 350, 200, 400, 100, 220, 380]
}

df = pd.DataFrame(data)

print(df)

amount = df.groupby("City")["Amount"].sum()
print("\nTotal sales by city:\n", amount)

avg_amount = df.groupby("City")["Amount"].mean()
print("\nAverage sales by city:\n", avg_amount.round(2))

highest_amount = df.groupby("City")["Amount"].max()
print("\nHighest sales by city:\n", highest_amount)

no_of_orders = df.groupby("Item").size()
print("\nNumber of orders by item:\n", no_of_orders)

city_report = df.groupby("City").agg({"Amount": ['sum', 'mean', 'count']})
print("\nCity-wise sales report:\n", city_report)

sales = df.groupby(["City", "Item"])["Amount"].sum()
best_selling = sales.groupby(level=0).idxmax()
print("\nBest selling item by city:\n", best_selling)