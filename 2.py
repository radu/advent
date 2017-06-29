#!/usr/bin/python3.5

import sys

cdir = 0

ax = {'U' : [-1, 0], 'R' : [0, 1], 'D': [1, 0], 'L' : [0, -1]}

nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]

pos = [1,1]

while True:
    try:
        line = sys.stdin.readline().rstrip()
    except KeyboardInterrupt:
        break

    if not line:
        break

    for c in line:
        mov = ax[c]

        pos = [max(min(2,a+b), 0) for (a,b) in zip(pos, mov)]

    print(nums[pos[0]][pos[1]])

