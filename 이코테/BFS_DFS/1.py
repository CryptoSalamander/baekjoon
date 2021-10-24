import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    return gcd(num2, num1%num2)

print(gcd(A,B))