import numpy as np

# Part One

string = open('Day6/input', 'r').read()
# string = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
counter = 0
lastfour = []
for el in string:
    counter += 1
    if len(lastfour) == 4:
        lastfour[0] = lastfour[1]
        lastfour[1] = lastfour[2]
        lastfour[2] = lastfour[3]
        lastfour[3] = el
        if lastfour[0] == lastfour[1] or lastfour[0] == lastfour[2] or lastfour[0] == lastfour[3]:
            continue
        elif lastfour[1] == lastfour[2] or lastfour[1] == lastfour[3]:
            continue
        elif lastfour[2] == lastfour[3]:
            continue
        else:
            print(lastfour)
            print(counter)
            break
    if len(lastfour) < 4:
        lastfour.append(el)

# Part 2

def isequal(input):
    for k in range(len(input)):
        aux = np.array([input[k] for x in range(len(input) - 1)])
        aux2 = np.delete(input, k)
        if any(x1 == x2 for (x1,x2) in zip(aux, aux2)):
            return True

counter = 0
lastfourteen = []
for el in string:
    counter += 1
    if len(lastfourteen) == 14:
        lastfourteen = np.roll(lastfourteen, -1)
        lastfourteen[-1] = el
        auxarray = np.array([el for x in range(3)])
        if isequal(lastfourteen):
            continue
        else:
            print(lastfourteen)
            print(counter)
            break
    if len(lastfourteen) < 14:
        lastfourteen = np.append(lastfourteen, el)