from math import sqrt
from typing import List

class Field:
    row_search = []
    col_search = []
    matrix_search = []

    def __init__(self, row, col, size):
        self.size = size
        self.row = row
        self.col = col
        self.matrix_no = int(sqrt(size)) * int((row // sqrt(size))) + int(col // sqrt(size))
        self.search_space = self.get_search_space()

    # take cell of least constrained cell (least search_space)
    def get_search_space(self):
        if not Field.row_search:
            self.create_search_space()
        return list(set(self.row_search[self.row]) & set(self.col_search[self.col]) & set(self.matrix_search[self.matrix_no]))

    def create_search_space(self):
        domain = []
        for i in range(1, self.size + 1):
            domain.append(i)
        for i in range(1, self.size + 1):
            # stack overflow for better perf
            a1 = domain.copy()
            b1 = domain.copy()
            c1 = domain.copy()
            Field.row_search.append(a1)
            Field.col_search.append(b1)
            Field.matrix_search.append(c1)

    def reduce_search_space(self, val):
        Field.row_search[self.row].remove(val)
        Field.col_search[self.col].remove(val)
        Field.matrix_search[self.matrix_no].remove(val)

    def return_arc_consistency(self, val):
        Field.row_search[self.row].append(val)
        Field.col_search[self.col].append(val)
        Field.matrix_search[self.matrix_no].append(val)

    @staticmethod
    def reset():
        Field.row_search = []
        Field.col_search = []
        Field.matrix_search = []

    def inspect_sudoku(self, sudoku):
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if sudoku[i][j] != 0:
                    self.row = i
                    self.col = j
                    self.reduce_search_space(sudoku[i][j])

        self.choose_field()

    def choose_field(self):
        # min = list.index(min(list, key=len))
        most_cons_row_index = Field.row_search.index(min(Field.row_search, key=len))
        most_cons_col_index = Field.col_search.index(min(Field.col_search, key=len))
        # if sudoku[least_cons_row_index][least_cons_col_index] != 0:

        return most_cons_row_index, most_cons_col_index


