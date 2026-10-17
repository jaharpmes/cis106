import os

players = {}

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "batting.txt")

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            players[parts[0]] = float(parts[1])


def display_players(players):
    print(f"{'Player':<15}{'Average':>10}")
    print("-" * 25)
    for name in players:
        print(f"{name:<15}{players[name]:>10.3f}")


display_players(players)
