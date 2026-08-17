from .chunks import chunker


def check(sudoko, i=-1, j=-1, added_number=0):
    org = sudoko[i][j]
    if (i != -1) and (j != -1):
        sudoko[i][j] = added_number
    sudoko_row, sudoko_column, sudoko_square = chunker(sudoko, i, j)
    for count_i in range(len(sudoko_row)):
        for k in range(1, 10):
            if sudoko_row[count_i].count(k) > 1:
                sudoko[i][j] = org
                return False
            if sudoko_column[count_i].count(k) > 1:
                sudoko[i][j] = org
                return False
            if sudoko_square[count_i].count(k) > 1:
                sudoko[i][j] = org
                return False
    sudoko[i][j] = org
    return True


def check_all(sudoku):
    for chunk in sudoku:
        if 0 in chunk:
            return False
    sudoko_row, sudoko_column, sudoko_square = chunker(sudoku)
    for count_i in range(len(sudoko_row)):
        for k in range(1, 10):
            if sudoko_row[count_i].count(k) > 1:
                # print(f"the number {k} repeated more then ones in row {count_i}")
                return False
            if sudoko_column[count_i].count(k) > 1:
                # print(f"the number {k} repeated more then ones in column {count_i}")
                return False
            if sudoko_square[count_i].count(k) > 1:
                # print(f"the number {k} repeated more then one in square {count_i + 1}")
                return False
    return True
