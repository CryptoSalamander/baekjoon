import sys
import itertools
input = sys.stdin.readline

N,M = map(int, input().split())
best = 1000000
cards = list(map(int, input().split()))
for c in itertools.combinations(cards,3):
    if(M - sum(c) < best and sum(c) <= M):
        best = M - sum(c)
        answer = sum(c)
print(answer)

