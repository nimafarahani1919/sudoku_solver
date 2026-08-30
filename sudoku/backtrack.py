from .techniques import techniques_imputer
from .validation import check_all, check
from copy import deepcopy
def min_possible(p_sudoku):
    min_p = [[], -1, -1]

    for i in range(len(p_sudoku)):
        for j in range(len(p_sudoku[i])):
            if type(p_sudoku[i][j]) == list:
                if len(min_p[0])==0:
                    min_p[0] = p_sudoku[i][j]
                    min_p[1] = i
                    min_p[2] = j
                elif len(p_sudoku[i][j]) < len(min_p[0]):
                    min_p[0] = p_sudoku[i][j]
                    min_p[1] = i
                    min_p[2] = j

    return min_p
def backtrack(sudoku, p_sudoku):
    if techniques_imputer(p_sudoku, sudoku) == False:
        return False

    if check_all(sudoku):
        return True

    if check(sudoku) == False:
        return False

    min_p = min_possible(p_sudoku)

    if min_p[0] is None or min_p[0] == []:
        return False

    row = min_p[1]
    column = min_p[2]

    for number in min_p[0]:
        temp_sudoku = deepcopy(sudoku)
        temp_psudoku = deepcopy(p_sudoku)

        temp_sudoku[row][column] = number
        temp_psudoku[row][column] = number

        if backtrack(temp_sudoku, temp_psudoku):
            sudoku[:] = temp_sudoku
            p_sudoku[:] = temp_psudoku
            return True

    return False