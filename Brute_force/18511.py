import sys, heapq
from collections import deque
from itertools import product
def input():
    return sys.stdin.readline().rstrip()
N, num_k = map(int,input().split())
length = len(str(N))
K = list(map(str, input().split()))

while(True):
    answer = []
    candi = list(product(K,repeat=length))
    for c in candi:
        num = int("".join(c))
        if num <= N:
            answer.append(num)
    if len(answer) > 0:
        print(max(answer))
        exit()

    length -= 1