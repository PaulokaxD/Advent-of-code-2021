import numpy as np


def read_file(file):
    hydrothermal_vents_hv = []
    hydrothermal_vents_diag = []
    max_coordinate = 0
    with open(file) as input:
        while line := input.readline():
            vent = line.strip().split(" -> ")
            start_x, start_y = vent[0].split(",")
            end_x, end_y = vent[1].split(",")
            if start_x == end_x or start_y == end_y:
                hydrothermal_vents_hv.append(
                    ordenate_coordinates(int(start_x), int(start_y), int(end_x), int(end_y)))
            else:
                hydrothermal_vents_diag.append(
                    [[int(start_x), int(start_y)], [int(end_x), int(end_y)]])
        max_hv = max(max([max(start), max(end), max_coordinate])
                     for start, end in hydrothermal_vents_hv)
        max_diag = max(max([max(start), max(end), max_coordinate])
                       for start, end in hydrothermal_vents_diag)
        max_coordinate = max(max_hv, max_diag) + 1
    return hydrothermal_vents_hv, hydrothermal_vents_diag, max_coordinate


def ordenate_coordinates(ix, iy, fx, fy):
    start_x = min(ix, fx)
    end_x = max(ix, fx)
    start_y = min(iy, fy)
    end_y = max(iy, fy)
    return [[start_x, start_y], [end_x, end_y]]


def add_diagonal(diagram, start_x, start_y, end_y, y_direction, x_direction):
    x = start_x
    for i in range(start_y, end_y+1*y_direction, y_direction):
        diagram[i, x] += 1
        x += 1*x_direction


def day_5_1(file):
    vents, diag, max_coord = read_file(file)
    diagram = np.zeros((max_coord, max_coord), dtype=int)
    for [start_x, start_y], [end_x, end_y] in vents:
        diagram[start_y:end_y+1, start_x:end_x+1] += 1
    print(np.count_nonzero(diagram > 1))
    return diag, diagram, max_coord


def day_5_2(file):
    diag, diagram, max_coord = day_5_1(file)
    for [start_x, start_y], [end_x, end_y] in diag:
        if start_y < end_y:
            # y coordinate increases
            if start_x < end_x:
                # x coordinate increases
                add_diagonal(diagram, start_x, start_y, end_y, 1, 1)
            else:
                # x coordinate decreases
                add_diagonal(diagram, start_x, start_y, end_y, 1, -1)
        else:
            # y coordinate decreases
            if start_x < end_x:
                # x coordinate increases
                add_diagonal(diagram, start_x, start_y, end_y, -1, 1)
            else:
                # x coordinate decreases
                add_diagonal(diagram, start_x, start_y, end_y, -1, -1)
    print(np.count_nonzero(diagram > 1))


# day_5_1("files/input5.txt")
day_5_2("files/input5.txt")
