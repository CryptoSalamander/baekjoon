from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

class Deque():
    def __init__(self):
        self.deque = deque()

    def push_front(self, num):
        self.deque.appendleft(num)

    def push_back(self,num):
        self.deque.append(num)

    def pop_front(self):
        return self.deque.popleft() if self.deque else -1

    def pop_back(self):
        return self.deque.pop() if self.deque else -1

    def size(self):
        return len(self.deque)

    def empty(self):
        return 1 if not self.deque else 0

    def front(self):
        return self.deque[0] if self.deque else -1

    def back(self):
        return self.deque[-1] if self.deque else -1

N = int(input())
que = Deque()
result = ""
for _ in range(N):
    input_split = input().split()
    if input_split[0] == 'push_front':
        que.push_front(input_split[1])
    if input_split[0] == 'push_back':
        que.push_back(input_split[1])
    if input_split[0] == 'pop_front':
        result += str(que.pop_front()) + '\n'
    if input_split[0] == 'pop_back':
        result += str(que.pop_back()) + '\n'
    if input_split[0] == 'size':
        result += str(que.size()) + '\n'
    if input_split[0] == 'empty':
        result += str(que.empty()) + '\n'
    if input_split[0] == 'front':
        result += str(que.front()) + '\n'
    if input_split[0] == 'back':
        result += str(que.back()) + '\n'
print(result)