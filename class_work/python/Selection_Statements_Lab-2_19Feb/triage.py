age=int(input("Enter patient age: "))
heart_rate_abnormal=input("Is heart rate abnormal? (yes/no): ").lower()
severe_injury=input("Is there a severe injury? (yes/no): ").lower()
if heart_rate_abnormal == "yes" or severe_injury == "yes":
    condition = "Critical"
else:
    condition = "Moderate"
if age > 65 and condition == "Moderate":
    condition = "Critical"
print("Patient Condition:",condition)
