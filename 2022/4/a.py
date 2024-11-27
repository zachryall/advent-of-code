"""
Advent of Code 2022 - Day 4a
"""

TOTAL = 0

with open('example.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        areas = line.split(',')

        firstArea = areas[0].split('-')
        firstLength = int(firstArea[1]) - int(firstArea[0]) + 1

        secondArea = areas[1].split('-')
        secondLength = int(secondArea[1]) - int(secondArea[0]) + 1


        if firstLength == secondLength and int(firstArea[0]) == int(secondArea[0]):
            TOTAL += 1
        elif firstLength > secondLength:
            if firstArea[0] <= secondArea[0] and firstArea[1] >= secondArea[1]:
                TOTAL += 1
        elif firstLength < secondLength:
            if firstArea[0] >= secondArea[0] and firstArea[1] <= secondArea[1]:
                TOTAL += 1

    print(TOTAL)
