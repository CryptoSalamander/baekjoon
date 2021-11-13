import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
for row in range(N):
    line = list(map(int,input().split()))
    board.append(line)
    for col in range(M):
        if line[col] == 2:
            start_row = row
            start_col = col
            line[col] = 0
        elif line[col] == 0:
            line[col] = '0'
        else:
            line[col] = 0

def bfs():
    que = deque()
    que.append((start_row, start_col))
    board[start_row][start_col] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                que.append((nx,ny))
bfs()
for row in range(N):
    for col in range(M):
        if board[row][col] == '0':
            print('0',end=' ')
        else:
            print(board[row][col]-1, end=' ')
    print()