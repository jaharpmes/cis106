start = int(input('Enter start value: '))
stop = int(input('Enter stop value: '))
increment = int(input('Enter increment value: '))

if increment == 0:
    print('Increment cannot be zero.')
else:
    number = start
    while (increment > 0 and number <= stop) or (increment < 0 and number >= stop):
        print(number)
        number += increment
