import sys, heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
visited = [False] * N
graph = [[] for _ in range(N)]
C = int(input())
visit = []
answer = 0
for _ in range(C):
    node1, node2 = map(int,input().split())
    graph[node1-1].append(node2-1)
    graph[node2-1].append(node1-1)

def dfs(cur):
    global answer
    if visited[cur] == False:
        visited[cur] = True
        answer += 1
        for node in graph[cur]:
            dfs(node)
dfs(0)
print(answer-1)