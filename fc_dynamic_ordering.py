from AI_Sudoku.sudoku import Sudoku
from AI_Sudoku.field import Field


# noinspection PyShadowingBuiltins
class ForwardCheckingDO(Sudoku):
    def __init__(self, repr):
        super().__init__(repr)

    def add_values(self, row, col):
        if col == self.num:
            if row == self.num - 1:
                return True
            else:
                col = 0
                row += 1

        f = Field(row, col, self.num)
        next_row, next_col = f.choose_field()

        if self.repr[row][col] == 0:
            for val in f.search_space:
                if self.check(val, row, col):

                    self.repr[row][col] = val

                    f.reduce_search_space(val)
                    if self.add_values(next_row, next_col):
                        return True
                    else:
                        f.return_arc_consistency(val)
                        self.repr[row][col] = 0
        else:
            if self.add_values(next_row, next_col):
                return True

    def solve_sudoku(self):
        f = Field(0, 0, self.num)
        f.inspect_sudoku(self.repr)
        if self.add_values(0, 0):
            print(self)


f = ForwardCheckingDO([[0, 0, 0, 0],
                       [0, 0, 0, 4],
                       [3, 0, 0, 0],
                       [1, 0, 0, 0]])

f.solve_sudoku()
