"""
Advent of Code 2024 - Day 2a - 591
"""

from pathlib import Path

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """

    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            values = [int(x) for x in line.rstrip().split(' ')]
            increasing, valid = True, True

            if values[1] < values[0]:
                increasing = False

            for x in range(0, len(values) - 1):
                rules = [
                    increasing and values[x + 1] < values[x],
                    not increasing and values[x + 1] > values[x],
                    not 1 <= abs(values[x + 1] - values[x]) <= 3
                ]

                if any(rules):
                    valid = False
                    break

            if valid:
                answer += 1

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
