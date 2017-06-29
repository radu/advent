#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter

regs='[a-d]'

inc = re.compile('inc (%s)'%regs)
dec = re.compile('dec (%s)'%regs)
cpyr = re.compile('cpy (%s) (%s)'%(regs,regs))
cpyv = re.compile('cpy (\d+) (%s)'%regs)
jnzr = re.compile('jnz (%s) (-?\d+)'%regs)
jnzv = re.compile('jnz (-?\d+) (-?\d+)')

_INC = 'inc'
_DEC = 'dec'
_CPYR = 'cpyr'
_CPYV = 'cpyv'
_JNZR = 'jnzr'
_JNZV = 'jnzv'

codes = [(_INC,inc), (_DEC,dec), (_CPYR,cpyr), (_CPYV,cpyv), (_JNZR,jnzr), (_JNZV, jnzv)]

cmds = []

while True:
    try:
        line = sys.stdin.readline().rstrip()
        for (cmd, c) in codes:
            m = c.match(line)
            if m:
                cmds.append((cmd, m.groups()))
                break


    except KeyboardInterrupt:
        break

    if not line:
        break

ptr = 0

rn = ['a', 'b', 'c', 'd']
rv = dict.fromkeys(rn, 0)

rv['c']=1


print(len(cmds))
print(rv)
pprint(cmds)

cn = 0

while ptr < len(cmds):
    c = cmds[ptr]

    if not cn%100000:
        print('%d %d -> '%(cn,ptr), c, rv)
    cn+=1

    cname = c[0]
    cargs = c[1]

    if cname == _INC:
        rv[cargs[0]] += 1
    elif cname == _DEC:
        rv[cargs[0]] -= 1
    elif cname == _CPYR:
        rv[cargs[1]] = rv[cargs[0]]
    elif cname == _CPYV:
        rv[cargs[1]] = int(cargs[0])

    if cname == _JNZR:
        if rv[cargs[0]]:
            ptr += int(cargs[1])
        else:
            ptr += 1
    elif cname == _JNZV:
        if int(cargs[0]):
            ptr+= int(cargs[1])
        else:
            ptr += 1
    else:
        ptr += 1


print(rv['a'])
