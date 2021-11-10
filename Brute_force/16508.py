import sys, heapq
from collections import deque
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()
books = []
T = input()
N = int(input())
for _ in range(N):
    price, name = input().split()
    price = int(price)
    books.append([price, name])
books.sort()
answer = []
for book in books:
    check = True
    for alpha in range(ord('A'), ord('Z')+1):
        bb = chr(alpha)
        cc = T.count(bb)
        dd = book[1].count(bb)
        if T.count(chr(alpha)) > book[1].count(chr(alpha)):
            check = False
    if check:
        answer.append(book[0])

for t in range(2,min(len(T), N)+1):
    for comb in combinations(books, t):
        book_name = ""
        book_price = 0
        for book in comb:
            book_price += book[0]
            book_name += book[1]
        check = True
        for alpha in range(ord('A'), ord('Z') + 1):
            if T.count(chr(alpha)) > book_name.count(chr(alpha)):
                check = False
        if check:
            answer.append(book_price)
if answer:
    print(min(answer))
    exit()
print(-1)