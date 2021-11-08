import sys
def input():
    return sys.stdin.readline().rstrip()

left_loc, right_loc = input().split()
target = input()

left = "qwertasdfgzxcv"
right = "yuiophjklbnm"

keyboard = []
keyboard += list("qwertyuiop")
keyboard += list("asdfghjkl0")
keyboard += list("zxcvbnm000")

left_loc_x = keyboard.index(left_loc) % 10
left_loc_y = keyboard.index(left_loc) // 10
right_loc_x = keyboard.index(right_loc) % 10
right_loc_y = keyboard.index(right_loc) // 10
answer = 0
for char in target:
    if char in left:
        target_x, target_y = keyboard.index(char) % 10, keyboard.index(char) // 10
        tmp = abs(left_loc_x - target_x) + abs(left_loc_y - target_y)
        answer += (tmp+1)
        left_loc_x, left_loc_y = target_x, target_y
    else:
        target_x, target_y = keyboard.index(char) % 10, keyboard.index(char) // 10
        tmp = abs(right_loc_x - target_x) + abs(right_loc_y - target_y)
        answer += (tmp+1)
        right_loc_x, right_loc_y = target_x, target_y

print(answer)