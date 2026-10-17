grades = {
    "Smith": [88, 79, 91],
    "Johnson": [92, 85, 88],
    "Williams": [75, 82, 70],
    "Brown": [64, 71, 68],
    "Jones": [99, 95, 97],
}


def student_averages(grades):
    averages = []
    for name in grades:
        total = 0
        count = 0
        for grade in grades[name]:
            total += grade
            count += 1
        averages.append([name, total / count])
    return averages


def class_averages(grades):
    totals = [0, 0, 0]
    count = 0
    for name in grades:
        for i in range(3):
            totals[i] += grades[name][i]
        count += 1
    averages = []
    for i in range(3):
        averages.append(totals[i] / count)
    return averages


print(f"{'Student':<15}{'Grade 1':>10}{'Grade 2':>10}{'Grade 3':>10}{'Average':>10}")
print("-" * 55)
for student in student_averages(grades):
    name = student[0]
    g = grades[name]
    print(f"{name:<15}{g[0]:>10}{g[1]:>10}{g[2]:>10}{student[1]:>10.2f}")
print("-" * 55)
avgs = class_averages(grades)
print(f"{'Class Average':<15}{avgs[0]:>10.2f}{avgs[1]:>10.2f}{avgs[2]:>10.2f}")
