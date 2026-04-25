def manage_inventory(stock):
    updated = [s + 50 if s < 10 else s for s in stock if s > 0]
    
    return {
        "Updated_Stock": updated,
        "Total_Count": sum(updated)
    }

current_stock = [0, 5, 12, 8, 0, 45, 3]
print(manage_inventory(current_stock))