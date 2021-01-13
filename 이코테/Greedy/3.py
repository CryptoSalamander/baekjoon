import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))

M.sort()
cnt = 0
group = 0

for i in range(N):
    goal = M[i]
    cnt += 1
    if cnt >= goal:
        group += 1
        cnt = 0
print(group)

