import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    st = list(map(lambda x: ord(x) -97, input().strip()))
    target = int(input())
    mn = 99999999
    mx = -1

    check = [[] for _ in range(26)]
    for idx, val in enumerate(st):
        check[val].append(idx)

    for alpha in check:
        for i in range(len(alpha) - target + 1):
            mn = min(mn, alpha[i+target-1] - alpha[i] + 1)
            mx = max(mx, alpha[i+target-1] - alpha[i] + 1)
    if mx == -1:
        print("-1")
    else:
        print(mn, mx)