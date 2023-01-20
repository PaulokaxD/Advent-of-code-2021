import copy

def create_caves_map(file):
    caves = dict()
    with open(file) as input:
        while line := input.readline().strip():
            origin, destiny = line.split("-")
            # We do not want to come back to the start point
            if destiny != "start":
                caves.setdefault(origin, []).append(destiny)
            if origin != "start":
                caves.setdefault(destiny, []).append(origin)
    return caves

def eliminate_destiny(destiny,caves):
    print('\n',destiny)
    for cave in caves:
        if destiny in caves[cave]: caves[cave].remove(destiny)
    return caves

def day_12_1(file):
    n_paths = 0
    caves = create_caves_map(file)
    n_paths += count_paths("start", caves, ["start"])
    return n_paths

def count_paths(origin, caves, paths):
    # I am suposing there are not two big caves connected (no cycles)
    n_paths = 0
    destinations = caves[origin]
    if len(destinations) > 0:
        for destiny in destinations:
            caves_aux = copy.deepcopy(caves)
            paths_aux = copy.deepcopy(paths)
            if destiny == "end":
                # print(paths_aux+["end"])
                n_paths += 1
            elif destiny.islower():
                caves_aux = eliminate_destiny(destiny,caves_aux)
                n_paths += count_paths(destiny, caves_aux, paths_aux+[destiny])
            else:
                n_paths += count_paths(destiny, caves_aux, paths_aux+[destiny])

    return n_paths

def day_12_2(file):
    n_paths = 0
    caves = create_caves_map(file)
    n_paths += count_paths_part_2("start", caves, [], False)
    return n_paths

def can_visit(destination, small_visited, twice):
    return destination.isupper() or not twice or destination not in small_visited

def count_paths_part_2(origin, caves, small_visited, twice):
    # I am suposing there are not two big caves connected (no cycles)
    n_paths = 0

    if not twice and origin.islower() and origin in small_visited:
        twice = True

    small_visited.append(origin)
    for destiny in caves[origin]:

        if destiny == "end":
            n_paths += 1
        elif can_visit(destiny, small_visited, twice):
            n_paths += count_paths_part_2(destiny, caves, small_visited, twice)

    small_visited.pop()

    return n_paths

print(day_12_2("files/input12.txt"))