import sys
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int,input().split())
dic = dict()
pocs = []
answer = []
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(N):
    pok = input()
    pocs.append(pok)
    dic[pok] = str(i+1)
for _ in range(M):
    temp = input()
    if temp[0] in alpha:
        answer.append(dic[temp])
    else:
        answer.append(pocs[int(temp)-1])
print("\n".join(answer))