import re

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

total = 0

for line in lines:
    segments = re.split(r'[:|]', line)
    print(segments)

    winning_numbers = segments[1].split()
    our_numbers = segments[2].split()

    matches = len([key for key, val in enumerate(our_numbers) if val in set(winning_numbers)])

    if matches != 0:
        score = pow(2, matches - 1)
        total = total + score

print(total)