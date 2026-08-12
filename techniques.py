from chunks import chunker,square_to_normal
def imputer(sudoko:list[list[int]],psudoko :list[list[int | list[int]]]):
    changes = 0
    for row in range(9):
        for column in range(9):
            if sudoko[row][column] == 0:
                if len(psudoko[row][column]) == 1 :
                    sudoko[row][column] = psudoko[row][column][0]
                    changes += 1
    return changes , sudoko
def check_alone_number(chunk, number,i):
    if number not in chunk[i]:
        temp_loc = [-1, -1]
        count = 0
        for j in range(len(chunk[i])):
            if type(chunk[i][j]) == list:
                if number in chunk[i][j]:
                    temp_loc = [i, j]
                    count += 1
        i, j = temp_loc
        if count == 1:
            return count,i,j
        if count == 0 :
            return 0,-1,-1
        return count,i,j
    return -1,-1,-1
def where_the_number(sudoko:list[list[int]],psudoko :list[list[int | list[int]]]):
    change_count = 0
    chunk_row,chunk_column,chunk_square = chunker(psudoko)
    for i in range (len(sudoko)):
        for k in range (1,10):
            count,temp_i,temp_j = check_alone_number(chunk_row,k,i)
            if count == 1 :
                sudoko[temp_i][temp_j] = k
                change_count += 1
            elif count == 0 :
                return -1,sudoko
            count, temp_i, temp_j = check_alone_number(chunk_column, k, i)
            if count == 1:
                sudoko[temp_j][temp_i] = k
                change_count += 1
            elif count == 0:
                return -1,sudoko
            count, temp_i, temp_j = check_alone_number(chunk_square, k, i)
            if count == 1:
                real_row,real_col = square_to_normal(i,temp_j)
                sudoko[real_row][real_col] = k
                change_count += 1
            elif count == 0:
                return -1, sudoko
    return change_count, sudoko
def only_two_detector(sudoku):
    """
    Detect a number that appears in exactly two candidate cells
    within a row, column, or square, and eliminate it from
    corresponding cells in the related unit.
    """

    chunk_row, chunk_column, chunk_square = chunker(sudoku)
    size = len(sudoku)

    for i in range(size):
        for k in range(1, 10):

            # Check rows
            count, temp_i, temp_j = check_alone_number(chunk_row, k, i)

            if count == 2:
                print(k,temp_i,temp_j,chunk_row[temp_i][temp_j])
                for j in range(len(chunk_row[i])):
                    if type(chunk_row[i][j]) == list:
                        if k in chunk_row[i][j]:
                            if temp_j % 3 == j % 3:
                                square_row = i // 3 * 3 + j % 3

                                for j2 in range(temp_j + 1, len(chunk_row[i])):
                                    row, col = square_to_normal(square_row, j2)

                                    if row != i and (col != temp_j or col != j):
                                        if type(sudoku[row][col]) == list:
                                            if k in sudoku[row][col]:
                                                sudoku[row][col].remove(k)

                        break

            # Check columns
            count, temp_i, temp_j = check_alone_number(
                chunk_column, k, i
            )

            if count == 2:
                for j in range(len(chunk_column[i])):
                    if type(chunk_column[i][j]) == list:
                        if k in chunk_column[i][j]:
                            if temp_j % 3 == j % 3:
                                square_row = j // 3 * 3 + i % 3

                                for j2 in range(temp_j + 1,len(chunk_column[i])):
                                    row, col = square_to_normal(square_row, j2)
                                    if type(sudoku[row][col])==list:
                                        if col != i and (row != temp_j or row != j):
                                            if k in sudoku[row][col]:
                                                sudoku[row][col].remove(k)

                        break

            # Check squares
            count, temp_i, temp_j = check_alone_number(

                chunk_square, k, i
            )

            if count == 2:
                list_ij = []

                for j in range(len(chunk_square[i])):
                    if type(chunk_square[i][j]) == list:
                        if k in chunk_square[i][j]:
                            list_ij.append([i, j])

                row_1, col_1 = square_to_normal(
                    list_ij[0][0],
                    list_ij[0][1]
                )

                row_2, col_2 = square_to_normal(
                    list_ij[1][0],
                    list_ij[1][1]
                )

                if row_1 == row_2 and col_1 == col_2:
                    print("it should not happen oops")
                    break

                if row_1 == row_2:
                    for j_2 in range(len(chunk_column[i])):
                        if j_2 != col_1 and j_2 != col_2:
                            if type(sudoku[row_1][j_2]) == list:
                                if k in sudoku[row_1][j_2]:
                                    sudoku[row_1][j_2].remove(k)

                if col_1 == col_2:
                    for j_2 in range(len(chunk_column[i])):
                        if j_2 != row_1 and j_2 != row_2:
                            if type(sudoku[j_2][col_1]) == list:
                                if k in sudoku[j_2][col_1]:
                                    sudoku[j_2][col_1].remove(k)

    return sudoku