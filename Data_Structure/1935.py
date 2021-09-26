import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
val = []
str = input()
stack = []
for _ in range(N):
    val.append(int(input()))


for char in str:
    if char == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a*b)
    elif char == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)
    elif char == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    elif char == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    else:
        stack.append(val[ord(char)-ord('A')])

print(f"{stack[0]:.2f}")