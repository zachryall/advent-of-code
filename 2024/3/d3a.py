"""
Advent of Code 2024 - Day 2a - 181345830
"""

from pathlib import Path
import re

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """

    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
            for match in matches:
                values = [int(x) for x in match[4:-1].split(',')]
                answer += values[0] * values[1]

    return answer

ANSWER_EXAMPLE = main('exampleA.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
