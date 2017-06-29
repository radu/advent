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

    tiles = [ c == '.' for c in line]

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

rows = 400000
total = tiles.count(True)

for i in range(1,rows):
    newtiles = []
    for j in range(len(tiles)):
        newtiles.append(trap(tiles, j))
    tiles = newtiles
    total += tiles.count(True)

#pprint([''.join(['.' if c else '^' for c in row ]) for row in tiles])
#print(sum([x.count(True) for x in tiles]))

print(total)
