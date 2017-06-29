#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter

tiles = []

while True:
    try:
        line = sys.stdin.readline().rstrip()

    except KeyboardInterrupt:
        break

    if not line:
        break

    tiles.append([ c == '.' for c in line])

print(tiles)

def trap(x,a):
    if a==0:
        l=True
    else:
        l=x[a-1]

    if a==len(x)-1:
        r=True
    else:
        r=x[a+1]

    return not(l != r)

for i in range(1,40):
    tiles.append([])
    for j in range(len(tiles[i-1])):
        tiles[i].append(trap(tiles[i-1], j))

pprint([''.join(['.' if c else '^' for c in row ]) for row in tiles])
print(sum([x.count(True) for x in tiles]))

