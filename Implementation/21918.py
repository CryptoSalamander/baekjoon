import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
light = list(map(int, input().split()))

for _ in range(M):
    input_split = input().split()
    a = int(input_split[1])
    b = int(input_split[2])
    if input_split[0] == '1':
        light[a-1] = b
    elif input_split[0] == '2':
        for i in range(a-1, b):
            light[i] = int(not light[i])
    elif input_split[0] == '3':
        for i in range(a-1, b):
            light[i] = 0
    elif input_split[0] == '4':
        for i in range(a-1, b):
            light[i] = 1
for li in light:
    print(li, end=' ')