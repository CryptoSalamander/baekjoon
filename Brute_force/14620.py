import sys, heapq, copy
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

board = []
N = int(input())
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)
candi = combinations(range(N**2), 3)
answer = []
for c in candi:
    tmp_board = copy.deepcopy(board)
    is_valid = True
    cost = 0
    for flower in c:
        row, col = flower//N, flower%N
        if 1<= row <= N-2 and 1<= col <= N-2:
            cost += tmp_board[row][col]
            tmp_board[row][col] = 999999999999
            cost += tmp_board[row-1][col]
            tmp_board[row - 1][col] = 9999999999999
            cost += tmp_board[row+1][col]
            tmp_board[row + 1][col] = 9999999999999
            cost += tmp_board[row][col-1]
            tmp_board[row][col - 1] = 9999999999999
            cost += tmp_board[row][col+1]
            tmp_board[row][col + 1] = 9999999999999
        else:
            is_valid = False
            break
    if is_valid:
        answer.append(cost)
print(min(answer))

