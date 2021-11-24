import random
print('\nWelcome to the guess number app.')

name = input('\n Hello! What is your name: ').title().strip()

print('\n Well ', name, ' I am thinking of a number between 1 and 20. ')
random_number = random.randint(1, 20)

for i in range(1, 6):
    guessed_number = int(input('\n Take a Guess : '))

    if guessed_number > 20:
        print('\n Choose a number between 1 and 20 : ')
    elif guessed_number < random_number:
        print(f'\n Your guess is too low. ')
    elif guessed_number > random_number:
        print(f'\n Your guess is too high.')
    else:
        break
if guessed_number == random_number:
    print(f'\n Good Jobe {name}, You guessed my number in {i} guesses!')
else:
    print(f'\n Game over! The number I was thinking of was {random_number}') 