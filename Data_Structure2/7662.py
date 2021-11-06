import sys,heapq
def input():
    return sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    is_live = [False] * 1000001
    K = int(input())
    max_h = []
    min_h = []
    for i in range(K):
        input_split = input().split()
        val = int(input_split[1])
        if input_split[0] == 'I':
            heapq.heappush(max_h,(-val, val, i))
            heapq.heappush(min_h, (val, val, i))
            is_live[i] = True
        else:
            if val == -1:
                while min_h and not is_live[min_h[0][2]]:
                    heapq.heappop(min_h)
                if min_h:
                    is_live[min_h[0][2]] = False
                    heapq.heappop(min_h)

            elif val == 1:
                while max_h and not is_live[max_h[0][2]]:
                    heapq.heappop(max_h)
                if max_h:
                    is_live[max_h[0][2]] = False
                    heapq.heappop(max_h)
    while min_h and not is_live[min_h[0][2]]:
        heapq.heappop(min_h)
    while max_h and not is_live[max_h[0][2]]:
        heapq.heappop(max_h)

    if min_h and max_h:
        print(max_h[0][1], min_h[0][1])
    else:
        print('EMPTY')
