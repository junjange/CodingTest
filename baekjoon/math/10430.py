import sys

A, B, C = map(int, sys.stdin.readline().split())

# 문제의 조건에 맞게 출력
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C,)
print(((A % C) * (B % C)) % C)
