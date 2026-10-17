grades = {
    "Smith": 88,
    "Johnson": 92,
    "Williams": 75,
    "Brown": 64,
    "Jones": 99,
}


def class_average(grades):
    total = 0
    count = 0
    for name in grades:
        total += grades[name]
        count += 1
    return total / count


print(f"{'Student':<15}{'Grade':>8}")
print("-" * 23)
for name in grades:
    print(f"{name:<15}{grades[name]:>8}")
print("-" * 23)
print(f"{'Class Average':<15}{class_average(grades):>8.2f}")
