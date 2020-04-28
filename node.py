class sudoku:
    representation = [[]]
    numbers = [1, 2, 3, 4]

    def __init__(self, row, col, search_space, val):
        self.row = row
        self.col = col
        self.search_space = []
        self.val = val

    def fill_sudoku(self):
        for i in range(0, len(self.representation)):
            for j in range(0, len(self.representation[self.row])):
                if self.place_no():
                    break
                sudoku.representation[self.row][self.col - 1] = 0
                j = j -1

                # for k in range(1, 5):
                #     self.val = k
                #     self.row = i
                #     self.col = j
                #     # print('[', i, "][", j, ']=', k)
                #     if self.place_no():
                #         break

    def place_no(self):
        for num in sudoku.numbers:
            if self.representation[self.row][self.col] == 0:
                for i in range(0, 2):
                    for j in range(0, 2):
                        self.search_space.append(self.representation[self.row // 2 + i][self.col // 2 + j])

                if (num not in sudoku.representation[self.row]
                        and num not in [row[self.col] for row in sudoku.representation]
                        and num not in self.search_space):
                    sudoku.representation[self.row][self.col] = num

                return True

        return False
# def place_no(self):
#         if self.representation[self.row][self.col] == 0:
#             for i in range(0, 2):
#                 for j in range(0, 2):
#                     self.search_space.append(self.representation[self.row // 2 + i][self.col // 2 + j])
#
#         if (self.val not in sudoku.representation[self.row]
#                 and self.val not in [row[self.col] for row in sudoku.representation]
#                 and self.val not in self.search_space):
#             sudoku.representation[self.row][self.col] = self.val
#             return True
#
#         return False

# print(self.search_space)
# print(self.representation[1][1])
