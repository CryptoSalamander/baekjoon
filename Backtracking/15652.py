import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
result = deque()

def dfs():
    if len(result)==M:
        print(*result)
        return
    if result:
        prev = result[-1]
    else:
        prev = -1
    for i in range(1,N+1):
        if i >= prev:
            result.append(i)
            dfs()
            result.pop()
dfs()