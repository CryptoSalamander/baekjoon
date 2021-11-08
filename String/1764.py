import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
dic = dict()
cnt = 0
answer = []
for _ in range(N):
    name = input()
    dic[name] = 1

for _ in range(M):
    name = input()
    if name in dic:
        dic[name] += 1
        cnt += 1
        answer.append(name)
    else:
        dic[name] = 1

print(cnt)
for item in sorted(answer):
    print(item)