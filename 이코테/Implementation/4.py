S = input()
my_str = []
sum = 0
for char in S:
    if ord('1') <= ord(char) <= ord('9'):
        sum += int(char)
    else:
        my_str.append(char)
print(''.join(sorted(my_str)) + str(sum))