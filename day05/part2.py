#!/usr/bin/env python3
# https://adventofcode.com/2023/day/5
#

# Attempt 1: Brute Force: Failed. Too many numbers to check

import re
import sys
from collections import defaultdict

# CHECK: sample 46
# NCHECK: input

def parse():
    raw_seeds = sys.stdin.readline().split(':')[-1].strip()
    seeds = [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r'(\d+) (\d+)', raw_seeds)] # (id_min, id_span)
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

seeds, maps = parse()
loc_min = sys.maxsize

for (s_min, s_span) in seeds:
    for s in range(s_min, s_min + s_span):
        cur = 'seed'
        v = s
        while cur != 'location':
            dst, m = next(((k.split('-')[-1], m) for (k, m) in maps.items() if k.startswith(cur)))
            v = to_dst(v, m)
            cur = dst
        loc_min = min(loc_min, v)
        print(s, "=>", v, "min =>", loc_min)

print(loc_min)
