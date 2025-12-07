"""
Advent of Code 2020 - Day 1a - 1018336
"""

from pathlib import Path

def main(file_name):
    """Main function
    """
    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        for i, line in enumerate(lines):
            x = i + 1
            while i + x < len(lines):
                if int(line) + int(lines[i+x]) == 2020:
                    answer = int(line) * int(lines[i+x])
                    break
                else:
                    x += 1
            if answer != 0:
                break
    return answer

# ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

# print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
