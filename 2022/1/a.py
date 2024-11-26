"""
Advent of Code 2022 - Day 1a
"""

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    array = []
    CALORIE_COUNT = 0

    for line in lines:
        if line == '\n':
            array.append(CALORIE_COUNT)
            CALORIE_COUNT = 0
        else:
            CALORIE_COUNT += int(line)

    array.append(CALORIE_COUNT)

    array.sort(reverse=True)
    print(array[0])
