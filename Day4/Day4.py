import numpy as np

total = 0

for line in open('Day4/input'):
    line = line.strip()
    part1, part2 = [], []
    counter = 0
    for el in line:
        if el == '-':
            continue
        if el == ',':
            counter += 1
        else:
            if counter < 1:
                part1.append(el)
            else:
                part2.append(el)
    if len(part1) == 2:
        max1, min1 = int(part1[1]), int(part1[0])
    if len(part1) == 3:
        max1, min1 = 10 * int(part1[1]) + int(part1[2]),  int(part1[0])
    if len(part1) == 4:
        max1, min1 = 10 * int(part1[2]) + int(part1[3]), 10 * int(part1[0]) + int(part1[1])
    if len(part2) == 2:
        max2, min2 = int(part2[1]), int(part2[0])
    if len(part2) == 3:
        max2, min2 = 10 * int(part2[1]) + int(part2[2]), int(part2[0])
    if len(part2) == 4:
        max2, min2 = 10 * int(part2[2]) + int(part2[3]), 10 * int(part2[0]) + int(part2[1])
    newcounter = 0
    if min2 >= min1 and max2 <= max1:
        total += 1
    elif min1 >= min2 and max1 <= max2:
        total += 1

print(total)

# Part 2

total = 0

for line in open('Day4/input'):
    line = line.strip()
    part1, part2 = [], []
    counter = 0
    for el in line:
        if el == '-':
            continue
        if el == ',':
            counter += 1
        else:
            if counter < 1:
                part1.append(el)
            else:
                part2.append(el)
    if len(part1) == 2:
        max1, min1 = int(part1[1]), int(part1[0])
    if len(part1) == 3:
        max1, min1 = 10 * int(part1[1]) + int(part1[2]),  int(part1[0])
    if len(part1) == 4:
        max1, min1 = 10 * int(part1[2]) + int(part1[3]), 10 * int(part1[0]) + int(part1[1])
    if len(part2) == 2:
        max2, min2 = int(part2[1]), int(part2[0])
    if len(part2) == 3:
        max2, min2 = 10 * int(part2[1]) + int(part2[2]), int(part2[0])
    if len(part2) == 4:
        max2, min2 = 10 * int(part2[2]) + int(part2[3]), 10 * int(part2[0]) + int(part2[1])
    newcounter = 0
    if max1 >= min2 >= min1:
        total += 1
    elif min1 <= max2 <= max1:
        total += 1
    elif max2 >= min1 >= min2:
        total += 1
    elif min2 <= max1 <= max2:
        total += 1

print(total)
