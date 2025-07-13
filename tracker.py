import pandas as pd
from datetime import datetime

def add_transaction(category, amount, description=""):
    df = pd.read_csv("data/transactions.csv")
    new = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Category": category,
        "Amount": float(amount),
        "Description": description
    }
    new_row = pd.DataFrame([new])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("data/transactions.csv", index=False)
    print("✅ Added:", new)

if __name__ == "__main__":
    add_transaction("Food", 250, "Lunch")
    add_transaction("Travel", 150, "Bus fare")
    add_transaction("Education", 500, "Course fee")
    add_transaction("Shopping", 1200, "New shoes")
    add_transaction("Entertainment", 300, "Movie night")
def show_summary():
    df = pd.read_csv("data/transactions.csv")
    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
    summary = df.groupby(["Month", "Category"])["Amount"].sum().unstack(fill_value=0)
    print("\n📊 Expense Summary by Month and Category:\n")
    print(summary)
if __name__ == "__main__":
    add_transaction("Food", 250, "Lunch")
    add_transaction("Travel", 150, "Bus fare")
    add_transaction("Education", 500, "Course fee")
    add_transaction("Shopping", 1200, "New shoes")
    add_transaction("Entertainment", 300, "Movie night")
    show_summary()
import matplotlib.pyplot as plt

def plot_summary():
    df = pd.read_csv("data/transactions.csv")
    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
    summary = df.groupby(["Month", "Category"])["Amount"].sum().unstack(fill_value=0)

    # Plot
    colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F',"#098D82"][:len(summary.columns)] # one color per category
    ax = summary.plot(kind="bar", figsize=(10,6), width=0.8, color=colors,edgecolor='white',linewidth=2)
    ax.set_title("Monthly Expense by Category")
    ax.set_ylabel("Amount (₹)")
    ax.set_xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/summary.png")  # Save the image
    plt.show()
if __name__ == "__main__":
    add_transaction("Food", 250, "Lunch")
    add_transaction("Travel", 150, "Bus fare")
    add_transaction("Education", 500, "Course fee")
    add_transaction("Shopping", 1200, "New shoes")
    add_transaction("Entertainment", 300, "Movie night")
    show_summary()
    plot_summary()