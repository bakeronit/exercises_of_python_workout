#!/usr/bin/env python
## this point of this excercise is to learn how to accumulate data over time and avoid invalid input.
## floating-point numbers are good enough here but not completely accurate in some sensitive measurement. Try 0.1+0.2 in python, it's not 0.3


def run_timing():

    number_of_runs = 0
    total_time = 0

    while True:
        try:
            one_run = float(input('Enter 10km run time: '))
        except ValueError as e:
            if not number_of_runs:
                print("Hey! That\'s not a valid number!")
                break
            average_time = total_time / number_of_runs

            print(f'Average of {average_time:.2f}, over {number_of_runs} runs')
            break

        number_of_runs += 1
        total_time += one_run

#run_timing()

def by1(f, b, a):
    before = str(int(f))[-b:]
    after = str(f).split('.')[1][:a]
    print(f'{before}.{after}')

by1(1234.5678, 2,3)
