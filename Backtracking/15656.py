import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
answer = []

def solve():
    if len(answer)==M:
        print(*answer)
        return
    for i in num:
        answer.append(i)
        solve()
        answer.pop()
solve()