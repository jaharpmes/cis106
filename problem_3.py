total_bonuses = 0

with open('employees.txt') as employee_file:
    name = employee_file.readline().strip()
    while name != '':
        salary = float(employee_file.readline())
        if salary >= 100000:
            bonus_rate = 0.20
        elif salary >= 50000:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.10
        bonus = salary * bonus_rate
        total_bonuses += bonus
        print(f'{name}: Salary ${salary:,.2f}, Bonus ${bonus:,.2f}')
        name = employee_file.readline().strip()

print(f'Total bonuses: ${total_bonuses:,.2f}')
