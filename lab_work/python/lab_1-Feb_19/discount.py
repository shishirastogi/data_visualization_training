cart_value=float(input("Enter cart value: "))
membership=input("Enter membership (Silver/Gold/Platinum): ")
festival=input("Is it festival season? (yes/no): ")
discount_v2=0
if membership == "silver":
    discount_v2=5
elif membership == "gold":
    discount_v2=10
elif membership == "platinum":
    discount_v2=15
if cart_value >= 20000:
    discount_v2=max(discount_v2,20)
elif cart_value >= 10000:
    discount_v2=max(discount_v2,10)
elif cart_value >= 5000:
    discount_v2=max(discount_v2,5)
if festival == "yes":
    discount_v2=max(discount_v2,12)
discount_amount=cart_value * discount_v2 / 100
final_amount=cart_value - discount_amount
print("Highest Discount Applied:",discount_v2, "%")
print("Final Payable Amount: Rs",final_amount)
