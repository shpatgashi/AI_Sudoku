import numpy as np

from src.field import Field
from src.sudoku import Sudoku


# noinspection PyShadowingBuiltins,PyAttributeOutsideInit
class ForwardCheckingDO(Sudoku):
    closed_list = []

    def __init__(self, repr):
        super().__init__(repr)
        self.elements_search_space = np.array(self.create_elements_search_space())

    def add_values(self):
        if self.count_zeros() == 0:
            return True
        else:
            row, col = self.get_min()
        field = Field(row, col, self.num)
        if self.repr[row][col] == 0:
            for val in field.search_space:
                if self.check(val, row, col):
                    self.repr[row][col] = val
                    field.reduce_search_space(val)
                    if self.add_values():
                        return True
                    else:
                        field.return_arc_consistency(val)
                        self.repr[row][col] = 0
                        if (row, col) in ForwardCheckingDO.closed_list:
                            self.elements_search_space[row][col] -= 10
                            ForwardCheckingDO.closed_list.remove((row, col))
        else:
            if self.add_values():
                return True

    def solve_sudoku(self):
        self.create_elements_search_space()
        if self.add_values():
            print(self)

    def create_elements_search_space(self):
        field = Field(0, 0, self.num)
        field.inspect_sudoku(self.repr)
        search_space = []
        for i in range(self.num):
            a = []
            for j in range(self.num):
                a.append(len(Field(i, j, self.num).get_search_space()))
            search_space.append(a)
        return search_space

    def get_min(self, i=0, val=0):
        res = np.where(self.elements_search_space == self.elements_search_space.min() + val)
        if i < len(res[0]):
            row, col = res[0][i], res[1][i]
            if (row, col) not in ForwardCheckingDO.closed_list:
                self.elements_search_space[row][col] += 10
                ForwardCheckingDO.closed_list.append((row, col))
                return row, col
            else:
                return self.get_min(i + 1, val)
        else:
            if val < self.elements_search_space.max():
                return self.get_min(0, val + 1)
            else:
                res = np.where(self.elements_search_space == self.elements_search_space.max())
                return self.get_min(res[0][-1], res[1][-1])
