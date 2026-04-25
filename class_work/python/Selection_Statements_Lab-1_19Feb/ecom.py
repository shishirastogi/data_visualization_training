cart_value=float(input("Enter cart value: "))
membership=input("Enter membership (Silver/Gold/Platinum): ").lower()
festival=input("Is it festival season? (yes/no): ").lower()
discount_v2=0
if cart_value >= 10000:
    discount_v2=10
elif cart_value >= 5000:
    discount_v2=5
if membership == "silver":
    discount_v2=max(discount_v2,5)
elif membership == "gold":
    discount_v2=max(discount_v2,10)
elif membership == "platinum":
    discount_v2=max(discount_v2,15)
if festival == "yes":
    discount_v2=max(discount_v2,20)
final_amount=cart_value - cart_value * discount_v2 / 100
print("Highest Discount Applied:",discount_v2, "%")
print("Final Payable Amount: ₹",final_amount)
