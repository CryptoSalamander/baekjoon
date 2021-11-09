import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = input()
l = len(N)
int_N = int(N)
for i in range(int_N):
    tmp = i
    st_i = str(i)
    for char in st_i:
        tmp += int(char)
    if tmp == int_N:
        print(i)
        exit()
print(0)