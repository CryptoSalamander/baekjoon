import sys, heapq
from collections import deque
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
satisfaction = []
answer = []
for _ in range(N):
    satis = list(map(int, input().split()))
    satisfaction.append(satis)

for c in combinations(range(M), 3):
    tmp = 0
    for s in satisfaction:
        tmp += max([s[c[0]], s[c[1]], s[c[2]]])
    answer.append(tmp)
print(max(answer))
