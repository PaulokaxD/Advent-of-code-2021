def day_10_1(file):
    parenthesis = {")": "(", "]": "[", "}": "{", ">": "<"}
    puntuation = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    incomplete_lines = []
    open_parenthesis = parenthesis.values()
    with open(file) as input:
        while line := input.readline():
            controller = ""
            for elem in line:
                if elem in open_parenthesis:
                    controller += elem
                elif elem == '\n':
                    # For this we need an extra blank line at the end
                    # of the file to ensure the last '\n'
                    incomplete_lines.append(controller)
                elif parenthesis[elem] == controller[-1]:
                    controller = controller[:-1]
                else:
                    score += puntuation[elem]
                    break
    print(score)
    return incomplete_lines


def day_10_2(file):
    puntuation = {"(": 1, "[": 2, "{": 3, "<": 4}
    incomplete_lines = day_10_1(file)
    scores = []
    for line in incomplete_lines:
        score = 0
        for parenthesis in line[::-1]:
            score = 5*score + puntuation[parenthesis]
        scores.append(score)
    scores.sort()
    print(scores[len(scores)//2])


# day_10_1("files/input10.txt")
day_10_2("files/input10.txt")
