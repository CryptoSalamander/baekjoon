import sys, heapq
import math
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

if math.sqrt(N).is_integer():
    print(1)
    exit()

for i in range(1, int(math.sqrt(N))+1):
    if math.sqrt((N - i ** 2)).is_integer():
        print(2)
        exit()

for i in range(1, int(math.sqrt(N))+1):
    for j in range(1, int(math.sqrt(N - i**2))+1):
        if math.sqrt(N - i**2 - j**2).is_integer():
            print(3)
            exit()

print(4)





