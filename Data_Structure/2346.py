from collections import deque

N = int(input())
queue = deque([i for i in range(1,N+1)])
boom_list = list(map(int, input().split()))

while queue:
    i = queue.popleft()
    print(i, end=' ')
    if boom_list[i-1] > 0:
        queue.rotate(-1*(boom_list[i-1]-1))
    else:
        queue.rotate(-1*boom_list[i-1])


