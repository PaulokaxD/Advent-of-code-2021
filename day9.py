import igraph


def day_9_1(file):
    g = create_graph(file)
    # layout = g.layout(layout='auto')
    # igraph.plot(g)
    risk_levels = []
    for vertex in g.vs():
        vertex_name = vertex["name"]
        if all([vertex_name < neighbor["name"] for neighbor in vertex.neighbors()]):
            risk_levels.append(vertex)
    print(sum([vertex["name"] for vertex in risk_levels])+len(risk_levels))
    return g, risk_levels


def day_9_2(file):
    g, basin_focuses = day_9_1(file)
    basin_sizes = {vertex: get_basin_size(
        g, vertex) for vertex in basin_focuses}
    largest_basins = sorted(basin_sizes.values())[-3:]
    print(mult(largest_basins))


def create_graph(file):
    g = igraph.Graph()
    line_number = 0
    with open(file) as input:
        old_line = input.readline().strip()
        add_line_to_graph(g, old_line, line_number, True)
        while line := input.readline().strip():
            line_number += 1
            add_line_to_graph(g, line, line_number, False)
    return g


def add_line_to_graph(graph, line, line_number, first_line):
    length = len(line)
    line_position = line_number*length
    old_position = (line_number - 1)*length
    graph.add_vertex(name=int(line[0]))
    if not first_line:
        graph.add_edge(old_position, line_position)
    for i in range(1, length):
        graph.add_vertex(name=int(line[i]))
        graph.add_edge(line_position + i-1, line_position + i)
        if not first_line:
            graph.add_edge(old_position + i, line_position + i)


def get_basin_size(graph, vertex):
    basin = get_basin_recursive(graph, vertex, [vertex])
    return len(basin)


def get_basin_recursive(graph, vertex, basin):
    locations = vertex.neighbors()
    for neighbor in locations:
        if neighbor not in basin and neighbor["name"] != 9:
            basin.append(neighbor)
            get_basin_recursive(graph, neighbor, basin)
    return basin


def mult(list):
    result = 1
    for i in list:
        result *= i
    return result


# day_9_1("files/input9.txt")
day_9_2("files/input9.txt")
