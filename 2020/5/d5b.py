"""
Advent of Code 2020 - Day 5b - 594
"""

from pathlib import Path
import re
import math

def main(file_name):
    """Main function
    """
    answer = []
    array = []

    path = Path(__file__).with_name(file_name)
    with path.open('r', encoding='UTF-8') as file:
        lines = file.readlines() 
        record = ''
        for line in lines:
            array.append(line)

    for boarding_pass in array:
        row_min = 0
        row_max = 127
        seat_min = 0
        seat_max = 7
        for x in range(len(boarding_pass)):
            if boarding_pass[x] == 'F':
                row_max -= math.ceil((row_max - row_min) / 2)
            elif boarding_pass[x] == 'B':
                row_min += math.ceil((row_max - row_min) / 2)
            elif boarding_pass[x] == 'L':
                seat_max -= math.ceil((seat_max - seat_min) / 2)
            elif boarding_pass[x] == 'R':
                seat_min += math.ceil((seat_max - seat_min) / 2)
        seat_id = (row_min * 8) + seat_min
        answer.append(seat_id)
    
    answer = sorted(answer)
    max = answer[-1]
    min = answer[0]
    expected_sum = (max - min + 1) * ((max + min) / 2)
    actual_sum = sum(answer)

    return abs(expected_sum - actual_sum)

ANSWER_INPUT = main('input.txt')
print(f'Puzzle Input: {ANSWER_INPUT}')
