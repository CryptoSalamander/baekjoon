import sys, heapq
from collections import deque
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
questions = []
numbers = ['1','2','3','4','5','6','7','8','9']
answer = 0
for _ in range(N):
    ans, strike, ball = map(int, input().split())
    questions.append((str(ans),strike,ball))

candi = list(map(lambda x : "".join(x), permutations(numbers, 3)))
# c 모든 경우의 수
# q 물어봤던 숫자값
for c in candi:
    strike = 0
    ball = 0
    for q in questions:
        strike = 0
        ball = 0
        is_valid = True
        for idx, char in enumerate(q[0]):
            if char in c:
                if c[idx] == q[0][idx]:
                    strike += 1
                else:
                    ball += 1
        if strike != q[1] or ball != q[2]:
            is_valid = False
            break
    if is_valid:
        answer += 1
print(answer)
