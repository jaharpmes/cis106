def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.90
    return total


total_extended_price = 0
again = input('Enter an item? (Yes or No): ')
while again.strip().lower() == 'yes':
    quantity = int(input('Enter quantity: '))
    price = float(input('Enter unit price: '))
    total = compute_total(quantity, price)
    print(f'Quantity: {quantity}, Price: ${price:,.2f}, Total: ${total:,.2f}')
    total_extended_price += total
    again = input('Enter another item? (Yes or No): ')
print(f'Total extended price: ${total_extended_price:,.2f}')
