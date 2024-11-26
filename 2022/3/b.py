"""
Advent of Code 2022 - Day 3b
"""

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    TOTAL = 0
    COUNTER = 0
    INDEX = 0

    while INDEX < len(lines):

        bagA = list(lines[INDEX][:-1])
        bagB = list(lines[INDEX + 1][:-1])
        bagC = list(lines[INDEX + 2][:-1])

        dupeAB = set(bagA).intersection(bagB)
        dupeBC = set(bagB).intersection(bagC)
        dupeAC = set(dupeAB).intersection(dupeBC)

        item = list(dupeAC)[0]

        if item.islower():
            TOTAL += ord(item) - 96
        else:
            TOTAL += ord(item) - 38

        INDEX += 3

    print(TOTAL)
