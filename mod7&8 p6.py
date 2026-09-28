student_count = 0
continue_program = input('Do you want to enter a student? (Yes to continue): ')

while continue_program.strip().lower() == 'yes':
    last_name = input('Enter last name: ')
    exam_1 = float(input('Enter first exam score: '))
    exam_2 = float(input('Enter second exam score: '))
    average = (exam_1 + exam_2) / 2
    print(f'{last_name}: Average exam score {average:.2f}')
    student_count += 1
    continue_program = input('Do you want to enter another student? (Yes to continue): ')

print(f'Number of students: {student_count}')
