import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
password = dict()
for _ in range(N):
    domain,pw = input().split()
    password[domain] = pw
for _ in range(M):
    target = input()
    print(password[target])
