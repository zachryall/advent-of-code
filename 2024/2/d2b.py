"""
Advent of Code 2024 - Day 2a - 591
"""

from pathlib import Path

def check_list(levels_list):
    """Checks whether the list of levels meet the criteria

    :param levels_list: List of levels
    :return: Whether the list is valid
    """
    increasing, valid = True, True

    if levels_list[1] < levels_list[0]:
        increasing = False

    for x in range(0, len(levels_list) - 1):
        rules = [
            increasing and levels_list[x + 1] < levels_list[x],
            not increasing and levels_list[x + 1] > levels_list[x],
            not 1 <= abs(levels_list[x + 1] - levels_list[x]) <= 3
        ]

        if any(rules):
            valid = False
            break

    if valid:
        return True

    return False

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

            if check_list(values):
                answer += 1
            else:
                for i in range(len(values)):
                    safety_list = values[:i] + values[i+1:]
                    if check_list(safety_list):
                        answer += 1
                        break



    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
