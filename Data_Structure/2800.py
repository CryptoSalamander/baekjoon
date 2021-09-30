import itertools
st = input()
stack = []
idx_list = []
def get_result(idx):
    erase_index = []
    for i in range(len(idx)):
        if idx[i] == 0:
            erase_index.append(idx_list[i][0])
            erase_index.append(idx_list[i][1])
    string = ""
    for i, char in enumerate(st):
        if i not in erase_index:
            string += char
    string += '\n'
    return string

for i,char in enumerate(st):
    if char == '(':
        stack.append(i)
    if char == ')':
        l_idx = stack.pop()
        idx_list.append([l_idx,i])

result = list(itertools.product(([0,1]), repeat=len(idx_list)))
answer = []
for i in result:
    if sum(i) == len(idx_list):
        continue
    answer.append(get_result(i))
answer = sorted(set(answer))
print("".join(answer))


