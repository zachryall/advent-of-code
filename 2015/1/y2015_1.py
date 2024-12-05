"""
Advent of Code 2015 - Day 1
"""

from pathlib import Path

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """

    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        current_floor = 0
        for line in lines:
            for i, x in enumerate(line):
                if x == '(':
                    current_floor += 1
                else:
                    current_floor -= 1

                if part == 2 and current_floor == -1:
                    answer = i + 1
                    break
        if part == 1:
            answer = current_floor

    return answer

ANSWER_A, ANSWER_B = main('input.txt', 1), main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
