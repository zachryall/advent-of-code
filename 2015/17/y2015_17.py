"""
Advent of Code 2015 - Day 17
"""

from pathlib import Path
import itertools


def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """

    answer = 0
    goal = 150
    data = []

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            data.append(int(line.strip()))

    for length in range(1, len(data) + 1):
        perms = list(itertools.combinations(data, length))
        for perm in perms:
            if sum(perm) == goal:
                answer += 1
        if part == 2 and answer > 0:
            break

    return answer

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
