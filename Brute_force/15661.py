import sys, heapq
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()
scores = []
answer = []
N = int(input())
members = [i for i in range(N)]
for _ in range(N):
    score = list(map(int, input().split()))
    scores.append(score)
board = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        board[i][j] = scores[i][j] + scores[j][i]
for t in range(1, N//2+1):
    mn = 9999999999999999
    candi = combinations(range(N), t)
    for c in candi:
        start_team = list(c)
        link_team = list(set(members) - set(start_team))
        # start_team 점수
        start_score = 0
        link_score = 0
        for start_combi in combinations(start_team, 2):
            start_score += board[start_combi[0]][start_combi[1]]
            start_score += scores[start_combi[0]][start_combi[1]]
        for link_combi in combinations(link_team,2):
            link_score += board[link_combi[0]][link_combi[1]]
        if start_score == link_score:
            print(0)
            exit()
        if abs(start_score-link_score) < mn:
            mn = abs(start_score-link_score)
print(mn)