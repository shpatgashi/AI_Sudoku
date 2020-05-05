from backtracking import Backtracking
from examples import *
from fc_dynamic_ordering import ForwardCheckingDO
from forward_checking import ForwardChecking

if __name__ == '__main__':

    Backtracking(sudoku1).solve_sudoku()
    ForwardChecking(sudoku7).solve_sudoku()
    ForwardCheckingDO(sudoku3).solve_sudoku()
