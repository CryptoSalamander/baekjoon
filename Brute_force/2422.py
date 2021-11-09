import sys, heapq
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
N, M =map(int,input().split())
ice_cream = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ice_cream[a-1].append(b-1)
    ice_cream[b-1].append(a-1)
answer = 0
for c in combinations(range(N),3):
    if c[1] in ice_cream[c[0]] or c[2] in ice_cream[c[1]] or c[2] in ice_cream[c[0]]:
        continue
    answer += 1
print(answer)