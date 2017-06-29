#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter

xbyy = re.compile('\((\d+)x(\d+)\)')

def decomp(cur, totlen):
    m = xbyy.search(cur)

    if m:
        print('c: ', len(cur), cur)
        print('len: ', totlen)

        times = int(m.group(2))
        nchars = int(m.group(1))

        start = m.end()
        end = start + nchars

        print ('decompressing %d by %d starting at %d:%d'%(nchars, times, start, end))

        return int(m.start()) + times * decomp(cur[start:end], 0) + decomp(cur[end:], totlen)

    else:
        return len(cur) + totlen

s = []

while True:
    try:
        line = sys.stdin.readline().rstrip()

        d = decomp(line, 0)
        s.append(d)

        print(d)

    except KeyboardInterrupt:
        break

    if not line:
        break


print(sum(s))
