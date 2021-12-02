def day_1_1(file):
    with open(file) as input:
        content = input.readlines()
        solution = 0
        for i in range(1, len(content)):
            solution += int(content[i-1]) < int(content[i])
        print(solution)


def day_1_2(file):
    with open(file) as input:
        content = [int(elem.strip()) for elem in input.readlines()]
        solution = 0
        sum1 = sum(content[0:3])

        for i in range(1, len(content)-1):
            sum2 = sum(content[i-1:i+2])
            solution += sum1 < sum2
            sum1 = sum2
        print(solution)


day_1_1("files/input1.txt")
day_1_2("files/input1.txt")
