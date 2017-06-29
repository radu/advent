#!/usr/bin/python3.5

import sys
import re
import copy
import time

from pprint import pprint
from itertools import combinations, repeat
#from sortedcontainers import SortedList
#from operator import itemgetter
from collections import deque

from hashlib import md5

#seen_states = SortedList()
#good_pos = set()

curpos = (0,0)

gen = 'ihgpwlah'
gen = 'kglvqrro'
gen = 'ulqzkmiv'
gen = 'bwnlcvfs'

destpos = (3,3)

dirs = {'U':0, 'D':1, 'L':2, 'R':3}

def valid_moves(pos, moves):
    vm = []

    locks = md5(gen+moves).hexdigest()[:4]
    amoves = all_moves(pos)

    for m in amoves:
        if m[1] == -1 or m[2] == -1 or m[1]==4 or m[2]==4:
            continue
        if locks[dirs[m[0]]] in ['b','c','d','e','f']:
            vm.append(((m[1],m[2]),moves+m[0]))

    return vm


def all_moves(pos):
    return [(d, pos[0]+x, pos[1]+y) for (d,x,y) in zip(['D','R','U','L'],[+1,0,-1,0],[0,+1,0,-1]) ]

def at_finish(pos):
    return (pos == destpos)

def next_states(pos):
    time_start = time.time()

    checked = 0

    new_states = deque([(pos, '')])

    while new_states:
        (p, moves) = new_states.popleft()

        if at_finish(p):
            print('at final position: ', p, 'after %s moves'%moves)
            return moves

        for (np,nmoves) in valid_moves(p, moves):
            new_states.append((np, nmoves))


print(next_states(curpos))

