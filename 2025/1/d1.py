"""
Advent of Code 2025 - Day 1
"""

from pathlib import Path
import re


def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """
    answer = 0
    dial = 50

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            value = int(line[1:])
            direction = line[0]

            for _ in range(value):
                if direction == 'R':
                    dial += 1
                else:
                    dial -= 1

                dial %= 100

                if part == 2 and dial == 0:
                    answer += 1

            if part == 1 and dial == 0:
                answer += 1


    return answer

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')