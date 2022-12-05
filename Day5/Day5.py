import numpy as np
import string

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

for number in range(10):
    values[str(number)] = number

def findheights(state):
    nrows, ncolumns = np.shape(init)
    heights = np.zeros(ncolumns)
    for k in range(ncolumns):
        vaux = state[:, k]
        heights[k] = int(np.amax( np.where( vaux == 0)[0] ))
    return heights

def update(state, tomove, start, target):
    start = int(start - 1)
    target = int(target - 1)
    hs = int(heights[start]) + 1
    ht = int(heights[target]) + 1
    nn = 0
    while nn < tomove:
        state[ht - 1 - nn, target] = state[hs + nn, start]
        state[hs + nn, start] = 0
        nn += 1
    return state

def new_update(state, tomove, start, target):
    start = int(start - 1)
    target = int(target - 1)
    hs = int(heights[start]) + 1
    ht = int(heights[target]) + 1
    nn = 0
    while nn < tomove:
        state[ht - tomove + nn, target] = state[hs + nn, start]
        state[hs + nn, start] = 0
        nn += 1
    return state

init = []
counter = 0

for line in open('Day5/input'):
    newcounter = 0
    line = line.strip()
    if len(line) == 0:
        # Parse Initial State
        counter += 1
        init = np.array(init)
        init = np.delete(init, len(init) - 1, 0 )
        nrows, ncolumns = np.shape(init)
        state = np.zeros((10 * nrows, ncolumns))
        for j in range(nrows):
            state[j + 9 * nrows] = init[j]
        heights = findheights(state)
    if counter < 1:
        # Construct Initial State
        row = []
        for el in line:
            if el == '[' or el == ']':
                continue
            if el == ' ' and newcounter == 3:
                row.append(0)
                newcounter = 0
            elif el == ' ':
                newcounter += 1
            elif el != ' ':
                newcounter = 0
                row.append(values[el])
        if len(row) < 9:
            row.append(0)
        init.append(row)
    if counter == 1 and len(line) != 0:
        # Get Instructions
        instructions = []
        for el in line:
            if el.isdigit():
                instructions.append(int(el))  
        if len(instructions) == 4:
            tomove = 10 * instructions[0] + instructions[1]
            start = instructions[2]
            target = instructions[3]
        elif len(instructions) == 3:
            tomove = instructions[0]
            start = instructions[1]
            target = instructions[2]
        # Update state:
        state = new_update(state, tomove, start, target)
        heights = findheights(state)

inv_map = {v: k for k, v in values.items()}

final_message = []
for col in range(ncolumns):
    ntop = int(state[int(heights[col] + 1), col])
    final_message.append(inv_map[ntop])

print(final_message)

print(values['F'])

print(inv_map[6])
print(inv_map[8])