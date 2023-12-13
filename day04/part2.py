#!/usr/bin/env python3
# https://adventofcode.com/2023/day/4
#

import re
import sys
from collections import defaultdict

# CHECK: sample 30
# CHECK: input 15455663

def cards():
    cards = [] # (id, wins, nums)

    for l in sys.stdin:
        card_id, rest = l.strip().split(':')
        card_id = int(re.search(r'\d+$', card_id).group())

        wins, nums = rest.split('|')
        wins = [int(n) for n in wins.strip().split()]
        nums = [int(n) for n in nums.strip().split()]

        cards.append((card_id, wins, nums))
    return cards

def score(card):
    _, wins, nums = card
    score = 0
    return len([n for n in nums if n in wins])

count = defaultdict(lambda : 1)
for c in cards():
    card_id, _, _ = c
    mult = count[card_id]
    for other_id in range(card_id + 1, card_id + 1 + score(c)):
        count[other_id] = count[other_id] + mult

print(sum(count.values()))

