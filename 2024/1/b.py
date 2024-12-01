"""
Advent of Code 2024 - Day 1b
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

for content in idsA:
    TOTAL += content * (idsB.count(content))

print(TOTAL)
