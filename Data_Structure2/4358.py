import sys

def input():
    return sys.stdin.readline().rstrip()
dic = dict()
total = 0
while(True):
    st = input()
    if st =='':
        break
    else:
        if st not in dic.keys():
            dic[st] = 1
        else:
            dic[st] += 1
        total += 1

sorted_dict = sorted(dic.items(), key = lambda item: item[0])
for item in sorted_dict:
    print(f"{item[0]} {float(item[1])/total*100:.4f}")