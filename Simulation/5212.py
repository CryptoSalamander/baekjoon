import sys, copy
def input():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = []
islands = []
for row in range(R):
    line = list(input())
    board.append(line)
    for col in range(C):
        if line[col] == 'X':
            islands.append((row,col))
answer = copy.deepcopy(board)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
mn_x, mn_y, mx_x, mx_y = 9999,9999,-1000,-1000
for island in islands:
    x, y = island
    island_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if board[nx][ny] == 'X':
            island_cnt += 1
    if island_cnt < 2:
        answer[x][y] = '.'
    else:
        mn_x = min(mn_x, x)
        mn_y = min(mn_y, y)
        mx_x = max(mx_x, x)
        mx_y = max(mx_y, y)

for row in range(mn_x, mx_x+1):
    for col in range(mn_y, mx_y+1):
        print(answer[row][col],end='')
    print('')