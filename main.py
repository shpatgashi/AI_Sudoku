from AI_Sudoku.backtracking import Backtracking
from AI_Sudoku.forward_checking import ForwardChecking
from AI_Sudoku.fc_dynamic_ordering import ForwardCheckingDO
from AI_Sudoku.examples import sudokus


if __name__ == '__main__':

    for sudoku in sudokus:
        try:
            ForwardCheckingDO(sudoku).solve_sudoku()
        except:
            continue
