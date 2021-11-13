import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
nums = sorted(list(set(list(map(int, input().split())))))
answer = []
chk = dict()

def solve():
    if len(answer) == M:
        print(*answer)
        return
    prev = answer[-1] if answer else -1
    for i in nums:
        if i >= prev:
            answer.append(i)
            solve()
            answer.pop()
solve()
