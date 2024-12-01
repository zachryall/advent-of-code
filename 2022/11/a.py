"""
Advent of Code 2022 - Day 11a - 50172
"""

import math

monkey_info = {}

with open('input.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for index, line in enumerate(lines):
        if line.startswith('Monkey'):
            split = line.split()
            monkey_info[split[1].rstrip(":")] = {
                'items': [],
                'operation': {
                    'operator': lines[index + 2].split()[4].strip(),
                    'value': lines[index + 2].split()[5].strip()
                },
                'test': int(lines[index + 3].split()[3].strip()),
                'true': lines[index + 4].split()[5].strip(),
                'false': lines[index + 5].split()[5].strip(),
                'inspect_count': 0
            }
            items = list(lines[index + 1].split(': '))
            for item in items[1].split(', '):
                monkey_info[split[1].rstrip(":")]['items'].append(int(item.rstrip()))

for game_round in range(20):
    for x in range(len(monkey_info)):
        ITEM_CHECKED = 0
        for item in monkey_info[str(x)]['items']:
            worry_level = item
            if monkey_info[str(x)]['operation']['operator'] == '*':
                if monkey_info[str(x)]['operation']['value'] == 'old':
                    worry_level = worry_level ** 2
                else:
                    worry_level = worry_level * int(monkey_info[str(x)]['operation']['value'])
            if monkey_info[str(x)]['operation']['operator'] == '+':
                if monkey_info[str(x)]['operation']['value'] == 'old':
                    worry_level = worry_level * 2
                else:
                    worry_level = worry_level + int(monkey_info[str(x)]['operation']['value'])

            worry_level = math.floor(worry_level / 3)

            if worry_level % monkey_info[str(x)]['test'] == 0:
                next_monkey = monkey_info[str(x)]['true']
            else:
                next_monkey = monkey_info[str(x)]['false']

            monkey_info[next_monkey]['items'].append(worry_level)
            ITEM_CHECKED += 1
            monkey_info[str(x)]['inspect_count'] += 1

        for y in range(ITEM_CHECKED):
            monkey_info[str(x)]['items'].pop()

INSPECT_LIST = []
for z in range(len(monkey_info)):
    INSPECT_LIST.append(monkey_info[str(z)]['inspect_count'])
INSPECT_LIST.sort(reverse=True)

print(f'Monkey Business: {INSPECT_LIST[0] * INSPECT_LIST[1]}')
