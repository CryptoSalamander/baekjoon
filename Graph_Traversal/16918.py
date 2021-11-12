import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

R,C,N = map(int, input().split())
N -= 1
board = []
for row in range(R):
    line = list(input())
    board.append(line)

def bfs(bomb_list):
    global board
    que = deque(bomb_list)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while(que):
        x,y = que.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            board[nx][ny] = '.'

while N:
    bomb = deque()
    for row in range(R):
        for col in range(C):
            if board[row][col] == 'O':
                bomb.append((row, col))
            else:
                board[row][col] = 'O'
    N -= 1
    if N == 0:
        break
    bfs(bomb)
    N -= 1

for row in range(R):
    print("".join(board[row]))


