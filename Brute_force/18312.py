import sys, heapq
from collections import deque
import itertools
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int,input().split())
hours = [i for i in range(N+1)]
ms = [i for i in range(60)]
all = itertools.product(hours,ms,ms,repeat=1)
answer = 0

for i in all:
    hours = f"{i[0]:02d}"
    minute = f"{i[1]:02d}"
    sec = f"{i[2]:02d}"
    if str(K) in hours or str(K) in minute or str(K) in sec:
        answer += 1
print(answer)
