import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

for tar in target:
    if tar in A:
        print("1")
    else:
        print("0")
