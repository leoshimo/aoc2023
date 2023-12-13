#!/usr/bin/env python3
# https://adventofcode.com/2023/day/4
#

import sys

# CHECK: sample 13
# CHECK: input 23678

def cards():
    cards = [] # (wins, nums)
    for l in sys.stdin:
        _, rest = l.strip().split(':')
        wins, nums = rest.split('|')
        wins = [int(n) for n in wins.strip().split()]
        nums = [int(n) for n in nums.strip().split()]

        cards.append((wins, nums))
    return cards

def score(card):
    wins, nums = card
    score = 0
    for n in nums:
        if n in wins:
            score = 1 if score == 0 else score * 2
    return score

total = 0
for c in cards():
    total += score(c)
print(total)
