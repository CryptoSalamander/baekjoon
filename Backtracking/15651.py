import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
answer = []
def dfs():
    if len(answer) == M:
        print(*answer)
        return

    for i in range(1,N+1):
        answer.append(i)
        dfs()
        answer.pop()
dfs()