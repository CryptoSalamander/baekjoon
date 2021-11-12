import copy
import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, L, R = map(int, input().split())

board = []
num = 0
for row in range(N):
    line = list(map(int, input().split()))
    board.append(line)

def bfs(row,col):
    global is_move
    que = deque()
    que.append([row,col])
    visited[row][col] = True
    cnt = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    union_list = []
    num = tmp_board[row][col]
    while(que):
        x,y = que.popleft()
        union_list.append((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue

            if L <= abs(tmp_board[x][y] - tmp_board[nx][ny]) <= R:
                que.append((nx,ny))
                union_list.append((nx,ny))
                visited[nx][ny] = True
                num += tmp_board[nx][ny]
                cnt += 1
    moved_people = num // cnt

    if cnt > 1:
        is_move = True
        for x, y in union_list:
            tmp_board[x][y] = moved_people


tmp_board = copy.deepcopy(board)
answer = 0
while(True):
    is_move = False
    visited = [[False]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                bfs(row, col)
    if is_move:
        answer += 1
    else:
        break
print(answer)
