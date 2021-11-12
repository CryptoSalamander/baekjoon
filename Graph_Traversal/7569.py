import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

M, N, H = map(int, input().split())
board = [[] for _ in range(H)]
tomato_idx = []
mx = 0
for level in range(H):
    for row in range(N):
          line = list(map(int, input().split()))
          board[level].append(line)
          for col in range(M):
              if line[col] == 1:
                  tomato_idx.append((level, row, col,0))
def bfs(tomatoes):
    global mx
    que = deque(tomatoes)
    while que:
        z, x, y, day = que.popleft()
        for i in range(6):
            nz = z+dz[i]
            nx = x+dx[i]
            ny = y+dy[i]
            if nz < 0 or nz >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nz][nx][ny] == 0:
                board[nz][nx][ny] = 1
                que.append((nz,nx,ny,day+1))
        mx = max(day, mx)

bfs(tomato_idx)
for level in range(H):
    for row in range(N):
        for col in range(M):
            if board[level][row][col] == 0:
                print(-1)
                exit()
print(mx)

