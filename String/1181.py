import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
answer = []
for _ in range(N):
    st = input()
    answer.append((len(st), st))
answer = list(set(answer))
answer = sorted(answer, key=lambda x: (x[0],x[1]))
for item in answer:
    print(item[1])