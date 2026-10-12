import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Food", "Travel", "Shopping", "Food", "Education", "Travel", "Shopping", "Food", "Education", "Travel"],
    "Amount": [150, 80, 500, 200, 300, 100, 250, 120, 450, 70]
}

df = pd.DataFrame(data)

print("EXPENSE DATA")
print(df)

amounts = df["Amount"].to_numpy()

print("\nEXPENSE SUMMARY")
print("Total Spending: ₹", np.sum(amounts))
print("Average Expense: ₹", np.mean(amounts))
print("Highest Expense: ₹", np.max(amounts))
print("Lowest Expense: ₹", np.min(amounts))

category_spending = df.groupby("Category")["Amount"].sum()
category_spending = category_spending.sort_values(ascending=False)

print("\nCATEGORY-WISE SPENDING")
print(category_spending)

print("\nHighest Spending Category:")
print(category_spending.idxmax())

category_spending.plot(kind="bar")

plt.xlabel("Expense Category")
plt.ylabel("Total Amount (₹)")
plt.title("Category-wise Expense Analysis")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

plt.pie(
    category_spending,
    labels=category_spending.index,
    autopct="%1.1f%%"
)

plt.title("Expense Distribution")
plt.show()
