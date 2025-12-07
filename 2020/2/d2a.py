"""
Advent of Code 2020 - Day 2a - 517
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
            count = result.group(4).count(result.group(3))
            if int(result.group(1)) <= count <= int(result.group(2)):
                answer += 1
    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
