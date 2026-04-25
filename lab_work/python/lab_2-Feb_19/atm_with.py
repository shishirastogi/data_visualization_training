account_balance=float(input("Enter account balance: "))
withdraw_amount=float(input("Enter withdrawal amount: "))
atm_cash=float(input("Enter ATM available cash: "))
daily_limit=50000
if withdraw_amount > daily_limit:
    print("Transaction Failed: Exceeds daily withdrawal limit of Rs 50, 000.")
elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM has insufficient cash.")
elif withdraw_amount > account_balance:
    print("Transaction Failed: Insufficient account balance.")
else:
    account_balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Withdrawal Successful! Please collect your cash.")
    print("Remaining Account Balance: Rs",account_balance)
    print("Remaining ATM Cash: Rs ",atm_cash)
