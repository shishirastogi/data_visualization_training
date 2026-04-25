credit_score=int(input("Enter credit score: "))
monthly_income=float(input("Enter monthly income: "))
existing_loan=float(input("Enter existing loan amount: "))
if credit_score < 600:
    print("Loan Rejected: Credit score below 600.")
elif credit_score > 750:
    print("Loan Approved: Excellent credit score.")
elif monthly_income < 30000 and existing_loan > 500000:
    print("Loan Rejected: Low income and high existing loan burden.")
else:
    print("Loan Approved: Meets eligibility conditions.")
