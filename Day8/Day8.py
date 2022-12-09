import numpy as np
import pandas as pd

forest = []
for line in open('Day8/input'):
    line = line.strip()
    lenline = len(line)
    for el in line:
        forest.append(int(el))

nn = 98

forest = np.reshape(forest, (nn+1, nn+1))

def is_visible(n, m):
    if n == 0 or n == nn or m == 0 or m == nn:
        return True
    else:
        tree = forest[n, m]
        treelinehor1 = forest[n, 0:m]
        treelinehor2 = forest[n, m+1:]
        treelinever1 = forest[0:n, m]
        treelinever2 = forest[n+1:, m]
        max1 = np.max(treelinehor1)
        max2 = np.max(treelinehor2)
        max3 = np.max(treelinever1)
        max4 = np.max(treelinever2)
        minmax = np.min([max1,max2,max3,max4])
        if minmax >= tree:
            return False
        else:
            return True

# counter = 0

# for i in range(99):
#     for j in range(99):
#         if is_visible(i,j):
#             counter +=  1

# print(counter)

def scenic_score(i, j):
    if i == 0 or j == 0 or i == nn or j == nn:
        return 0
    else:
        tree = forest[i, j]
        treelinehor1 = np.flip(forest[i, 0:j])
        treelinehor2 = forest[i, j+1:]
        treelinever1 = np.flip(forest[0:i, j])
        treelinever2 = forest[i+1:, j]
        max1 = np.max(treelinehor1)
        max2 = np.max(treelinehor2)
        max3 = np.max(treelinever1)
        max4 = np.max(treelinever2)
        if max1 < tree:
            west = j
        else:
            west = 1 + next(ind for ind,val in enumerate(treelinehor1) if val >= tree)
        if max2 < tree:
            east = nn - j
        else:
            east = 1 + next(ind for ind,val in enumerate(treelinehor2) if val >= tree)
        if max3 < tree:
            north = i
        else:
            north = 1 + next(ind for ind,val in enumerate(treelinever1) if val >= tree)
        if max4 < tree:
            south = nn - i
        else:
            south = 1 + next(ind for ind,val in enumerate(treelinever2) if val >= tree)
        return north * south * east * west

scenic_scores = np.zeros((nn+1,nn+1))

for i in range(nn):
    for j in range(nn):
        scenic_scores[i,j] = scenic_score(i,j)
    
print(np.max(scenic_scores))


