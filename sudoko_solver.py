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
from techniques import imputer, where_the_number, only_two_detector
from candidates import All_possible_numbers
from validation import check_all, check
from copy import deepcopy


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


def min_possible(psudoku):
    min_p = [None, -1, -1]

    for i in range(len(psudoku)):
        for j in range(len(psudoku[i])):
            if type(psudoku[i][j]) == list:
                if min_p[0] is None or len(psudoku[i][j]) < len(min_p[0]):
                    min_p[0] = psudoku[i][j]
                    min_p[1] = i
                    min_p[2] = j

    return min_p


def techniques_imputer(psudoku, sudoku):
    changed = True
    while changed:
        changed = False
        c1, sudoku = imputer(sudoku, psudoku)
        if c1 > 0:
            only_two_detector(psudoku)
            changed = True
        if c1 == -1:
            return False
        c2, sudoku = where_the_number(sudoku, psudoku)
        if c2 > 0:
            only_two_detector(psudoku)
            changed = True
        if c2 == -1:
            return False
        if c2 > 0:
            changed = True
    return True


def backtrack(sudoku, psudoku):
    if techniques_imputer(psudoku, sudoku) == False:
        return False

    if check_all(sudoku):
        return True

    if check(sudoku) == False:
        return False

    min_p = min_possible(psudoku)

    if min_p[0] is None or min_p[0] == []:
        return False

    row = min_p[1]
    column = min_p[2]

    for number in min_p[0]:
        temp_sudoku = deepcopy(sudoku)
        temp_psudoku = deepcopy(psudoku)

        temp_sudoku[row][column] = number
        temp_psudoku[row][column] = number

        if backtrack(temp_sudoku, temp_psudoku):
            sudoku[:] = temp_sudoku
            psudoku[:] = temp_psudoku
            return True

    return False


psudoku = All_possible_numbers(board)
backtrack(board, psudoku)
# techniques_imputer(psudoku=psudoku,sudoku = board)
sudoku_printer(psudoku)
print(check_all(board))
