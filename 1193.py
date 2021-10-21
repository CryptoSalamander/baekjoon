a = int(input())
num = 1
ssum = 0

while(True):
    ssum += num
    if(ssum >= a):
        ssum = ssum - num
        break
    num += 1

diff = a - ssum - 1
b = num - diff
c = 1 + diff
if num % 2 == 0:
    print(c, b, sep='/')
else:
    print(b, c, sep='/')