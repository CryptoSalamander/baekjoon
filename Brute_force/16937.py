import sys, heapq
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

H, W = map(int,input().split())
N = int(input())
stickers = []
for _ in range(N):
    sticker_r, sticker_c = map(int,input().split())
    stickers.append((sticker_r, sticker_c))
answer = []
comb = combinations(stickers,2)
for c in comb:
    first_r, first_c = c[0][0], c[0][1]
    second_r, second_c = c[1][0], c[1][1]
    if (first_r + second_r <= H and max(first_c, second_c) <= W) or (max(first_r,second_r) <= H and first_c + second_c <= W):
        answer.append(first_r*first_c + second_r*second_c)
    if (first_c + second_r <= H and max(first_r, second_c) <= W) or (max(first_c,second_r) <= H and first_r + second_c <= W):
        answer.append(first_c * first_r + second_r * second_c)
    if (first_r + second_c <= H and max(first_c, second_r) <= W) or (max(first_r,second_c) <= H and first_c + second_r <= W):
        answer.append(first_r*first_c + second_r*second_c)
    if (first_c + second_c <= H and max(first_r,second_r) <= W) or (max(first_c, second_c) <= H and first_r + second_r <= W):
        answer.append(first_r*first_c + second_r* second_c)
if answer:
    print(max(answer))
else:
    print(0)