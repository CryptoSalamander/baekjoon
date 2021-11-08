import sys

cow_loc = [100] * 11
answer = 0
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    cow, loc = map(int, input().split())
    if abs(cow_loc[cow]-loc) == 1:
        answer += 1
        cow_loc[cow] = loc
    else:
        cow_loc[cow] = loc
print(answer)
