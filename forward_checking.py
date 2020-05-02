from AI_Sudoku.field import Field
from AI_Sudoku.sudoku import Sudoku


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


z = ForwardChecking([[0, 0, 0, 2],
                     [0, 0, 0, 4],
                     [3, 0, 0, 0],
                     [1, 0, 0, 0]])

y = ForwardChecking([[0, 0, 0, 2],
                     [0, 0, 0, 4],
                     [3, 0, 0, 0],
                     [1, 0, 0, 0]])
# e = ForwardChecking([[0, 6, 0, 0, 0, 0, 0, 0, 0],
#                      [7, 0, 0, 5, 0, 0, 0, 0, 3],
#                      [0, 3, 0, 7, 2, 6, 0, 0, 0],
#
#                      [4, 8, 0, 0, 0, 0, 0, 0, 1],
#                      [0, 0, 3, 1, 6, 7, 8, 0, 0],
#                      [2, 0, 0, 0, 0, 0, 0, 7, 5],
#
#                      [0, 0, 0, 9, 3, 1, 0, 8, 0],
#                      [5, 0, 0, 0, 0, 4, 0, 0, 2],
#                      [0, 0, 0, 0, 0, 0, 0, 9, 0]])

import time

start_time = time.time()

z.solve_sudoku()

print("--- %s seconds ---" % (time.time() - start_time))

y.solve_sudoku()
