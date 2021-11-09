import sys, heapq, copy
from collections import deque
from itertools import product
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
a = [0, 1]
candi = list(product(a, repeat=8))
candi_4 = []
for c in candi:
    if sum(c) == 4:
        candi_4.append(c)
for _ in range(T):
    tmp_board = []
    answer = []
    for _ in range(3):
        tmp = []
        for char in list(input().split()):
            if char == 'H':
                tmp.append(True)
            else:
                tmp.append(False)
        tmp_board.append(tmp)
    for c in candi:
        board = copy.deepcopy(tmp_board)
        # 첫째열 변경
        if c[0]:
            board[0] = list(map(lambda x : not x, board[0]))
        # 둘째 열 변경
        if c[1]:
            board[1] = list(map(lambda x : not x, board[1]))
        # 셋째 열 변경
        if c[2]:
            board[2] = list(map(lambda x : not x, board[2]))
        # 첫째 행 변경
        if c[3]:
            for i in range(3):
                board[i][0] = not board[i][0]
        # 둘째 행 변경
        if c[4]:
            for i in range(3):
                board[i][1] = not board[i][1]
        # 셋째 행 변경
        if c[5]:
            for i in range(3):
                board[i][2] = not board[i][2]
        # 대각선 왼쪽위에서 오른쪽 아래
        if c[6]:
            for i in range(3):
                board[i][i] = not board[i][i]
        # 대각선 왼쪽 아래에서 오른쪽 위
        if c[7]:
            for i in range(3):
                board[2-i][i] = not board[2-i][i]
        chk = 0
        for i in range(3):
            for j in range(3):
                chk += int(board[i][j])
        if chk == 9 or chk == 0:
            answer.append(sum(c))
    if answer:
        print(min(answer))
    else:
        print(-1)


