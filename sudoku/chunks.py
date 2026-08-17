def chunker(sudoko, i=-1, j=-1):
    chunk_column = []
    temp_column = []
    chunk_square = []
    temp_square = []
    count = 0
    if j == -1 or i == -1:  # checking the whole thing
        for row in range(9):
            for column in range(9):
                temp_column.append(sudoko[column][row])  # adding each column to a list
                # adding each square
                if row % 3 == 0:
                    templist = [sudoko[row][column], sudoko[row + 1][column], sudoko[row + 2][column]]
                    temp_square += templist
                    count += 1
                if (count == 3):
                    chunk_square.append(temp_square)
                    temp_square = []
                    count = 0
            chunk_column.append(temp_column)
            temp_column = []
        sudoko_row = sudoko
    else:
        for number in range(9):
            chunk_column.append(sudoko[number][j])
        temp_i = i - i % 3
        temp_j = j - j % 3
        for i_count in range(3):
            for j_count in range(3):
                chunk_square.append(sudoko[i_count + temp_i][j_count + temp_j])
        sudoko_row = [sudoko[i]]
        chunk_column = [chunk_column]
        chunk_square = [chunk_square]
    return (sudoko_row, chunk_column, chunk_square)


def square_to_normal(i, j):
    square_row = (i // 3) * 3
    square_col = (i % 3) * 3

    real_row = square_row + (j % 3)
    real_col = square_col + (j // 3)

    return real_row, real_col
