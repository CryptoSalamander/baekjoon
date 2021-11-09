import sys, heapq
from itertools import permutations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
cards = []
my_set = set()
for _ in range(n):
    cards.append(input())
for c in permutations(cards,k):
    my_set.add("".join(c))
print(len(my_set))
