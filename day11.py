import sys
import numpy as np

class Octopus:
    flashed:bool
    enery:int

    def __init__(self, energy):
        self.flashed = False
        self.enery = energy

    def flash(self):
        self.flashed = True
        self.enery = 0
        for neighbor in self.neighbors:
            neighbor.increment_energy()

    def increment_energy(self):
        self.enery += 1
        if self.enery > 9 and not self.flashed:
            self.flash()

    def add_neighbors(self, list):
        self.neighbors += list

    def __repr__(self):
        return f'{self.position}'


def create_board(file):
    octopuses = []
    with open(file) as input:
        while line := input.readline().strip():
            octopuses.append([int(i) for i in line])
    return np.array(octopuses)

def day_11_1(file, epochs):
    flashes = 0
    sync_flash = -1
    board = create_board(file)
    n_rows = len(board)
    n_col = len(board[0])
    for epoch in range(epochs):
        flashed = np.array([[0 for _ in range(n_col)] for _ in range(n_rows)])
        board = board + 1
        while len(board[board>9]) != 0:
            for y, y_val in enumerate(board):
                for x, x_val in enumerate(y_val):
                    if x_val > 9:
                        board[y,x] = 0
                        flashes += 1
                        if x > 0:
                            board[y,x-1] += 1 if flashed[y,x-1] == 0 else 0
                            if y > 0:
                                board[y-1,x-1] += 1 if flashed[y-1,x-1] == 0 else 0
                            if y < n_rows - 1:
                                board[y+1,x-1] += 1 if flashed[y+1,x-1] == 0 else 0
                        if x < n_col - 1:
                            board[y,x+1] += 1 if flashed[y,x+1] == 0 else 0
                            if y > 0:
                                board[y-1,x+1] += 1 if flashed[y-1,x+1] == 0 else 0
                            if y < n_rows - 1:
                                board[y+1,x+1] += 1 if flashed[y+1,x+1] == 0 else 0
                        if y > 0:
                            board[y-1,x] += 1 if flashed[y-1,x] == 0 else 0
                        if y < n_rows - 1:
                            board[y+1,x] += 1 if flashed[y+1,x] == 0 else 0
                        flashed[y,x] = 1

        if sync_flash == -1 and len(flashed[flashed == 0]) == 0:
            sync_flash = epoch + 1
    print(f"There were {flashes} flashes in {epochs} epochs")
    print(f"Syncronysing in epoch {sync_flash}!")


day_11_1("files/input11.txt", 1000)
