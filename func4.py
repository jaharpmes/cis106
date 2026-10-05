def car_price(msrp, make, model, electric_code):
    make = make.strip().lower()
    model = model.strip().lower()
    if electric_code.strip().upper() == 'Y':
        discount_rate = 0.30
    elif make == 'honda' and model == 'accord':
        discount_rate = 0.10
    elif make == 'toyota' and model == 'rav4':
        discount_rate = 0.15
    else:
        discount_rate = 0.05
    discounted_price = msrp * (1 - discount_rate)
    return discounted_price * 1.07


total_msrp = 0
total_sales_price = 0
again = input('Enter a vehicle? (Yes or No): ')
while again.strip().lower() == 'yes':
    make = input('Enter make: ')
    model = input('Enter model: ')
    electric_code = input('Electric vehicle? (Y or N): ')
    msrp = float(input('Enter MSRP: '))
    total = car_price(msrp, make, model, electric_code)
    print(f'{make} {model}: Out the door price ${total:,.2f}')
    total_msrp += msrp
    total_sales_price += total
    again = input('Enter another vehicle? (Yes or No): ')
print(f'Total MSRP: ${total_msrp:,.2f}')
print(f'Total sales prices: ${total_sales_price:,.2f}')
