def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats


player_count = 0
again = input('Enter a player? (Yes or No): ')
while again.strip().lower() == 'yes':
    last_name = input('Enter last name: ')
    hits = int(input('Enter number of hits: '))
    at_bats = int(input('Enter number of at bats: '))
    average = batting_average(hits, at_bats)
    print(f'{last_name}: Batting average {average:.3f}')
    player_count += 1
    again = input('Enter another player? (Yes or No): ')
print(f'Number of players: {player_count}')
