import copy
import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visit = [False]*N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for rel in graph:
    rel.sort()
def dfs(cur, visited):
    visit[cur] = True
    visited.add(cur)
    if len(visited) == 5:
        print(1)
        exit()
    for v in graph[cur]:
        if v not in visited:
            dfs(v, visited.copy())
    visit[cur] = False
    return 0
for i in range(N):
    if not visit[i]:
        dfs(i,set([]))
print(0)


