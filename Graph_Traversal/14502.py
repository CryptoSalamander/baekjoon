import copy
import sys, heapq
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
available_area = []
virus_area = []
board = []
mx = -999
for row in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for col in range(M):
        if line[col] == 0:
            available_area.append((row,col))
        elif line[col] == 2:
            virus_area.append((row,col))
def bfs():
    que = deque(virus_area)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny <0 or ny >= M:
                continue
            if tmp_board[nx][ny] == 0:
                tmp_board[nx][ny] = 2
                que.append((nx,ny))

for candi in list(combinations(available_area,3)):
    safe = 0
    tmp_board = copy.deepcopy(board)
    tmp_board[candi[0][0]][candi[0][1]] = 1
    tmp_board[candi[1][0]][candi[1][1]] = 1
    tmp_board[candi[2][0]][candi[2][1]] = 1
    bfs()
    for row in range(N):
        for col in range(M):
            if tmp_board[row][col] == 0:
                safe += 1
    mx = max(safe, mx)
print(mx)

