import re

file = open('example.txt', 'r')
lines = file.readlines()
file.close()

total = 0
tickets_won = []

for i, line in enumerate(lines):
    if i > 30:
        print('loop')
        break
    print()
    segments = re.split(r'[:|]', line)
    print(segments)

    winning_numbers = segments[1].split()
    our_numbers = segments[2].split()

    matches = len([key for key, val in enumerate(our_numbers) if val in set(winning_numbers)])

    if matches != 0:
        print(f"Matches: {matches}")
        current_game_number = int(segments[0].split()[1])
        
        for match in range(1, matches):

            game_to_add = f'Card {current_game_number + match}'
            print(f'Ticket won: {game_to_add}')

            index_next = [key for key, val in enumerate(lines, i) if game_to_add in val]
            index_to_add = int(index_next[0]) + 1
            print(f'Index to add at: {index_to_add}')
            print(f'Line to add at: {lines[current_game_number + match]}')

            #add(where, what)

            lines.insert(index_to_add, lines[current_game_number + match])

print(total)