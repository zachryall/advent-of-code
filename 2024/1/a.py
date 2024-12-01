"""
Advent of Code 2024 - Day 1a - 1830467
"""

ANSWER = 0
idsA = []
idsB = []

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        row = line.rstrip().split('   ')
        idsA.append(int(row[0]))
        idsB.append(int(row[1]))

idsA.sort()
idsB.sort()

for index, content in enumerate(idsA):
    ANSWER += abs(content - idsB[index])

print(ANSWER)
