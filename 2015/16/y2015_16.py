"""
Advent of Code 2015 - Day 16
"""

from pathlib import Path
import re


def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """

    answer = 0
    data = {}
    aunt = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            split = re.split(': |, ', line.strip())
            data[split[0]] = {}
            for x in range(1, len(split), 2):
                data[split[0]][split[x]] = int(split[x + 1])

    for key, value in data.items():
        match = True
        for key_b, _ in value.items():
            if part == 1 and value[key_b] != aunt[key_b]:
                match = False

            if part == 2:
                if key_b in ('cats', 'trees'):
                    if value[key_b] <= aunt[key_b]:
                        match = False
                elif key_b in ('pomeranians', 'goldfish'):
                    if value[key_b] >= aunt[key_b]:
                        match = False
                elif value[key_b] != aunt[key_b]:
                    match = False
        if match:
            answer = int(key[4:])

    return answer

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
