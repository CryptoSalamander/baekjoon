from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = []
target = deque()
answer = []
for _ in range(N):
    target.append(int(input()))
val = target.popleft()
for i in range(1,val+1):
    answer.append('+')
    stack.append(i)
answer.append('-')
val = stack.pop()
while target:
    tmp = target.popleft()

    if val > tmp:
        if tmp != stack[-1]:
            answer = ["NO"]
            break
        else:
            answer.append('-')
            stack.pop()
    else:
        for i in range(val+1, tmp+1):
            stack.append(i)
            answer.append('+')
        answer.append('-')
        val = stack.pop()
print("\n".join(answer))



