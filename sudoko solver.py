board = [
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 8, 0, 0, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]
]
def chunker(sudoko,i=-1,j=-1):
    chunk_column=[]
    temp_column = []
    chunk_square = []
    temp_square = []
    count = 0
    if j == -1 or i == -1: # checking the whole thing
        for row in range (9):
            for column in range (9):
                temp_column.append(sudoko[column][row])# adding each column to a list
                #adding each square
                if row % 3 == 0:
                    templist = [sudoko[row][column],sudoko[row+1][column],sudoko[row+2][column]]
                    temp_square += templist
                    count += 1
                if (count == 3):
                    chunk_square.append(temp_square)
                    temp_square = []
                    count = 0
            chunk_column.append(temp_column)
            temp_column = []
        sudoko_row = sudoko
    else :
        for number in range (9):
            chunk_column.append(sudoko[number][j])
        temp_i=i-i%3
        temp_j=j-j%3
        for i_count in range (3):
            for j_count in range (3):
                chunk_square.append(sudoko[i_count+temp_i][j_count+temp_j])
        sudoko_row = [sudoko[i]]
        chunk_column = [chunk_column]
        chunk_square = [chunk_square]
    return (sudoko_row,chunk_column, chunk_square)
def check(sudoko,i=-1,j=-1,Added_Number=0):
    org = sudoko[i][j]
    sudoko[i][j] = Added_Number
    sudoko_row, sudoko_column, sudoko_square = chunker(sudoko,i,j)
    for count_i in range(len(sudoko_row)):
        for k in range(1,10):
            if sudoko_row[count_i].count(k)>1 :
                if (i == -1 and j == -1):
                    print (f"the number {k} repeated more then ones in row {count_i}")
                sudoko[i][j] = org
                return False
            if sudoko_column[count_i].count(k)>1 :
                if (i==-1 and j==-1):
                    print(f"the number {k} repeated more then ones in column {count_i}")
                sudoko[i][j] = org
                return False
            if sudoko_square[count_i].count(k)>1 :
                if (i == -1 and j == -1):
                    print (f"the number {k} repeated more then one in square {count_i+1}")
                sudoko[i][j] = org
                return False
    sudoko[i][j] = org
    return True
def possible_numbers(sudoko,i=-1,j=-1):
    Possible_numbers = []
    for k in range(1, 10):
        # print(check(sudoko,row,column,Added_Number=k),row,column,k)
        if check(sudoko, i, j, Added_Number=k):
            Possible_numbers.append(k)
    return Possible_numbers
def All_possible_numbers(sudoko):
    table =[]
    train=[]
    for row in range (9):
        for column in range (9):
            if sudoko[row][column]==0 :
                temp=possible_numbers(sudoko,row,column)
                train.append(temp)
            else :
                train.append(sudoko[row][column])
        table.append(train)
        train = []
    return table
def imputer(sudoko):
    changes = 0
    psudoko = All_possible_numbers(sudoko)
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
        if count == 1:
            i,j =  temp_loc
            return count,i,j
        if count == 0 :
            return 0,-1,-1
        return -1,-1,-1
    return -1,-1,-1
def where_the_number(sudoko):
    change_count = 0
    chunk_row,chunk_column,chunk_square = chunker(All_possible_numbers(sudoko))
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
                square_row = (i // 3) * 3
                square_col = (i % 3) * 3
                real_row = square_row + (temp_j%3)
                real_col = square_col + (temp_j//3)
                sudoko[real_row][real_col] = k
                change_count += 1
            elif count == 0:
                return -1, sudoko
    return change_count, sudoko




#checking
changed = True
while changed:
    changed = False

    c1, board = imputer(board)
    if c1 > 0:
        changed = True

    c2, board = where_the_number(board)
    if c2 == -1:
        print("No valid move found")
        break
    if c2 > 0:
        changed = True

for row in board:
    print(row)
