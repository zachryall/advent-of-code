"""
Advent of Code 2015 - Day 5
"""

from pathlib import Path
import re

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """

    answer = 0

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            if part == 1:
                if (
                    len(re.findall('[aeiou]', line)) >= 3 and
                    re.search('([a-z])\\1', line) and
                    re.search('^(?!.*(ab|cd|pq|xy)).*$', line)
                ):
                    answer += 1
            else:
                if (
                    re.search('(\\w).\\1', line) and
                    re.search('(\\w{2}).*\\1', line)
                ):
                    answer += 1

    return answer

ANSWER_A, ANSWER_B = main('input.txt', 1), main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
