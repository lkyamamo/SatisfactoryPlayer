import random
import numpy as np

level = 4
dim = 3
tiles = []
print(tiles)

for i in range(level):
    tiles.append((random.randint(0,dim-1), random.randint(0,dim-1)))

print(tiles)