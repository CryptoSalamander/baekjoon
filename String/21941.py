import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
S = input()
M = int(input())
del_list = []
scores = []
for _ in range(M):
    line = input().split()
    del_list.append(line[0])
    scores.append(int(line[1]))
def check(idx):
    if idx >= len(S):
        return 0
    if dp[idx] != -9999:
        return dp[idx]
    dp[idx] = check(idx+1)+1
    st = S[idx:]
    for i in range(M):
        if st[:len(del_list[i])] == del_list[i]:
            dp[idx] = max(dp[idx], check(idx+len(del_list[i]))+scores[i])
    return dp[idx]
dp = [-9999]*len(S)
print(check(0))



