file = open('input.txt', 'r')
# file = open('example.txt', 'r')
lines = file.readlines()
file.close()


time = int(lines[0][5:].replace(" ","").rstrip())
distance = int(lines[1][9:].replace(" ","").rstrip())
score = 0

print(time)
print(distance)

winning_opps = 0
for hold_length in range(time):
    print(f'Index: {hold_length}')
    my_distance = (time - hold_length) * hold_length
    if my_distance > distance:
        winning_opps += 1
    if my_distance < distance and score != 0:
        break

print(f'{winning_opps} ways to win the race')
