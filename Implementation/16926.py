import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, R = map(int,input().split())
array = []
for _ in range(N):
    line = list(map(int,input().split()))
    array.append(line)
