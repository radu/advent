#!/usr/bin/env python2.7

from string import maketrans
from collections import deque


def dragon(a):
    b = ''.join([a,
                 '0',
                 a[::-1].translate(maketrans("10","01"))])
    return b

def checksum(v):
    v = deque(v)
    c = []
    while v:
        a,b = v.popleft(), v.popleft()
        c.append('1' if a == b else '0')

    return ''.join(c)

b = '11011110011011101'
#b = '10000'

req_chars = 272
#req_chars = 20
req_chars = 35651584

while len(b) < req_chars:
    b = dragon(b)

c = b[:req_chars]
#print(c)

while True:
    c = checksum(c)
    if len(c)%2:
        break
    #print(c)

print(c)
