import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

dir = [(-1,-1), (-1, 0), (-1,1), (0,1), (1,1), (1,0), (1, -1), (0,-1)]

for _ in range(T):
    numbers = []
    N,D = map(int,input().split())
    center = N//2

    for _ in range(N):
        line = list(map(int,input().split()))
        numbers.append(line)

    for i in range(1,center+1):
        tmp = deque()
        for d in dir:
            tmp.append(numbers[center+d[0]*i][center+d[1]*i])
        tmp.rotate(D//45)
        for j in range(8):
            numbers[center+dir[j][0]*i][center+dir[j][1]*i] = tmp[j]

    for i in range(N):
        print(*numbers[i])



