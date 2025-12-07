"""
Advent of Code 2020 - Day 8a - 1262
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """
    answer = 0
    instructions = []

    path = Path(__file__).with_name(file_name)
    lines = path.read_text(encoding='UTF-8').strip().split('\n') 
    for line in lines:
        match = re.match(r'(\w{3}) ([+-])(\d+)', line)
        command, sign, number = match.groups()
        number = int(number)
        if sign == '-':
            number *= -1
        instructions.append({'cmd': command, 'val': number, 'visited': 0})
    
    index = 0
    while index < len(instructions):
        if instructions[index]['visited'] == 1:
            break
        
        instructions[index]['visited'] = 1
        jump = 1

        if instructions[index]['cmd'] == 'acc':
            answer += instructions[index]['val']
        elif instructions[index]['cmd'] == 'jmp':
            jump = instructions[index]['val']
        index += jump

    return answer

ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
