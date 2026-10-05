def exam_results(exam_1, exam_2, exam_3):
    total_points = exam_1 + exam_2 + exam_3
    average = total_points / 3
    return total_points, average


again = input('Enter a student? (Yes or No): ')
while again.strip().lower() == 'yes':
    last_name = input('Enter last name: ')
    exam_1 = float(input('Enter first exam score: '))
    exam_2 = float(input('Enter second exam score: '))
    exam_3 = float(input('Enter third exam score: '))
    total_points, average = exam_results(exam_1, exam_2, exam_3)
    print(f'{last_name}: Total points {total_points:.2f}, Average {average:.2f}')
    again = input('Enter another student? (Yes or No): ')
