product_prices = [100, 200, 300, 400, 500, 200, 400]
no_redundancy = set(product_prices)
print(no_redundancy)

total = sum(no_redundancy)
discount = 0
if total > 5000:
    discount = 0.1 * total
    print(f"discount: {discount}")
else:
    print("No discount")

gst = 0.18 * total
print(f"gst: {gst}")

final_bill = total - discount + gst
print(f"final_bill: {final_bill}")