"""
Advent of Code 2022 - Day 14a
"""

import re

X_MAX = 500
X_MIN = 500
Y_MAX = 0
WALLS = []
CAVE_LAYOUT = []

def create_empty_cave():
  for i in range(Y_MAX + 1):
      CAVE_LAYOUT.append([])
      for _ in range(X_MAX - X_MIN + 1):
        CAVE_LAYOUT[i].append('.')
  CAVE_LAYOUT[0][500 - X_MIN] = '+'

def add_walls():
  for wall in WALLS:
    last_wall_section = []
    for wall_section in wall:
      coord = wall_section.split(',')
      CAVE_LAYOUT[int(coord[1])][int(coord[0])  - X_MIN] = '#'

      if last_wall_section:
        last_coord = last_wall_section.split(',')

        if last_coord[0] == coord[0]:
          # direction = 1
          # if last_coord[1] < coord[1]:
          #   direction = -1
          # for i in range(int(coord[1]), int(last_coord[1]), direction):
          #   CAVE_LAYOUT[i][int(coord[0]) - X_MIN] = '#'
          wall_filler(last_coord[1], coord[1], coord[0], 'vertical')
          
        else:
          wall_filler(last_coord[0], coord[0], coord[1], 'horizontal')

      last_wall_section = wall_section

def wall_filler(last_coordinates, current_coordinates, other_value, plane):
  direction = 1
  current_coordinates = int(current_coordinates)
  last_coordinates = int(last_coordinates)
  other_value = int(other_value) # TODO make ints earlier
  if last_coordinates < current_coordinates:
    direction = -1
  for i in range(current_coordinates, last_coordinates, direction):
    if plane == 'horizontal':
      CAVE_LAYOUT[other_value][i - X_MIN] = '#'
    else:
      CAVE_LAYOUT[i][other_value - X_MIN] = '#'

def display_values():
  for entry in CAVE_LAYOUT:
    print(entry)


with open('example.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

    for line in lines:
      coords = re.split(' -> |\n', line)
      coords = list(filter(None, coords))
      WALLS.append(coords)
      for coord in coords:
        coord_values = coord.split(',')
        coord_values = [int(item) for item in coord_values]

        if Y_MAX < coord_values[1]:
          Y_MAX = coord_values[1]

        if X_MAX < coord_values[0]:
          X_MAX = coord_values[0]
        elif X_MIN > coord_values[0]:
          X_MIN = coord_values[0]


create_empty_cave()
add_walls()
display_values()
