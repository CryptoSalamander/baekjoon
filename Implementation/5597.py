import sys

lst = []
def input():
    return sys.stdin.readline().rstrip()

for _ in range(28):
    num = int(input())
    lst.append(num)

for i in range(1,31):
    if i not in lst:
        print(i)