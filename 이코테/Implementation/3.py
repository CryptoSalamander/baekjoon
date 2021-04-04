a = input()
x = int(ord(a[0]) - ord('a'))
y = int(a[1])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
cnt = 0

for i in range(8):
    if 1 <= x+dx[i] <= 8 and 1 <= y+dy[i] <= 8:
        cnt += 1
print(cnt)


