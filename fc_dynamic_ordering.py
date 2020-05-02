import numpy as np

from examples import sudoku4
from field import Field
from sudoku import Sudoku


# noinspection PyShadowingBuiltins,PyAttributeOutsideInit
class ForwardCheckingDO(Sudoku):
    closed_list = []

    def __init__(self, repr):
        super().__init__(repr)
        self.ss = np.array(self.create_whole_ss())

    def add_values(self):
        if self.count_zeros() == 0:
            return True
        else:
            row, col = self.get_min()

        f = Field(row, col, self.num)
        self.create_whole_ss()

        if self.repr[row][col] == 0:
            for val in f.search_space:
                if self.check(val, row, col):
                    self.repr[row][col] = val
                    f.reduce_search_space(val)
                    if self.add_values():
                        return True
                    else:
                        f.return_arc_consistency(val)
                        self.repr[row][col] = 0
                        if (row, col) in ForwardCheckingDO.closed_list:
                            self.ss[row][col] -= 10
                            ForwardCheckingDO.closed_list.remove((row, col))
        else:
            if self.add_values():
                return True

    def solve_sudoku(self):
        self.create_whole_ss()
        if self.add_values():
            print(self)

    def create_whole_ss(self):
        f = Field(0, 0, self.num)
        f.inspect_sudoku(self.repr)
        search_space = []
        for i in range(self.num):
            a = []
            for j in range(self.num):
                a.append(len(Field(i, j, self.num).get_search_space()))
            search_space.append(a)
        return search_space

    def get_min(self):
        res = np.where(self.ss == self.ss.min())
        row, col = res[0][0], res[1][0]
        if (row, col) not in ForwardCheckingDO.closed_list:
            self.ss[row][col] += 10
            ForwardCheckingDO.closed_list.append((row, col))
            return row, col
        else:
            return self.get_min()


if __name__ == '__main__':
    representation = [[0, 0, 0, 2],
                      [0, 0, 0, 4],
                      [3, 0, 0, 0],
                      [1, 0, 0, 0]]

    fcdo = ForwardCheckingDO(sudoku4)
    # fcdo = ForwardCheckingDO(representation)

    fcdo.solve_sudoku()
