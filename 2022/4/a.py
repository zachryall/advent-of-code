"""
Advent of Code 2022 - Day 4a - 530
"""

import re

TOTAL = 0

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        trim = line.rstrip()
        areas = trim.split(',')

        split = re.split('[-,]', line.rstrip())

        firstLength = int(split[1]) - int(split[0])
        secondLength = int(split[3]) - int(split[2])

        if firstLength == secondLength:
            if int(split[0]) == int(split[2]):
                TOTAL += 1
        elif firstLength > secondLength:
            if split[0] <= split[2] and split[1] >= split[3]:
                TOTAL += 1
        elif firstLength < secondLength:
            if split[0] >= split[2] and split[1] <= split[3]:
                TOTAL += 1

    print(TOTAL)
