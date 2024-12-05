"""
Advent of Code 2015 - Day 3
"""

from pathlib import Path
import hashlib

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """

    counter = 0
    key = 0
    found = False

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            key = line

    while not found:
        print(counter)
        to_search = key + str(counter)
        hash_output = hashlib.md5(to_search.encode('utf-8')).hexdigest()
        if (
            (hash_output.startswith('00000') and part == 1) or
            (hash_output.startswith('000000') and part == 2)
        ):
            found = True
        else:
            counter += 1

    print(counter)
    return counter

ANSWER_A, ANSWER_B = main('input.txt', 1), main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
