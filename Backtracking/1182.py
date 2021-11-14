import sys
def input():
    return sys.stdin.readline().rstrip()

N, S = map(int,input().split())
nums = list(map(int,input().split()))
visit = [False]*N
res = []
answer = 0
def solve(prev):
    global answer
    if res and sum(res) == S:
        answer += 1
    for i in range(prev,N):
        if not visit[i]:
            visit[i] = True
            res.append(nums[i])
            solve(i)
            res.pop()
            visit[i] = False
solve(0)
print(answer)
