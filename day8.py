def day_8_1(file):
    output = [i for [_, output] in get_signal(file) for i in output]
    known = (2, 3, 4, 7)
    counter = 0
    for digit in output:
        if(len(digit) in known):
            counter += 1
    print(counter)


def day_8_2(file):
    signals = get_signal(file)
    result = 0
    for signal, output in signals:
        tracker = process_signal(signal)
        number = get_number(tracker, output)
        result += number
    print(result)


def get_signal(file):
    with open(file) as input:
        signals = []
        while line := input.readline():
            line = line.strip().split("|")
            signal = line[0].strip().split(" ")
            output = line[1].strip().split(" ")
            signals.append([signal, output])
    return signals


def process_signal(signal):
    signal.sort(key=len)
    tracker = {i: [] for i in range(10)}
    tracker['1'] = [i for i in signal[0]]
    tracker['7'] = [i for i in signal[1]]
    tracker['4'] = [i for i in signal[2]]
    tracker['8'] = [i for i in signal[9]]
    for i in range(3, 9):
        elem = signal[i]
        lenght = len(elem)
        list_char = [i for i in elem]
        checker_one = [a in list_char for a in tracker['1']]
        checker_four = [a in list_char for a in tracker['4']]
        if lenght == 5:
            # Case 3 2 5
            if all(checker_one):
                tracker['3'] = [i for i in elem]
            elif checker_four.count(True) == 3:
                tracker['5'] = [i for i in elem]
            else:
                tracker['2'] = [i for i in elem]
        elif lenght == 6:
            # Caso 0 6 9
            if not all(checker_one):
                tracker['6'] = [i for i in elem]
            elif all(checker_four):
                tracker['9'] = [i for i in elem]
            else:
                tracker['0'] = [i for i in elem]
        else:
            print("Wrong input!")
    return tracker


def get_number(tracker, output):
    number = ''
    for elem in output:
        lenght = len(elem)
        if lenght == 2:
            number += '1'
        elif lenght == 3:
            number += '7'
        elif lenght == 4:
            number += '4'
        elif lenght == 7:
            number += '8'
        elif lenght == 5:
            # Case 3 2 5
            number += check_possibilities(tracker, elem, ['2', '3', '5'])
        else:
            # Caso 0 6 9
            number += check_possibilities(tracker, elem, ['0', '6', '9'])
    return int(number)


def check_possibilities(tracker, elem, possibilities):
    lenght = len(possibilities)
    checker = False
    i = 0
    while not checker and i < lenght:
        checker = all([a in tracker[possibilities[i]] for a in elem])
        i += 1
    return possibilities[i-1]


day_8_1("files/input8.txt")
day_8_2("files/input8.txt")
