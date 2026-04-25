credit_score=int(input("Enter credit score: "))
income=float(input("Enter monthly income: "))
existing_loan=float(input("Enter existing loan amount: "))
if credit_score < 600:
    print("Loan Rejected: Low credit score.")
elif credit_score >= 750:
    print("Loan Approved.")
elif income < 30000 and existing_loan > 500000:
    print("Loan Rejected: Low income and high existing loan.")
else:
    print("Loan Approved (after additional checks).")
