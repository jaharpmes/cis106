import os

last_names = []
scores = []

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores.txt")

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            last_names.append(parts[0])
            scores.append(int(parts[1]))


def display_names(names, scores):
    print(f"{'Last Name':<15}{'Score':>5}")
    for i in range(len(names)):
        print(f"{names[i]:<15}{scores[i]:>5}")


def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Highest score: {names[high_index]} {high_var}")
    print(f"Lowest score: {names[low_index]} {low_var}")


display_names(last_names, scores)
print()
display_high_low(last_names, scores)
