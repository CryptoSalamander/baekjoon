a = list(map(int,input().split()))

answer = 0
for i in a:
    answer += i**2
print(answer%10)