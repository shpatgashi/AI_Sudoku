from examples import sudoku4
from field import Field
from sudoku import Sudoku


# noinspection PyShadowingBuiltins
class ForwardChecking(Sudoku):
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
            f = Field(row, col, self.num)
            for val in f.search_space:
                if self.check(val, row, col):
                    self.repr[row][col] = val

                    f.reduce_search_space(val)
                    if self.add_values(row, col + 1):
                        return True
                    else:
                        f.return_arc_consistency(val)
                        self.repr[row][col] = 0
        else:
            if self.add_values(row, col + 1):
                return True

    def solve_sudoku(self):
        if self.add_values(0, 0):
            f = Field(0, 1, 3)
            Field.reset()
            print(self)
            f.reset()


import time

start_time = time.time()

e = ForwardChecking(sudoku4)
e.solve_sudoku()

print("--- %s seconds ---" % (time.time() - start_time))

# y.solve_sudoku()
