#!/usr/bin/env python

def pig_latin(word):
    if word[0] in 'aeiouAEIOU':
        return f'{word}way'
    if word[0].isupper():
        return f'{word[1].upper()}{word[2:]}{word[0].lower()}ay'
    return f'{word[1:]}{word[0]}ay'

# strings are inmutable

print(pig_latin('python'),pig_latin('Python'),pig_latin('Oricle'))
