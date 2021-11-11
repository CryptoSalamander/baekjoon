import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N, M, V = map(int,input().split())
visited = [False]*N
graph = [[] for _ in range(N)]
for _ in range(M):
    n1, n2 = map(int,input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)
for g in graph:
    g.sort()

dfs_visit = []
def dfs(cur):
    dfs_visit.append(cur+1)
    visited[cur] = True
    for n in graph[cur]:
        if visited[n] == False:
            dfs(n)
def bfs(cur):
    answer = []
    que = deque()
    que.append(cur)
    while que:
        v = que.popleft()
        if visited[v] == True:
            continue
        answer.append(v+1)
        visited[v] = True
        for n in graph[v]:
            if visited[n] == False:
                que.append(n)
    return answer
dfs(V-1)
print(*dfs_visit)
visited = [False]*N
print(*bfs(V-1))
