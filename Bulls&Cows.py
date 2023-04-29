"""projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Šárka Böhmová
email: sarka.bohmova@seznam.cz
discord: ShareenBoom#6281
"""

import random

separator = "-"*30

def generate_secret_number():
    digits = random.sample(range(1, 10), 4)  # Unikátní číslice od 1 do 9
    return ''.join(map(str, digits))


def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def is_valid_guess(guess):
    if len(guess) != 4:
        return False
    if not guess.isdigit():
        return False
    if guess[0] == '0':
        return False
    if len(set(guess)) != 4:
        return False
    return True

def bulls_and_cows():
    print("Hi there!")
    print(separator)
    print("""I've generated a random 4 digit number for you. 
Let's play a bulls and cows game.""")
    print(separator)
    secret_number = generate_secret_number()
    attempts = 0
    while True:
        guess = input("Enter your 4 digit number: ")
        print(separator)
        if not is_valid_guess(guess):
            print("Wrong number! Guess 4 unique numbers!")
            continue
        bulls, cows = evaluate_guess(secret_number, guess)
        attempts += 1
        if bulls == 4:
            print(f"Correct, you've guessed the {secret_number} in {attempts} guesses!")
            print(separator)
            if attempts < 5:
                print("That's amazing!")
            elif attempts > 5 and attempts < 10:
                print("That's average!")
            else:
                print("That's not so good!")
            break
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

bulls_and_cows()
