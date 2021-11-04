import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.list = []

    def push(self,num):
        return self.list.append(num)

    def size(self):
        return len(self.list)

    def empty(self):
        if self.list:
            return 0
        else:
            return 1

    def pop(self):
        if not self.list:
            return -1
        return self.list.pop()

    def top(self):
        return self.list[-1] if self.list else -1

N = int(input().rstrip())
s = Stack()
for _ in range(N):
    input_split = input().rstrip().split()
    cmd = input_split[0]

    if cmd == 'push':
        s.push(input_split[1])
    if cmd == 'pop':
        print(s.pop())
    if cmd == 'size':
        print(s.size())
    if cmd == 'empty':
        print(s.empty())
    if cmd == 'top':
        print(s.top())

