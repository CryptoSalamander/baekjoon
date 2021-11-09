import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

A = int(input())
T = int(input())
target = int(input())

bbun = []
ddegi = []
start = 0
phase = 1
while(True):
    if target == 0:
        if len(bbun) >= T:
            print(bbun[T-1] % A)
            break
    else:
        if len(ddegi) >= T:
            print(ddegi[T-1] % A)
            break
    for _ in range(2):
        bbun.append(start)
        start += 1
        ddegi.append(start)
        start += 1
    for _ in range(phase+1):
        bbun.append(start)
        start += 1
    for _ in range(phase+1):
        ddegi.append(start)
        start += 1
    phase += 1



