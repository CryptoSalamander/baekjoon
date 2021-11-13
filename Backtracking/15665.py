import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
nums = sorted(list(map(int,input().split())))
result = []
chk = dict()

def solve():
    if len(result) == M:
        s = "".join(map(str, result))
        if s not in chk:
            chk[s] = 1
            print(*result)
        return
    prev = result[-1] if result else -1
    for i in nums:
        result.append(i)
        solve()
        result.pop()
solve()