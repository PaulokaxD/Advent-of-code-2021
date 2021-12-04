def day_4_1(file):
    numbers, matrixes = instantiate_game(file)
    play_game(numbers, matrixes, True)


def day_4_2(file):
    numbers, matrixes = instantiate_game(file)
    play_game(numbers, matrixes, False)


def instantiate_game(file):
    with open(file) as input:
        numbers = input.readline().strip().split(",")
        matrixes = []
        matrix = []
        while line := input.readline():
            line = line.strip()
            if(line):
                matrix.append(line.strip().split())
            elif(matrix):
                # WARNING: For this to work properly we need an extra blank
                # line at the end of the input file. If not the last matrix
                # it's not appended.
                matrixes.append(matrix)
                matrix = []
    return numbers, matrixes


def play_game(numbers, matrixes, first_to_win):
    '''
    #### Play the bingo game.
    `numbers`: list of digits that are appearing.
    `matrixes`: list of boards.
    `fist_to_win`: boolean that decides if we are pleaying to win or loose
    '''
    n_boards = len(matrixes)
    playing_boards = len(matrixes)
    size_matrix = len(matrixes[0][0])
    # Every element in the bingo_tracker represent one board and has two
    # lists of 'size_matrix' elements and a boolean. The first one are the
    # number of matched elements in each row and the second one in each
    # column. The last boolean controls if the board has already won or not.
    bingo_tracker = [[[0 for _ in range(size_matrix)], [
        0 for _ in range(size_matrix)], False] for _ in range(n_boards)]
    for elem in numbers:
        for n_matrix in range(n_boards):
            # If the board hasn't won still
            if not bingo_tracker[n_matrix][2]:
                matrix = matrixes[n_matrix]
                for n_row in range(size_matrix):
                    row = matrix[n_row]
                    for n_column in range(size_matrix):
                        if row[n_column] == elem:
                            row[n_column] = "*"
                            bingo_tracker[n_matrix][0][n_row] += 1
                            bingo_tracker[n_matrix][1][n_column] += 1
                            playing_boards, won = check_winner(
                                matrixes, elem, size_matrix, n_matrix, n_row, n_column, bingo_tracker, first_to_win, playing_boards)
                            if won:
                                return

    print("There is still no bingo!")


def check_winner(matrixes, elem, size_matrix, n_matrix, n_row, n_column, bingo_tracker, first_to_win, playing_boards):
    matrix = matrixes[n_matrix]
    won = False
    if bingo_tracker[n_matrix][0][n_row] == size_matrix or bingo_tracker[n_matrix][1][n_column] == size_matrix:
        sum_unmarked = sum(
            [int(unmarked) for unmarked in sum(matrix, []) if unmarked != "*"])
        # For this we are supposing that there are more than one board
        if first_to_win or playing_boards == 1:
            print("Bingo! The final score is ",
                  sum_unmarked * int(elem))
            won = True
        else:
            bingo_tracker[n_matrix][2] = True
            playing_boards -= 1
    return playing_boards, won


day_4_1("files/input4.txt")
day_4_2("files/input4.txt")
