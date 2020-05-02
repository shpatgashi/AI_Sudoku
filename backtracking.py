from sudoku import Sudoku


# noinspection PyShadowingBuiltins
class Backtracking(Sudoku):

    def __init__(self, repr):
        super().__init__(repr)

    def add_values(self, row, col):

        if col == self.num:
            if row == self.num - 1:
                return True
            else:
                col = 0
                row += 1

        if self.repr[row][col] == 0:
            for val in range(1, 10):
                if self.check(val, row, col):
                    self.repr[row][col] = val
                    if self.add_values(row, col + 1):
                        return True
                    else:
                        self.repr[row][col] = 0
        else:
            if self.add_values(row, col + 1):
                return True

    def solve_sudoku(self):
        if self.add_values(0, 0):
            print(self)