import sys

def input():
    return sys.stdin.readline().rstrip()
T = int(input())
xs = []
ys = []
for _ in range(T):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
max_x = max(xs)
max_y = max(ys)
dp = [[0]*31 for _ in range(31)]
dp[1] = [i for i in range(31)]
for x in range(2, max_x+1):
    for y in range(x, max_y+1):
        dp[x][y] = dp[x][y-1] + dp[x-1][y-1]
for i in range(T):
    x = xs[i]
    y = ys[i]
    print(dp[x][y])

