#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2

import sys
import re
from functools import reduce

# CHECK: sample1 2286
# CHECK: input 54911

def parse(line):
    game_id, games_str = line.split(':')
    game_id = int(re.search(r'Game (\d+)', game_id).group(1))

    games = []
    for g in games_str.split(';'):
        g = g.strip()
        colors = {}
        for c in g.strip().split(','):
            num, color = c.split()
            colors[color] = int(num)
        games.append(colors)

    return (int(game_id), games)

def power(games):
    m = {}
    for g in games:
        for (c, n) in g.items():
            m[c] = max(m.get(c, 0), n)
    return reduce(lambda x, y: x * y, m.values(), 1)

total = 0
for line in sys.stdin:
    game_id, games = parse(line)
    total += power(games)

print(total) 
