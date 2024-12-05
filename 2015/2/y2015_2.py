"""
Advent of Code 2015 - Day 2
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
        for line in lines:
            sides = [int(x) for x in line.rstrip().split('x')]
            sides.sort()

            if part == 1:
                area = (
                    sides[0] * sides[1] * 3 +
                    sides[1] * sides[2] * 2 +
                    sides[0] * sides[2] * 2
                )
            else:
                area = (
                    (sides[0] + sides[1]) * 2 +
                    sides[0] * sides[1] * sides[2]
                )
            answer += area

    return answer

ANSWER_A, ANSWER_B = main('input.txt', 1), main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
