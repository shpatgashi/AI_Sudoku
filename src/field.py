from math import sqrt


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

    def get_search_space(self):
        if not Field.row_search:
            self.create_search_space()
        return list(
            set(self.row_search[self.row]) & set(self.col_search[self.col]) & set(self.matrix_search[self.matrix_no]))

    def create_search_space(self):
        domain = []
        for i in range(1, self.size + 1):
            domain.append(i)
        for i in range(1, self.size + 1):
            Field.row_search.append(domain.copy())
            Field.col_search.append(domain.copy())
            Field.matrix_search.append(domain.copy())

    def reduce_search_space(self, val):
        for search in [Field.row_search[self.row], Field.col_search[self.col], Field.matrix_search[self.matrix_no]]:
            if val in search:
                search.remove(val)

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
                    Field(i, j, self.size).reduce_search_space(sudoku[i][j])

