"""
Advent of Code 2022 - Day 2a
"""

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    SCORE = 0

    for line in lines:
        SCORE += ord(line[2]) - 87

        diff = ord(line[2]) - ord(line[0])

        if diff in (21, 24):
            SCORE += 6
        elif diff == 23:
            SCORE += 3
        elif diff in (22, 25):
            SCORE += 0

    print(SCORE)
