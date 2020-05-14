from AI_Sudoku.backtracking import Backtracking
from AI_Sudoku.forward_checking import ForwardChecking
from AI_Sudoku.fc_dynamic_ordering import ForwardCheckingDO
from AI_Sudoku.examples import *


if __name__ == '__main__':

    ForwardChecking(sudoku1).solve_sudoku()
