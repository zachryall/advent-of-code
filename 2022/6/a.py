"""
Advent of Code 2022 - Day 6a - 1080
"""

MESSAGE_LENGTH = 4

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        lineList = list(line)

        for i in range(0,len(lineList)-3):
            checkList = []
            for j in range(MESSAGE_LENGTH):
                checkList += lineList[i + j]
            dedupe = list(dict.fromkeys(checkList))
            if len(dedupe) == MESSAGE_LENGTH:
                print(f'marker - {i + MESSAGE_LENGTH}')
                break
