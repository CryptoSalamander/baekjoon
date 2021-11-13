import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
visit = [False]*N
nums = sorted(list(map(int,input().split())))
nums = deque(nums)
answer = []
final_answer = dict()
real_answer = deque()
def solve():
    if len(answer) == M:
        s = "".join(map(str, answer))
        if s not in final_answer:
            final_answer[s] = 1
            real_answer.append(answer[0:])
        return
    for i in range(len(nums)):
        if visit[i] == False:
            answer.append(nums[i])
            visit[i] = True
            solve()
            answer.pop()
            visit[i] = False
solve()
for i in real_answer:
    print(*i)