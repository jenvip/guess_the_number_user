import random

def guess_user(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low. Guess again.')
        elif guess > random_number:
            print('Too high. Guess again.')

    print(f"Congrats! You have guessed {random_number} correctly!")

guess_user(50)


