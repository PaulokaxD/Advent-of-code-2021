# First approach. Slow and not optimal. It works though for small numbers.
def day_6_1(file, days):
    with open(file) as input:
        fishes = list(map(int, input.readline().strip().split(",")))
        for _ in range(days):
            newborns = 0
            for i in range(len(fishes)):
                if fishes[i] == 0:
                    fishes[i] = 6
                    newborns += 1
                else:
                    fishes[i] -= 1
            fishes = fishes + [8]*newborns
        print(len(fishes))


# Better approach. Optimized and faster. Works well for bigger numbers.
def day_6_2(file, days):
    with open(file) as input:
        fishes = list(map(int, input.readline().strip().split(",")))
        ranked_fishes = {i: 0 for i in range(9)}
        for elem in fishes:
            ranked_fishes[elem] += 1
        for _ in range(days):
            newborns = ranked_fishes[0]
            for i in range(1, 9):
                ranked_fishes[i-1] = ranked_fishes[i]
            ranked_fishes[8] = newborns
            ranked_fishes[6] += newborns
        print(sum(ranked_fishes.values()))


# day_6_1("files/input6.txt", 80)
# day_6_1("files/input6.txt", 256) Not a solution. Not optimized.
day_6_2("files/input6.txt", 256)
