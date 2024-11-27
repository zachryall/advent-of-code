"""
Advent of Code 2022 - Day 4b - 903
"""

import re

TOTAL = 0

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        split = re.split('[-,]', line.rstrip())

        if int(split[0]) <= int(split[3]) and int(split[1]) >= int(split[2]):
            TOTAL += 1

    print(TOTAL)
