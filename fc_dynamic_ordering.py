from field import Field
from sudoku import Sudoku


# noinspection PyShadowingBuiltins,PyAttributeOutsideInit
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
        self.create_whole_ss()
        # next_row, next_col = row, col + 1
        next_row, next_col = self.get_min()
        if self.repr[row][col] == 0:
            for val in f.search_space:
                if self.check(val, row, col):
                    self.repr[row][col] = val
                    # self.create_whole_ss()

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
        self.create_whole_ss()
        if self.add_values(0, 0):
            print(self)

    def create_whole_ss(self):
        search_space = []
        for i in range(self.num):
            a = []
            for j in range(self.num):
                a.append(len(Field(i, j, self.num).search_space))
                # a.append(Field(i, j, self.num).search_space)
            search_space.append(a)
        print(search_space)
        return search_space

    def get_min(self):
        import numpy as np
        ss = np.array(self.create_whole_ss())
        res = np.where(ss == ss.min())
        return res[0][0], [1][0]


representation = [[0, 0, 0, 2],
                  [0, 0, 0, 4],
                  [3, 0, 0, 0],
                  [1, 0, 0, 0]]

fcdo = ForwardCheckingDO(representation)

fcdo.solve_sudoku()
