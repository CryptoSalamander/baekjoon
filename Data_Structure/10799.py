st = input()
num_stick = 0
answer = 0
tmp = 'f'
for char in st:
    if char == '(':
        num_stick += 1
    if char == ')':
        if tmp == ')':
            num_stick -= 1
            answer += 1
        if tmp == '(':
            num_stick -= 1
            answer += num_stick
    tmp = char
print(answer)

