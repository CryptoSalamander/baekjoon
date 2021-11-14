import copy
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
eggs = []
s = [0]*N
w = [0]*N
for i in range(N):
    status, weight = map(int, input().split())
    s[i] = status
    w[i] = weight
answer = -1
def dfs(cur, egg_list):
    global answer
    if cur == N:
        ans = 0
        for egg in egg_list:
            if egg <= 0:
                ans += 1
        answer = max(answer, ans)
        return

    if egg_list[cur] > 0:
        for i in range(N):
            chk = False
            if egg_list[i] > 0 and i != cur:
                chk = True
                tmp = egg_list[:]
                tmp[cur] -= w[i]
                tmp[i] -= w[cur]
                dfs(cur+1, tmp)
        if not chk:
            dfs(cur+1,egg_list)
    else:
        dfs(cur+1, egg_list)

dfs(0, s)
print(answer)


