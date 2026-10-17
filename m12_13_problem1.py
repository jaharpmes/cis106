last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]


def display_names(names):
    for i in range(len(names)):
        print(names[i])


def display_names_reverse(names):
    for i in range(len(names) - 1, -1, -1):
        print(names[i])


print("Names:")
display_names(last_names)
print()
print("Names in reverse order:")
display_names_reverse(last_names)