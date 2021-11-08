s_h, s_m, s_s = map(int, input().split(':'))
e_h, e_m, e_s = map(int, input().split(':'))

t1 = s_h * 3600 + s_m * 60 + s_s
t2 = e_h * 3600 + e_m * 60 + e_s
if t1>=t2:
    answer = t2-t1 + 24*3600
else:
    answer = t2-t1
h = answer//3600
answer %= 3600
m = answer//60
answer %= 60
s = answer
print(f"{h:02d}:{m:02d}:{s:02d}")



