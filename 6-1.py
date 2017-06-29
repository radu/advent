#!/usr/bin/python3.5

import sys
from operator import itemgetter

chars = ['']*8

while True:
    try:
        line = sys.stdin.readline().rstrip()

    except KeyboardInterrupt:
        break

    if not line:
        break

    nc = list(line)

    chars = [c + n for (c,n) in zip(chars, nc)]

    print(nc,chars)

code = ''

for ch in list(chars):
    uni_chars = []
    uni_sum = []
    for i in ch:
        if not i in uni_chars:
            uni_chars.append(i)
            uni_sum.append(ch.count(i))

    (c,s)=zip(*sorted(zip(uni_chars, uni_sum), key=itemgetter(1), reverse=True))

    print(c,s)

    code += c[0]


print(code)

