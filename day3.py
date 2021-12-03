def day_3_1(file):
    with open(file) as input:
        line = input.readline().strip()
        counter = [[1 - int(i), int(i)] for i in line]
        length = len(counter)
        while (line := input.readline().strip()):
            for i in range(0, length):
                counter[i] = (counter[i][0] + 1 - int(line[i]),
                              counter[i][1] + int(line[i]))
        gamma_rate = "".join(
            ["0" if zero > one else "1" for zero, one in counter])
        epsilon_rate = "".join(
            ["0" if zero < one else "1" for zero, one in counter])

        gamma_decimal = int(gamma_rate, 2)
        epsilon_decimal = int(epsilon_rate, 2)

    print("Solution 3.1: ", gamma_decimal*epsilon_decimal)


def day_3_2(file):
    with open(file) as input:
        list_oxygen = [elem.strip() for elem in input.readlines()]
        list_co2 = list_oxygen.copy()
        lenght = len(list_co2[0])

        for i in range(lenght):
            if(len(list_oxygen) > 1):
                old_list_oxygen = list_oxygen
                aux_oxygen = [elem[i] for elem in list_oxygen]
                aux_oxygen_ones = aux_oxygen.count('1')
                val_oxygen = 1 if aux_oxygen_ones >= (len(
                    list_oxygen) - aux_oxygen_ones) else 0

                list_oxygen = [elem for elem in old_list_oxygen if int(
                    elem[i]) == val_oxygen]

            if(len(list_co2) > 1):
                old_list_co2 = list_co2
                aux_co2 = [elem[i] for elem in list_co2]
                aux_co2_ones = aux_co2.count('1')
                val_co2 = 1 if aux_co2_ones < (len(
                    list_co2) - aux_co2_ones) else 0

                list_co2 = [elem for elem in old_list_co2 if int(
                    elem[i]) == val_co2]

        oxygen_generator_rating = int(list_oxygen[0], 2)
        co2_scrubber_rating = int(list_co2[0], 2)
        print(oxygen_generator_rating, co2_scrubber_rating)
    print(oxygen_generator_rating*co2_scrubber_rating)


day_3_1("files/input3.txt")
day_3_2("files/input3.txt")
