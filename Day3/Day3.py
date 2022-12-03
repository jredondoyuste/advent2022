import numpy as np
import string

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

repeated = []
total = 0

for line in open('Day3/input'):
    line = line.strip()
    length = len(line)
    part1 = line[:int(length/2)]
    part2 = line[int(length/2):]
    counter = 0
    for el in part1:
        for el2 in part2:
            if counter < 1:
                if el == el2:
                    counter += 1
                    repeated.append(el)
                    total += values[el]

print(total)

# Part 2

group = []
total = 0
counter, newcounter = 0, 0
for line in open('Day3/input'):
    counter += 1
    line = line.strip()
    if counter == 3:
        counter, newcounter = 0, 0
        group.append(line)
        for el1 in group[0]:
            for el2 in group[1]:
                if el1 == el2:
                    for el3 in group[2]:
                        if newcounter < 1:
                            if el2 == el3:
                                newcounter += 1
                                total += values[el3]
        group = []
    else:
        group.append(line)

print(total)
