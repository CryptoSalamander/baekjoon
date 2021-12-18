import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(i, j):
    que = deque()
    que.append((i,j))
    dx = [1,-1, 0,0]
    dy = [0,0,1,-1]
    visit[i][j] = True

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 1 and not visit[nx][ny]:
                que.append((nx,ny))
                visit[nx][ny] = True


T = int(input())
for _ in range(T):
    cnt = 0
    M,N,K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1 and not visit[row][col]:
                bfs(row, col)
                cnt += 1
    print(cnt)
