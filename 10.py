#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter
from collections import defaultdict

class Receiver(object):
    def __init__(self, n):
        self.num = n
        self.receives = []

    def print_all(self):
        print('Receiver %d receives: '%self.num, self.receives)

    def receive(self, n):
        if n not in self.receives:
            self.receives.append(n)

class Bin(Receiver):
    def __init__(self, n):
        Receiver.__init__(self, n)

    def print_all(self):
        print('Bin %d contains: '%self.num, self.receives)

    def run_all(self):
        pass

class Bot(Receiver):
    def __init__(self, n):
        Receiver.__init__(self, n)
        self.low_bot = None
        self.high_bot = None
        self.settled = False

    def low_to(self, bot):
        self.low_bot = bot

    def high_to(self, bot):
        self.high_bot = bot

    def run_all(self):
        if not self.settled and self.high_bot and self.low_bot and len(self.receives)==2:
            self.settled = True
            self.low_bot.receive(min(self.receives))
            self.high_bot.receive(max(self.receives))

            self.low_bot.run_all()
            self.high_bot.run_all()

    def print_all(self):
        print('Bot %d compares: '%self.num, self.receives)

bots = {}
outputs = {}

def get_or_create(d, num, cl):
    if num not in list(d.keys()):
        d[num] = cl(num)
    return d[num]

def get_bot(num):
    return get_or_create(bots, num, Bot)

def get_bin(num):
    return get_or_create(outputs, num, Bin)


regive = re.compile('bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)')
reval = re.compile('value (\d+) goes to bot (\d+)')

def get_it(t, num):
    if t == 'bot':
        return get_bot(num)
    elif t == 'output':
        return get_bin(num)
    else:
        return None

while True:
    try:
        line = sys.stdin.readline().rstrip()

        m = reval.match(line)

        if m:
            botnum = int(m.group(2))
            val = int(m.group(1))

            print('%d -> %d'%(val, botnum))

            get_bot(botnum).receive(val)

        m = regive.match(line)

        if m:
            botnum = int(m.group(1))
            b = get_bot(botnum)

            lowtype = m.group(2)
            lownum = int(m.group(3))

            hightype = m.group(4)
            highnum = int(m.group(5))

            low_to = get_it(lowtype,lownum)
            high_to = get_it(hightype,highnum)

            b.high_to(high_to)
            b.low_to(low_to)

            b.run_all()

    except KeyboardInterrupt:
        break

    if not line:
        break

for b in list(bots.keys()):
    bots[b].run_all()

for b in list(bots.keys()):
    bots[b].print_all()

for b in list(outputs.keys()):
    outputs[b].print_all()

print(outputs[0].receives[0]*outputs[1].receives[0]*outputs[2].receives[0])
