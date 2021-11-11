import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
for _ in range(N):
    line = list(input())
    line = list(map(int, line))
    board.append(line)
visit = [[0] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(row, col):
    que = deque()
    que.append((row,col))
    answer = 0
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    que.append((nx, ny))
bfs(0,0)
print(board[N-1][M-1])



