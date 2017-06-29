#!/usr/bin/python3.5

import sys


pos = []

while True:
    c = [[],[],[]]
    for i in range(3):
        try:
            line = sys.stdin.readline().rstrip()
        except KeyboardInterrupt:
            break

        if not line:
            break

        c[i] = [int(x) for x in line.split()]

    if not c[0]:
        break

    for i in range(3):
        d = [x[i] for x in c]

        d.sort()

        if d[0] + d[1] > d[2]:
            pos.append(d)

print(len(pos))
