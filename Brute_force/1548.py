import copy
import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int,(input().split())))
A.sort()
answer = N
if len(A) > 2:
    answer = -9999
    for i in range(len(A)-2):
        for j in range(N-1, i+1, -1):
            if A[i] + A[i+1] > A[j]:
                answer = max(answer, j-i+1)

    if answer == -9999:
        answer = 2
print(answer)



