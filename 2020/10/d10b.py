"""
Advent of Code 2020 - Day 10b - 
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [int(row) for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    data.append(0)
    data.append(max(data) + 3)
    data.sort()

    paths = [0] * (max(data) + 1)
    paths[0] = 1

    for index in range(1, max(data) + 1):
        for x in range(1, 4):
            if (index - x) in data:
                paths[index] += paths[index - x]
    print(paths)
    return paths[-1]

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
