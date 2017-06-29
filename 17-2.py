#!/usr/bin/python3.5

import sys
import re
import copy
import time

from pprint import pprint
from itertools import combinations, repeat
from sortedcontainers import SortedList
#from operator import itemgetter
from collections import deque

from hashlib import md5

#seen_states = SortedList()
#good_pos = set()

curpos = (0,0)

#gen = 'ihgpwlah'
#gen = 'kglvqrro'
#gen = 'ulqzkmiv'
gen = 'bwnlcvfs'

destpos = (3,3)

dirs = {'U':0, 'D':1, 'L':2, 'R':3}

def valid_moves(pos, moves):
    vm = []

    locks = md5(gen+moves).hexdigest()[:4]
    amoves = all_moves(pos)

    for m in amoves:
#        if ((m[1],m[2]), locks) in seen_states:
#            next
        if m[1] == -1 or m[2] == -1 or m[1]==4 or m[2]==4:
            continue
        if locks[dirs[m[0]]] in ['b','c','d','e','f']:
            vm.append(((m[1],m[2]),moves+m[0]))
#            seen_states.add(((m[1],m[2]), locks))

    return vm



def all_moves(pos):
    return [(d, pos[0]+x, pos[1]+y) for (d,x,y) in zip(['D','R','U','L'],[+1,0,-1,0],[0,+1,0,-1]) ]

def at_finish(pos):
    return (pos == destpos)

longest = 0

def next_states(pos, path):
    global longest

    if at_finish(pos):
        lp = len(path)
        if lp > longest:
            longest = lp
            print(longest)

    else:
        for (np,nmoves) in valid_moves(pos, path):
            next_states(np, nmoves)


next_states(curpos, '')

print(longest)

