import sys

def input():
    return sys.stdin.readline().rstrip()
answer = 0
N, M = map(int,input().split())
lst = []
for _ in range(N):
    lst.append(input())

for _ in range(M):
    st = input()
    if st in lst:
        answer += 1
print(answer)
