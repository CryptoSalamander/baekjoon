from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

answer = []
for _ in range(N):
    answer.append(int(input()))

for i in range(1,N+1):
    answer.append(i)
