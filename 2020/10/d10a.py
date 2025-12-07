"""
Advent of Code 2020 - Day 10a - 2664
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [int(row) for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    data.sort()
    data.append(data[-1] + 3)
    data.insert(0, 0)

    diff_count_one = 0
    diff_count_three = 0

    for index, value in enumerate(data):
        try:
            if data[index + 1] - value == 1:
                diff_count_one += 1
            elif data[index + 1] - value == 3:
                diff_count_three += 1
        except IndexError:
            break

    return diff_count_one * diff_count_three

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
