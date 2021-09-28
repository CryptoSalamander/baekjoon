import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    queue = deque()
    answer = 0
    doc_cnt, idx = map(int, input().split())
    input_split = list(map(int,input().split()))
    for i in range(doc_cnt):
        queue.append([i,input_split[i]])
    input_split = sorted(input_split)
    while(True):
        if queue[0][1] == input_split[-1]:
            answer += 1
            input_split.pop()
            if queue[0][0] == idx:
                print(answer)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())

