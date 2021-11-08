import sys
def input():
    return sys.stdin.readline().rstrip()

board = []
white_idx = []
black_idx = []
for row in range(19):
    line = list(map(int, input().split()))
    for col in range(19):
        if line[col] == 1:
            black_idx.append((row,col))
        if line[col] == 2:
            white_idx.append((row,col))
    board.append(line)

def validate(unit,type):
    row, col = unit
    # 대각선

    if row <= 14 and col <= 14:
        crs_check = True
        for i in range(1,5):
            if board[row+i][col+i] != type:
                crs_check = False
                break
        if crs_check:
            if row+i <= 17 and col+i <= 17:
                if board[row+i+1][col+i+1] == type:
                    crs_check = False
            if row >= 1 and col >=1:
                if board[row-1][col-1] == type:
                    crs_check = False
            if crs_check:
                print(type)
                print(row+1,col+1)
                exit()

    if row <= 14 and col >= 4:
        crs_check = True
        for i in range(1,5):
            if board[row + i][col - i] != type:
                crs_check = False
                break
        if crs_check:
            if row + i <= 17 and col - i >= 1:
                if board[row + i + 1][col - i - 1] == type:
                    crs_check = False
            if row >= 1 and col <=17:
                if board[row-1][col+1] == type:
                    crs_check = False
            if crs_check:
                print(type)
                print(row + i + 1, col - i + 1)
                exit()
    # 아래
    if row <= 14:
        row_check = True
        for i in range(1,5):
            if board[row+i][col] != type:
                row_check = False
                break
        if row_check:
            if row+i <= 17:
                if board[row+i+1][col] == type:
                    row_check = False
            if row >= 1:
                if board[row-1][col] == type:
                    row_check= False
            if row_check:
                print(type)
                print(row+1,col+1)
                exit()
    if col <= 14:
        col_check = True
        for i in range(1,5):
            if board[row][col+i] != type:
                col_check = False
                break
        if col_check:
            if col+i <= 17:
                if board[row][col+i+1] == type:
                    col_check = False
            if col>= 1:
                if board[row][col-1] == type:
                    col_check = False
            if col_check:
                print(type)
                print(row+1,col+1)
                exit()

for white in white_idx:
    validate(white,2)

for black in black_idx:
    validate(black,1)

print(0)


