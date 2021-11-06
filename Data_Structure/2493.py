import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int,input().split()))
stack = []
answer = ['0']
#height, idx
stack.append([lst[0],0])

for i in range(1,N):
    while(stack):
        if lst[i] <= stack[-1][0]:
            answer.append(str(stack[-1][1]+1))
            break
        else:
            stack.pop()
    if not stack:
        answer.append('0')
    stack.append([lst[i], i])
print(" ".join(answer))