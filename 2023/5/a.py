import math

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

part = 'b'
seeds = []

if part == 'a':
    seeds = lines[0][7:].split()
if part == 'b':
    seeds_split = lines[0][7:].split(" ")
    seeds_join = " ".join(seeds_split[:2]), " ".join(seeds_split[2:])

    for seed in seeds_join:
        seed_info = seed.split()

        start = int(seed_info[0])
        end = start + int(seed_info[1])

        for range_index in range(start, end + 1):
            seeds.append(str(range_index))

print(len(seeds))


seed_to_index = 0
soil_to_index = 0
fert_to_index = 0
water_to_index = 0
light_to_index = 0
temp_to_index = 0
humid_to_index = 0

lowest = math.inf

# get map indexes
for index, line in enumerate(lines):
    if line.startswith('seed-to'):
        seed_to_index = index + 1
    elif line.startswith('soil'):
        soil_to_index = index + 1
    elif line.startswith('fertilizer'):
        fert_to_index = index + 1
    elif line.startswith('water'):
        water_to_index = index + 1
    elif line.startswith('light'):
        light_to_index = index + 1
    elif line.startswith('temperature'):
        temp_to_index = index + 1
    elif line.startswith('humidity'):
        humid_to_index = index + 1

# create map lists
seed_to_soil = lines[seed_to_index:soil_to_index - 2]
soil_to_fert = lines[soil_to_index:fert_to_index - 2]
fert_to_water = lines[fert_to_index:water_to_index - 2]
water_to_light = lines[water_to_index:light_to_index - 2]
light_to_temp = lines[light_to_index:temp_to_index - 2]
temp_to_humid = lines[temp_to_index:humid_to_index - 2]
humid_to_locat = lines[humid_to_index:]

map_names = [
    seed_to_soil,
    soil_to_fert,
    fert_to_water,
    water_to_light,
    light_to_temp,
    temp_to_humid,
    humid_to_locat
]


def process_map(map_list, seed_number):
    for list_index, entry in enumerate(map_list):

        segments = entry.rstrip().split(' ')

        out_number = int(segments[0])
        in_number = int(segments[1])
        steps = int(segments[2])

        if in_number <= seed_number <= in_number + steps:
            return (seed_number - in_number) + out_number

        if list_index == len(map_list) - 1:
            return seed_number


for seed in seeds:
    next_value = int(seed.rstrip())

    for map_name in map_names:
        next_value = process_map(map_name, next_value)

    print(f'Location for seed {seed.rstrip()} - {next_value}')

    if lowest > next_value:
        lowest = next_value

print(f'Lowest Location Value - {lowest}')
