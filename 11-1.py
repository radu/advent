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

locations = [
    [0,1], #,'Polonium'],
    [0,1], #,'Promethium'],
    [0,0], #,'Thulium'],
    [0,0], #,'Ruthenium'],
    [0,0], #,'Cobalt']
#    [0,0], #,'Elerium']
#    [0,0], #,'Dilithium']
]

seen_states = SortedList()
bad_states = SortedList()

efloor = 0;


def state_valid(state):
    # unprotected_chips = set([i[1] for i in state if i[0]!=i[1]])
    generators = set([i[0] for i in state])

    for i in state:
        if i[0] != i[1] and i[1] in generators:
            return False

    return True

def floor_items(state,floor):
    items = []
    for i, val in enumerate(state):
        if val[0] == floor:
            items.append((i,0))
        if val[1] == floor:
            items.append((i,1))

    return items

def new_state(state, nf, items):
    s = copy.deepcopy(state)
    for i in items:
        s[i[0]][i[1]] = nf
    return s

def state_final(state):
    return all([ i[0] == 3 and i[1] == 3 for i in state])

def next_states(floor, cur_state, num_moves):
    time_start = time.time()

    checked = 0

    new_states = deque([(floor, cur_state, num_moves)])

    while new_states:
        (floor, cur_state, num_moves) = new_states.popleft()

        if floor == 0 :
            possible_floors = [1]
        elif floor == 3 :
            possible_floors = [2]
        else:
            possible_floors = [floor-1, floor+1]

        items = floor_items(cur_state, floor)
        item_pairs = [[i] for i in items] + list(combinations(items, 2))


        for f in possible_floors:
            for its in item_pairs:
                ns = sorted(new_state(cur_state, f, its))
                checked += 1
                if not checked%10000:
                    print(checked, num_moves, f, ns, len(new_states),'/',len(seen_states), '*', len(bad_states), time.time() - time_start)
                if ns not in bad_states:
                    if (ns, f) not in seen_states:
                        seen_states.add((ns,f))
                        if state_valid(ns):
                            if state_final(ns):
                                print('final state:' , ns)
                                print('number of moves:', num_moves + 1)
                                return (num_moves + 1)
                            else:
                                new_states.append((f,ns, num_moves + 1))
                        else:
                            bad_states.add(ns)


print(next_states(efloor, locations, 0))

exit(0)


while True:
    try:
        line = sys.stdin.readline().rstrip()

        print(line)


    except KeyboardInterrupt:
        break

    if not line:
        break


