import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    n1, n2 = map(int,input().split())
    graph[n2-1].append(n1-1)
for i in graph:
    i.sort()
mx = -9999
answer = []
if N == 1:
    print(1)
    exit()
def bfs(cur):
    visit = [False] * N
    que = deque()
    que.append(cur)
    stage = 0
    while(que):
        v = que.popleft()
        if visit[v] == True:
            continue
        else:
            visit[v] = True
            stage += 1
            for n in graph[v]:
                que.append(n)
    return stage
for i in range(N):
    mx = -9999
    answer.append(bfs(i))
real_max = max(answer)
for i in range(N):
    if answer[i] == real_max:
        print(i+1, end=' ')




