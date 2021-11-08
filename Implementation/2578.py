import sys

def input():
    return sys.stdin.readline().rstrip()

board_idx = dict()
board = []
order = []
bingo = 0
crs_bingo_done = False
crs2_bingo_done = False
for row in range(5):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for col in range(5):
        board_idx[tmp[col]] = (row,col)
for _ in range(5):
    tmp = list(map(int, input().split()))
    order += tmp

for i, num in enumerate(order):
    check_row, check_col = board_idx[num][0], board_idx[num][1]
    board[check_row][check_col] = 0
    col_is_bingo = True
    crs_is_bingo = True
    crs_2_is_bingo = True

    if sum(board[check_row]) == 0:
        bingo += 1
    for j in range(5):
        if board[j][check_col] != 0:
            col_is_bingo = False
        if board[j][j] != 0:
            crs_is_bingo = False
        if board[j][4-j] != 0:
            crs_2_is_bingo = False
    if col_is_bingo:
        bingo += 1
    if crs_is_bingo and not crs_bingo_done:
        bingo += 1
        crs_bingo_done = True
    if crs_2_is_bingo and not crs2_bingo_done:
        bingo += 1
        crs2_bingo_done = True

    if bingo >= 3:
        print(i+1)
        exit()
