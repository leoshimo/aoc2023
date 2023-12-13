#!/usr/bin/env python3
# https://adventofcode.com/2023/day/1

# CHECK: sample2 281
# CHECK: input 54676

import sys
import re

def norm(s):
    return s.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")

def num(line):
    matches = [m.group(1) for m in re.finditer("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)]
    num = norm(matches[0]) + norm(matches[-1])
    return int(num)

total = 0
for line in sys.stdin:
    total += num(line)
print(total)
