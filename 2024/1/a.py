"""
Advent of Code 2024 - Day 1a - 1830467
"""

idsA = []
idsB = []
TOTAL = 0

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        row = line.rstrip().split('   ')
        idsA.append(int(row[0]))
        idsB.append(int(row[1]))

idsA.sort()
idsB.sort()

for index, content in enumerate(idsA):
    TOTAL += abs(content - idsB[index])

print(TOTAL)
