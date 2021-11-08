import sys
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
S = list(map(int,input().split()))
D = list(map(int,input().split()))

D_sort = []
for i in range(N):
    D_sort.append((D[i], i))

D_sort.sort()
answer = S.copy()
for _ in range(K):
    recovery = []
    for item in D_sort:
        recovery.append(answer[item[1]])
    answer = recovery.copy()
print(*answer)