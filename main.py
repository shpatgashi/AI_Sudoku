from node import sudoku

sudoku.representation = [[0, 0, 0, 2],
                         [0, 2, 0, 4],
                         [0, 0, 0, 0],
                         [3, 0, 0, 0]]

box = sudoku(0, 0, [], 3)

box.fill_sudoku()
