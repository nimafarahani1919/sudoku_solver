from .candidates import All_possible_numbers

board = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
from copy import deepcopy
from .backtrack import backtrack
from .display import sudoku_printer


class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = deepcopy(sudoku)
        self.p_sudoku = All_possible_numbers(sudoku)

    def fit(self):
        backtrack(self.sudoku, self.p_sudoku)

    def __str__(self):
        return sudoku_printer(self.sudoku)

    def p_sudoku_print(self):
        sudoku_printer(self.p_sudoku)
