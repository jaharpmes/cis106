def compute_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    return discount_amount, discounted_price


again = input('Enter an item? (Yes or No): ')
while again.strip().lower() == 'yes':
    quantity = int(input('Enter quantity: '))
    price = float(input('Enter unit price: '))
    discount_rate = float(input('Enter discount rate as a decimal (0.10 for 10%): '))
    discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)
    print(f'Quantity: {quantity}, Price: ${price:,.2f}')
    print(f'Discount amount: ${discount_amount:,.2f}')
    print(f'Discounted price: ${discounted_price:,.2f}')
    again = input('Enter another item? (Yes or No): ')
