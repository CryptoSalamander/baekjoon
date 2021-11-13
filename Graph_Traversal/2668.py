import copy
import sys, heapq
from collections import deque, defaultdict
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
num = []
answer = []
visit = [False]*(N+1)
graph = defaultdict(list)
for i in range(1,N+1):
    tmp = int(input())
    graph[tmp].append(i)

def dfs(cur, cycle):
    global answer
    visit[cur] = True
    cycle.add(cur)
    for v in graph[cur]:
        if v not in cycle:
            dfs(v, copy.deepcopy(cycle))
        else:
            answer += list(cycle)
            return

for i in range(1,N+1):
    if not visit[i]:
        dfs(i, set([]))
print(len(answer))
for item in sorted(answer):
    print(item)