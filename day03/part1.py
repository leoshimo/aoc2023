#!/usr/bin/env python3
# https://adventofcode.com/2023/day/3
#
import re
import sys

# CHECK: sample 4361
# CHECK: input 544664

def parse():
    parts = []  # (num, x, y)
    syms = {}   # syms[(x, y)] = '*'

    for (y, l) in enumerate(sys.stdin):
       for m in re.finditer(r'(\d+|[^.])', l.strip()):
           val, x = m.group(), m.start()
           try:
               num = int(val)
               parts.append((num, m.start(), y))
           except ValueError:
               syms[(x, y)] = val
    return (parts, syms)

def is_adj(syms, x_min, y_min, width):
    for y in range(y_min - 1, y_min + 2):
        for x in range(x_min - 1, x_min + width + 1):
            if (x, y) in syms:
                return True
    return False


total = 0
parts, syms = parse()
for (num, x, y) in parts:
    if is_adj(syms, x, y, len(str(num))):
        total += num
print(total)

