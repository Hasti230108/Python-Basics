import pandas as pd

data = {
    "Customer": ["Aarav", "Himanshi", "Kabir", "Kajal", "Dev", "Anaya", "Krish", "Sara"],
    "City": ["Mumbai", "Mumbai", "Thane", "Mumbai", "Thane", "Navi Mumbai", "Thane", "Navi Mumbai"],
    "Item": ["Coffee", "Tea", "Pizza", "Coffee", "Pizza", "Tea", "Coffee", "Pizza"],
    "Amount": [180, 120, 350, 200, 400, 100, 220, 380]
}

df = pd.DataFrame(data)

print(f"Original DataFrame: \n{df}")
print(f"\nSort Values by Amount in Ascending Order: \n{df.sort_values('Amount')}")
print(f"\nSort Values by Amount in Descending Order: \n{df.sort_values('Amount', ascending=False)}")
print(f"\nSort Values by City and Amount: \n{df.sort_values(['City', 'Amount'], ascending=[True, False])}")
print(f"\nSort Index in ascending order: \n{df.sort_index()}")
print(f"\nSort Index in descending order: \n{df.sort_index(ascending=False)}")

df["Rank"] = df["Amount"].rank(ascending=False)
print(f"DataFrame After Ranking: \n{df}")

print(f"\nTop 3 Customers by Amount: \n{df.nlargest(3, 'Amount')}")
print(f"\nBottom 3 Customers by Amount: \n{df.nsmallest(3, 'Amount')}")

customer_sales = df.groupby("Customer")["Amount"].sum()
print(f"\nSales by Customer in Descending Order: \n{customer_sales.sort_values(ascending=False)}")
print(f"\nSales by Top 3 Customers: \n{customer_sales.nlargest(3)}")

sales = df.groupby(["City", "Item"])["Amount"].sum()
print(f"\nSales by City and Item in Descending Order: \n{sales.sort_values(ascending=False)}")