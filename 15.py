#!/usr/bin/env python2.7

import sys
import re
from pprint import pprint
#from operator import itemgetter


l = re.compile(r'Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+).')

numpos = []
startpos = []

while True:
    try:
        line = sys.stdin.readline().rstrip()

        m = l.match(line)

        if m:
            numpos.append(int(m.group(2)))
            startpos.append(int(m.group(3)))


    except KeyboardInterrupt:
        break

    if not line:
        break

print(numpos)
print(startpos)

print('------')

t = 0
disc = 0
num_discs = len(numpos)

def posat(t):
    return [(s+i+t)%n for (i,s,n) in zip(range(len(numpos)), startpos, numpos)]

def find_miss(p):
    for (d,x) in enumerate(p):
        if x:
            return d
    return None

m = 0

while True:
    positions = posat(t+1)
    m  = find_miss(positions)
    if m == None:
        break

    time_needed = ( - positions[m]) % numpos[m]

    t+=time_needed

print(t, positions, time_needed)

