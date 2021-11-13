import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

answer = []
N, M = map(int, input().split())

def dfs():
    if len(answer) == M:
        print(*answer)

    if answer:
        prev = answer[-1]
    else:
        prev = -1
    for i in range(1,N+1):
        if i not in answer:
            if i >= prev:
                answer.append(i)
                dfs()
                answer.pop()
dfs()
