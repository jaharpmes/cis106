last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
exam_scores = [88, 92, 75, 64, 99, 81, 70, 85, 93, 78]

def display_names(names, scores):
    print(f"{'Last Name':<15}{'Score':>5}")
    for i in range(len(names)):
        print(f"{names[i]:<15}{scores[i]:>5}")

def display_names_reverse(names, scores):
    print(f"{'Last Name':<15}{'Score':>5}")
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]:<15}{scores[i]:>5}")

print("Names and scores:")
display_names(last_names, exam_scores)
print()
print("Names and scores in reverse order:")
display_names_reverse(last_names, exam_scores)