"""
Advent of Code 2020 - Day 12a - 9967721333886
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    
    memory = {}
    current_mask = 'x'
    for row in data:
        if 'mask' in row:
            current_mask = row[7:]
            continue

        matches = re.search(r'mem\[(\d+)] = (\d+)', row)
        mem_position = int(matches.group(1))
        mem_value = f'{int(matches.group(2)):b}'
        mem_value = mem_value.zfill(len(current_mask))

        for i in range(len(current_mask)-1, -1, -1): 
            if current_mask[i] != 'X':
                mem_value = mem_value[:i] + current_mask[i] + mem_value[i + 1:]
        memory[mem_position] = int(mem_value, 2)

    return sum(memory.values())


ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
