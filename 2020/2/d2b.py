"""
Advent of Code 2020 - Day 2b - 284
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """
    answer = 0
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        for line in lines:
            result = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
            if (
                (result.group(4)[int(result.group(1)) - 1] == result.group(3)) 
                ^ (result.group(4)[int(result.group(2)) - 1] == result.group(3))
            ):
                answer += 1
    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
