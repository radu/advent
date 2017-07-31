#!/usr/bin/env python3

def next_state(index, size, limit):
    while True:
        if size == limit:
            return (limit, limit - index)

        add = ((index + ((size+1) // 2) - 1) % size ) + 1
        size = size + 1

        if index <= add:
           index = (size + index - 1) % size



i = 3005290
result = next_state(0,1,i)

print(result)

