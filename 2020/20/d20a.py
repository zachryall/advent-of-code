"""
Advent of Code 2020 - Day 20 - 
"""

from pathlib import Path

def main(file_name):
    """Main function
    """

    answer = 0
    path = Path(__file__).with_name(file_name)
    data = [
        int(row) for row in path.read_text(encoding='UTF-8').strip().split('\n') 
        if row.isdigit()
    ]

    midpoint = len(data) // 2 
    deck_player_one = data[:midpoint]
    deck_player_two = data[midpoint:]

    while len(deck_player_one) > 0 and len(deck_player_two) > 0:
        if deck_player_one[0] > deck_player_two[0]:
            deck_player_one.append(deck_player_one.pop(0))
            deck_player_one.append(deck_player_two.pop(0))
        else:
            deck_player_two.append(deck_player_two.pop(0))
            deck_player_two.append(deck_player_one.pop(0))

    if len(deck_player_one) > 0:
        winner = deck_player_one
    else:
        winner = deck_player_two

    for index, card in enumerate(winner):
        answer += (card * (len(winner) - index))


    return answer


ANSWER_EXAMPLE = main('example.txt')
ANSWER_INPUT = main('input.txt')

print(f'Example Input: {ANSWER_EXAMPLE}')
print(f'Puzzle Input: {ANSWER_INPUT}')
