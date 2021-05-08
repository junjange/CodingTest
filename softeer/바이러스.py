import sys

k, p, n = list(map(int,sys.stdin.readline().split()))
result = k
for i in range(n):
    result = (result * p) % 1000000007


print(result)
