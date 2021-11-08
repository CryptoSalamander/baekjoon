import sys

def input():
    return sys.stdin.readline().rstrip()

schedule = [0]*366
N = int(input())
for _ in range(N):
    start_date, end_date = map(int,input().split())
    for i in range(start_date, end_date+1):
        schedule[i] += 1
max = 0
len = 0
answer = 0
for day in schedule[1:]:
    if day == 0:
        answer += max*len
        max = 0
        len = 0
    else:
        if day > max:
            max = day
        len += 1
answer += max*len

print(answer)
