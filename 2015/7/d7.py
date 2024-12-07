"""
Advent of Code 2024 - Day 6
"""

from pathlib import Path
from collections import Counter

import signal
import readchar

def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        print(values)
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)

signal.signal(signal.SIGINT, handler)

values = {}
circuit = []

def main(file_name, part):
    """Main function

    Args:
        file_name (str): The input file to use
        part (int): Whether to process for part 1 or 2

    Returns:
        _type_: _description_
    """

    answer = 0

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            circuit.append(line.strip().split(' '))
            split = line.strip().split(' ')
            if split[0].isdigit():
                values[split[-1]] = int(split[0])
            else:
                values[split[-1]] = 0

    finished = False
    while not finished:
        print(f'Values left to find: {Counter(values.values())[0]}/{len(values)}')
        if all(x != 0 for x in values.values()):
            finished = True
            print(f'finished: {values}')
            break

        values_copy = values.copy()
        for key, value in values_copy.items():
            if value != 0:
                for y in circuit:
                    # print(y)
                    # if y[2].isdigit():
                    #     print(f'{values[y[0]]} {y[1]} {y[2]} = {values[y[4]]}')
                    # elif y[0] == 'NOT':
                    #     print(f'{y[0]} {values[y[1]]} = {values[y[3]]}')
                    # elif y[0].isdigit() and y[1] == 'AND':
                    #     print(f'{y[0]} {y[1]} = {values[y[4]]}')
                    # elif y[1] == '->':
                    #     print(f'{y[0]} = {y[1]}')
                    # else:
                    #     print(f'{values[y[0]]} {y[1]} {values[y[2]]} = {values[y[4]]}')

                    if y[1] == '->' and y[0] == key:
                        values[y[2]] = values[y[0]]
                    elif y[1] == '->' and y[2] == key:
                        values[y[0]] = values[y[2]]
                    elif y[0] == 'NOT' and y[1] == key:
                        if ~values[y[1]] < 0:
                            values[y[3]] = 65536 + ~values[y[1]]
                        else:
                            values[y[3]] = ~values[y[1]]
                    elif y[0] == 'NOT' and y[3] == key:
                        if ~values[y[3]] < 0:
                            values[y[1]] = 65536 + ~values[y[3]]
                        else:
                            values[y[1]] = ~values[y[3]]
                    elif y[1] == 'LSHIFT' and y[0] == key:
                        if (values[y[0]] << 2) < 0:
                            values[y[4]] = 65536 + (values[y[0]] << 2)
                        else:
                            values[y[4]] = values[y[0]] << 2
                    elif y[1] == 'RSHIFT' and y[0] == key:
                        if (values[y[0]] >> 2) < 0:
                            values[y[4]] = 65536 + (values[y[0]] >> 2)
                        else:
                            values[y[4]] = values[y[0]] >> 2
                    elif y[1] == 'AND' and y[0] == key and values[y[2]] != 0:
                        if (values[y[0]] & values[y[2]]) < 0:
                            values[y[4]] = 65536 + (values[y[0]] & values[y[2]])
                        else:
                            values[y[4]] = values[y[0]] & values[y[2]]
                    elif y[1] == 'AND' and y[0] == 1 and values[y[2]] != 0:
                        if (1 & values[y[2]]) < 0:
                            values[y[4]] = 65536 + (1 & values[y[2]])
                        else:
                            values[y[4]] = 1 & values[y[2]]
                    elif y[1] == 'OR' and y[0] == key and values[y[2]] != 0:
                        if (values[y[0]] | values[y[2]]) < 0:
                            values[y[4]] = 65536 + (values[y[0]] | values[y[2]])
                        else:
                            values[y[4]] = values[y[0]] | values[y[2]]

    return answer

# ANSWER_EXAMPLE_A = main('example.txt', 1)
ANSWER_INPUT_A = main('input.txt', 1)
# ANSWER_EXAMPLE_B = main('example.txt', 2)
# ANSWER_INPUT_B = main('input.txt', 2)

# print(f'A Example Input: {ANSWER_EXAMPLE_A}')
print(f'A Puzzle Input: {ANSWER_INPUT_A}')
# print(f'B Example Input: {ANSWER_EXAMPLE_B}')
# print(f'B Puzzle Input: {ANSWER_INPUT_B}')
