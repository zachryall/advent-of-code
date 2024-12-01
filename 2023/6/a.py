file = open('input.txt', 'r')
# file = open('example.txt', 'r')
lines = file.readlines()
file.close()

times = lines[0][5:].split(' ')
distances = lines[1][9:].split(' ')
# times = [s.strip() for s in times]
# distances = [s.strip() for s in distances]
times = list(filter(None, times))
distances = list(filter(None, distances))
score = 0

print(times)
print(distances)

total_race = len(distances)
for race in range(len(distances)):
    time_value = int(times[race])
    winning_opps = 0
    for hold_length in range(time_value):
        my_distance = (time_value - hold_length) * hold_length
        if my_distance > int(distances[race]):
            winning_opps += 1
    if score == 0:
        score = winning_opps
    else:
        score *= winning_opps
    print(f'{winning_opps} ways to win Race {race}')
print(f'Total ways to win {score}')
