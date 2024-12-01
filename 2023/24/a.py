file = open('input.txt', 'r')
# file = open('example.txt', 'r')
hailstones = file.readlines()
file.close()

collisions = 0
# test_area_start = 7
test_area_start = 200000000000000
# test_area_end = 27
test_area_end = 400000000000000


def get_line_definition(line_info):
    segments = line_info.replace(',', '').split()

    a = (int(segments[1]) + int(segments[5])) - int(segments[1])
    b = int(segments[0]) - (int(segments[0]) + int(segments[4]))
    c = (a * int(segments[0])) + (b * int(segments[1]))
    return a, b, c


def collision_checker(a_info, b_info, a1, a2, b1, b2, c1, c2):
    direction = (a1 * b2) - (a2 * b1)
    if not direction == 0:
        x = round(((b2 * c1) - (b1 * c2)) / direction, 3)
        y = round(((a1 * c2) - (a2 * c1)) / direction, 3)

        if test_area_start <= x <= test_area_end and test_area_start <= y <= test_area_end:
            a_segments = a_info.replace(',', '').split()
            b_segments = b_info.replace(',', '').split()
            if not (x > int(a_segments[0]) or y > int(b_segments[0])):
                return True
    return False


for hailstone_a_index, hailstone_a_info in enumerate(hailstones):
    for hailstone_b_index in range(hailstone_a_index + 1, len(hailstones)):
        if hailstone_a_index == len(hailstones) - 1:
            break
        else:
            hailstone_b_info = hailstones[hailstone_b_index]
            line1_a, line1_b, line1_c = get_line_definition(hailstone_a_info)
            line2_a, line2_b, line2_c = get_line_definition(hailstone_b_info)

            answer = collision_checker(
                hailstone_a_info,
                hailstone_b_info,
                line1_a, line2_a,
                line1_b, line2_b,
                line1_c, line2_c
            )

            if answer:
                collisions += 1

print(f'Collisions = {collisions}')

# too low
# 5582
