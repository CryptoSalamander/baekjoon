import sys, heapq, itertools
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
cards = list(map(int, input().split()))
candi = itertools.combinations(cards,3)
min = 999999999999
answer = 0
for item in candi:
    tmp = M - sum(item)
    if tmp >= 0 and tmp < min:
        min = tmp
        answer = sum(item)
print(answer)