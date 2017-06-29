#!/usr/bin/python3.5

import sys
import re

from operator import itemgetter

count = 0

while True:
    try:
        line = sys.stdin.readline().rstrip()
    except KeyboardInterrupt:
        break

    if not line:
        break

    m = re.match(r"(.*)-(\d+)\[(\w+)\]", line)

    (total,name,sector,csum) = (m.group(0),m.group(1),m.group(2),m.group(3))

    chars = [a for a in list(name) if a != '-']

    chars.sort()

    uni_chars = []
    uni_sum = []
    for i in chars:
        if not i in uni_chars:
            uni_chars.append(i)
            uni_sum.append(chars.count(i))

    (c,s)=zip(*sorted(zip(uni_chars, uni_sum), key=itemgetter(1), reverse=True))

    if (''.join(c[:5]) == csum):
        count += int(sector)

print(count)

