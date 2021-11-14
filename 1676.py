N = int(input())
start = N
answer = 0
two_count = 0
five_count = 0
for i in range(1,N+1):
    if i % 10 == 0:
        while(True):
            i = int(i / 10)
            answer += 1
            if i % 10 != 0:
                break
    if i % 5 == 0:
        while(True):
            i = int(i / 5)
            five_count += 1
            if i % 5 != 0:
                break
    if i % 2 == 0:
        while(True):
            i = int(i / 2)
            two_count += 1
            if i % 2 != 0:
                break
print(answer+min(two_count,five_count))