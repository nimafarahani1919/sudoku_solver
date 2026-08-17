from .validation import check
from .chunks import square_to_normal, chunker


def possible_numbers(sudoko, i=-1, j=-1):
    Possible_numbers = []
    for k in range(1, 10):
        # print(check(sudoko,row,column,Added_Number=k),row,column,k)
        if check(sudoko, i, j, added_number=k):
            Possible_numbers.append(k)
    return Possible_numbers


def All_possible_numbers(sudoko):
    table = []
    train = []
    for row in range(9):
        for column in range(9):
            if sudoko[row][column] == 0:
                temp = possible_numbers(sudoko, row, column)
                train.append(temp)
            else:
                train.append(sudoko[row][column])
        table.append(train)
        train = []
    return table


def numb_remover(psudoku, row, column, Added_Number):
    for i in range(len(psudoku[row])):
        if type(psudoku[row][i]) == list:
            if Added_Number in psudoku[row][i]:
                psudoku[row][i].remove(Added_Number)
    for i in range(len(psudoku)):
        if type(psudoku[i][column]) == list:
            if Added_Number in psudoku[i][column]:
                psudoku[i][column].remove(Added_Number)
    square = (row // 3) * 3 + (column // 3)
    for i in range(9):
        temp_i, temp_j = square_to_normal(square, i)
        if type(psudoku[temp_i][temp_j]) == list:
            if Added_Number in psudoku[temp_i][temp_j]:
                psudoku[temp_i][temp_j].remove(Added_Number)
    return psudoku
