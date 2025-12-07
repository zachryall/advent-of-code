"""
Advent of Code 2020 - Day 6a - 6170
"""

from pathlib import Path

def main(file_name):
    """Main function
    """
    answer = 0

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        group = ''
        for line in lines:
            if line == '\n':
                answer += len(set(group))
                group = ''
            else:
                group += line.rstrip()
        answer += len(set(group))

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
