"""
Advent of Code 2022 - Day 11b - 11614682178
"""

monkey_info = {}
TOTAL_ROUNDS = 10000
MODULUS = 1

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


for z in range(len(monkey_info)):
    MODULUS *= monkey_info[str(z)]['test']
    print(MODULUS)

for game_round in range(TOTAL_ROUNDS):
    print(f'Calculating round {game_round + 1}...')
    for x in monkey_info:
        ITEM_CHECKED = 0
        current_monkey = monkey_info[str(x)]
        for item in current_monkey['items']:
            worry_level = item
            if current_monkey['operation']['operator'] == '*':
                if current_monkey['operation']['value'] == 'old':
                    worry_level = worry_level ** 2
                else:
                    worry_level *= int(current_monkey['operation']['value'])
            elif current_monkey['operation']['operator'] == '+':
                if current_monkey['operation']['value'] == 'old':
                    worry_level *= 2
                else:
                    worry_level += int(current_monkey['operation']['value'])

            if worry_level % current_monkey['test'] == 0:
                next_monkey = current_monkey['true']
            else:
                next_monkey = current_monkey['false']

            monkey_info[next_monkey]['items'].append(worry_level % MODULUS)
            ITEM_CHECKED += 1
            current_monkey['inspect_count'] += 1

        for y in range(ITEM_CHECKED):
            current_monkey['items'].pop()

INSPECT_LIST = []
for z in range(len(monkey_info)):
    INSPECT_LIST.append(monkey_info[str(z)]['inspect_count'])
INSPECT_LIST.sort(reverse=True)

print(f'Monkey Business: {INSPECT_LIST[0] * INSPECT_LIST[1]}')
