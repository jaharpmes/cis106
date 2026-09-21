quantity = int(input("Enter the quantity: "))
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax
print(f"Quantity: {quantity}")
print(f"Unit price: ${unit_price:.2f}")
print(f"Extended price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
