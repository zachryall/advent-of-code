"""
Advent of Code 2020 - Day 15a - 421
"""

from pathlib import Path

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]

    numbers = data[0].split(',')
    numbers = [int(s.strip()) for s in numbers]

    history = {
        number: i
        for i, number in enumerate(numbers[:-1])
    }

    previous_number = numbers[-1]

    for i in range(len(numbers) - 1, 2020 - 1):

        if previous_number in history:
            last_spoken_turn = history[previous_number]
            next_number = i - last_spoken_turn
        else:
            next_number = 0

        history[previous_number] = i
        previous_number = next_number

    return previous_number


ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
