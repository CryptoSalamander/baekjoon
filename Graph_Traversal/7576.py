import copy
import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
M, N = map(int, input().split())
ripe_idx = []
board = []
mx = -9999
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for row in range(N):
    line = list(map(int,input().split()))
    for col in range(M):
        if line[col] == 1:
            ripe_idx.append((row,col,0))
    board.append(line)
def bfs(ripe):
    global mx
    que = deque(ripe)
    while que:
        x, y, day = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                que.append((nx,ny,day+1))
        mx = max(day, mx)
bfs(ripe_idx)
for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            print(-1)
            exit()
print(mx)
