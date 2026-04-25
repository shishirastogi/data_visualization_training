amount=float(input("Enter transaction amount:"))
account_age=int(input("Enter account age in months: "))
transaction_type=input("Is the transaction international? (yes/no):")
if amount > 200000 and account_age < 6 and (transaction_type == "yes"):
    print("Transaction Flagged for Manual Verification")
else:
    print("Transaction is normal")
