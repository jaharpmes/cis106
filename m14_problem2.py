class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits
    def compute_tuition(self):
        if self.district_code == "I":
            return self.credits * 250.00
        else:
            return self.credits * 500.00
student_1 = Student("John", "Smith", "I", 12)
student_2 = Student("Jane", "Doe", "O", 9)
for s in [student_1, student_2]:
    print(f"{s.first_name} {s.last_name}  District: {s.district_code}  Credits: {s.credits}  Tuition: ${s.compute_tuition():,.2f}")
