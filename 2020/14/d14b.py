"""
Advent of Code 2020 - Day 12b - 4355897790573
"""

from pathlib import Path
import re
import itertools

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
        mem_position_b = f'{int(mem_position):b}'
        mem_position_b = mem_position_b.zfill(len(current_mask))
        mem_value = int(matches.group(2))

        for i in range(len(current_mask)-1, -1, -1): 
            if current_mask[i] == 'X':
                mem_position_b = mem_position_b[:i] + 'X' + mem_position_b[i + 1:]
            elif current_mask[i] == '1':
                mem_position_b = mem_position_b[:i] + '1' + mem_position_b[i + 1:]

        x_count = mem_position_b.count('X')

        combinations = itertools.product('01', repeat=x_count)

        resolved_addresses = []

        for combo in combinations:
            combo_list = list(combo)
            current_address = list(mem_position_b)
            combo_index = 0
            
            for i in range(len(current_address)):
                if current_address[i] == 'X':
                    current_address[i] = combo_list[combo_index]
                    combo_index += 1
            
            binary_address = "".join(current_address)
            
            decimal_address = int(binary_address, 2)
            resolved_addresses.append(decimal_address)

        for addr in resolved_addresses:
            memory[addr] = mem_value

    return sum(memory.values())


ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
