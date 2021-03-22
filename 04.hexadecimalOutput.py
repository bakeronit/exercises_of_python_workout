#!/usr/bin/env python

## for loop in python don't give us (or even use) the characters's indexes while in other languages, like C, for loop iterate over sequences of numbers. So we need to use enumerate()

## to reverse a string, one can use reversed() or seq[::-1]. but seq[::-1] is confusing and will create a new string. reversed use less memory.

def hex_output():
    decnum = 0 
    hexnum = input("Enter a hex number to convert: ")
    for power, digit in enumerate(reversed(hexnum)):
        if ord(digit) >= 48 and ord(digit) <=57:
            decnum += (ord(digit) - 48) * (16 ** power)
        elif ord(digit) >=65 and ord(digit) <=70:
            decnum += (ord(digit)-55) * (16 ** power)
        else:
            print("ERROR: not hex input")
    print(decnum)

hex_output()

def name_triangle():
    name = input("Please input your name: ")
    for index, zimu in enumerate(name):
        print(name[:index])
name_triangle()
