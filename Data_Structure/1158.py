N, K = map(int, input().split())

my_list = [i for i in range(1,N+1)]
answer = []
num = 0
for i in range(N):
    num += K-1
    if num >= len(my_list):
        num %= len(my_list)
    answer.append(str(my_list.pop(num)))
print("<",", ".join(answer)[:],">",sep='')







