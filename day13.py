import numpy as np

def read_file(file):
    dots = set()
    instructions = []

    with open(file) as input:
        while line := input.readline().strip():
            if line == "":
                break
            x,y = line.split(",")
            dots.add((int(x), int(y)))
        while line := input.readline().strip():
            axis, number = line.split(" ")[-1].split("=")
            instructions.append((axis, int(number)))
    return dots, instructions

def apply_instruction(dots, instruction):
    folding_axis = 0 if instruction[0] == 'x' else 1
    distance = instruction[1]
    # Como hacer esto mas bonito??
    aux_dots = set()
    for dot in dots:
        aux_dot = [-1,-1]
        shift = 0
        if dot[folding_axis] > distance:
            shift = 2*(dot[folding_axis] - distance) 
        elif dot[folding_axis] == distance:
            print(dot[folding_axis])
            pass
        aux_dot[folding_axis] = dot[folding_axis] - shift
        aux_dot[1-folding_axis] = dot[1-folding_axis]
        aux_dots.add(tuple(aux_dot))
    dots = aux_dots
    
    return dots

def represent_numbers(dots):
    min_x, min_y = [min(coord) for coord in zip(*dots)]
    max_x, max_y = [max(coord) for coord in zip(*dots)]

    sheet = [["█" if (x,y) in dots else " " for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]

    for line in sheet: print("".join(line))

def day_13(file):
    dots, instructions = read_file(file)

    dots = apply_instruction(dots, instructions[0])
    print(len(dots))

    for instruction in instructions[1:]:
        dots = apply_instruction(dots, instruction)

    represent_numbers(dots)

    
day_13("files/input13.txt")