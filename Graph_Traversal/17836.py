import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M, T = map(int, input().split())
board = []
sword_idx = []
visit = [[False]*M for _ in range(N)]
for row in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for col in range(M):
        if line[col] == 2:
            line[col] = '2'
            sword_idx.append((row,col))
        if line[col] == 1:
            line[col] = '1'

def bfs(row, col):
    que = deque()
    que.append((row,col))
    visit[row][col] = True
    board[row][col] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0 or board[nx][ny] == '2':
                que.append((nx,ny))
                board[nx][ny] = board[x][y] + 1
bfs(0,0)
if board[N-1][M-1] == 0 or board[N-1][M-1] == '1':
    ans = 99999
else:
    ans = board[N-1][M-1]-1

for row in range(N):
    print(*board[row])

for sword in sword_idx:
    x, y = sword
    if board[x][y] == '2':
        continue
    ans = min(ans, (board[x][y]-1) + abs(N-1-x) + abs(M-1-y))
if ans <= T:
    print(ans)
else:
    print("Fail")
