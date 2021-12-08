import numpy as np


def day_7_1(file):
    with open(file) as input:
        line = list(map(int, input.readline().strip().split(",")))
        median = np.median(line)
        sol = 0
        for i in line:
            sol += abs(median-i)
        print(sol)


def day_7_2(file):
    with open(file) as input:
        line = list(map(int, input.readline().strip().split(",")))
    # Use Euler's sum's formula
        mean = np.mean(line)
        mean_up = (mean - 1/2)//1
        mean_down = (mean + 1/2)//1
        sol_up = 0
        for i in line:
            fuel = sum([i for i in range(1, int(abs(i-mean_up))+1)])
            sol_up += fuel
        sol_down = 0
        for i in line:
            fuel = sum([i for i in range(1, int(abs(i-mean_down))+1)])
            sol_down += fuel
        print(sol_down, sol_up)
        print(min([sol_up, sol_down]))


day_7_1("files/input7.txt")
day_7_2("files/input7.txt")
