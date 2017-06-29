#!/usr/bin/python3.5

import sys

cdir = 0

ax = {'U' : [-1, 0], 'R' : [0, 1], 'D': [1, 0], 'L' : [0, -1]}

nums = [[0,0,1,0,0],
        [0,2,2,3,0],
        [5,6,7,8,9],
        [0,'A','B','C',0],
        [0,0,'D',0,0]]

pos = [3,0]

while True:
    try:
        line = sys.stdin.readline().rstrip()
    except KeyboardInterrupt:
        break

    if not line:
        break

    for c in line:
        mov = ax[c]

        npos = [max(min(4,a+b), 0) for (a,b) in zip(pos, mov)]

        if nums[npos[0]][npos[1]]:
            pos = npos

    print(nums[pos[0]][pos[1]])

