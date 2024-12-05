"""
Advent of Code 2015 - Day 3
"""

from pathlib import Path

def travel(directions_list):
    """Calculate Santa's travels

    Args:
        directions_list (list): A list of directions to be taken

    Returns:
        list: A list of coordinates that were travelled to
    """
    history = [0,0]
    x, y = 0, 0
    for arrow in directions_list:
        if arrow == '^':
            y += 1
        elif arrow == 'v':
            y -= 1
        elif arrow == '>':
            x += 1
        elif arrow == '<':
            x -= 1
        history.append(f'{x},{y}')
    return history

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    """

    answer = []
    directions = []
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            directions = list(line)

    if part == 1:
        answer = travel(directions)

    if part == 2:
        answer += travel(directions[::2])
        answer += travel(directions[1::2])
        answer.remove("0,0")

    answer = list(dict.fromkeys(answer))
    return len(answer)

ANSWER_A, ANSWER_B = main('input.txt', 1), main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B - 1}')
