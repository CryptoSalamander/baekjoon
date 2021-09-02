while(True):
    a = input()
    if a == '0':
        break

    reversed_a = a[::-1]
    if reversed_a == a:
        print("yes")
    else:
        print("no")