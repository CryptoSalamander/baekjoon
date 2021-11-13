import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
result = deque()

def solve():
    if len(result) == M:
        print(*result)
    for i in num:
        if i not in result:
            result.append(i)
            solve()
            result.pop()
solve()