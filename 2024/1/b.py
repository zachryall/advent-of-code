"""
Advent of Code 2024 - Day 1b - 26674158
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

for content in idsA:
    ANSWER += content * (idsB.count(content))

print(ANSWER)
