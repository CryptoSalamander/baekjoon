from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

class Queue():
    def __init__(self):
        self.queue = deque()

    def push(self,num):
        self.queue.append(num)

    def pop(self):
        return self.queue.popleft() if self.queue else -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if not self.queue else 0

    def front(self):
        return self.queue[0] if self.queue else -1

    def back(self):
        return self.queue[-1] if self.queue else -1

que = Queue()
answer = ""
N = int(input())
for _ in range(N):
    input_split = input().split()
    if input_split[0] == 'push':
        que.push(input_split[1])

    if input_split[0] == 'pop':
        answer += str(que.pop()) +'\n'

    if input_split[0] == 'size':
        answer += (str(que.size())+'\n')

    if input_split[0] == 'empty':
        answer += (str(que.empty())+'\n')

    if input_split[0] == 'front':
        answer += (str(que.front())+'\n')

    if input_split[0] == 'back':
        answer += (str(que.back())+'\n')

print(answer)