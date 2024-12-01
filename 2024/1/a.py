"""
Advent of Code 2024 - Day 1a - 1830478
"""

from pathlib import Path

ids_a = []
ids_b = []

def main(file_name):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """

    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            row = line.rstrip().split('   ')
            ids_a.append(int(row[0]))
            ids_b.append(int(row[1]))

    ids_a.sort()
    ids_b.sort()

    for index, content in enumerate(ids_a):
        answer += abs(content - ids_b[index])
    return answer

answer_example = main('example.txt')
answer_input = main('input.txt')

print(f'Example Input: {answer_example}')
print(f'Puzzle Input: {answer_input}')
