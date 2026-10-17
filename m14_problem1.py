class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    def fullname(self):
        return f"{self.first} {self.last}"
    def compute_bonus(self, bonus_rate):
        return bonus_rate * self.salary
emp_1 = Employee("John", "Smith", 50000)
emp_2 = Employee("Jane", "Doe", 60000)
print(emp_1.fullname(), emp_1.salary)
print(emp_2.fullname(), emp_2.salary)
rate = float(input("Enter bonus rate (e.g. 0.05 for 5%): "))
print(f"{emp_1.fullname()} bonus: ${emp_1.compute_bonus(rate):,.2f}")
print(f"{emp_2.fullname()} bonus: ${emp_2.compute_bonus(rate):,.2f}")
