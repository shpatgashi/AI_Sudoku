import argparse
import sys
from src.examples import *
from src.backtracking import Backtracking
from src.forward_checking import ForwardChecking
from src.fc_dynamic_ordering import ForwardCheckingDO


def str_to_attr(name):
    try:
        return getattr(sys.modules[__name__], name)
    except AttributeError as ex:
        return ex


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--sudoku", required=True, type=str)
    parser.add_argument("--algorithm", required=True, type=str)

    args = parser.parse_args()

    algorithm = str_to_attr(args.algorithm)
    sudoku = str_to_attr(args.sudoku)

    assert isinstance(algorithm(sudoku).solve_sudoku, object)
    algorithm(sudoku).solve_sudoku()
