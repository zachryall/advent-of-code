"""
Advent of Code 2022 - Day 10b
"""

REGISTER = 1
TOTAL = 0
SCREEN = ['.'] * 240
TRACKER = 0


def signal_check():
    if REGISTER in (TRACKER, TRACKER + 1, TRACKER + 2):
        print('woop')
        SCREEN[TRACKER] = '#'
    else:
        print('nope')

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
        line = line.rstrip()
        if line != 'noop':
            signal_check()
            TRACKER += 1
            REGISTER += int(line.split()[1])
            signal_check()
            TRACKER += 1
        else:
            signal_check()
            TRACKER += 1


    u, v, w, x, y, z = '', '', '', '', '', ''
    for i in range(0, 240):
        if i < 40:
            u += SCREEN[i]
        elif 40 <= i < 80:
            v += SCREEN[i]
        elif 80 <= i < 120:
            w += SCREEN[i]
        elif 120 <= i < 160:
            x += SCREEN[i]
        elif 160 <= i < 200:
            y += SCREEN[i]
        elif 200 <= i < 240:
            z += SCREEN[i]
    print(u)
    print(v)
    print(w)
    print(x)
    print(y)
    print(z)
