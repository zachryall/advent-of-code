"""
Advent of Code 2020 - Day 8b - 1643
"""

from pathlib import Path
import copy
import re

def sequence_checker(new_instructions):
    index = 0
    result = 0
    while index < len(new_instructions):
        if new_instructions[index]['visited'] == 1:
            return None
        
        new_instructions[index]['visited'] = 1
        jump = 1

        if new_instructions[index]['cmd'] == 'acc':
            result += new_instructions[index]['val']
        elif new_instructions[index]['cmd'] == 'jmp':
            jump = new_instructions[index]['val']
        index += jump

    return result

def main(file_name):
    """Main function
    """
    instructions = []

    path = Path(__file__).with_name(file_name)
    lines = path.read_text(encoding='UTF-8').strip().split('\n') 
    for line in lines:
        match = re.match(r'(\w{3}) ([+-])(\d+)', line)
        command, sign, number_str = match.groups()
        number = int(sign + number_str)
        instructions.append({'cmd': command, 'val': number, 'visited': 0})

    answer = 0
    for i in range(len(instructions)):
        instructions_modified = copy.deepcopy(instructions)
        if instructions_modified[i]['cmd'] == 'nop':
            instructions_modified[i]['cmd'] = 'jmp'
        elif instructions_modified[i]['cmd'] == 'jmp':
            instructions_modified[i]['cmd'] = 'nop'
        else:
            continue

        answer = sequence_checker(instructions_modified)

        if answer is not None:
            return answer
    return 0


ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
