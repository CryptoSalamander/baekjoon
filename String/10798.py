import sys

def input():
    return sys.stdin.readline().rstrip()

board = [[0]*15 for _ in range(5)]
for row in range(5):
    st = input()
    for col in range(len(st)):
        board[row][col] = st[col]

for col in range(15):
    for row in range(5):
        if board[row][col] != 0:
            print(board[row][col],end='')
