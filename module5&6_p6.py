last_name = input("Enter the employee's last name: ")
salary = float(input("Enter the employee's salary: $"))
job_level = int(input("Enter the employee's job level: "))
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
bonus = salary * bonus_rate
print(f"Employee last name: {last_name}")
print(f"Bonus: ${bonus:.2f}")
