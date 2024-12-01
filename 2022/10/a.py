"""
Advent of Code 2022 - Day 10a - 13860
"""

REGISTER = 1
CYCLE = 2
TOTAL = 0


def signal_check():
    """
    Calculate the signal strength if on the correct cycle
    :return: The value to add to the TOTAL
    """
    # if CYCLE is 1, 2
    if CYCLE in (20, 60, 100, 140, 180, 220):
        print(f'Cycles: {CYCLE}, Register: {REGISTER}, Signal Strength: {CYCLE * REGISTER}')
        return CYCLE * REGISTER
    return 0


with open('example.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        line = line.rstrip()
        if line != 'noop':
            REGISTER += int(line.split()[1])
            CYCLE += 1
            TOTAL += signal_check()
            CYCLE += 1
            TOTAL += signal_check()
        else:
            CYCLE += 1
            TOTAL += signal_check()

    print(f'Final Register Value: {REGISTER}')
    print(f'Total Cycles: {CYCLE}')
    print(f'Signal Strength Sum: {TOTAL}')
