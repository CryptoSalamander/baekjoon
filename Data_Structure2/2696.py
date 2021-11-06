import sys,math,time
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for iter in range(T):
    heap = []
    answer = []
    M = int(input())
    numbers = []
    for _ in range(M//10):
        numbers += list(map(int, input().split()))
    numbers += list(map(int, input().split()))

    for i, item in enumerate(numbers):
        heap.append(item)
        if (i+1) % 2 == 1:
            heap.sort()
            idx = math.ceil((i + 1) / 2.0)
            answer.append(str(heap[idx-1]))
    length = len(answer)
    print(length)
    if length <= 10:
        print(" ".join(answer))
    elif length > 10:
        for ten in range(length//10):
            print(" ".join(answer[ten*10:ten*10+10]))
        answer = answer[ten*10+10:]
        print(" ".join(answer))