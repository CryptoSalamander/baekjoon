import sys


def input():
    return sys.stdin.readline().rstrip()


A, B, C = map(int, input().split())


def my_pow(a, b):
    if b == 1:
        return a % C

    div_mul = my_pow(a, b // 2)
    if b % 2 == 0:
        return div_mul * div_mul % C
    else:
        return div_mul * div_mul * a % C


print(my_pow(A, B))