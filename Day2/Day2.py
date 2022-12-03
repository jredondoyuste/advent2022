import numpy as np
# Part One
whowins = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

totpts = 0
for line in open('Day2/input'):
    totpts += whowins[line.strip()]

print(totpts)

# Part Two
whattodo = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X'
}

totpts = 0
for line in open('Day2/input'):
    totpts += whowins[whattodo[line.strip()]]

print(totpts)