#!/usr/bin/env python3
# https://adventofcode.com/2023/day/1

# CHECK: sample1 142
# CHECK: input 53921

import sys

def first_digit(s):
    return next((c for c in s if c.isdigit()))

total = 0
for line in sys.stdin:
    num = first_digit(line) + first_digit(line[::-1])
    total += int(num)

print(total)

