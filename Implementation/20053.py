import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))