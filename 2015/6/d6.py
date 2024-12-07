"""
Advent of Code 2024 - Day 6
"""

from pathlib import Path
import re

def change_on_part(part, lights_list, instruction, x, y):
    """Using the part variable to determine how to follow the instructions

    Args:
        part (int): The part of the challenge
        lights_list (list): The nested list of lights
        instruction (str): The instruction to follow
        x (int): The x coordinate to change
        y (int): The y coordinate to change
    """
    if instruction.startswith('turn on'):
        if part == 1:
            lights_list[y][x] = 1
        else:
            lights_list[y][x] += 1
    elif instruction.startswith('toggle'):
        if part == 2:
            lights_list[y][x] += 2
        elif lights_list[y][x] == 1:
            lights_list[y][x] = 0
        elif lights_list[y][x] == 0:
            lights_list[y][x] = 1
    else:
        if part == 1:
            lights_list[y][x] = 0
        elif lights_list[y][x] > 0:
            lights_list[y][x] -= 1

def change_lights(instruction, lights_list, part):
    """Changes the christmas lights due to a specific instruction

    Args:
        instruction (str): How to change the lights
        lights_list (list): A nested list of the current state of the lights

    Returns:
        list: The amended christmas lights
    """
    mod = 1
    split = re.split(r'[ ,]', instruction)
    if instruction.startswith('toggle'):
        mod = 0

    for x in range(int(split[1 + mod]), int(split[4 + mod]) + 1):
        for y in range(int(split[2 + mod]), int(split[5 + mod]) + 1):
            change_on_part(part, lights_list, instruction, x, y)

    return lights_list

def main(file_name, part):
    """Main function

    Args:
        file_name (str): The input file to use
        part (int): Whether to process for part 1 or 2

    Returns:
        _type_: _description_
    """

    answer = 0
    lights = [[0]*1000 for _ in range(1000)]
    instructions = []

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            instructions.append(line.strip())

    for instruction in instructions:
        lights = change_lights(instruction, lights, part)

    for row in lights:
        for x in row:
            answer += x

    return answer

ANSWER_EXAMPLE_A = main('example.txt', 1)
ANSWER_INPUT_A = main('input.txt', 1)
ANSWER_EXAMPLE_B = main('example.txt', 2)
ANSWER_INPUT_B = main('input.txt', 2)

print(f'A Example Input: {ANSWER_EXAMPLE_A}')
print(f'A Puzzle Input: {ANSWER_INPUT_A}')
print(f'B Example Input: {ANSWER_EXAMPLE_B}')
print(f'B Puzzle Input: {ANSWER_INPUT_B}')
