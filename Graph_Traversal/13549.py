import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
N, K = map(int, input().split())
visit = [999999999] * 200001

def bfs():
    que = deque()
    que.append((N,0))
    while(que):
        loc, sec = que.popleft()
        if sec < visit[loc]:
            visit[loc] = sec
        else:
            continue
        if loc+1 < 100001:
            que.append((loc+1, sec+1))
        if loc-1 > -1:
            que.append((loc-1, sec+1))
        if abs(2*loc- K) < abs(K - loc) and loc*2 < 200001:
            que.append((loc*2, sec))
bfs()
print(visit[K])