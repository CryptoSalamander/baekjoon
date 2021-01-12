S = input()
num = []

for char in S:
    num.append(int(char))

for i in range(len(num)-1):
    if num[i] + num[i+1] > num[i] * num[i+1]:
        num[i+1] = num[i] + num[i+1]
    else:
        num[i+1] = num[i] * num[i+1]
print(num[-1])