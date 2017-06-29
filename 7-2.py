#!/usr/bin/python3.5

import sys
import re
from itertools import chain
import regex
#from operator import itemgetter

from colorama import init, Fore, Style

init(strip=False)

def find_brackets(s):
    return re.findall(r'\[\w*\]', s)

def find_doubles(s):
    m = re.findall(r'((\w)(\w)\3\2)', s)
    return [x[0] for x in m if x[1] != x[2]]

def split_br(s):
    br = []
    nbr = [s]

    for x in find_brackets(s):
        br.append(x)
        nbr = list(chain(*[n.split(x) for n in nbr]))

    return br,nbr

def find_bab(s):
    ma = regex.findall(r'(\w)(\w)\1', s,overlapped=True)

    marr = []

    for m in ma:
        if m[0] != m[1]:
            marr.append((m[0], m[1]))

    return marr

def find_aba(s,aba):
    m = re.findall(r'%s'%aba,s)
    if m:
        print(m)
    return m


ssll = []

while True:
    try:
        line = sys.stdin.readline().rstrip()

    except KeyboardInterrupt:
        break

    if not line:
        break

    bap = []

    (br,nbr) = split_br(line)


    for b in br:
       x = find_bab(b)
       if x:
           bap.append(x)


    if bap:
        bap = list(chain(*bap))
        ssl = False

        linef = line

        for n in nbr:
            for (b,a) in bap:
                aba = a+b+a
                bab = b+a+b
                abam = find_aba(n,aba)
                if abam:
                    print(bab,abam)
                    linef = linef.replace(aba, Fore.RED+aba+Style.RESET_ALL)
                    linef = linef.replace(bab, Fore.GREEN+bab+Style.RESET_ALL)
                    ssl = True

        if ssl:
            ssll.append(linef)

for l in ssll:
    print(l)

print(len(ssll))
