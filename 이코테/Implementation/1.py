N = int(input())
S = list(input().split())
print(S)

started_x = 1
started_y = 1

for dir in S:
    if dir == 'R':
        if 1 <= started_x+1 <= N:
            started_x += 1
    elif dir == 'L':
        if 1 <= started_x-1 <= N:
            started_x -= 1
    elif dir == 'U':
        if 1 <= started_y-1 <= N:
            started_y -= 1
    elif dir == 'D':
        if 1 <= started_y+1 <= N:
            started_y += 1
print(started_x, started_y)