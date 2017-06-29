#!/usr/bin/python3.5

import sys

cdir = 0
ax = [[1, 0], [0, 1], [-1, 0], [0, -1]]

dirs = []
pos = [0,0]

while True:
	try:
		line = sys.stdin.readline().rstrip()
	except KeyboardInterrupt:
		break

	if not line:
		break

	dirs += line.split(', ')

print(dirs)

locs = []
doubles = []

for move in dirs:
	turn = move[0]
	num = int(move[1:])

	cdir += {'L': -1, 'R': +1}[turn]
	cdir = cdir % 4

	mov = ax[cdir]

	for i in range(num):
		pos = [a+b for (a,b) in zip(pos, mov)]
		if pos in locs:
			doubles.append(pos)
		locs.append(pos)

print(locs)
print(doubles)
print(sum([abs(x) for x in doubles[0]]))
