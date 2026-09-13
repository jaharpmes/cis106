purchase_price = float(input("Enter the purchase price per share: $"))
current_price = float(input("Enter the current stock price: $"))
quantity = int(input("Enter the quantity of stock: "))
value_change = (current_price - purchase_price) * quantity
print(f"Increase or decrease in stock value: ${value_change:.2f}")
