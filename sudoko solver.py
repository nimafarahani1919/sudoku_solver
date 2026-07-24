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
def chunker(sudoko):
    chunk_column=[]
    temp_column = []
    chunk_square = []
    temp_square = []
    temp = 0
    for i in range (9):
        for j in range (9):
            temp_column.append(sudoko[j][i])
            if i % 3 == 0:
                templist = [sudoko[i][j],sudoko[i+1][j],sudoko[i+2][j]]
                temp_square += templist
                temp += 1
            if (temp == 3):
                chunk_square.append(temp_square)
                temp_square = []
                temp = 0
        chunk_column.append(temp_column)
        temp_column = []
    return (sudoko,chunk_column, chunk_square)
def check(sudoko):
    sudoko_row, sudoko_column, sudoko_square = chunker(sudoko)
    for i in range(9):
        for k in range(1,10):
            if sudoko_row[i].count(k)>1 :
                print (f"the number {k} repeated more then ones in row {i}")
                return False
            if sudoko_column[i].count(k)>1 :
                print (f"the number {k} repeated more then ones in column {i}")
                return False
            if sudoko_square[i].count(k)>1 :
                print (f"the number {k} repeated more then one in square {i}")
                return False
    return True
print(check(board))