import sys

def input():
    return sys.stdin.readline().rstrip()
my_dict = dict()
N = int(input())

for _ in range(N):
    file = input()
    ext = file.split(".")[-1]
    if ext not in my_dict.keys():
        my_dict[ext] = 1
    else:
        my_dict[ext] += 1
answer = sorted(my_dict.items(), key=lambda x : x[0])
for ans in answer:
    print(ans[0], ans[1])