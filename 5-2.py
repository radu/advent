#!/usr/bin/python3

import hashlib

did = 'cxdnnyjw'

i = 0

p = [None] * 8

while True:
    ts = did + str(i)
    h = hashlib.md5(ts.encode('utf-8')).hexdigest()

    if h.startswith('00000'):
        print(i, h[:4],h[5],h[6],h[7:])

        try:
            pos = int(h[5])

            if (pos in range(len(p))) and not p[pos]:
                p[pos]= h[6]

                print(p)
        except:
            next

    if all(p):
        break

    i += 1

print(''.join(p))
