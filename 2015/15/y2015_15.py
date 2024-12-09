"""
Advent of Code 2015 - Day 15
"""

from pathlib import Path

def process_data(file_name):
    """Generate a nested list from the input file

    Args:
        file_name (str): The file name to process

    Returns:
        list: Nested list of input file
    """
    data = []
    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            split = line.strip().split(' ')
            data.append([
                split[0][:-1],
                int(split[2][:-1]),
                int(split[4][:-1]),
                int(split[6][:-1]),
                int(split[8][:-1]),int(split[10])
            ])
    return data

def main(file_name, part):
    """Main function

    :param file_name: The file that contexts the puzzle input
    :param part: The part of the challenge
    """

    answer = 0
    data = process_data(file_name)

    for a in range(100):
        for b in range(100 - a):
            for c in range(100 - a - b):
                d = 100 - a - b - c

                score = 1
                for x in range(1, len(data[0]) - 1):
                    running = data[0][x] * a + data[1][x] * b + data[2][x] * c + data[3][x] * d
                    if running < 0:
                        score = 0
                    else:
                        score *= running

                calories = data[0][5] * a + data[1][5] * b + data[2][5] * c + data[3][5] * d

                if part == 1 or (part == 2 and calories == 500):
                    answer = max(answer, score)



    return answer

ANSWER_A = main('input.txt', 1)
ANSWER_B = main('input.txt', 2)
print(f'Part 1 - Puzzle Input: {ANSWER_A}')
print(f'Part 2 - Puzzle Input: {ANSWER_B}')
