import pandas as pd
import numpy as np

def analyze_sales():
    """Generates synthetic data and performs basic analysis."""
    print("Generating synthetic sales data...")
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
    data = {
        "Date": dates,
        "Sales": np.random.normal(loc=1000, scale=200, size=100).round(2),
        "Category": np.random.choice(["A", "B", "C"], size=100)
    }
    df = pd.DataFrame(data)
    
    print("\nBasic Statistics:")
    print(df.describe())
    
    print("\nTotal Sales by Category:")
    summary = df.groupby("Category")["Sales"].sum().reset_index()
    print(summary)
    
    # Save to a temporary CSV
    df.to_csv("synthetic_sales_data.csv", index=False)
    print("\nSaved data to synthetic_sales_data.csv")

if __name__ == "__main__":
    analyze_sales()
