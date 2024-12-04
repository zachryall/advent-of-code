"""
Advent of Code 2024 - Day 4a - 2011
"""

from pathlib import Path

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """
    data = []
    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            data.append(list(line.rstrip()))

    for j in range(len(data[0]) - 2):
        for i in range(len(data) - 2):
            to_check = data[i][j] + data[i][j+2] + data[i+1][j+1] + data[i+2][j] + data[i+2][j+2]
            if to_check in ('MMASS', 'SMASM', 'SSAMM', 'MSAMS'):
                answer += 1
    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
