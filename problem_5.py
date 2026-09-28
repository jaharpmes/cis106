total_tuition = 0
student_count = 0

with open('students.txt') as student_file:
    name = student_file.readline().strip()
    while name != '':
        district_code = student_file.readline().strip().upper()
        credits = int(student_file.readline())
        if district_code == 'I':
            cost_per_credit = 250
        else:
            cost_per_credit = 500
        tuition = credits * cost_per_credit
        total_tuition += tuition
        student_count += 1
        print(f'{name}: Credits {credits}, Tuition ${tuition:,.2f}')
        name = student_file.readline().strip()

print(f'Total tuition: ${total_tuition:,.2f}')
print(f'Number of students: {student_count}')
