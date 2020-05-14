from math import sqrt


class Sudoku:
    def __init__(self, repr):
        super().__init__()
        self.repr = repr
        self.num = len(self.repr)

    def check(self, val, row, column):
        if val in self.repr[row] or val in list(zip(*self.repr))[column]:
            return False

        sub_matrix = int(sqrt(self.num))
        r, c = row // sub_matrix * sub_matrix, column // sub_matrix * sub_matrix

        for i in range(sub_matrix):
            for j in range(sub_matrix):
                if val == self.repr[r + i][c + j]:
                    return False
                else:
                    continue
        else:
            return True

    def count_zeros(self):
        zeros = 0

        for i in range(self.num):
            for j in range(self.num):
                if self.repr[i][j] == 0:
                    zeros += 1
        return zeros

    def __repr__(self):

        sub_matrix = int(sqrt(self.num))
        for row in range(self.num):
            for column in range(self.num):
                print(self.repr[row][column], end=" ")
                if column % sub_matrix == 2:
                    print("\t", end="")
            print()
            if row % sub_matrix == 2:
                print()

        return ""
