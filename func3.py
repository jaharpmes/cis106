def sales_forecast(month, sales):
    month = month.strip().lower()[:3]
    if month in ('jan', 'feb', 'mar'):
        forecast_percent = 0.10
    elif month in ('apr', 'may', 'jun'):
        forecast_percent = 0.15
    elif month in ('jul', 'aug', 'sep'):
        forecast_percent = 0.20
    elif month in ('oct', 'nov', 'dec'):
        forecast_percent = 0.25
    else:
        raise ValueError('Enter a month name, such as Jan or January.')
    return sales * (1 + forecast_percent)


again = input('Enter sales information? (Yes or No): ')
while again.strip().lower() == 'yes':
    last_name = input('Enter last name: ')
    month = input('Enter month name: ')
    sales = float(input('Enter sales: '))
    forecast = sales_forecast(month, sales)
    print(f'{last_name}: Next month sales forecast ${forecast:,.2f}')
    again = input('Enter more sales information? (Yes or No): ')
