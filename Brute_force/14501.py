import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
sche = [(0,0)]
N = int(input())
dp = [0] * 21
for _ in range(N):
    t, p = map(int, input().split())
    sche.append((t,p))

for i in range(N+1):
    for j in range(i+1, N+1):
        dp[j+sche[j][0]] = max(dp[j+sche[j][0]-1],dp[j]+sche[j][1],dp[j+sche[j][0]])
        dp[j+1] = max(dp[j+1], dp[j])
print(max(dp[N+1],dp[N]))