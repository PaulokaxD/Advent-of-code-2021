def day_2_1(file):
    with open(file) as input:
        position, depth = 0, 0
        while (line := input.readline()):
            kind, quantity = line.split(" ")
            kind, quantity = kind.strip(), int(quantity.strip())
            if kind == "forward":
                position += quantity
            elif kind == "down":
                depth += quantity
            elif kind == "up":
                depth -= quantity
        print("Solution 2.1: ", position*depth)


def day_2_2(file):
    with open(file) as input:
        position, depth, aim = 0, 0, 0
        while (line := input.readline()):
            kind, quantity = line.split(" ")
            kind, quantity = kind.strip(), int(quantity.strip())
            if kind == "forward":
                position += quantity
                depth += aim*quantity
            elif kind == "down":
                aim += quantity
            elif kind == "up":
                aim -= quantity
        print("Solution 2.2: ", position*depth)


day_2_1("files/input2.txt")
day_2_2("files/input2.txt")
