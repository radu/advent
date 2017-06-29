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

seen_states = SortedList()
good_pos = set()

curpos = (1,1)

gen = 1352
destpos = (31,39)

#gen = 10
#destpos = (7,4)

def pos_valid(pos):
    (x,y) = (pos[0], pos[1])

    if x==-1 or y==-1:
        return False

    v = (3+x+2*y) * x + (y+1) * y
    v += gen

    cnt = 0

    for i in range(v.bit_length()-1, -1, -1):
        cnt += (v >> i & 1)

    if cnt % 2:
        return False
    else:
        return True



def all_moves(pos):
    return [(pos[0]+x, pos[1]+y) for (x,y) in zip([+1,0,-1,0],[0,+1,0,-1])]

def at_finish(pos):
    return (pos == destpos)

def next_states(pos):
    time_start = time.time()

    checked = 0

    new_states = deque([(pos, 0)])
    seen_states.add(pos)
    good_pos.add(pos)

    while new_states:
        (p, num_moves) = new_states.popleft()

        if num_moves == 50:
            print('seen ',len(seen_states),' states after ',num_moves)
            print('states left: ', new_states)
            return len(good_pos)

        if at_finish(p):
            print('at final position: ', p, 'after %d moves'%num_moves)
            return num_moves

        for np in all_moves(p):
            if np not in seen_states:
                seen_states.add(np)

                checked += 1

                if pos_valid(np):
                    good_pos.add(np)
                    print(checked, np, num_moves, len(new_states), time.time()-time_start)
                    new_states.append((np, num_moves + 1))


print('   0123456789')

for x in range(10):
    print(x,' ', end='')

    for y in range(10):
        print('.' if pos_valid((x,y)) else '#',end='')

    print('')

print(next_states(curpos))
print(good_pos)

