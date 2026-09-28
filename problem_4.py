total_extended_prices = 0
order_count = 0

with open('orders.txt') as order_file:
    item = order_file.readline().strip()
    while item != '':
        quantity = int(order_file.readline())
        price = float(order_file.readline())
        extended_price = quantity * price
        total_extended_prices += extended_price
        order_count += 1
        print(f'{item}: Quantity {quantity}, Price ${price:,.2f}, Extended price ${extended_price:,.2f}')
        item = order_file.readline().strip()

average_order = total_extended_prices / order_count if order_count > 0 else 0
print(f'Total extended prices: ${total_extended_prices:,.2f}')
print(f'Number of orders: {order_count}')
print(f'Average order: ${average_order:,.2f}')
