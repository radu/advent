#!/usr/bin/python3

import hashlib

did = 'cxdnnyjw'

i = 0

p = ''

while True:
    ts = did + str(i)
    h = hashlib.md5(ts.encode('utf-8')).hexdigest()

    if h.startswith('00000'):
        print(h[:4],h[5],h[6:])
        p += h[5]

    if len(p) == 8:
        break

    i += 1

print(p)
