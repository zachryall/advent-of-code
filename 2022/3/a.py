"""
Advent of Code 2022 - Day 3a
"""

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    TOTAL = 0

    for line in lines:
        firstCompartment = list(line[:len(line) // 2])
        secondCompartment = list(line[len(line) // 2:-1])

        duplicateSet = set(firstCompartment).intersection(secondCompartment)

        item = list(duplicateSet)[0]

        if item.islower():
            TOTAL += ord(item) - 96
        else:
            TOTAL += ord(item) - 38

    print(TOTAL)
