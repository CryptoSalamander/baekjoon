import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
set_x = sorted(list(set(x)))

dict1 = {set_x[i] : i for i in range(len(set_x))}
for i in x:
    print(dict1[i], end= ' ')