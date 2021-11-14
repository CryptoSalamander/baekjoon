import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
is_boomerang = [[False]*M for _ in range(N)]
mx = -99999999
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

def dfs(cnt, total):
    global mx
    if cnt == N*M:
        mx = max(total, mx)
        return

    x = cnt // M
    y = cnt % M
    if is_boomerang[x][y]:
        dfs(cnt+1, total)

    else:
        # 9시, 12시 부메랑 체크
        if x-1 >= 0 and y-1 >= 0 and not is_boomerang[x-1][y] and not is_boomerang[x][y-1]:
            is_boomerang[x-1][y] = True
            is_boomerang[x][y-1] = True
            is_boomerang[x][y] = True
            dfs(cnt+1,total + board[x-1][y] + board[x][y-1] + 2*board[x][y])
            is_boomerang[x - 1][y] = False
            is_boomerang[x][y - 1] = False
            is_boomerang[x][y] = False
        # 12시, 3시 부메랑 체크
        if x-1 >= 0 and y+1 < M and not is_boomerang[x-1][y] and not is_boomerang[x][y+1]:
            is_boomerang[x-1][y] = True
            is_boomerang[x][y+1] = True
            is_boomerang[x][y] = True
            dfs(cnt+1,total + board[x-1][y] + board[x][y+1] + 2*board[x][y])
            is_boomerang[x - 1][y] = False
            is_boomerang[x][y + 1] = False
            is_boomerang[x][y] = False
        # 3시, 6시 부메랑 체크
        if x+1 < N and y+1 < M and not is_boomerang[x+1][y] and not is_boomerang[x][y+1]:
            is_boomerang[x+1][y] = True
            is_boomerang[x][y+1] = True
            is_boomerang[x][y] = True
            dfs(cnt+1,total + board[x+1][y] + board[x][y+1] + 2*board[x][y])
            is_boomerang[x + 1][y] = False
            is_boomerang[x][y + 1] = False
            is_boomerang[x][y] = False
        # 6시, 9시 부메랑 체크
        if x+1 < N and y-1 >= 0 and not is_boomerang[x+1][y] and not is_boomerang[x][y-1]:
            is_boomerang[x+1][y] = True
            is_boomerang[x][y-1] = True
            is_boomerang[x][y] = True
            dfs(cnt+1,total + board[x+1][y] + board[x][y-1] + 2*board[x][y])
            is_boomerang[x + 1][y] = False
            is_boomerang[x][y - 1] = False
            is_boomerang[x][y] = False
        dfs(cnt+1, total)
dfs(0,0)
print(mx)