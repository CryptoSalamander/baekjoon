import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

R, C = map(int,input().split())
board = []
for row in range(R):
    line = list(map(int, input().split()))
    board.append(line)

def bfs(row, col,is_hole):
    que = deque()
    tmp = []
    que.append((row,col))
    tmp.append((row,col))
    visit[row][col] = True
    if is_hole:
        board[row][col] = 'N'
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nx][ny] == 'N' and is_hole == 0:
                board[x][y] = 'C'
            if visit[nx][ny]:
                continue
            if is_hole:
                if board[nx][ny] != 1:
                    board[nx][ny] = 'N'
                    visit[nx][ny] = True
                    que.append((nx,ny))
            else:
                if board[nx][ny] == 1:
                    que.append((nx,ny))
                    visit[nx][ny] = True

hour = 0

while True:
    visit = [[False] * C for _ in range(R)]
    bfs(0,0,1)
    final_cheese = 0
    is_move = False
    for row in range(R):
        for col in range(C):
            if not visit[row][col] and board[row][col] == 1:
                is_move = True
                bfs(row,col,0)
    if is_move == False:
        break
    for row in range(R):
        for col in range(C):
            if board[row][col] == 'C':
                final_cheese += 1
                board[row][col] = 0
    hour += 1
    cheese = final_cheese
print(hour)
print(cheese)
