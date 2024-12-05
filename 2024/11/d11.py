"""
Advent of Code 2024 - Day 11
"""

from pathlib import Path
from collections import Counter
from functools import cache

@cache
def calculate(stone):
    """Calculate the how the stone changes according to the rules

    Args:
        stone (int): The value of the stone

    Returns:
        list: The new value of the stone or stones
    """
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        return [
            str(int(stone[:len(str(stone))//2])),
            str(int(stone[len(str(stone))//2:]))
        ]
    return [str(int(stone) * 2024)]

def main(file_name, blinks_limit):
    """Main function

    Args:
        file_name (str): The input file to use
        blinks (int): Number of blinks to iterate over

    Returns:
        int: The answer of the challenge
    """

    stones = []

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        stones = lines[0].split(' ')

    old = Counter(stones)

    for x in range(blinks_limit):
        print(f'Blink number {x+1}...')
        new = Counter()
        for stone, _ in old.items():
            for result in calculate(stone):
                new[result] += old[stone]
        old = new

    return sum(old.values())

ANSWER_EXAMPLE_A = main('example.txt', 6)
ANSWER_INPUT_A = main('input.txt', 25)
ANSWER_INPUT_B = main('input.txt', 75)

print(f'A Example Input: {ANSWER_EXAMPLE_A}')
print(f'A Puzzle Input: {ANSWER_INPUT_A}')
print(f'B Puzzle Input: {ANSWER_INPUT_B}')
