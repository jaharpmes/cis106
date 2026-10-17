class Student:
    tuition_rates = {
        "I": 250.00,
        "O": 500.00,
        "X": 800.00,
        "G": 250.00,
    }
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits
    def compute_tuition(self):
        return self.credits * Student.tuition_rates[self.district_code]
students = [
    Student("John", "Smith", "I", 12),
    Student("Jane", "Doe", "O", 9),
    Student("Wei", "Chen", "X", 15),
    Student("Maria", "Lopez", "G", 6),
]
for s in students:
    print(f"{s.first_name} {s.last_name}  District: {s.district_code}  Credits: {s.credits}  Tuition: ${s.compute_tuition():,.2f}")
