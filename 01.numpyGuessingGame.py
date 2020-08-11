#!/usr/bin/env python
import random
def guessing_game():
    number = random.randint(10, 30)
    name = input('Enter your name: ')
    print(f'Hello, {name}!')
    # while s := input('What is your guess?') # walrus operator, works from python 3.8
    n_try = 0
    while True:
        n_try += 1
        s = int(input('From 10 to 30, what is your guess?'))

        if s == number:
            print(f'Right! The answer is {s}')
            break

        if s < number:
            print(f'Your guess of {s} is too low!')
        else:
            print(f'Your guess of {s} is too high!')

        if n_try == 3:
            print('Sorry, you have reached the limit for guessing...')
            break



guessing_game()
