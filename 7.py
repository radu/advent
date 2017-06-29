#!/usr/bin/python3.5

import sys
import re
from pprint import *
#from operator import itemgetter


def find_brackets(s):
    return re.findall(r'\[\w*\]', s)

def find_doubles(s):
    m = re.findall(r'((\w)(\w)\3\2)', s)
    return [x[0] for x in m if x[1] != x[2]]

def find_bab(s):
    for x in find_brackets(s):
        pprint(s - x)

tls = []

while True:
    try:
        line = sys.stdin.readline().rstrip()

    except KeyboardInterrupt:
        break

    if not line:
        break


    n = False

    for b in find_brackets(line):
        if find_doubles(b):
            n = True

    if not n:
        x = find_doubles(line)

        if x:
            tls.append([line, x])

pprint(tls)
pprint(len(tls))
