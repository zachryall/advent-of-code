"""
Advent of Code 2022 - Day 2b
"""

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    SCORE = 0

    for line in lines:

        if line[2] == 'Z':
            SCORE += 7
            if line[0] == 'A':
                SCORE += 1
            elif line[0] == 'B':
                SCORE += 2
        elif line[2] == 'Y':
            SCORE += 4
            if line[0] == 'B':
                SCORE += 1
            elif line[0] == 'C':
                SCORE += 2
        elif line[2] == 'X':
            SCORE += 1
            if line[0] == 'A':
                SCORE += 2
            elif line[0] == 'C':
                SCORE += 1

    print(SCORE)
