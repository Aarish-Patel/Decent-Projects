question = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],

            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],

            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]]
# question = [ [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
#                        [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
#                        [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
#                        [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
#                        [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
#                        [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
#                        [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
#                        [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
#                        [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] ]

def check_row(y,x,n):
    flag = 0
    for col in question[y]:
        if col == n:
            flag += 1
    if flag > 0:
        return False
    else:
        return True

def check_col(y,x,n):
    temp = 0
    flag = 0
    for row in question:
        if row[x]==n:
            flag += 1
    if flag > 0:
        return False
    else:
        return True
    
def check_block(y,x,n):
    bl_x = x//3
    bl_y = y//3
    flag = 0
    for i in range(0,3):
        for j in range(0,3):
            if question[(bl_y*3)+i][(bl_x*3)+j] == n:
                flag+= 1
    if flag >0:
        return False
    else:
        return True
    
def check_possible(y,x,n):
    return check_block(y,x,n) & check_col(y,x,n) & check_row(y,x,n)

def solver():
    for row in range(0,9):
        for col in range(0,9):
            if question[row][col]==0:
                for i in range(1,10):
                    if check_possible(row, col, i):
                        question[row][col]=i
                        if solver():
                            return True
                        question[row][col]=0
                return False
    return True

solver()
print(question)


    