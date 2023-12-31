#!/usr/bin/env python3
# https://adventofcode.com/2023/day/2

import sys
import re

# CHECK: sample1 8
# CHECK: input 2476

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

def is_possible(games, limit):
    return all(n <= limit.get(c, 0) for g in games for (c, n) in g.items())

total = 0
limit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
for line in sys.stdin:
    game_id, games = parse(line)
    possible = True
    if is_possible(games, limit):
        total += game_id

print(total) 
