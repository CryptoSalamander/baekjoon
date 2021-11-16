import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    answer = 1
    for i in range(b):
        answer *= a
        answer %= 10
    if answer == 0:
        print(10)
    else:
        print(answer)