dp = [[0]*101 for _ in range(101)]
dp[5][0], dp[5][1], dp[5][2], dp[5][3], dp[5][4], dp[5][5] = 1, 5, 10, 10, 5,1

for row in range(6, 101):
    dp[row][0] = 1
    for col in range(1, 101):
        dp[row][col] = dp[row-1][col]+dp[row-1][col-1]

n, m = map(int, input().split())
print(dp[n][m])
