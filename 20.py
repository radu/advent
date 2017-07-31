#!/usr/bin/env python2.7

import sys
import re

full = [(0,4294967295)]

def remove_from(rng, low, high):
    newrange = []

    n = 0

    while n < len(rng) and rng[n][1] < low:
        print '0->', rng[n]
        newrange.append(rng[n])
        n+=1

    if n == len(rng):
        return newrange

    lbr = rng[n][1]

    if n < len(rng) and lbr < low:
        print 'l->', (lbr,low-1)
        newrange.append((lbr,low-1))
    else:
        if low > rng[n][0]:
            print 'l2->', (rng[n][0], low-1)
            newrange.append((rng[n][0], low-1))

    hbr = min(lbr,low)

    while n < len(rng) and rng[n][1] < high:
        n+=1

    if n == len(rng)-1:
        if high < rng[n][1]:
            print 'm1->', (max(high+1,rng[n][0]), rng[n][1])
            newrange.append((max(high+1, rng[n][0]), rng[n][1]))
    else:
        if high < rng[n][1]:
            print 'm2->', (high+1, rng[n][1])
            newrange.append((high+1, rng[n][1]))

    n+=1

    while n < len(rng):
        print 'h->', rng[n]
        newrange.append(rng[n])
        n+=1

    return newrange

rr = re.compile(r'^(\d+)-(\d+)$')

while True:
    try:
        line = sys.stdin.readline().rstrip()

    except KeyboardInterrupt:
        break

    if not line:
        break

    print full

    m = rr.match(line)
    if m:
        low = int(m.group(1))
        high = int(m.group(2))

        print '-',low,':',high
        full = remove_from(full, low, high)

    else:
        print 'ERROR IN INPUT'
        break

print full

