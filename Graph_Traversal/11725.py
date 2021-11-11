import sys, heapq
from collections import deque
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)
answer = []

def dfs(cur,parent):
    if visited[cur] == False:
        visited[cur] = True
        answer.append([cur+1, parent+1])
        for n in graph[cur]:
            if visited[n] == False:
                dfs(n, cur)
        return 1
    else:
        return 0
dfs(0,0)
answer.sort()
for ans in answer[1:]:
    print(ans[1])