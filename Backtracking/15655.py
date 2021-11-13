import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
nums = sorted(list(map(int, input().split())))
answer = deque()

def solve():
    if len(answer) == M:
        print(*answer)
        return
    if answer:
        prev = answer[-1]
    else:
        prev = -1
    for i in nums:
        if i not in answer and i > prev:
            answer.append(i)
            solve()
            answer.pop()
solve()
