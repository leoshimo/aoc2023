#!/usr/bin/env python3
# https://adventofcode.com/2023/day/5
#

import re
import sys
from collections import defaultdict

# CHECK: sample 35
# CHECK: input 535088217

def parse():
    seeds = [int(n) for n in sys.stdin.readline().split(':')[-1].strip().split()] # [seed_1, seed_2, ...]
    maps = defaultdict(list)
    last = None

    for l in sys.stdin:
        l = l.strip()
        if not l: continue
        m = re.search(r'(.*) map:$', l)
        if m:
            last = m.group(1)
        else:
            dst_min, src_min, span = l.split()
            maps[last].append((int(src_min), int(dst_min), int(span)))

    return (seeds, dict(maps))

def to_dst(val, mapping):
    for (src_min, dst_min, span) in mapping:
        if val in range(src_min, src_min + span):
            return dst_min + val - src_min
    return val

cur = 'seed'
vals, maps = parse()
while cur != 'location':
    dst, m = next(((k.split('-')[-1], m) for (k, m) in maps.items() if k.startswith(cur)))
    vals = [to_dst(v, m) for v in vals]
    cur = dst
    # print(cur, vals, m)

print(min(vals))

