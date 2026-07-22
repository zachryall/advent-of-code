"""
Advent of Code 2025 - Day 3
"""

from pathlib import Path
import re


def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """
    answer = 0
    max_length = 2

    if part == 2:
        max_length = 12

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        bank = file.readlines()
        for battery in bank:
            battery = battery.strip()
            max_value = ''
            pointer = 0

            length = max_length
            for _ in range(length):
                largest_digit = max(battery[pointer:len(battery) - length + 1])
                index = battery.index(largest_digit, pointer)
                pointer = index + 1
                length -= 1
                max_value += largest_digit
            
            answer += int(max_value)

    return answer

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')