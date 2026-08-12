board = [
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 8, 0, 0, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]]

from techniques import imputer, where_the_number, only_two_detector
from candidates import All_possible_numbers
psudoko = All_possible_numbers(board)
def min_possible(psudoku):
    min = [-1,-1,-1]
    for i in range(len(psudoku)):
        for j in range(len(psudoku[i])):
            if type(psudoku[i][j]) == list:
                if len(psudoku[i][j])<min[0]:
                    min[0]=len(psudoku[i][j])
                    min [1]=i
                    min [2]=j
    return min
def techniques_imputer(psudoku, sudoku):
    changed = True
    while changed:
        changed = False
        c1, sudoku = imputer(sudoku, psudoku)
        if c1 > 0:
            only_two_detector(psudoku)
            changed = True

        c2, sudoku = where_the_number(sudoku, psudoku)
        if c2 > 0:
            only_two_detector(psudoku)
            changed = True
        if c2 == -1:
            print("No valid move found")
            break
        if c2 > 0:
            changed = True
    return psudoku ,sudoku
techniques_imputer(sudoku=board, psudoku=psudoko)
def sudoku_printer(sudoku):
    for i, row in enumerate(sudoku):
        print(
            " | ".join(
                f"{str(cell):^15}"
                for cell in row[:3]
            ),
            "||",
            " | ".join(
                f"{str(cell):^15}"
                for cell in row[3:6]
            ),
            "||",
            " | ".join(
                f"{str(cell):^15}"
                for cell in row[6:]
            )
        )

        if i in [2, 5]:
            print("=" * 153)
        else:
            print("-" * 153)

def backtrack(sudoku):
    a=1
sudoku_printer(psudoko)