import numpy as np
import pandas as pd

class ExpenseAnalyzer:
    def __init__(self, categories, expenses):
        self.categories = categories
        self.expenses = np.array(expenses)

    def show_expenses(self):
        print("\nCategories and Expenses:")
        for category, expense in zip(self.categories, self.expenses):
            print(f"- {category}: {expense}/-")

    def total_expense(self):
        print(f"\nTotal Expense: {np.sum(self.expenses)}")

    def average_expense(self):
        print(f"\nAverage Expense: {np.mean(self.expenses)}")

    def highest_expense(self):
        print(f"\nHighest Expense: {np.max(self.expenses)}")

    def category_analysis(self):
        df = pd.DataFrame({
            "Category": self.categories,
            "Amount": self.expenses
        })
        category_total = df.groupby("Category")["Amount"].sum()
        print(f"\nCategory-wise Totals:")
        for category, total in category_total.items():
            print(f"- {category}: {total}")

    def expense_level(self):
        df = pd.DataFrame({
            "Category": self.categories,
            "Amount": self.expenses
        })
        df["Expense Level"] = np.where(
            df["Amount"] >= 1000,
            "High",
            "Normal"
        )
        print(f"\nExpense Levels:")
        for category, level in zip(self.categories, df["Expense Level"]):
            print(f"- {category}: {level}")

categories = ["Food", "Travel", "Shopping", "Food", "Entertainment", "Travel", "Shopping", "Food"]

expenses = [250, 120, 1500, 450, 600, 180, 2200, 300 ]

analyzer = ExpenseAnalyzer(categories, expenses)
analyzer.show_expenses()
analyzer.total_expense()
analyzer.average_expense()
analyzer.highest_expense() 
analyzer.category_analysis()
analyzer.expense_level()