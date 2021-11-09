import sys, heapq
from collections import deque
import itertools
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
cnt = [[0] *4 for _ in range(M)]
s = []
nuc = ['A','C','G','T']
hamming = 0
answer = []
for _ in range(N):
    dna = input()
    for idx, n in enumerate(dna):
        cnt[idx][nuc.index(n)] += 1

for item in cnt:
    hamming += (N-max(item))
    answer.append(nuc[item.index(max(item))])
print("".join(answer))
print(hamming)