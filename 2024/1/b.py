"""
Advent of Code 2024 - Day 1b - 26674158
"""

from pathlib import Path

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """
    ids_a = []
    ids_b = []
    answer = 0

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            row = line.rstrip().split('   ')
            ids_a.append(int(row[0]))
            ids_b.append(int(row[1]))

    for content in ids_a:
        answer += content * (ids_b.count(content))

    return answer

answer_example = main('example.txt')
answer_input = main('input.txt')

print(f'Example Input: {answer_example}')
print(f'Puzzle Input: {answer_input}')
