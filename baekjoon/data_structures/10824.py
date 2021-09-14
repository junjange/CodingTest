import sys

a, b, c, d = map(str, sys.stdin.readline().split())

left = a + b
right = c + d

print(int(left) + int(right))
