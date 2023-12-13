#!/usr/bin/env python3
# https://adventofcode.com/2023/day/3
#
from functools import reduce
import re
import sys

# CHECK: sample 467835
# CHECK: input 84495585

def parse():
    parts = []   # (num, x, y)
    gears = {}   # gears[(x, y)] = [NUM]

    for (y, l) in enumerate(sys.stdin):
       for m in re.finditer(r'(\d+|[^.])', l.strip()):
           val, x = m.group(), m.start()
           try:
               num = int(val)
               parts.append((num, m.start(), y))
           except ValueError:
               if val == '*':
                   gears[(x, y)] = []

    for (num, x, y) in parts:
        for (g_x, g_y) in adj_gears(gears, x, y, len(str(num))):
            gears[(g_x, g_y)].append(num)

    return (parts, gears)

def adj_gears(gears, x_min, y_min, width):
    adj = []
    for y in range(y_min - 1, y_min + 2):
        for x in range(x_min - 1, x_min + width + 1):
            if (x, y) in gears:
                adj.append((x, y))
    return adj


_, gears = parse()
total = 0
for v in gears.values():
    if len(v) != 2:
        continue
    total += reduce(lambda x, y: x * y, v, 1)

print(total)

