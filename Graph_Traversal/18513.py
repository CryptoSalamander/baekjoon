import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
visit_idx = set()
N, K = map(int, input().split())
well_idx = list(map(int, input().split()))
well = []
answer = []
for tmp in well_idx:
    well.append((tmp, 0))
    visit_idx.add(tmp)

def bfs():
    que = deque(well)
    answer = 0
    house = 0
    while que:
        x, satis = que.popleft()
        for i in [1,-1]:
            nx = x + i
            if nx in visit_idx:
                continue
            answer -= satis-1
            house += 1
            que.append((nx, satis-1))
            visit_idx.add(nx)
            if house == K:
                print(answer)
                exit()
bfs()
