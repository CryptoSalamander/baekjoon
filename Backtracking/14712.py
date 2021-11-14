N, M = map(int, input().split())

board = [[0]*(M+1) for _ in range(N+1)]
answer = 0
def solve(cnt):
    global answer
    if cnt == N*M:
        answer += 1
        return

    x = cnt // M + 1
    y = cnt % M + 1
    if board[x-1][y] == 0 or board[x][y-1] == 0 or board[x-1][y-1] == 0:
        board[x][y] = 1
        solve(cnt+1)
        board[x][y] = 0
    solve(cnt+1)
solve(0)
print(answer)