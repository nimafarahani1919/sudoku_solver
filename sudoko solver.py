board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
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
def check(sudoko,i=-1,j=-1):
    sudoko_row, sudoko_column, sudoko_square = chunker(sudoko,i,j)
    for count_i in range(len(sudoko_row)):
        for k in range(1,10):
            if sudoko_row[count_i].count(k)>1 :
                if (i!=-1 and j!=-1):
                    print (f"the number {k} repeated more then ones in row {i}")
                else :
                    print (f"the number {k} repeated more then ones in row {count_i}")
                return False
            if sudoko_column[count_i].count(k)>1 :
                if (i!=-1 and j!=-1):
                    print (f"the number {k} repeated more then ones in column {i}")
                else :
                    print(f"the number {k} repeated more then ones in column {count_i}")
                return False
            if sudoko_square[count_i].count(k)>1 :
                if (i!=-1 and j!=-1):
                    print (f"the number {k} repeated more then one in square {((i//3)*3+j//3)+1}")
                else :
                    print (f"the number {k} repeated more then one in square {count_i+1}")
                return False
    return True
print(check(board,8,2))