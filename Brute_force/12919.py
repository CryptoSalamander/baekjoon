import sys, heapq, copy
from itertools import permutations
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

S = deque(list(input()))
T = deque(list(input()))

def pos(target):
    if len(target) == len(S):
        if target == S:
            print(1)
            exit()
        else:
            return 0
    if target[-1] == 'B':
        if target.popleft() != 'B':
            return 0
        target.reverse()
        pos(copy.deepcopy(target))
    else:
        if target[0] == 'A':
            target.pop()
            pos(copy.deepcopy(target))
        else:
            target.pop()
            pos(copy.deepcopy(target))
            target.append('A')
            if target.popleft() != 'B':
                return 0
            target.reverse()
            pos(copy.deepcopy(target))
pos(copy.deepcopy(T))
print(0)



