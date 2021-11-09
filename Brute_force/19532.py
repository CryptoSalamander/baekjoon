import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

a,b,c,d,e,f = map(int,input().split())
# y = (d*c - a*f) / ((b*d) - (e*a))
# x = (c - b*y) / a
# print(int(x),int(y))

for x in range(-999, 1000):
    for y in range(-999, 1000):
        first = a*x+b*y
        second = d*x+e*y
        if first == c and second == f:
            print(x,y)
            break