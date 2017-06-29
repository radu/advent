#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter

xbyy = re.compile('\((\d+)x(\d+)\)')

def decomp(cur, rest):
    m = xbyy.search(cur)

    if m:
        print('c: ', len(cur), cur)
        print('r: ', len(rest), rest)


        rest = rest + cur[:m.start()]

        times = int(m.group(2))
        nchars = int(m.group(1))


        start = m.end()
        end = start + nchars

        print ('decompressing %d by %d starting at %d:%d'%(nchars, times, start, end))

        if start + (nchars * times) > len(cur):
            print('ERROR')
            print('not enough chars to decompress')

        for _ in range(times):
            rest = rest + cur[start:end]

        cur = cur[end:]

        return decomp(cur, rest)
    else:
        print('no more found', cur, rest)
        rest = rest + cur
        print('returning ', len(rest))
        return rest

s = []

while True:
    try:
        line = sys.stdin.readline().rstrip()

        d = decomp(line, "")
        print(d, len(d))
        s.append(len(d))

    except KeyboardInterrupt:
        break

    if not line:
        break


print(sum(s))
