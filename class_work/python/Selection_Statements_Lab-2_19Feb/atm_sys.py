account_balance=float(input("Enter account balance: "))
withdraw_amount=float(input("Enter withdrawal amount: "))
atm_cash=float(input("Enter ATM cash available: "))
if withdraw_amount > account_balance:
    print("Transaction Failed: Insufficient account balance.")
elif withdraw_amount > 50000:
    print("Transaction Failed: Daily withdrawal limit exceeded.")
elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM has insufficient cash.")
else:
    print("Transaction Successful.")
    print("Please collect your cash: ₹",withdraw_amount)
