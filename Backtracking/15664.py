import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = sorted(list(map(int,input().split())))
answer = []
chk = dict()
visit = [False]*N
real_answer = []
def solve():
    if len(answer) == M:
        s = "".join(map(str, answer))
        if s not in chk:
            chk[s] = 1
            real_answer.append(answer[0:])
        return
    prev = answer[-1] if answer else -1
    for i in range(len(nums)):
        if visit[i] == False and nums[i] >= prev:
            answer.append(nums[i])
            visit[i] = True
            solve()
            answer.pop()
            visit[i] = False
solve()
for i in real_answer:
    print(*i)