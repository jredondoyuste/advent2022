import numpy as np
import pandas as pd

x = []
sums = []
for line in open('Day1/input'):
    line = line.strip()
    if len(line) != 0:
        x.append(int(line))
    if len(line) == 0:
        sums.append(np.sum(x))
        x = []
    
print(np.amax(sums))

total = np.amax(sums)

sums.pop(np.where(sums == np.amax(sums))[0][0])

total += np.amax(sums)
print(np.amax(sums), total)
sums.pop(np.where(sums == np.amax(sums))[0][0])
total += np.amax(sums)
print(np.amax(sums), total)