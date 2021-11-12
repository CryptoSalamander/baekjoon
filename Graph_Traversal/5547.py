import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

W, H = map(int, input().split())
board = []
final_answer = 0
for _ in range(H):
    line = list(map(int, input().split()))
    board.append(line)

def bfs(c, r, is_building):
    global final_answer
    cnt = 0
    que = deque()
    que.append((c,r))
    dx = [-1,1,0,1,0,1]
    dy = [0,0,-1,-1,1,1]
    if is_building == 1:
        while(que):
            x, y = que.popleft()
            if board[y][x] == 'B':
                continue
            board[y][x] = 'B'
            for i in range(6):
                if y%2 == 1 and i >= 2:
                    nx = x - dx[i]
                    ny = y - dy[i]
                else:
                    nx = x + dx[i]
                    ny = y - dy[i]
                if nx < 0 or nx >= W or ny < 0 or ny >= H:
                    cnt += 1
                    continue
                if board[ny][nx] == 0 or board[ny][nx] == 'N':
                    cnt += 1
                elif board[ny][nx] == 1:
                    que.append((nx,ny))
        final_answer += cnt
    else:
        is_rounded = True
        while(que):
            x, y = que.popleft()
            if board[y][x] == 'N':
                continue
            board[y][x] = 'N'
            for i in range(6):
                if y%2 == 1 and i >= 2:
                    nx = x - dx[i]
                    ny = y - dy[i]
                else:
                    nx = x + dx[i]
                    ny = y - dy[i]
                if nx < 0 or nx >= W or ny < 0 or ny >= H:
                    is_rounded = False
                    continue
                if board[ny][nx] == 'B' or board[ny][nx] == 1:
                    cnt += 1
                elif board[ny][nx] == 0:
                    que.append((nx,ny))
        if is_rounded:
            final_answer -= cnt

for row in range(H):
    for col in range(W):
        if board[row][col] == 1:
            bfs(col,row,1)
        elif board[row][col] == 0:
            bfs(col,row,0)
print(final_answer)