#!/usr/bin/python3.5

import sys
import re
from pprint import pprint
#from operator import itemgetter

while True:
    try:
        line = sys.stdin.readline().rstrip()

        print(line)

    except KeyboardInterrupt:
        break

    if not line:
        break


