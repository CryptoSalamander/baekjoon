import sys, heapq
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
mn = 99999999999999999999999
N = int(input())
ingre = []
for _ in range(N):
    sour, bitter = map(int, input().split())
    ingre.append([sour,bitter])

for i in range(1,N+1):
    for candi in combinations(ingre, i):
        ingre_list = list(candi)
        total_sour = 1
        total_bitter = 0
        for item in ingre_list:
            total_sour *= item[0]
            total_bitter += item[1]
        diff = abs(total_bitter - total_sour)
        if diff == 0:
            print(0)
            exit()
        else:
            if diff < mn:
                mn = diff
print(mn)