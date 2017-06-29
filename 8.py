#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter
W = 50
H = 6
d = [ [0] *50 for i in range(H) ]

while True:
    try:
        line = sys.stdin.readline().rstrip()

        rrect = re.compile('rect (\d+)x(\d+)')
        rotate = re.compile('rotate (row|column) \w=(\d+) by (\d+)')

        m=rrect.match(line)
        if m:
            print(m.group(0))
            (_, w, h) = (m.group(0), int(m.group(1)), int(m.group(2)))
            for x in range(h):
                for y in range(w):
                    d[x][y]=1

        m=rotate.match(line)
        if m:
            print(m.group(0))
            (_, way, num, amt) = (m.group(0), m.group(1), int(m.group(2)), int(m.group(3)))

            if way=='row':
                d[num] = d[num][-amt:] + d[num][:-amt]
            elif way=='column':
                col = [0] * H
                for x in range(H):
                    col[x] = d[(x-amt) % H][num]
                for x in range(H):
                    d[x][num] = col[x]

    except KeyboardInterrupt:
        break

    if not line:
        break

    for row in d:
        print(''.join(['*' if c else ' ' for c in row]))

print(sum([x for r in d for x in r]))
