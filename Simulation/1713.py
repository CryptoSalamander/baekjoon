import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
T = int(input())
candi = list(map(int, input().split()))
pictures = []
voting = [0]*101
for i in candi:
    if len(pictures) < N and i not in pictures:
        voting[i] += 1
        pictures.append(i)
    elif i not in pictures:
        mn = 999999
        for pic in pictures:
            if voting[pic] < mn:
                mn = voting[pic]
                out = pic
        pictures.remove(out)
        voting[out] = 0
        pictures.append(i)
        voting[i] += 1
    else:
        voting[i] += 1

print(*sorted(pictures))




