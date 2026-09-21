tickets = int(input("Enter the number of concert tickets: "))
if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00
total_cost = tickets * price_per_ticket
print(f"Number of tickets: {tickets}")
print(f"Price per ticket: ${price_per_ticket:.2f}")
print(f"Total cost: ${total_cost:.2f}")
