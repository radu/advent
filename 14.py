#!/usr/bin/env python

from hashlib import md5
from collections import deque
import re

salt = 'yjdafjpo'
#salt = 'abc'

hashes = deque()

triple = re.compile(r'([0-9a-f])\1\1')

hashdict = {}

searched = 0

def get_triple(h):
    m = triple.search(h)

    if m:
        return m.group(1)
    else:
        return None

def has_five(h, c):
    f = re.compile(c*5)
    return f.search(h)

#def hex_string(val):
#    return hex(val)[2:]

def search_1000(c):
    for i in range(1000):
        if has_five(hashes[i], c):
            return True

    return False

def hash_cache(m):
    if m in hashdict:
        return hashdict[m]
    else:
        d = md5(m).hexdigest()
        hashdict[m] = d
        return d

def gen_hash(num):
    code = salt+str(num)

    for i in range(2017):
        code = hash_cache(code)

    return code

SEARCH = 1000

for i in range(SEARCH+1):
    h = gen_hash(i)
    hashes.append(h)

found = []

while len(found) < 64:
    t = hashes.popleft()

    c = get_triple(t)

    if c:
        if search_1000(c):
            print('GOOD KEY: ',len(found), t, searched)
            found.append((searched, t))

    searched += 1
    hashes.append(gen_hash(SEARCH+searched))

print(found)
print(found[-1][0])
