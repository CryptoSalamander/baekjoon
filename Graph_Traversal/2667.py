import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
board = []
for _ in range(N):
    line = input()
    tmp = []
    for char in line:
        if char == '0':
            tmp.append(False)
        else:
            tmp.append(True)
    board.append(tmp)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(col, row,val):
    que = deque()
    que.append((col,row))
    while(que):
        x, y = que.popleft()
        if board[x][y] != True:
            continue
        board[x][y] = val
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                que.append((nx,ny))
val = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == True:
            val += 1
            bfs(i,j,val)
answer = []
for chk in range(2,val+1):
    cnt = 0
    for i in board:
        cnt += i.count(chk)
    answer.append(cnt)
print(val-1)
for ans in sorted(answer):
    print(ans)