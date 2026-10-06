import random
import pyfiglet


print('Hello! Welcome to the number guessing game!')

decimals = input('Would you like to add decimals to the game? (Y/N) ')
if decimals.lower() not in ('y', 'yes', 'n', 'no'):
    print('Please enter Y or N.')


# if decimals are decided to be included
elif decimals.lower() in ('y', 'yes'):
    print('Decimals enabled!\n')

    while True:
        places = input('How many decimal places would you like? ')
        try:
            places = int(places)
            break
        except ValueError:
            print('Please enter a integer.')
              
    while True:
        try:
            higher = float(input('What would you like the higher bound to be (number): '))
            print(f'Upper Bound: {higher:.{places}f}')
            break
        except ValueError:
            print('Please enter a integer or decimal.')
            
    while True:
        try:
            lower = float(input('What would you like the lower bound to be (number): ')) 
            if lower >= higher:
                print('Lower bound must be smaller than higher bound.')
            else:
                print(f'Lower Bound: {lower:.{places}f}')
                break 
        except ValueError:
            print('Please enter a integer or decimal.')

    print(f"\nDecimal Places: {places}\nUpper Bound: {higher:.{places}f}\nLower Bound: {lower:.{places}f}\n")
    target =  round(random.uniform(lower, higher), places)
    print(target,'\n\n\n')
    while True:
        try:
            guess = float(input('Please input your guess: '))
            if guess == target:
                print(pyfiglet.figlet_format('Wow! You got it!'))
                print(pyfiglet.figlet_format(f'Correct Guess: {guess:.{places}f}'))
                break
            elif guess > higher or guess < lower:
                print(pyfiglet.figlet_format('Out of bounds.'))
            elif guess > target:
                print(pyfiglet.figlet_format('Too high.'))
                print(f'Guess: {guess:.{places}f}\n')
            elif guess < target:
                print(pyfiglet.figlet_format('Too low.'))
                print(f'Guess: {guess:.{places}f}\n')
        except ValueError:
            print('Please enter a number.')


# only integers   
else:
    print('Only whole numbers!\n')
              
    while True:
        try:
            higher = int(input('What would you like the higher bound to be (number): '))
            print(f'Upper Bound: {higher}')
            break
        except ValueError:
            print('Please enter a integer.')
            
    while True:
        try:
            lower = int(input('What would you like the lower bound to be (number): ')) 
            if lower >= higher:
                print('Lower bound must be smaller than higher bound.')
            else:
                print(f'Lower Bound: {lower}')
                break 
        except ValueError:
            print('Please enter a integer.')

    print(f"\nUpper Bound: {higher}\nLower Bound: {lower}\n")
    target =  random.randint(lower, higher)
    print(target,'\n\n\n')
    while True:
        try:
            guess = int(input('Please input your guess: '))
            if guess == target:
                print(pyfiglet.figlet_format('Wow! You got it!'))
                print(pyfiglet.figlet_format(f'Correct Guess: {guess}'))
                break
            elif guess > higher or guess < lower:
                print(pyfiglet.figlet_format('Out of bounds.'))
            elif guess > target:
                print(pyfiglet.figlet_format('Too high.'))
                print(f'Guess: {guess}\n')
            elif guess < target:
                print(pyfiglet.figlet_format('Too low.'))
                print(f'Guess: {guess}\n')
        except ValueError:
            print('Please enter a number.')