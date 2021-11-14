import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))
answer = []
mn = 99999999
def solve(sum_, cur, cnt):
    global mn
    if cnt == N:
        if mat[cur][answer[0]] != 0:
            mn = min(sum_+mat[cur][answer[0]], mn)
        return
    if sum_ > mn:
        return
    for i in range(N):
        if i not in answer:
            answer.append(i)
            if cur == -1:
                solve(sum_,i,cnt+1)
            elif mat[cur][i] != 0:
                solve(sum_+mat[cur][i],i,cnt+1)
            answer.pop()
solve(0,-1,0)
print(mn)