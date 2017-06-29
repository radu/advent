#!/usr/bin/env python2.7

n = 3005290

def last(n):
    en = 0
    skip = 1

    while en+skip < n:
        if (n / skip) % 2:
            en = en + skip*2

        skip = skip << 1

    return(en+1)

print([(a,last(a)) for a in [5,6,7,8,9,10,n]])
