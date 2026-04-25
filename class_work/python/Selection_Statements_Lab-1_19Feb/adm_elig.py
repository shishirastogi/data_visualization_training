percentage=float(input("Enter 12th grade percentage: "))
maths=input("Have you studied Mathematics? (yes/no): ").lower()
entrance_score=int(input("Enter entrance exam score: "))
eligible=True
if percentage < 75:
    print("Not eligible: 12th percentage is below 75%.")
    eligible=False
if maths != "yes":
    print("Not eligible: Mathematics was not studied.")
    eligible=False
if entrance_score < 80:
    print("Not eligible: Entrance exam score is below 80.")
    eligible=False
if eligible:
    print("Eligible for admission_v2.")
