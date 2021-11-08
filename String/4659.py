import sys
def input():
    return sys.stdin.readline().rstrip()

while(True):
    first_option = False
    second_option = True
    third_option = True
    m_cnt = 0
    j_cnt = 0
    st = input()

    if st == 'end':
        break
    if len(st) == 1:
        if st[0] in 'aeiou':
            first_option = True
    else:
        prev = st[0]
        if prev in 'aeiou':
            first_option = True
            m_cnt += 1
        else:
            j_cnt += 1
        for char in st[1:]:
            if char in 'aeiou':
                first_option = True
                m_cnt += 1
                j_cnt = 0
                if m_cnt == 3:
                    second_option = False
                if char == prev and char not in 'eo':
                    third_option = False
                prev = char
            else:
                m_cnt = 0
                j_cnt += 1
                if char == prev:
                    third_option = False
                if j_cnt == 3:
                    second_option = False
                prev = char
    if first_option and second_option and third_option:
        print(f"<{st}> is acceptable.")
    else:
        print(f"<{st}> is not acceptable.")

