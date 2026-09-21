quantity = int(input("Enter the quantity of widgets: "))
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax
print(f"Extended price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
