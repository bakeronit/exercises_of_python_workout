#!/usr/bin/env python

# this function reimplement the python sum function. This function takes a variable number of arguments.

# * the "splat" operator allows mysum to receive any number of arguments. other arguments behind it need to be key argumentis instead of positional arguments.
def mysum(*numbers, starting_value=0):
    output = starting_value
    for number in numbers:
        if isinstance(number, int):  #ignore non-integer
            output += number
    return output, output/len(numbers)

print(mysum(1,2,3,4,5))

print(mysum(*[1,2,3]))
"""
mysum function will only take individual numbers and packed them into tuple then iterate the tuple to get the sum. If you want to pass a list directly to the function, python will complain about adding int to a list. use * when we invoke the function, the list becomes three separate arguments.
"""

