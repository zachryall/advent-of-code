"""
Advent of Code 2020 - Day 16a - 26009
"""

from pathlib import Path
import re

def main(file_name):
    """Main function
    """

    path = Path(__file__).with_name(file_name)
    data = [row for row in path.read_text(encoding='UTF-8').strip().split('\n')]
    rules = []
    tickets = []
    answer = 0
    invalid_tickets = []

    for row in data:
        if row == '':
            break
        rule = re.search(r'(\d+)-(\d+) or (\d+)-(\d+)', row)
        rules.append([int(rule.group(1)),int(rule.group(2))])
        rules.append([int(rule.group(3)),int(rule.group(4))])

    for row in data:
        if len(row) == 0:
            continue
        if row[0].isdigit():
            tickets.append([int(field) for field in row.split(',')])

    my_ticket = tickets.pop(0)

    for index, ticket in enumerate(tickets):
        for field in ticket:
            is_valid = any(
                rule[0] <= field <= rule[1]
                for rule in rules
            )
            if not is_valid:
                invalid_tickets.append(index)

    invalid_tickets_set = set(invalid_tickets)
    valid_tickets = [
        element 
        for index, element in enumerate(tickets) 
        if index not in invalid_tickets_set
    ]

    for index, ticket in enumerate(valid_tickets):
        for field in ticket:
            match_count = 0
            last_match = ''
            for rule in rules:
                if rule[0] <= field <= rule[1]:
                    match_count += 1
                    last_match = rule
            if match_count == 1:
                print(field)
                print(last_match)

    return answer


ANSWER_EXAMPLE = main('example.txt')
# ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
# print(f'Puzzle Input: {ANSWER_INPUT}')
