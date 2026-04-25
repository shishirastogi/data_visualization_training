amount=int(input("Enter the amount: "))
account_age=int(input("Enter the account age: "))
is_international=input("Is the transaction international? (yes/no): ").lower()
if amount > 200000 or account_age < 6 or is_international == "yes":
    print("Suspicious transaction detected!")
else:
    print("Transaction is normal.")
